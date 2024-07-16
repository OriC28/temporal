
const nombre = "Cafrlos";
const promesa = new Promise((resolve, reject)=>{ //Se crea un objeto de la clase Promise.
    if(nombre!="Carlos") reject("El nombre no es Carlos"); /*reject se utiliza cuando ocurra un error en 
                                                            el programa o alguna condición no se cumpla. */
    else resolve(nombre);//En caso de éxito, resolve se ejecutará.                                 
});

//Accediendo a los valores devueltos.
promesa.then((valor)=>{
    console.log(valor); //Si todo sale bien devolverá el valor en resolve.
}).catch((e)=>{
    console.log(e); //En caso de algún error mostrará el mensaje de reject.
});
