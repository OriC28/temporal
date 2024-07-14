/*               EVENTO SETTIMEOUT:
setTimeout recibe de parámetros: una función y
el tiempo en milisegundos en el que se ejecutará
la misma.
*/
const temporizador = setTimeout(() => {
    alert("Epale, chamo.");
}, 2000);

clearTimeout(temporizador); //Evita que se ejecute el evento.


/*              EVENTO SETINTERVAL: 
Similar a setTimeout pero este evento ejecutará la 
función cada n cantidad de milisegundos proporcionados.
*/
const intervalo = setInterval(() => {
    alert("Hola, chamo");
}, 2000);

clearInterval(intervalo); //Detiene la ejecución constante del evento.
