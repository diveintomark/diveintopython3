#!/usr/bin/python3

import re

# get list of chapters
chapters = []
for line in open('index.html', encoding="utf-8"):
    if not line.count('<li') or not line.count('<a href'): continue
    chapters.append(line.split('<a href=', 1)[1].split('>', 1)[0])
sections = {}

for filename in chapters:
    chapter_id = filename.split(".", 1)[0]
    with open(filename, encoding="utf-8") as f: data = f.read()
    sections[chapter_id] = re.findall("<h([23]) id=(.*?)>(.*?)</h", data)

with open('index.html', encoding="utf-8") as f: data = f.read()
short_toc = data.split('<!-- toc -->')[1].split('<!-- /toc -->')[0]

full_toc = ['<!-- toc -->', '<ol start=-1>']
chapter_id = ''
for line in short_toc.splitlines():
    if not line.count('<li') or not line.count('<a href'): continue
    chapter_id = line.split('<a href=', 1)[1].split('.', 1)[0]
    line = re.sub(' id=.*?>', '>', line)
    line = line.replace('<li>', '<li id={0}>'.format(chapter_id))
    full_toc.append(line)
    section_number = 0
    previous_section_level = section_level = 1
    for section_level, section_id, section_title in sections[chapter_id]:
        section_level = int(section_level)
        if section_level < previous_section_level:
            full_toc.append('</ol>')
        elif section_level > previous_section_level:
            full_toc.append('<ol>')
        section_number += 1
        full_toc.append('<li><a href={0}.html#{1}>{2}</a>'.format(chapter_id, section_id, section_title))
        previous_section_level = section_level
    section_level = int(section_level)
    while (section_level > 1):
        full_toc.append('</ol>')
        section_level -= 1
full_toc.append('</ol>')
full_toc.append('<!-- /toc -->')
with open('table-of-contents.html', encoding="utf-8") as f: data = f.read()
with open('table-of-contents.html', mode="w", encoding="utf-8") as f:
    f.write(data.split('<!-- toc -->')[0] + "\n".join(full_toc) + data.split('<!-- /toc -->')[1])
