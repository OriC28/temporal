/*COFLA NECESITA COMPRAR UNA PANTALLA FUL HD*/

let alto = window.screen.availHeight;
let ancho = window.screen.availWidth;
let resolucion = alto + "x" + ancho;

let comprar = confirm("La pantalla actual tiene una resolución de: " + resolucion + " ¿Desea comprarla?");

if (comprar){
    alert("Compra realizada con éxito.");
}else{
    alert("Compra cancelada.");
}