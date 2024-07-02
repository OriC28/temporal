
let edad = prompt("Ingrese su edad: ");
let edadInt = parseInt(edad);

function verificarEdad(edad){
	if (edad>0 && edad >=18){
		alert("Eres mayor de edad.");
		return true;
	}
	else if(edad<0){
		alert("Ctm inserta una edad válida.");
	}else{
		alert("Eres menor de edad.");
	}
	return false;
}

verificacionEdad = verificarEdad(edadInt);

function validarAcceso(verificacionEdad){
	if (verificacionEdad){
		document.write("Tienes acceso a la discoteca.")
	}
	else{
		document.write("No tienes acceso a la discoteca")
	}
}

validarAcceso(verificacionEdad);