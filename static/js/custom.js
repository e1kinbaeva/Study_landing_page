(function($) {
    'use strict'; // Start of use strict

    $(window).on("load scroll", function() {

        /*------------------------------------------------------------------
        Loader
        ------------------------------------------------------------------*/
        $("#loader").fadeOut("fast");
        // map zooming 	 
        $('.google-map').on('click', function() {
            $('.google-map').find('iframe').css("pointer-events", "auto");
        });
		 /*----------------------------------------------------
          Start Change Menu Bg
		 ----------------------------------------------------*/
        $(window).on('scroll', function() {
            if ($(window).scrollTop() > 200) {
                $('.header-top-area').addClass('menu-bg');
            } else {
                $('.header-top-area').removeClass('menu-bg');
            }
        });
       /*------------------------------------------------------------------
        Animation Numbers
        ------------------------------------------------------------------*/
        $('.animateNumber').each(function() {
            var num = $(this).attr('data-num');

            var top = $(document).scrollTop() + ($(window).height());
            var pos_top = $(this).offset().top;
            if (top > pos_top && !$(this).hasClass('active')) {
                $(this).addClass('active').animateNumber({
                    number: num
                }, 2000);
            }
        });
        $('.animateProcent').each(function() {
            var num = $(this).attr('data-num');
            var percent_number_step = jQuery.animateNumber.numberStepFactories.append('%');
            var top = $(document).scrollTop() + ($(window).height());
            var pos_top = $(this).offset().top;
            if (top > pos_top && !$(this).hasClass('active')) {
                $(this).addClass('active').animateNumber({
                    number: num,
                    numberStep: percent_number_step
                }, 2000);
                $(this).css('width', num + '%');
            }
        });
    });
		
    /*------------------------------------------------------------------
     Scroll Top
     ------------------------------------------------------------------*/
    $.scrollUp({
        scrollText: '<i class="fa fa-chevron-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    /*----------------------------------------------------
                  Portfolio Isotope
   ----------------------------------------------------*/
    var body_s = $('body'),
        window_s = $(window);

    //======= ISOTOP FILTERING JS  ========//
    window_s.on('load', function() {
        var grid_container = $('.portfolio-container'),
            grid_item = $('.work');


        grid_container.imagesLoaded(function() {
            grid_container.isotope({
                itemSelector: '.work',
                layoutMode: 'masonry'
            });
        });

        $('.portfolio-filter').find('li').on('click', function(e) {
            $('.portfolio-filter li.active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            grid_container.isotope({
                filter: selector
            });
            return false;
            e.preventDefault();
        });
    });


    //======= MAGNIFIC POPUP ========//
    $('.work a').magnificPopup({
        type: 'inline'
    });
    /*------------------------------------------------------------------
    Navigation Hover effect
    ------------------------------------------------------------------*/
    // jQuery for page scrolling feature - requires jQuery Easing plugin

    $('.smoth-scroll').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });
    // Highlight the top nav as scrolling occurs

    $('body').scrollspy({
        target: '.navbar-default',
        offset: 70
    });
    // Closes the Responsive Menu on Menu Item Click

    $('.navbar-collapse ul li a:not(.dropdown-toggle)').on('click', function() {
        $('.navbar-toggle:visible').click();
    });

    /*------------------------------------------------------------------
   	 Scrollup opacity downarrow 
	 ------------------------------------------------------------------*/
    var bottom_arrow = $('.bottom_row, .banner-content');
    $(window).on('scroll', function() {
        var st = $(this).scrollTop();
        bottom_arrow.css({
            'opacity': (1 - (st / 350))
        });
    });
	/*------------------------------------------------------------------
    Owl Carousel for screenshots
	------------------------------------------------------------------*/
    var owl = $("#testimonials");
    owl.owlCarousel({
        nav: true,
        margin: 10,
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            450: {
                items: 1
            },
            600: {
                items: 2
            },
            700: {
                items: 2
            },
            1000: {
                items: 3
            },
            1200: {
                items: 3
            },
            1400: {
                items: 3
            },
            1600: {
                items: 3
            }
        }
    });
    /*------------------------------------------------------------------
    	theme color change
    ------------------------------------------------------------------*/

    var theme_settings = $(".theme-settings").find(".theme-color");
    theme_settings.on('click', function() {
        var val = $(this).attr('data-color');
        $('#style_theme').attr('href', 'css/' + val + '.css');
        $(".logo-change").attr('src', 'img/logo-' + val + '.png');

        theme_settings.removeClass('theme-active');
        theme_settings.addClass('theme-active');
        return false;
    });
    $(".theme-click").on('click', function() {
        $("#switcher").toggleClass("active");
        return false;
    });

})(jQuery);