/*
 The following three functions are taken from
 http://code.google.com/p/javascript-search-term-highlighter/
 Copyright 2004 Dave Lemen
 
 Licensed under the Apache License, Version 2.0 (the "License"); 
 you may not use this file except in compliance with the License. 
 You may obtain a copy of the License at 
 
        http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License.
*/

function parseTerms(query) {
    var s = query + '';
    s = s.replace(/(^|\s)(site|related|link|info|cache):[^\s]*(\s|$)/ig, ' ');
    s = s.replace(/[^a-z0-9_\-]/ig, ' '); // word chars only.
    s = s.replace(/(^|\s)-/g, ' '); // +required -excluded ~synonyms
    s = s.replace(/\b(and|not|or)\b/ig, ' ');
    s = s.replace(/\b[a-z0-9]\b/ig, ' '); // one char terms
    return s.split(/\s+/);
}

function getParamValues(url, parameters) {
    var params = [];
    var p = parameters.replace(/,/, ' ').split(/\s+/);
    if (url.indexOf('?') > 0) {
	var qs = url.substr(url.indexOf('?') + 1);
	var qsa = qs.split('&');
	for (i = 0; i < qsa.length; i++) {
	    nameValue = qsa[i].split('=');
	    if (nameValue.length != 2) { continue; }
	    for (j = 0; j < p.length; j++) {
		if (nameValue[0] == p[j]) {
		    params.push(unescape(nameValue[1]).toLowerCase().replace(/\+/g, ' '));
		}
	    }
	}
    }
    return params;
}

function getSearchTerms() {
    var highlighterParameters = 'q as_q as_epq as_oq query search';
    var a = [];
    var params = getParamValues(document.referrer/*document.location.href*/, highlighterParameters);
    var terms;
    for (i = 0; i < params.length; i++) {
	terms = parseTerms(params[i]);
	for (j = 0; j < terms.length; j++) {
	    if (terms[j] !== '') {
		a.push(terms[j].toLowerCase());
	    }
	}
    }
    return a;
}
        
/*

The rest of this script is
Copyright (c) 2009, Mark Pilgrim, All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
*/

var HS = {'visible': 'hide', 'hidden': 'show'};

function hideTOC() {
    var toc = '<span class="nm u">&#8227;</span> <a href="javascript:showTOC()">show table of contents</a>';
    $("#toc").html(toc);
}

function showTOC() {
    var toc = '';
    var old_level = 1;
    var level;
    $('h2,h3').each(function(i, h) {
	    level = parseInt(h.tagName.substring(1), 10);
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
    toc = '<span class="nm u">&#9662;</span> <a href="javascript:hideTOC()">hide table of contents</a><ol start=0><li><a href=table-of-contents.html><span class=u>&uarr;</span> Full table of contents</a></li>' + toc.substring(4);
    $("#toc").html(toc);
}

$(document).ready(function() {
	hideTOC();
	prettyPrint();

	/* on-hover permalink markers on each section header */
	$('*:header[id]').each(function() {
		$('<a class=hl>#</a>').
		    attr('href', '#' + this.id).
		    appendTo(this);
	    });

	/* "hide", "open in new window", and (optionally) "download" widgets on code & screen blocks */
	$("pre > code").each(function(i) {
		var pre = $(this.parentNode);
		if (pre.parents("table").length === 0) {
		    pre.addClass("code");
		}
	    });
	$("pre.code:not(.nd), pre.screen:not(.nd)").each(function(i) {
		/* give each code block a unique ID */
		this.id = "autopre" + i;

		/* wrap code block in a div and insert widget block */
		$(this).wrapInner('<div class=b></div>');
		var widgetHTML = '<div class=w>[<a class=toggle href="javascript:toggleCodeBlock(\'' + this.id + '\')">' + HS.visible + '</a>] [<a href="javascript:plainTextOnClick(\'' + this.id + '\')">open in new window</a>]';
		if ($(this).hasClass('cmdline')) {
		    widgetHTML += ' [<a href="troubleshooting.html#getting-to-the-command-line">command line help</a>]';
		}
		widgetHTML += '</div>';
		$(this).prepend(widgetHTML);
		
		/* move download link into widget block */
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

	$("pre.screen.cmdline:not(.nd)").each(function(i) {
		/* add link to command-line help */
		this.id = "autopre" + i;
	    });
	
	/* make skip links disappear until you tab to them */
	$(".skip a").blur(function() {
		$(this).css({'position':'absolute','left':'0px','top':'-500px','width':'1px','height':'1px','overflow':'hidden'});
	    });
	$(".skip a").blur();
	$(".skip a").focus(function() {
		$(this).css({'position':'static','width':'auto','height':'auto'});
	    });
	
	if (!$.browser.msie) {
	    /* synchronized highlighting on callouts and their associated lines within code & screen blocks */
	    var hip = {'background-color':'#eee','cursor':'default'};
	    var unhip = {'background-color':'inherit','cursor':'inherit'};
	    $("pre.code, pre.screen").each(function() {
		    var _this = $(this);
		    window.setTimeout(function() {
			    var s = '';
			    var ol = _this.next("ol");
			    var refs = _this.find("a:not([href])");
			    refs.each(function(i) {
				    var li = ol.find("li:nth-child(" + (i+1) + ")");
				    s += "<tr><td style='text-align:center;vertical-align:baseline;margin:0;padding:0;width:2em;border:0'><span class='u'>&#x" + (parseInt('2460', 16) + i).toString(16) + ";</span></td><td style='vertical-align:top;margin:0;padding:0;width:auto;border:0'>" + li.html() + "</td></tr>";
				});
			    ol.replaceWith("<table style='width:100%;border-collapse:collapse;margin:0;border:0'>" + s + "</table>");
			    refs.each(function(i) {
				    var a = $(this);
				    var li = a.parents("pre").next("table").find("tr:nth-child(" + (i+1) + ") td:nth-child(2)");
				    li.add(a).hover(function() { a.css(hip); li.css(hip); },
						    function() { a.css(unhip); li.css(unhip); });
				});
			}, 0);
		});
	    
	    /* synchronized highlighting on callouts and their associated table rows */
	    $("table").each(function() {
		    $(this).find("tr:gt(0)").each(function(i) {
			    var tr = $(this);
			    window.setTimeout(function() {
				    var li = tr.parents("table").next("ol").find("li:nth-child(" + (i+1) + ")");
				    if (li.length > 0) {
					li.add(tr).hover(function() { tr.css(hip); li.css(hip); },
							 function() { tr.css(unhip); li.css(unhip); });
				    }
				}, 0);
			});
		});
	}

	/* match <dfn> terms with incoming search keywords and jump to the containing section */
	var searchTerms = getSearchTerms();
	$("dfn").each(function() {
		var dfn = $(this);
		var dfnTerm = dfn.text().toLowerCase();
		if ($.inArray(dfnTerm, searchTerms) != -1) {
		    var section = dfn.parents("p,table,ul,ol,blockquote").prevAll("*:header").get(0);
		    if (section) {
			window.setTimeout(function() {document.location.hash = section.id;}, 0);
			return false;
		    }
		}
	    });

    }); /* document.ready */

function toggleCodeBlock(id) {
    $("#" + id).find("div.b").toggle();
    var a = $("#" + id).find("a.toggle");
    a.text(a.text() == HS.visible ? HS.hidden : HS.visible);
}

function plainTextOnClick(id) {
    var clone = $("#" + id).clone();
    clone.find("div.w, span.u").remove();
    var win = window.open("about:blank", "plaintext", "toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=600,height=400,left=35,top=75");
    win.document.open();
    win.document.write('<pre>' + clone.html());
    win.document.close();
}
