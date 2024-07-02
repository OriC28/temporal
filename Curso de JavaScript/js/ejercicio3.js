let cantidad = prompt("¿Cuántos alumnos son? ");
let alumnosTotales = [];

for(let i=0; i<cantidad; i++){
alumnosTotales[i] = [prompt("Nombre del alumno " + (i+1)), 0];
}

const tomarAsistencia = (nombre, p)=>{
	let presencia = prompt(nombre);
	if (presencia == "presente" || presencia == "Presente"){
		alumnosTotales[p][1]++;
	}
}

for(let i=0; i<5; i++){
	for(alumno in alumnosTotales){
		tomarAsistencia(alumnosTotales[alumno][0], alumno);
	}
}

for(alumno in alumnosTotales){
	let resultado = `Nombre del alumno: ${alumnosTotales[alumno][0]} <br>
	________________Asistencias: ${alumnosTotales[alumno][1]} <br>
	________________Ausencias: ${5 - alumnosTotales[alumno][1]} <br>
	`;
	if(5 - alumnosTotales[alumno][1] > 2){
		resultado+= "<b style='color:red'>REPROBADO POR INASISTENCIAS</b><br>";
	}
	else{
		resultado+= "<br><br>";
	}
	document.write(resultado);
}

