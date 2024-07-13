let youtubeURL = "https://youtube.com";
//let ventana = window.open(youtubeURL);
let respuesta = confirm("¿Estás seguro que deseas salir?");

if (respuesta){
    alert("Ok, bobo");
}else{
    alert("Chao, bobo");
}

/*
################################RESUMEN#######################################

Métodos vistos:

open(): Permite abrir un sitio web/ventana en concreto.
close(): Cierra el sitio web/ventana en concreto.
closed(): Verifica si la ventana determinada está abierta o cerrada.
alert(): Muestra un mensaje al usuario.
prompt(): Permite ingresar datos por teclado.
confirm(): Permite ingresar datos por teclado para confirmar o cancelar una acción.
stop(): Detiene la carga de un sitio web/ventana determinada.
print(): Imprime el documento del sitio web en cuestión.
*/