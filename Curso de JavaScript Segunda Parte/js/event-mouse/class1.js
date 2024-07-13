const boton = document.querySelector(".button");
const containerInternal = document.querySelector(".internal-container");
const containerExternal = document.querySelector(".external-container");

/*                     EVENTO CLICK:

NOTA: El evento "click" se ejecuta cuando se da click y se suelta el elemento.

boton.addEventListener("click", (e)=>{ 
    alert("He dado click en el botón.");
});
*/

/*                    EVENTO DOBLE CLICK:

boton.addEventListener("dblclick", (e)=>{ 
    alert("He dado click en el botón.");
});
*/

/*                   EVENTO MOUSE SOBRE:

containerInternal.addEventListener("mouseover", (e)=>{
    containerInternal.style.background = "black";
});
*/

/*                 EVENTO MOUSE FUERA DE:

containerInternal.addEventListener("mouseout", (e)=>{
    containerInternal.style.background = "black";
    containerExternal.style.background = "purple";
});
*/

/*                 EVENTO CONTEXTMENU: 

containerInternal.addEventListener("contextmenu", (e)=>{
    alert("Accionando un evento...");
});
*/

/*                 EVENTO MOUSESDOWN: 

NOTA: El evento "mousedown" a diferencia de "click" no necesita que el usuario presione-suelte el mouse.
Con sólo hacer click el evento se ejecutará.

boton.addEventListener("mousedown", (e)=>{ 
    alert("He dado click en el botón.");
});
*/