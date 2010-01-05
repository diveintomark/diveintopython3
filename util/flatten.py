#!/usr/bin/python3

import re
import time

# get list of chapters
chapters = []
for line in open('index.html', encoding="utf-8"):
    if not line.count('<li') or not line.count('<a href'):
        continue
    chapters.append(line.split('<a href=', 1)[1].split('>', 1)[0])

# construct regexes used to fix internal xrefs
chapter_href = re.compile("<a href=({0})>".format("|".join(chapters)))
chapter_fragment_href = re.compile("<a href=({0})#(.*?)>".format("|".join(chapters)))
same_chapter_fragment_href = re.compile("<a href=#(.*?)")
id_munge = re.compile(" id=(.*?)[ >]")

# munge and combine chapter-specific styles
out = open('build/single.html', 'w', encoding="utf-8")
out.write(open('util/single-header.html', encoding="utf-8").read().replace('%%DATE%%', time.strftime('%Y-%m-%d', time.localtime())))
out.write("<style>\n")
for filename in chapters:
    include = False
    id_prefix = filename.split(".", 1)[0]
    chapter_id = "chapter-" + id_prefix
    for line in open(filename, encoding="utf-8"):
        if line.count('</style>'):
            include = False
        if include and not line.count('counter-reset'):
            line = "#{0} {1}".format(chapter_id, line)
            line = line.replace(",", ", #{0} ".format(chapter_id))
            out.write(line)
        if line.count('<style>'):
            include = True
out.write("</style>\n")
out.write(open('util/single-header2.html', encoding="utf-8").read())

# munge and combine chapters
for filename in chapters:
    include = False
    id_prefix = filename.split(".", 1)[0]
    chapter_id = "chapter-" + id_prefix
    out.write("<div id={0}>\n".format(chapter_id))
    for line in open(filename, encoding="utf-8"):
        if line.count('<h1>'):
            include = True
        if line.count('<p class=v') or line.count('<p class=c>&copy;'):
            include = False
        if line.count('<p id=toc'):
            line = line.replace(' id=toc', '')
        if include:
            # fix cross-references
            line = id_munge.sub(lambda x: " id={0}-{1}>".format(id_prefix, x.group(1)), line)
            line = same_chapter_fragment_href.sub(lambda x: "<a href=#{0}-{1}".format(id_prefix, x.group(1)), line)
            line = chapter_href.sub(lambda x: "<a href=#chapter-" + x.group(1).replace('.html', '') + ">", line)
            line = chapter_fragment_href.sub(lambda x: "<a href=#{0}-{1}>".format(x.group(1).replace('.html', ''), x.group(2)) , line)
            out.write(line)
    out.write("</div>\n")

out.write(open('util/single-footer.html', encoding="utf-8").read())
out.close()
