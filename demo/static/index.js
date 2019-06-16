$(document).ready(function(){
	var marker = 'black';
	var markerWidth = 10;

	var lastEvent;
	var mouseDown = false;

	var $canvas = $('canvas');
	var context = $('canvas')[0].getContext('2d');
  var $canvas = $('#canvas');
  context.fillStyle = "white";
  context.fillRect(0, 0, canvas.width, canvas.height);

	$canvas.mousedown(function(e) {
		lastEvent = e;
		mouseDown = true;
	}).mousemove(function(e) {
		if(mouseDown){
			context.beginPath();
			context.moveTo(lastEvent.offsetX, lastEvent.offsetY);
			context.lineTo(e.offsetX, e.offsetY);
			context.lineWidth = markerWidth;
			context.strokeStyle = marker;
			context.lineCap = 'round';
			context.stroke();
			lastEvent = e;
		}
	}).mouseup(function(){
		mouseDown = false;
	});

	$('#clear').click(function(){
		context.clearRect(0, 0, 280, 280);
    context.fillStyle = "white";
    context.fillRect(0, 0, canvas.width, canvas.height);
	});

});
