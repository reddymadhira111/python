$(document).ready(function() {
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
			// Left arrow key pressed
			case 37:
				$('img').animate({left: "-=10px"}, 'fast');
				break;
			// Up Arrow Pressed
			case 38:
			    $('img').animate({top:'-=10px'},'fast');
				// Put our code here
				break;
			// Right Arrow Pressed
			case 39:
				// Put our code here
				$('img').animate({right:'+=10px'},'fast');
				break;
			// Down Arrow Pressed
			case 40:
				// Put our code here
				$('img').animate({top:'+=10px'},'fast');
				break;
		}
	});
});