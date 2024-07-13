const button = document.querySelector(".button");

//CON UNA FUNCIÓN SIN PARÁMETROS:
button.addEventListener("click", saludar);

function saludar(){
    alert("Hola, qué tal.");
}

//CON UNA FUNCIÓN CON PARÁMETROS: 
let nombre = "Gabriel";
let nombre2 = "Ana";
button.addEventListener("click",()=>{
    alert("Hola, " + nombre + " y " + nombre2);
});

//ELIMINAR EVENTO:
button.addEventListener("click", saludar);

function saludar(){
    alert("Hola, qué tal.");
    button.removeEventListener("click", saludar);
}

