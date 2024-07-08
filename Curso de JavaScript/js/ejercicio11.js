//[Promedio de asistencias, Nota final, Evaluaciones, Nombre Materia]

const materias = {
	fisica: [90,6,4,"fisica"],
	quimica: [50,7,2,"quimica"],
	programacion: [80,7,4,"programacion"],
	logica: [95,8,3,"logica"],
	matematica: [80,10,4,"matematica"],
	algebra:[90,8,4,"algebra"]
};

const verificarAprobacion = ()=>{
	for(materia in materias){
		let asistencias = materias[materia][0];
		let promedio = materias[materia][1];
		let trabajos = materias[materia][2];
		
		console.log(`${materias[materia][3]}:`);
		
		if (asistencias>=90 && promedio>=7 && trabajos>=3){
			console.log("%c 	Aprobó", "color: green");
		}else{
			console.log("%c 	Desaprobó", "color: red");
		}
	}
}

verificarAprobacion();