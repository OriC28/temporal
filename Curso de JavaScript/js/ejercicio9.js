/*
CREAR SOLUCIONES:

1. CREAR UNA FUNCIÓN PARA PREGUNTARLE A COFLA EN QUÉ MATERIA
SE QUIERE INSCRIBIR.
2. SI HAY MÁS DE 20 ALUMNOS ANOTADOS EN LA MATERIA NEGARLE LA
INSCRIPCIÓN.
3. SI HAY MENOS DE 20 ALUMNOS INSCRIBIR A COFLA Y AÑADIRLO A
LA LISTA DE LOS ALUMNOS.
*/

let matematicas = ["Luis", "Karina"];
let programacion = ["Miriam", "Ángel", "Pedro"];
let redes = ["Marianys", "Lady"];
let cultura = ["Luis"];

const inscribir = (nombre, materia)=>{
	switch(materia){
		case "matematicas":
			if(matematicas.length<=20){
				matematicas.push(nombre);
				document.write(`Te has inscrito exitosamente, ${nombre} <br>`);
			}else{
				document.write("Ya se ha llenado esta materia.<br>");
			}break;
		case "programacion":
			if(programacion.length!=20){
				programacion.push(nombre);
				document.write(`Te has inscrito exitosamente, ${nombre}<br>`);
			}else{
				document.write("Ya se ha llenado esta materia.<br>");
			}break;
		case "redes":
			if(redes.length!=20){
				redes.push(nombre);
				document.write(`Te has inscrito exitosamente, ${nombre}<br>`);
			}else{
				document.write("Ya se ha llenado está materia.<br>");
			}break;
		case "cultura":
			if(cultura.length!=20){
				cultura.push(nombre);
				document.write(`Te has inscrito exitosamente, ${nombre}<br>`);
			}else{
				document.write("<br>Ya se ha llenado esta materia.<br>");
			}break;
		default:
			alert("Opción inválida.");
			return;
	}
}

inscribir("Cofla", "matematicas");
inscribir("José", "matematicas");
inscribir("María", "matematicas");
inscribir("Ana", "matematicas");
inscribir("Carla", "matematicas");
inscribir("Mariana", "matematicas");
inscribir("Ady", "programacion");
