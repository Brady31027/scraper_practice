function onMouseOverTab(selected) {
	selected.style.background = '#BDBDBD';
}
function onMouseOutTab(selected) {
	selected.style.background = '#f7f7f7';
}
function toast_early_check() {
    // Get the snackbar DIV
    var err = document.getElementById('snackbarErr');
    var contents = document.getElementById('contents').value.trim();
    if (contents.length > 0) {
        err.className = "show";
        setTimeout(function(){ err.className = err.className.replace("show", ""); }, 3000);
    }
}

function toast_err() {
    // Get the snackbar DIV
    var err = document.getElementById('snackbarErr');
    err.className = "show";
    setTimeout(function(){ err.className = err.className.replace("show", ""); }, 3000);
    
}

function toast_suc() {
    // Get the snackbar DIV
    var suc = document.getElementById('snackbarSuc');
    suc.className = "show";
    setTimeout(function(){ suc.className = suc.className.replace("show", ""); }, 3000);
    
}
