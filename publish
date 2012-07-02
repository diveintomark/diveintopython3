#!/bin/sh

die () {
  echo "$1" >/dev/stderr
  exit 1
}

echo "started build"

# build table of contents
python3 util/buildtoc.py

revision=`git rev-parse --short HEAD`
today=`date +"%Y-%m-%d"`

# make build directory and copy original files there for preflighting
rm -rf build
mkdir build
mkdir build/tmp
mkdir build/d
cp robots.txt *.css build/
cp -R j build/
cp -R i build/
rm -f examples/*.pyc
cp -R examples build/
cp .htaccess build/

echo "validating HTML"
for f in *.html; do
  python3 util/validate.py "$f" > /dev/null || die "Failed to validate $f"
done

echo "building HTML distribution"
htmlbasedir=diveintopython3-r"$revision"-"$today"
htmldir=build/"$htmlbasedir"
mkdir -p "$htmldir"
cp *.html "$htmldir"/
cp dip3.css "$htmldir"/
mkdir "$htmldir"/i
cp i/*.png "$htmldir"/i/
mkdir "$htmldir"/j
cp j/dip3.js j/html5.js j/jquery.js j/prettify.js "$htmldir"/j/
mkdir "$htmldir"/examples
cp examples/*.jpg examples/*.json examples/*.pickle examples/*.py examples/*.txt examples/*.xml "$htmldir"/examples/
cd build/ && \
    zip -9rq diveintopython3-html-r"$revision"-"$today".zip "$htmlbasedir" && \
cd ..
echo "Redirect /d/diveintopython3-html-latest.zip http://diveintopython3.org/d/diveintopython3-html-r$revision-$today.zip" >> build/d/.htaccess
mv "$htmldir" "$htmldir".html.bak

echo "building PDF distribution"
python3 util/flatten.py # outputs to build/single.html
pdfbasedir="$htmlbasedir"
pdfdir="$htmldir"
mkdir -p "$pdfdir"
pdffile="$pdfdir"/diveintopython3-r"$revision".pdf
prince --style=prince.css --output="$pdffile" build/single.html 2>build/prince.log
mkdir "$pdfdir"/examples
cp examples/*.jpg examples/*.json examples/*.pickle examples/*.py examples/*.txt examples/*.xml "$pdfdir"/examples/
cd build/ && \
    zip -9rq diveintopython3-pdf-r"$revision"-"$today".zip "$pdfbasedir" && \
cd ..
echo "Redirect /d/diveintopython3-pdf-latest.zip http://diveintopython3.org/d/diveintopython3-pdf-r$revision-$today.zip" >> build/d/.htaccess
mv "$pdfdir" "$pdfdir".pdf.bak
mv build/single.html build/single.html.bak

#echo "linting JS"
#
#[ -n "$(which js 2>/dev/null)" ] || die "SpiderMonkey (js or js.exe) not found"
#js_lint_results=`js j/jslint.js < build/j/dip3.js 2>/dev/null`
#[ "$js_lint_results" = "jslint: No problems found." ] || die "$js_lint_results"

echo "adding per-page dates"
for f in *.html; do
  cp "$f" build/tmp/
  log=`git log "$f" | grep "^Date"`
  num_changes=`echo "$log" | wc -l`
  lastmodified=`echo "$log" | head -1 | cut -d":" -f2- | cut -d" " -f4-8`
  lastmodified_pretty=`python3 -c "import time; print(time.strftime('%B %d, %Y', time.strptime('$lastmodified')).replace(' 0', ' '))"`
  firstmodified=`echo "$log" | tail -1 | cut -d":" -f2- | cut -d" " -f4-8`
  firstmodified_pretty=`python3 -c "import time; print(time.strftime('%B %d, %Y', time.strptime('$firstmodified')).replace(' 0', ' '))"`
  sed -i -e "s|<p id=level>|<p id=level>Updated <a title='$num_changes changes since $firstmodified_pretty' href=https://github.com/diveintomark/diveintopython3/blob/master/$f>$lastmodified_pretty</a> \&bull; |" build/tmp/"$f"
done

echo "minimizing HTML"

# minimize HTML (NB: this script is quite fragile and relies on knowledge of how I write HTML)
for f in *.html; do
  python3 util/htmlminimizer.py build/tmp/"$f" build/"$f" || die "Failed to minimize $f"
done

# build sitemap
ls build/*.html | sed -e "s|build/|http://diveintopython3.org/|g" -e "s|/index.html|/|g" > build/sitemap.txt || die "Failed to build sitemap"

# minimize JS and CSS
echo "minimizing JS"
java -jar util/compiler.jar -js build/j/prettify.js > build/j/prettify.min.js && \
    java -jar util/compiler.jar -js build/j/dip3.js > build/j/dip3.min.js || die "Failed to minimize JS"

# combine jQuery and our script
echo "combining JS"
cat build/j/jquery.min.js build/j/prettify.min.js build/j/dip3.min.js > build/j/$revision.js && \
    sed -i -e "s|<script src=j/jquery.js></script>||g" build/*.html && \
    sed -i -e "s|<script src=j/prettify.js></script>||g" build/*.html && \
    sed -i -e "s|<script src=j/dip3.js>|<script src=j/${revision}.js>|g" build/*.html || die "Failed to combine JS"

echo "minimizing CSS"
java -jar util/yuicompressor-2.4.2.jar build/dip3.css > build/$revision.css && \
    java -jar util/yuicompressor-2.4.2.jar build/mobile.css > build/m-$revision.css && \
    java -jar util/yuicompressor-2.4.2.jar build/print.css > build/p-$revision.css && \
    sed -i -e "s|;}|}|g" build/$revision.css && \
    sed -i -e "s|;}|}|g" build/m-$revision.css && \
    sed -i -e "s|;}|}|g" build/p-$revision.css || die "Failed to minimize CSS"

# put CSS inline and remove unused CSS properties on a page-by-page basis
# minimize URLs by stripping "http:" prefix
# add asynchronous Google Analytics script in head (after inline styles)
echo "inlining CSS, minimizing URLs, adding evil tracking code and affiliate links"
ga=`cat j/ga.js`
plug=`cat j/plug.html`
for f in build/*.html; do
  css=`python2.6 util/lesscss.py "$f" "build/$revision.css"` || die "Failed to remove unused CSS"
  mobilecss=`python2.6 util/lesscss.py "$f" "build/m-$revision.css"` || die "Failed to remove unused CSS"
  printcss=`python2.6 util/lesscss.py "$f" "build/p-$revision.css"` || die "Failed to remove unused CSS"
  sed -i -e "s|<link rel=stylesheet href=dip3.css>|<style>${css}</style>|g" -e "s|<link rel=stylesheet media='only screen and (max-device-width: 480px)' href=mobile.css>|<style>@media screen and (max-device-width:480px){${mobilecss}}</style>|g" -e "s|<link rel=stylesheet media=print href=print.css>|<style>@media print{${printcss}}</style>|g" -e "s|</style><style>||g" -e "s|href=index.html|href=/|g" -e "s|</style>|</style>${ga}|g" -e "s|<p id=toc>|${plug}<p id=toc>|g" "$f" || die "Failed to inline CSS"
done

# set file permissions
chmod 755 build/examples build/j build/i build/d && \
    chmod 644 build/*.html build/*.css build/*.txt build/*.zip build/examples/* build/examples/.htaccess build/j/* build/j/.htaccess build/i/* build/i/.htaccess build/d/.htaccess build/.htaccess || die "Failed to reset file permissions"

# ship it!
#die "Aborting without publishing"
echo -n "publishing"
rsync -essh -a build/d/.htaccess build/*.zip diveintomark.org:~/web/diveintopython3.org/d/ && \
    echo -n "." && \
    rsync -essh -a build/i/* build/i/.htaccess diveintomark.org:~/web/wearehugh.com/dip3/ && \
    echo -n "." && \
    rsync -essh -a build/j/$revision.js build/j/html5.js build/j/.htaccess diveintomark.org:~/web/diveintopython3.org/j/ && \
    echo -n "." && \
    rsync -essh -a build/examples build/*.txt build/*.html build/.htaccess diveintomark.org:~/web/diveintopython3.org/ && \
    echo "." || die "Failed to publish to remote server"
