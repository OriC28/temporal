const contenedor = document.querySelector(".contenedor");
const fragmento = document.createDocumentFragment();
for(let i=0; i<10; i++){
	const item = document.createElement("LI");
	item.innerHTML = `Item n° ${i + 1}`;
	fragmento.appendChild(item);
}

contenedor.appendChild(fragmento);

console.log(contenedor);