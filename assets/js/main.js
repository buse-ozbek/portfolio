(function () {
	"use strict";

	window.addEventListener("load", () => {
		on_page_load()
	});

	function on_page_load() {
		AOS.init({
			anchorPlacement: "top-left",
			duration: 600,
			easing: "ease-in-out",
			once: true,
			mirror: false,
			disable: "mobile"
		});
	}

	const navbar = document.getElementById("header-nav")
	var body = document.getElementsByTagName("body")[0]
	const scrollTop = document.getElementById("scrolltop")
	window.onscroll = () => {
		if (window.scrollY > 0) {
			navbar.classList.add("fixed-top", "shadow-sm")
			body.style.paddingTop = navbar.offsetHeight + "px"
			scrollTop.style.visibility = "visible";
			scrollTop.style.opacity = 1;
		} else {
			navbar.classList.remove("fixed-top", "shadow-sm")
			body.style.paddingTop = "0px"
			scrollTop.style.visibility = "hidden";
			scrollTop.style.opacity = 0;
		}
	};

})();
let darkBoxVisible = false;

		window.addEventListener('load', (event) => {
			let images = document.getElementById("gallery").querySelectorAll("img");
			if(images !== null && images !== undefined && images.length > 0) {
				images.forEach(function(img) {
					img.addEventListener('click', (evt) => {
						showDarkbox(img.src);
					});
				});
			}
		});

		function showDarkbox(url) {
			if(!darkBoxVisible) {
				let x = (window.innerWidth - 1280) / 2;
				let y = window.scrollY + 50;

				// Create the darkBox
				var div = document.createElement("div");
				div.id = "darkbox";
				div.innerHTML = '<img class="darkboximg" src="'+url+'" />';
				document.body.appendChild(div);
				let box = document.getElementById("darkbox");
				box.style.left = x.toString()+"px";
				box.style.top = y.toString()+"px";
				box.style.height = 'auto';
				box.addEventListener('click', (event) => {
					// Remove it
					let element = document.getElementById("darkbox");
					element.parentNode.removeChild(element);

					darkBoxVisible = false;
				})

				darkBoxVisible = true;

			} else {
				// Remove it
				let element = document.getElementById("darkbox");
				element.parentNode.removeChild(element);

				darkBoxVisible = false;
			}
		}