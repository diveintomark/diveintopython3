/*
var LANGS = {'python2': 'Python 2', 'java': 'Java', 'perl5': 'Perl 5', 'clang': 'C'};
*/
//google.load("jquery", "1.3");
//google.setOnLoadCallback(function() {
$(document).ready(function() {
  hideTOC();

  /* "hide", "open in new window", and (optionally) "download" widgets on code & screen blocks */
  var HS = {'visible': 'hide', 'hidden': 'show'};
  $("pre > code").each(function(i) {
    var pre = $(this.parentNode);
    if (pre.parents("table").length == 0) {
      pre.addClass("code");
    }
  });
  $("pre.code, pre.screen").each(function(i) {
    this.id = "autopre" + i;
    $(this).wrapInner('<div class="b"></div>');
    $(this).prepend('<div class="w">[<a class="toggle" href="javascript:toggleCodeBlock(\'' + this.id + '\')">' + HS['visible'] + '</a>] [<a href="javascript:plainTextOnClick(\'' + this.id + '\')">open in new window</a>]</div>');

    $(this).prev("p.d").each(function(i) {
      $(this).next("pre").find("div.w").append(" " + $(this).html());
      this.parentNode.removeChild(this);
    });

    /* create skip links */
    var postelm = $(this).next().get(0);
    var postid = postelm.id || ("postautopre" + i);
    postelm.id = postid;
    $(this).before('<p class=skip><a href=#' + postid + '>skip over this code listing</a>');
  });

  /* make skip links disappear until you tab to them */
  $(".skip a").blur(function() {
    $(this).css({'position':'absolute','left':'0px','top':'-500px','width':'1px','height':'1px','overflow':'hidden'});
  });
  $(".skip a").blur();
  $(".skip a").focus(function() {
    $(this).css({'position':'static','width':'auto','height':'auto'});
  });

  // synchronized highlighting on callouts and their associated lines within code & screen blocks
  var hip = {'background-color':'#eee','cursor':'default'};
  var unhip = {'background-color':'inherit','cursor':'inherit'};
  $("pre.code, pre.screen").each(function() {
    $(this).find("a:not([href])").each(function(i) {
      var a = $(this);
      var li = a.parents("pre").next("ol").find("li:nth-child(" + (i+1) + ")");
      li.add(a).hover(function() { a.css(hip); li.css(hip); },
                      function() { a.css(unhip); li.css(unhip); });
    });
  });

  // synchronized highlighting on callouts and their associated table rows
  $("table").each(function() {
    $(this).find("tr:gt(0)").each(function(i) {
      var tr = $(this);
      var li = tr.parents("table").next("ol").find("li:nth-child(" + (i+1) + ")");
      if (li.length > 0) {
        li.add(tr).hover(function() { tr.addClass("h"); li.addClass("h"); },
                         function() { tr.removeClass("h"); li.removeClass("h"); });
      }
    });
  });

/*
  // toggle-able language comparisons
  for (var lang in LANGS) {
    $("blockquote.compare").filter("blockquote." + lang).each(function(i) {
      $(this).wrapInner('<div class="block"></div>');
      $(this).prepend('<div class="w">[ <a href="#" onclick="toggleComparisonNotes(\'' + lang + '\');return false" class="toggle">hide ' + LANGS[lang] + ' notes</a> ]</div>');
    });
  }
*/

}); /* document.ready */
//}); /* google.setOnLoadCallback */

/*
function toggleComparisonNotes(lang) {
  // FIXME: save state in cookie, pass state to toggle(), reset text accordingly
  $("blockquote." + lang + " div.block").toggle(false);
  $("blockquote." + lang + " div.w a.toggle").text("show " + LANGS[lang] + " notes");
}
*/

function toggleCodeBlock(id) {
  $("#" + id).find("div.b").toggle();
  var a = $("#" + id).find("a.toggle");
  a.text(a.text() == HS['visible'] ? HS['hidden'] : HS['visible']);
}

function plainTextOnClick(id) {
  var clone = $("#" + id).clone();
  clone.find("div.w, span").remove();
  var win = window.open("about:blank", "plaintext", "toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=600,height=400,left=35,top=75");
  win.document.open();
  win.document.write('<pre>' + clone.html());
  win.document.close();
}

function hideTOC() {
  var toc = '<span>&#8227;</span> <a href="javascript:showTOC()">show table of contents</a>';
  $("#toc").html(toc);
}

function showTOC() {
  var toc = '';
  var old_level = 1;
  $('h2,h3').each(function(i, h) {
    level = parseInt(h.tagName.substring(1));
    if (level < old_level) {
      toc += '</ol>';
    } else if (level > old_level) {
      toc += '<ol>';
    }
    toc += '<li><a href=#' + h.id + '>' + h.innerHTML + '</a>';
    old_level = level;
  });
  while (level > 1) {
    toc += '</ol>';
    level -= 1;
  }
  toc = '<span>&#9662;</span> <a href="javascript:hideTOC()">hide table of contents</a>' + toc;
  $("#toc").html(toc);
}
