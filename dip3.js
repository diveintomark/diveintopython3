function getPreContent(elm) {
    if (elm.nodeType == 3) {
        // this string will be concatenated to a "<pre>" and displayed as HTML, so escape brackets
        return elm.nodeValue.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }
    if (elm.nodeType != 1) {
        // don't include comments
	return '';
    }
    if (elm.nodeName.toLowerCase() == 'span') {
        // don't include callouts
        return '';
    }
    if (elm.className && elm.className == 'widgets') {
        // don't include the "view as plain text" and "download" widgets
        return '';
    }
    var arChildren = elm.childNodes;
    var count = arChildren.length;
    var s = '';
    for (var i = 0; i < count; i++) {
        s += getPreContent(arChildren[i]);
    }
    return s;
}

function plainTextOnClick(id) {
    var elm = document.getElementById(id);
    if (!elm) { return; }
    var win = window.open("about:blank", "plaintext", "toolbar=0,scrollbars=1,location=0,statusbar=0,menubar=0,resizable=1,width=600,height=400,left=35,top=75");
    win.document.open();
    win.document.write('<pre>' + getPreContent(elm));
    win.document.close();
}

function toggleBlock(id) {
    var elm = document.getElementById(id);
    if (!elm) { return; }
    var elmToggle = document.getElementById(id + 'toggle');
    if (!elmToggle) { return; }
    var elmBlock = document.getElementById(id + 'block');
    if (!elmBlock) { return; }
    if (elmToggle.firstChild.nodeValue == 'show') {
	elmBlock.style.display = 'block';
	elmToggle.firstChild.nodeValue = 'hide';
    } else {
	elmBlock.style.display = 'none';
	elmToggle.firstChild.nodeValue = 'show';
    }
}

window.onload = function() {
// downloadable code samples
var arPre = document.getElementsByTagName('pre');
for (var i = arPre.length - 1; i >= 0; i--) {
    var elmPre = arPre[i];
    if (elmPre.className == 'screen' || elmPre.firstChild.nodeName.toLowerCase() == 'code') {
	var id = elmPre.id;
	if (!id) {
	    id = "autopre" + i;
	    elmPre.id = id;
	}
	elmPre.innerHTML = '<div id="' + id + 'widgets" class="widgets">[<a id="' + id + 'toggle" class="toggle" href="javascript:toggleBlock(\'' + id + '\')">hide</a>] [<a id="' + id + 'plaintext" href="javascript:plainTextOnClick(\'' + id + '\')">open in new window</a>]</div><div id="' + id + 'block">' + elmPre.innerHTML + '</div>';
    }
  
}

// synchronized highlighting for code blocks with callouts
// note: must do this after downloadable code samples loop because
//       setting innerHTML destroys event handlers
for (var i = arPre.length - 1; i >= 0; i--) {
    var elmPre = arPre[i];
    var arCallout = elmPre.getElementsByTagName('span');
    if (arCallout.length == 0) { continue; }
    var elmCalloutList = elmPre.nextSibling;
    while (elmCalloutList && (elmCalloutList.nodeType != 1)) {
        elmCalloutList = elmCalloutList.nextSibling;
    }
    if (elmCalloutList.nodeName.toLowerCase() != 'ol') { continue; }
    var arCalloutListItem = elmCalloutList.getElementsByTagName('li');
    if (arCalloutListItem.length != arCallout.length) {
        alert('Number of callouts != number of callout list items:\n' + elmPre.innerHTML);
        continue;
    }
    for (var j = arCallout.length - 1; j >= 0; j--) {
        var elmCallout = arCallout[j].parentNode;
        var elmCalloutListItem = arCalloutListItem[j];
        elmCallout._li = elmCalloutListItem;
        elmCalloutListItem._div = elmCallout;
        elmCallout.onmouseover = function() {
           this.className = 'hover';
           this._li.className = 'hover';
        };
        elmCalloutListItem.onmouseover = function() {
           this.className = 'hover';
           this._div.className = 'hover';
        };
        elmCallout.onmouseout = function() {
           this.className = '';
           this._li.className = '';
        };
        elmCalloutListItem.onmouseout = function() {
           this.className = '';
           this._div.className = '';
        };
        
    }
}

// synchronized highlighting for tables with callouts
var arTables = document.getElementsByTagName('table');
for (var i = arTables.length - 1; i >= 0; i--) {
    var elmTable = arTables[i];
    var olNotes = document.getElementById('skip' + elmTable.id);
    if (!olNotes) { continue; }
    var arNotes = olNotes.getElementsByTagName('li');
    var arTableRows = elmTable.getElementsByTagName('tr');
    if (arNotes.length == 0) { continue; }
    for (var j = arTableRows.length - 1; j >= 1; j--) {
        var elmTableRow = arTableRows[j];
        var elmNote = arNotes[j - 1];
        elmTableRow._li = elmNote;
        elmNote._tr = elmTableRow;
        elmTableRow.onmouseover = function() {
           this.className = 'hover';
           this._li.className = 'hover';
        };
        elmNote.onmouseover = function() {
           this.className = 'hover';
           this._tr.className = 'hover';
        };
        elmTableRow.onmouseout = function() {
           this.className = '';
           this._li.className = '';
        };
        elmNote.onmouseout = function() {
           this.className = '';
           this._tr.className = '';
        };
    }
}

}
