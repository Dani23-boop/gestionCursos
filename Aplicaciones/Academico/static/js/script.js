$(document).ready(function(){
    $('.slider').slick({
        autoplay: true, 
        dots: true, 
        infinite: true, 
        speed: 1000, 
        slidesToShow: 3, 
        slidesToScroll: 1, 
        responsive: [
            {
                breakpoint: 768, 
                settings: {
                    slidesToShow: 2, 
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1, 
                }
            }
        ]
    });
});