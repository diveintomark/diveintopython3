window.onload = function() {
// synchronized highlighting for code blocks with callouts
var arPre = document.getElementsByTagName('pre');
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
    var olNotes = document.getElementById("skip" + elmTable.id);
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
