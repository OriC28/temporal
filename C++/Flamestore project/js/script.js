const button = document.querySelector(".button");

button.addEventListener("click", (event) => {
	window.print();
});

window.addEventListener("beforeprint", (event) => {
	button.style.display = "None";
});

window.addEventListener("afterprint", (event) => {
	button.style.display = "block";
});