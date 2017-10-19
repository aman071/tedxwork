/*=======================================
	Schedule
=======================================*/
$(function() {
	
	// animate on scroll
	new WOW().init();


});
$(function(){

	$("#speakers").magnificPopup({
		delegate: 'a',
		type: 'image',
		gallery: {
			enabled: true
		}
	});

});
$(function(){
	$("#team-members").owlCarousel({
		items: 3,
		autoplay: true,
		smartSpeed: 1000,
		loop: true
	}); 
});
$(function(){
	$("#customers-past-speakers").owlCarousel({
		items: 1,
		autoplay: true,
		smartSpeed: 1000,
		loop: true
	}); 
});