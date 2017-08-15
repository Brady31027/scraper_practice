function onMouseOverTab(selected) {
	selected.style.background = '#BDBDBD';
}
function onMouseOutTab(selected) {
	selected.style.background = '#f7f7f7';
}
function toast() {
    // Get the snackbar DIV
    var suc = document.getElementById("snackbar_suc");
    var err = document.getElementById("snackbar_err");
    var contents = document.getElementById("contents").value.trim();
    var ui;
    if (contents.length > 0) {
    	ui = suc;
    } else {
    	ui = err;
    }

    ui.className = "show";
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ ui.className = ui.className.replace("show", ""); }, 3000);
}