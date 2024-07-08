const contenedor = document.querySelector(".contenedor");
//Creando elemento Input Type text:
const inputText = document.createElement("INPUT");
//Creando elemento Input Type submit:
const inputButton = document.createElement("INPUT");
//Creando elemento Form:
const formulario = document.createElement("FORM");
//Agregando los inputs al formulario:
formulario.appendChild(inputText);
formulario.appendChild(inputButton);
//Estableciendo type en los inputs:
inputText.setAttribute("type", "text");
inputButton.setAttribute("type", "submit");
//Agregando atributos y estilos:
inputText.required = "Obligatorio";
inputButton.style.color = "#444444";
//Agregando el formulario al div:
contenedor.appendChild(formulario);

console.log(formulario);
 
