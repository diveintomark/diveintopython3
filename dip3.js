/*
var LANGS = {'python2': 'Python 2', 'java': 'Java', 'perl5': 'Perl 5', 'clang': 'C'};
*/
var HIDESHOW = {'visible': 'hide', 'hidden': 'show'};

google.load("jquery", "1.3");
google.setOnLoadCallback(function() {
$(document).ready(function() {
/*
  // toggle-able language comparisons
  for (var lang in LANGS) {
    $("blockquote.compare").filter("blockquote." + lang).each(function(i) {
      $(this).wrapInner('<div class="block"></div>');
      $(this).prepend('<div class="widgets">[ <a href="#" onclick="toggleComparisonNotes(\'' + lang + '\');return false" class="toggle">hide ' + LANGS[lang] + ' notes</a> ]</div>');
    });
  }
*/

  // "hide", "open in new window", and (optionally) "download" widgets on code & screen blocks
  $("pre > code").each(function(i) {
    var pre = $(this.parentNode);
    if (pre.parents("table").length == 0) {
      pre.addClass("code");
    }
  });
  $("pre.code, pre.screen").each(function(i) {
    this.id = "autopre" + i;
    $(this).wrapInner('<div class="block"></div>');
    $(this).prepend('<div class="widgets">[<a class="toggle" href="javascript:toggleCodeBlock(\'' + this.id + '\')">' + HIDESHOW['visible'] + '</a>] [<a href="javascript:plainTextOnClick(\'' + this.id + '\')">open in new window</a>]</div>');

    $(this).prev("p.download").each(function(i) {
      $(this).next("pre").find("div.widgets").append(" " + $(this).html());
      this.parentNode.removeChild(this);
    });
  });

  // synchronized highlighting on callouts and their associated lines within code & screen blocks
  $("pre.code, pre.screen").each(function() {
    $(this).find("a:not([href])").each(function(i) {
      var a = $(this);
      var li = a.parents("pre").next("ol").find("li:nth-child(" + (i+1) + ")");
      li.add(a).hover(function() { a.addClass("hover"); li.addClass("hover"); },
                      function() { a.removeClass("hover"); li.removeClass("hover"); });
    });
  });

  // synchronized highlighting on callouts and their associated table rows
  $("table").each(function() {
    $(this).find("tr:gt(0)").each(function(i) {
      var tr = $(this);
      var li = tr.parents("table").next("ol").find("li:nth-child(" + (i+1) + ")");
      if (li.length > 0) {
        li.add(tr).hover(function() { tr.addClass("hover"); li.addClass("hover"); },
                         function() { tr.removeClass("hover"); li.removeClass("hover"); });
      }
    });
  });
}); /* document.ready */
}); /* google.setOnLoadCallback */

/*
function toggleComparisonNotes(lang) {
  // FIXME: save state in cookie, pass state to toggle(), reset text accordingly
  $("blockquote." + lang + " div.block").toggle(false);
  $("blockquote." + lang + " div.widgets a.toggle").text("show " + LANGS[lang] + " notes");
}
*/

function toggleCodeBlock(id) {
  $("#" + id).find("div.block").toggle();
  var a = $("#" + id).find("a.toggle");
  a.text(a.text() == HIDESHOW['visible'] ? HIDESHOW['hidden'] : HIDESHOW['visible']);
}

function plainTextOnClick(id) {
  var clone = $("#" + id).clone();
  clone.find("div.widgets, span").remove();
  var win = window.open("about:blank", "plaintext", "toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=600,height=400,left=35,top=75");
  win.document.open();
  win.document.write('<pre>' + clone.html());
  win.document.close();
}
