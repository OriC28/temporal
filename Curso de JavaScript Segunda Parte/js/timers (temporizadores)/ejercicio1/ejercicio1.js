/*REALIZAR:
1. UN FORMULARIO CON: NOMBRE COMPLETO, EMAIL Y MATERIA ADEUDADA.
2. VALIDAR EMAIL Y NOMBRES.
3. SE DEBE ENVIAR AL SERVIDOR DE MANERA PULIDA. */

const nombre = document.getElementById("nombre");
const email = document.getElementById("email");
const materia = document.getElementById("materia");
const boton = document.getElementById("boton");
const resultado = document.querySelector(".resultado");

boton.addEventListener("click", (e)=>{
    e.preventDefault();
    let error = validarCampos();
    if(error[0]){
        resultado.innerHTML = error[1];
        resultado.classList.add("invalid");
        resultado.classList.remove("valid");
    }else{
        resultado.innerHTML = "Solicitud enviada correctamente";
        resultado.classList.add("valid");
        resultado.classList.remove("invalid");
    }
});

const validarCampos = ()=>{
    let error = [];
    if(nombre.value.length < 5 || nombre.value.length > 40){
        error[0] = true;
        error[1] = "El nombre es inválido.";
        return error;
    }else if(email.value.length < 5 || email.value.length > 40 ||
        email.value.indexOf("@")==-1 || email.value.indexOf(".")==-1){
        error[0] = true;
        error[1] = "El email ingresado es inválido."
        return error;
    }else if(materia.value.length < 4 || materia.value.length > 40){
        error[0] = true;
        error[1] = "La materia ingresada no es válida."
        return error;
    }
    error[0] = false;
    return error;
};