VERSION = 1.0.1
PROJECT = chardet
XSLTPROC = xsltproc
XMLLINT = xmllint
PYTHON = python

test:
	${PYTHON} test.py tests/**/*

validate:
	${XMLLINT} --noout --valid docs/xml/${PROJECT}.xml

.PHONY: docs

docs: validate
	cd docs; \
	${XSLTPROC} xsl/html.xsl xml/${PROJECT}.xml; \
	${PYTHON} ../util/colorize.py . 0; \
	cd ..

clean:
	rm -f *.pyc
	rm -f ${PROJECT}/*.pyc
	rm -f util/*.pyc
	rm -rf build
	rm -rf dist
	rm -rf docs/dist

maintainer-clean: clean
	rm -f docs/*.html

release-check:
	${PYTHON} util/releasecheck.py

dist: validate
	cd docs; \
	mkdir -p dist/docs/; \
	rsync -rtpz --exclude=.svn ../css dist/docs/; \
	rsync -rtpz --exclude=.svn images dist/docs/; \
	${XSLTPROC} xsl/htmldist.xsl xml/${PROJECT}.xml; \
	${PYTHON} ../util/colorize.py dist/docs/ 0; \
	cd ..
	mkdir -p dist/${PROJECT}-${VERSION}
	cp COPYING dist/${PROJECT}-${VERSION}
	cp setup.py dist/${PROJECT}-${VERSION}
	rsync -rtpz --exclude=*.svn* ${PROJECT} dist/${PROJECT}-${VERSION}
	rsync -rtpz docs/dist/docs dist/${PROJECT}-${VERSION}
	cd dist; \
	tar cfz ${PROJECT}-${VERSION}.tgz ${PROJECT}-${VERSION}; \
	cd ..
	ls -l dist

all: validate release-check maintainer-clean docs dist
