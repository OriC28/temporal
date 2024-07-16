/*                  SOLUCIONES:
1. CREAR UNA MINI-INTERFAZ PARA INTRODUCIR LAS NOTAS.
2. VALIDAR QUE NO HAYA ERRORRES.
3. SE DEBE PROMEDIAR LA NOTA DEL PROFESOR, CON OTRAS DOS
NOTAS DE TRABAJOS ANTERIORES.
4. SI EL PROMEDIO ES MAYOR A 10/20 ENTONCES APROBÓ LA MATERIA.
*/

const boton = document.getElementById("button");
boton.addEventListener("click", (e)=>{
    e.preventDefault();
    let nota1,nota2,nota3, mensaje;
    try {
        nota1 = parseInt(document.getElementById("studiant-note-1").value);
        nota2 = parseInt(document.getElementById("studiant-note-2").value);
        nota3 = parseInt(document.getElementById("studiant-note-3").value);
        if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3)){ 
            mensaje = "Datos inválidos.";
        }
        resultados = definirDatos(nota1, nota2, nota3);
        mensaje = resultados[0];
        nota = resultados[1];
    }catch (error) {
        nota = "Invalidado";
        mensaje = "El dato ingresado no es válido.";
    }
    abrirModal(nota, mensaje);
});


const definirDatos = (nota1, nota2, nota3)=>{
    let mensaje;
    if(nota1>=0 && nota1<=20 && nota2>=0 && nota2<=20 && nota3>=0 && nota3<=20){
        let promedio = Math.round((nota1 + nota2 + nota3)/3);
        if(promedio>=10 && promedio<=20){
          mensaje = `<span class="green">APROBADO</span>`;
        }else if(promedio>20 || promedio<0){
            mensaje = `<span class="gray">NOTA INVÁLIDA</span>`;
            promedio = 0;
        }else{
            mensaje  = `<span class="red">REPROBADO</span>`
        }
        return [mensaje, promedio];
    }
    mensaje = "Notas inválidas";
    promedio = 0;
    return [mensaje, promedio];
};

const abrirModal = (nota, mensaje)=>{
    document.querySelector(".nota").innerHTML = "Promedio: " + nota;
    document.querySelector(".mensaje").innerHTML = "Estado: " + mensaje;
    let modal = document.querySelector(".modal-container");
    modal.style.animation = "aparecer 1s forwards";
    modal.style.display = "flex";
};