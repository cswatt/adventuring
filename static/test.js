function GetChar(event){
	var chCode = ('charCode' in event) ? event.charCode : event.keyCode;
	if (chCode == 13)
		ProcessInput();
}

function ProcessInput(){
	var newinput = $('#input').html(); //get input from box
	$('#console').append("> " + newinput + '\n'); //add input to textarea
	$('#console').scrollTop($('#console')[0].scrollHeight); //scroll textarea to bottom
	$('#input').html(''); //clear input box
	SendInput(newinput);
}

function SendInput(contents){
	$.ajax({
		url: "/story.py",
		type: "post",
		datatype:"text",
		data: 'hello world',
		success: function(response){
			alert(response);
		}
	});
}

/*init*/
$(document).ready(function(){
	$('#input').focus();
});