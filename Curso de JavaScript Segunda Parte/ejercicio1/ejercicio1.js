//Escribe una función en Python que determine si un número dado es un número narcisista.
//Ejemplo: 1^3 + 5^3 + 3^3 = 153
const boton = document.querySelector(".show");
const h2 = document.querySelector(".result");
const input = document.querySelector(".input");

boton.addEventListener("click", ()=>{
    const numeroIngresado = input.value;
    if (numeroIngresado!="") h2.innerHTML = "Resultado: " + esNarcisista(numeroIngresado);
    else h2.innerHTML = `Resultado: <b class="gray">No válido</b>`;
    h2.style.background = "#fff";
    setTimeout(()=>{
        h2.style.background = "#d1cfcf ";
    },2000);
})

const esNarcisista = (numero)=>{
    let numStr = numero.toString();
    let digitos = numStr.split('');
    let sumaNumeros = 0;
    for (i of digitos){
        let digito = Math.pow(parseInt(i), digitos.length);
        sumaNumeros += digito;
    }
    if (sumaNumeros == numero) return `<b class="green">Sí es narcisista</b>`;
    return `<b class="red">No es narcisista</b>`;
};

