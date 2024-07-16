const objeto = {
    nombre: "José",
    apellido: "García",
    edad: 24,
    ubicacion: "Islandia"
};

const obtenerInformacion = ()=>{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            resolve(objeto), 3000;
        })
    })
};

const mostrarInformacion = async ()=>{
    datos = await obtenerInformacion();
    console.log(datos);
}

mostrarInformacion();