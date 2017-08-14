function onMouseOverTab(selected) {
	selected.style.background = '#BDBDBD';
}
function onMouseOutTab(selected) {
	selected.style.background = '#f7f7f7';
}
function toast() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar")

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function queryRooms(){
	var rooms = document.getElementsByClassName('feroom');
	return rooms.length;
}

function generateRoomDiv(newRoomIndex){
	var plainHtml = '<div class="room_label">Room '+ newRoomIndex +'</div> \
					<span class="rlenght">Length</span> \
					<input type="text" name="fe_room_length_ft[]" size="5"/> \
					<span class="size_ft">ft</span> \
					<input type="text" name="fe_room_length_in[]" size="5"/> \
					<span class="size_in">in,</span> \
					<span class="rwidth">Width</span> \
					<input type="text" name="fe_room_width_ft[]" size="5"/> \
					<span class="size_ft">ft</span> \
					<input type="text" name="fe_room_width_in[]" size="5"/> \
					<span class="size_in">in</span>' ;
	if (newRoomIndex > 1) {
		plainHtml += '<span class="dashicons dashicons-no-alt fe_remove_room" \
					             title="Remove this room" onclick="deleteRoom(this)" id='+ newRoomIndex +'></span>';
    }

	return plainHtml;
}
function addRoom(){
	var newRoomIndex = queryRooms() + 1;
	var div = document.createElement('div');
    div.className = 'feroom';
    div.id = newRoomIndex;
    div.innerHTML = generateRoomDiv(newRoomIndex);
	document.getElementById('roomParent').appendChild(div);
}


function adjustRooms(){
	var children = document.getElementById('roomParent').childNodes;
 	var total = document.getElementsByClassName('feroom').length;
 	var cnt = 0;
 	for (var i = 0;; i++) {
 		if (children[i].innerHTML) {
 			//alert(children[i].innerHTML);
 			cnt += 1;
 			children[i].id = cnt;
 			children[i].innerHTML = generateRoomDiv(cnt);
 		}
 		if (cnt == total){
 			break;
 		}
 	}
}

function deleteRoom(selected){
	var toBeDeletedRoom = selected.getAttribute('id');
	var element = document.getElementById(toBeDeletedRoom);
	element.outerHTML = "";
	delete element;
	adjustRooms();	
}
