/*
CREAR SOLUCIONES:

1. CREAR UNA FUNCIÓN PARA PREGUNTARLE A COFLA EN QUÉ MATERIA
SE QUIERE INSCRIBIR.
2. SI HAY MÁS DE 20 ALUMNOS ANOTADOS EN LA MATERIA NEGARLE LA
INSCRIPCIÓN.
3. SI HAY MENOS DE 20 ALUMNOS INSCRIBIR A COFLA Y AÑADIRLO A
LA LISTA DE LOS ALUMNOS.
*/

//Materias:
let matematicas = [];
let redes = [];
let cultura = [];
let programacion = [];

//Clase para inscribirse:
class Inscripcion{
	inscribirMateria(nombre, materia=[], materiaNombre){
		if(materia.length<20){
			materia.push(nombre);
			document.write(`Inscripción exitosa, ${nombre}. <br>`);
		}else{
			document.write(`${materiaNombre} ya se encuentra llena. <br>`);
		}
	}
}

//Objeto inscripción:
const inscripcion = new Inscripcion();

//Uso del método. Párametros: (nombreEstudiante, materiaArray, nombreMateria):
inscripcion.inscribirMateria("Carla", cultura, "Cultura");
inscripcion.inscribirMateria("Pedro", cultura, "Cultura");
inscripcion.inscribirMateria("José", cultura, "Cultura");
inscripcion.inscribirMateria("Miguel", cultura, "Cultura");
inscripcion.inscribirMateria("Carlos", cultura, "Cultura");
inscripcion.inscribirMateria("Ana", cultura, "Cultura");