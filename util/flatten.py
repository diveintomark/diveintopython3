#!/usr/bin/python3

# TODO:
# - fix internal xrefs (look for href=<in [chapters]>.html)
# - fix duplicate IDs
# - print stylesheet

chapters = []
for line in open('index.html'):
    if not line.count('<li') or not line.count('<a href'):
        continue
    chapters.append(line.split('<a href=', 1)[1].split('>', 1)[0])

out = open('build/single.html', 'w', encoding="utf-8")
out.write(open('util/single-header.html', encoding="utf-8").read())
out.write("<style>\n")
for filename in chapters:
    include = False
    id = "chapter-" + filename.split(".", 1)[0]
    for line in open(filename, encoding="utf-8"):
        if line.count('</style>'):
            include = False
        if include and not line.count('counter-reset'):
            line = "#{0} {1}".format(id, line)
            line = line.replace(",", ", #{0} ".format(id))
            out.write(line)
        if line.count('<style>'):
            include = True
out.write("</style>\n")
out.write(open('util/single-header2.html', encoding="utf-8").read())

for filename in chapters:
    include = False
    id = "chapter-" + filename.split(".", 1)[0]
    out.write("<div id={0}>\n".format(id))
    for line in open(filename, encoding="utf-8"):
        if line.count('<h1>'):
            include = True
        if line.count('<p class=nav') or line.count('<p class=c>&copy;'):
            include = False
        if include:
            out.write(line)
    out.write("</div>\n")

out.write(open('util/single-footer.html', encoding="utf-8").read())
out.close()
