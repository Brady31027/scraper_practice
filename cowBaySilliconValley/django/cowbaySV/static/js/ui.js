function onMouseOverTab(selected) {
	selected.style.background = '#BDBDBD';
}
function onMouseOutTab(selected) {
	selected.style.background = '#f7f7f7';
}

function toast_input_err() {
    var err = document.getElementById('snackbarInputErr');
    err.className = "show";
    setTimeout(function(){ err.className = err.className.replace("show", ""); }, 3000);   
}

function toast_db_err() {
    var err = document.getElementById('snackbarDBErr');
    err.className = "show";
    setTimeout(function(){ err.className = err.className.replace("show", ""); }, 3000);   
}

function toast_suc() {
    var suc = document.getElementById('snackbarSuc');
    suc.className = "show";
    setTimeout(function(){ suc.className = suc.className.replace("show", ""); }, 3000);
}
