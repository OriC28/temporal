const input = document.querySelector("input");
const contenedor = document.querySelector(".container");
                        //EVENTO SELECT:
input.addEventListener("select", (e)=>{
    let start = e.target.selectionStart;
    let end = e.target.selectionEnd;
    let newValue = input.value.substring(start, end);
    contenedor.innerHTML = `El texto seleccionado es: <b>${newValue}</b>`;
});
                        //EVENTO KEYUP (YA VISTO):
input.addEventListener("keyup", (e)=>{
    let tecla = e.key;
    contenedor.innerHTML = `La última tecla presionada fue: <b>${tecla}</b>`;
});