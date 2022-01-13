(function ($) {
	'use strict';

	var easyArt = {
		 /* ---------------------------------------------
					## Content Loading
			--------------------------------------------- */
			contentLoading: function () {
				$("body").imagesLoaded(function () {
						$('.preloader').delay(2000).fadeOut('slow');
						setTimeout(function () {
								//After 2s, the no-scroll class of the body will be removed
								$('body').removeClass('no-scroll');
								$("body").addClass("loading-done");
						}, 2000); //Here you can change preloader time
				});
		},

		/* ---------------------------------------------
			## Scroll top
		--------------------------------------------- */
		scroll_top: function () {
			$('body').append(
				"<a href='#top' id='scroll-top' class='topbutton btn-hide'><span  class='fas fa-angle-double-up'></span></a>"
			);
			var $scrolltop = $('#scroll-top');
			$(window).on('scroll', function () {
				if ($(this).scrollTop() > $(this).height()) {
					$scrolltop.addClass('btn-show').removeClass('btn-hide');
				} else {
					$scrolltop.addClass('btn-hide').removeClass('btn-show');
				}
			});
			$("a[href='#top']").on('click', function () {
				$('html, body').animate(
					{
						scrollTop: 0,
					},
					'normal'
				);
				return false;
			});
		},

		/* ---------------------------------------------
			## Menu Script
		--------------------------------------------- */
		menu_script: function () {
			var w = $(window).width();
			if ($('.mobile-sidebar-menu').length && w < 1200) {
				var mobileMenu = $('.site-navigation .navigation').clone().appendTo('.mobile-sidebar-menu');
			}

			if ($('.site-navigation .mainmenu').find('li > a').siblings('.sub-menu')) {
				$('.mainmenu li > .sub-menu').siblings('a').append("<span class='menu-arrow fas fa-angle-down'></span>");
			}

			// Accordion Menu
			var $AccordianMenu = $('.sidebar-menu .navigation a');
			var $mobileSubMenuOpen = $('.hamburger-menus');
			var $overlayClose = $('.overlaybg');

			$overlayClose.on('click', function (e) {
				e.preventDefault();
				$(this).parent().removeClass('sidemenu-active');
				$mobileSubMenuOpen.removeClass("click-menu");
				$('#sticky-header').addClass("active");
			});

			$mobileSubMenuOpen.on('click', function () {
				$(this).toggleClass("click-menu");
				$('.mobile-sidebar-menu').toggleClass("sidemenu-active");
				$('#sticky-header').toggleClass("active");
			});

			$AccordianMenu.on('click', function () {
				var link = $(this);
				var closestUl = link.closest("ul");
				var parallelActiveLinks = closestUl.find(".active")
				var closestLi = link.closest("li");
				var linkStatus = closestLi.hasClass("active");
				var count = 0;

				closestUl.find("ul").slideUp(function () {
					if (++count == closestUl.find("ul").length)
						parallelActiveLinks.removeClass("active");
				});

				if (!linkStatus) {
					closestLi.children("ul").slideDown();
					closestLi.addClass("active");
				}
			});
		},

		/*-------------------------------------------
			## Sticky Header
		--------------------------------------------- */
		sticky_header: function () {
			if ($('#sticky-header.active').length) {
				var stickyMenu = $('.site-header').clone().appendTo('#sticky-header');
				$(window).on('scroll', function () {
					var w = $(window).width();
					if (w > 1200) {
						if ($(this).scrollTop() > 350) {
							$('#sticky-header').slideDown(500);
						} else {
							$('#sticky-header').slideUp(500);
						}
					}
				});
			}
		},

		/* ---------------------------------------------
		   ## Search
	   --------------------------------------------- */
		search: function () {
			$('.search-wrap .search-btn').on('click', function () {
				if ($(this).siblings('.search-form').hasClass('active')) {

					$(this).siblings('.search-form').removeClass('active').slideUp();
					$(this).removeClass('active');
				}
				else {
					$(this).siblings('.search-form').removeClass('active').slideUp();
					$(this).siblings('.search-form').removeClass('active');
					$(this).addClass('active');
					$(this).siblings('.search-form').addClass('active').slideDown();
				}
			});
		},

		/*-------------------------------------------
			## Frontpage Slider
		--------------------------------------------- */
		frontpage_slider: function () {
			if ($('.frontpage-slider-one').length) {
				$('.frontpage-slider-one').owlCarousel({
					center: true,
					items: 1,
					autoplay: false,
					autoplayTimeout: 3000,
					smartSpeed: 800,
					loop: true,
					margin: 0,
					singleItem: true,
					dots: false,
					nav: true,
					navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
				});
			}
			if ($('.frontpage-slider-two').length) {
				$('.frontpage-slider-two').owlCarousel({
					center: true,
					items: 1,
					autoplay: false,
					autoplayTimeout: 3000,
					smartSpeed: 800,
					loop: true,
					margin: 0,
					singleItem: true,
					dots: false,
					nav: true,
					navText: ["<span>Previous</span>", "<span>Next Post</span>"],
				});
			}
			if ($('.frontpage-slider-three').length) {
				$('.frontpage-slider-three').owlCarousel({
					center: false,
					items: 3,
					autoplay: false,
					autoplayTimeout: 3000,
					smartSpeed: 800,
					loop: true,
					margin: 5,
					singleItem: true,
					dots: false,
					nav: true,
					navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
					responsive: {
						280: {
							items: 1,
						},
						576: {
							items: 2,
						},
						768: {
							items: 2,
						},
						992: {
							items: 2,
						},
						1200: {
							items: 3,
						},
					},
				});
			}
			if ($('.frontpage-slider-four').length) {
				$('.frontpage-slider-four').owlCarousel({
					center: false,
					items: 3,
					autoplay: false,
					autoplayTimeout: 3000,
					smartSpeed: 800,
					loop: true,
					margin: 5,
					singleItem: true,
					dots: true,
					nav: false,
					responsive: {
						280: {
							items: 1,
						},
						576: {
							items: 2,
						},
						768: {
							items: 2,
						},
						992: {
							items: 2,
						},
						1200: {
							items: 3,
						},
					},
				});
			}
		},

		/*-------------------------------------------
			## Initialize Plugin
		--------------------------------------------- */
		initialize_plugin: function () {
			// Page Animation Script
			$('[data-animate]').scrolla({
				mobile: true,
				once: true,
			});
		},

		/* ---------------------------------------------
			## Masonry Grid
		--------------------------------------------- */
		masonry_grid: function () {
			var $container = $('.masonry-posts');
			$container.imagesLoaded(function () {
				$container.masonry({
					columnWidth: '.grid-item',
					itemSelector: '.grid-item',
					percentPosition: true
				});
			});
		},

		/* ---------------------------------------------
			## Pop Up Scripts
		 --------------------------------------------- */
		popupScript: function () {
			function getScrollBarWidth() {
				var $outer = $('<div>').css({ visibility: 'hidden', width: 100, overflow: 'scroll' }).appendTo('body'),
					widthWithScroll = $('<div>').css({ width: '100%' }).appendTo($outer).outerWidth();
				$outer.remove();
				return 100 - widthWithScroll;
			}

			// Image Pop up
			var $popupImage = $(".popup-image");
			if ($popupImage.length > 0) {
				$popupImage.magnificPopup({
					type: 'image',
					fixedContentPos: false,
					gallery: { enabled: true },
					removalDelay: 300,
					mainClass: 'mfp-fade',
					callbacks: {
						// This prevenpt pushing the entire page to the right after opening Magnific popup image
						open: function () {
							$(".page-wrapper, .navbar-nav").css("margin-right", getScrollBarWidth());
						},
						close: function () {
							$(".page-wrapper, .navbar-nav").css("margin-right", 0);
						}
					}
				});
			}
		},

		/* ---------------------------------------------
			## Sidebar Script
		--------------------------------------------- */
		sidebarScript: function () {
			var w = $(window).width();
			var MarginTop = w > 1199 ? 85 : 0;
			if ($('.sidebar-items').length) {
				$('.sidebar-items').theiaStickySidebar({
					containerSelector: '.main-wrapper',
					additionalMarginTop: MarginTop,
					minWidth: 992,
				});
			}
		},
		/* ---------------------------------------------
			## Count Down
		--------------------------------------------- */
		count_down: function() {
			if ($('#countdown').length) {
				$('#countdown').syotimer({
						year: 2022,
						month: 6,
						day: 9,
						hour: 20,
						minute: 30
				}); 
			}
		},
		/* ---------------------------------------------
		 function initialize
		 --------------------------------------------- */
		initialize: function () {
			easyArt.contentLoading();
			easyArt.scroll_top();
			easyArt.menu_script();
			easyArt.sticky_header();
			easyArt.search();
			easyArt.initialize_plugin();
			easyArt.frontpage_slider();
			easyArt.popupScript();
			easyArt.sidebarScript();
			easyArt.count_down();
		},
	};
	/* ---------------------------------------------
	 Document ready function
	 --------------------------------------------- */
	$(function () {
		easyArt.initialize();
	});

	$(window).on('load', function () {
		easyArt.contentLoading();
		easyArt.masonry_grid();
	});
})(jQuery);
