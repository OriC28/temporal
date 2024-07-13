const boton  = document.querySelector(".button");
const containerInternal = document.querySelector(".internal-container");
const containerExternal = document.querySelector(".external-container");

boton.addEventListener("click", (e)=>{ //El parámetro "e" se refiere a "event", se utiliza de forma predeterminada.
    alert("He dado click en el botón.");
    e.stopPropagation(); //Hará que sólo se ejecute este evento. (Siempre y cuando los otros eventos no tengan el parámetro "true").
});

containerInternal.addEventListener("click", (e)=>{
    alert("He dado click en el div azul.");
});

containerExternal.addEventListener("click", (e)=>{
    alert("He dado click en el div rojo.");
}, true); //Con el parámetro "true" forzamos qué evento se ejecutará primero.

//NOTA: Los eventos se ejecutan desde el elemento más específico hasta el menos específico.