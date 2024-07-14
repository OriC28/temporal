const contenedor = document.querySelector(".grid-container");
const boton = document.querySelector(".button-confirm");
const alumnos = [{
    nombre: "Ana Martínez",
    email: "anam233@gmail.com",
    materia: "Física"
},{
    nombre: "José García",
    email: "josegarcia12@gmail.com",
    materia: "Historia"
},{
    nombre: "Pedro Córdoba",
    email: "pedroc0rd0ba@gmail.com",
    materia: "Programación"
}, {
    nombre: "Mariannys Colina",
    email: "mariannyscolina@gmail.com",
    materia: "Matemáticas"
}, {
    nombre: "Miguel Rodríguez",
    email: "miguelr2601@gmail.com",
    materia: "Inteligencia Artificial"
}];

let rowHTML = "";

for(alumno in alumnos){
    let datos = alumnos[alumno];
    let nombre = datos["nombre"];
    let email = datos["email"];
    let materia = datos["materia"];
    rowHTML += `
    <div class="grid-item name">${nombre}</div>
    <div class="grid-item email">${email}</div>
    <div class="grid-item course">${materia}</div>
    <div class="grid-item week">
        <select class="option-choose">
            <option value="Semana 1">Semana 1</option>
            <option value="Semana 2">Semana 2</option>
        </select>
    </div>`
};
contenedor.innerHTML += rowHTML;

boton.addEventListener("click", ()=>{
    let confirmar = confirm("¿Está seguro que desea continuar?");
    if(confirmar){
        let elementos = document.querySelectorAll(".week");
        let semanasElegidas = document.querySelectorAll(".option-choose");
        for(elemento in elementos){
            let semana = elementos[elemento];
            semana.innerHTML = semanasElegidas[elemento].value;
        };
        boton.setAttribute("disabled", "true");
    }
});