let screenLeft = window.screenLeft;
let screenTop = window.screenTop;
let x = window.scrollX;
let y = window.scrollY;

document.write(`Left: ${screenLeft} <br>
                Top: ${screenTop}<br><br> `);

/*
#######################################RESUMEN########################################:

Propiedades y métodos vistos:

#Screen:

screenLeft: Devuelve la distancia horizontal del borde de la ventana con la pantalla.
screenTop: Devuelve la distancia vertical del borde de la ventana con la pantalla.
scrollX: Devuelve el número de píxeles que el documento se desplaza de forma vertical.
scrollY: Devuelve el número de píxeles que el documento se desplaza de forma horizontal.
scroll(): Recibe parámetros (x,y) para desplazar el documento hasta un lugar determinado. 

#Location:

location.href: Muestra la localización completa del archivo en cuestión.
location.hostname: Muestra el dominio/IP del documento en cuestión.
location.pathname: Devuelve las "subrutas" que se encuentren abiertas.
location.procol: Devuelve el protocolo utilizado en el sitio web. (https o http).
location.assign(): Reciebe de parámetro una ruta y cargadará dicho nuevo documento.
*/ 