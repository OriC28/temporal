//Clase persona con parámetros: nombre, instagram.
class Persona{
    constructor(nombre, instagram){
        this.nombre = nombre;
        this.instagram = instagram;
    }
};
//Datos de las personas: nombres e instagrams.
const data = [
    ["José García", "@joseG28"],
    ["Mariana López", "@marilopz"],
    ["Melisa Díaz", "@melissadiaz"]
], personas = []; //array vacío para llenar con los objetos a crear (personas).

//Creando varios objetos y llenado el array personas.
for (let i = 0; i<data.length; i++) {
   personas[i] = new Persona(data[i][0], data[i][1]);
};

//Funcion con el parámetro índice, retorna una promesa: ya sea con reject (error) o resolve (valor).
//Dependiendo de si se cumple o no la condición.
const obtenerPersona = (index)=>{
   return new Promise((resolve, reject)=>{
    if(personas[index]==undefined) reject("No se ha encontrado a la persona.");
    else {resolve(personas[index])};
})};

//Función con el parámetro índice, retorna una promesa: ya sea con reject (error) o resolve (valor).
//Dependiendo de si se cumple o no la condición. 
const obtenerInstagram = (index)=>{
    return new Promise((resolve, reject)=>{
        if(personas[index].instagram==undefined) reject("No se ha encontrado el Instagram");
        else {resolve(personas[index].instagram)};
})};
//Llamando a la función obtenerPersona.
obtenerPersona(4).then((persona)=>{ //Si todo sale bien entonces obtener el valor persona.
    console.log(persona.nombre); //Accedemos al nombre de la persona con índice 4.
    return obtenerInstagram(4); //retorna la promesa de obtenerInstagram
    }).then((instagram)=>{ //Si todo sale bien entonces obtener el valor del instagram.
        console.log(instagram); //Mostrar Instagram
    }).catch((e)=>{ //Si cualquier promesa retorna un error entonces...
        console.log(e); //Mostrar el error correspondiente.
    });