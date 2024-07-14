let num1 = 20, nume=3;

try {
    let resultado = num1/num2;
    console.log("La divisón es: " + resultado);
    throw "Ha ocurrido un error";
} catch (error) {
    console.log(error);
}

/*RESUMEN:

throw: Sirve para crear un error, el cual le será pasado
como parámetro a catch. Es posible crear un error de diferentes
tipos de datos: Objeto, String, Array...

finally: Es capaz de tener más "peso" que el mismo Try.

*/