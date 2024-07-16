/*CREAR UN SISTEMA QUE ALMACENE TODA LA INFORMACIÓN DE LAS MATERIAS Y LAS MUESTRE EN PANTALLA
DE FORMA ORDENADA.*/
const materiasHTML = document.querySelector(".materias-container");
materias = [
    {nombre: "Programación", nota: 16},
    {nombre: "Física", nota: 18},
    {nombre: "Historia", nota: 17},
    {nombre: "Matemáticas", nota: 20}
];
const obtenerMateria = (index)=>{
    return new Promise((resolve, reject)=>{
        materia = materias[index];
        if (materia==undefined) reject("La materia no está disponible.");
        setTimeout(() => {resolve(materia)}, 1000);
    });
};

const devolverInfo = async ()=>{
    let materiasObtenidas = [];
    for (let i = 0; i<materias.length; i++) {
        materiasObtenidas[i] = await obtenerMateria(i);
        let newHTMLCode = `
        <div class="materia-unidad">
           <div class="nombre">${materiasObtenidas[i].nombre}</div>
           <div class="nota">${materiasObtenidas[i].nota}</div>
        </div>`;
        materiasHTML.innerHTML += newHTMLCode;
    };
};

devolverInfo();