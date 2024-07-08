const contenedor = document.querySelector(".contenedor");
//const child = contenedor.lastElementChild;
//const childrenElements = contenedor.children;

//console.log(childrenElements);

//Métodos de childs:

const parrafoNuevo = document.createElement("P");
parrafoNuevo.innerHTML = "Párrafo";
const h2Nuevo = document.createElement("H2");
h2Nuevo.innerHTML = "Título";

const h2Antiguo = document.querySelector(".antiguo");

//######replaceChild():
//contenedor.replaceChild(h2Nuevo, h2Antiguo);

//######removeChild():
//contenedor.removeChild(h2Antiguo);

//#####hasChildNodes():
//let respuesta = contenedor.hasChildNodes();

//Propiedades de parents:

//######parentElement:
//contenedor.parentElement;

//######parentNode:

console.log(contenedor);
