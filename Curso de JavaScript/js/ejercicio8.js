/*
1. CREAR UNA FUNCIÓN QUE RECIBA COMO PARÁMETRO LA MATERIA Y DEVUELVA:
	A.- PROFESOR ASIGNADO.
	B.- EL NOMBRE DE TODOS LOS ALUMNOS.

2. CREAR UNA FUNCIÓN QUE NOS DIGA EN CUANTAS CLASES ESTÁ COFLA.
3. NOMBRAR LAS CLASES EN LAS QUE ESTÁ Y LOS PROFESORES DE CADA UNA.
*/

const obtenerInformacion = (materia) =>{
	let materias = {programacion: ["Ángel Gómez","María", "José", "Carlos", "Cofla"],
		matematicas: ["Pedro Díaz", "María", "José", "Carlos", "Cofla", "Ana"],
		cultura: ["Ronald Hernández", "María", "José", "Antonio", "Carlos", "Cofla"],
		redes: ["Ariana Rodríguez", "María", "José", "Carlos", "Cofla", "Jesús", "Miguel"]	
	};
	
	if(materias[materia]!=undefined){
		let profesor = materias[materia][0];
		let estudiantes = materias[materia].slice(1);
	
		document.write(`<b>Materia:</b> ${materia} <br>
					<b>Profesor:</b> ${profesor} <br>
					<b>Nombres de los Alumnos:</b><br>
					<b>Alumnos:</b> ${estudiantes}<br>`);
	}else{
		alert("La materia ingresada no es válida.");
	}
}

//obtenerInformacion("programacion");

const buscarCofla = (nombre)=>{
	let cantidad = 0;
	let clasesPresentes = [];
	let profesores = [];
	let materias = {programacion: ["Ángel Gómez","María", "José", "Carlos", "Cofla", "Miguel"],
		matematicas: ["Pedro Díaz", "María", "José", "Carlos", "Cofla", "Ana"],
		cultura: ["Ronald Hernández", "María", "José", "Antonio", "Carlos", "Cofla"],
		redes: ["Ariana Rodríguez", "María", "José", "Carlos", "Jesús", "Miguel"]	
	};
	
	for(let i in materias){
		if(materias[i].includes(nombre)){
			cantidad++;
			clasesPresentes.push(" " + i);
			profesores.push(" " + materias[i][0]);
		}
	}
	document.write(`<br>${nombre} se encuentra en ${cantidad} clases. <br>
	<b>Materias:</b> ${clasesPresentes} <br>
	<b>Profesores:</b> ${profesores}<br>`);

}
obtenerInformacion("programacion");
buscarCofla("Cofla");