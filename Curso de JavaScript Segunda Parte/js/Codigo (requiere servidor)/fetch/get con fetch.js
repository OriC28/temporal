//PETICION GET CON FETCH: 

/*NOTAS: 
1) fetch tiene el método GET por defecto.
2) fetch devuelve una promesa.
3) se accede a la promesa con el método then.
4) directamente los métodos json() y text()
convierten la petición a objeto/texto respectivamente.
*/ 
const request = fetch("https://dragonball-api.com/api/characters/1");
request.then(answer => answer.json()).
        then(answer => console.log(answer));