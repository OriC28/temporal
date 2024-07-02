let gratis = false;

const validarEntrada = (time)=>{
	let edad = prompt("Ingrese su edad: ");
	if (edad>=18){
		if (time>=2 && time<7 && gratis==false){
			alert("Puedes pasar gratis");
			gratis = true;
		}else{
			alert("No puedes pasar gratis. Compra una entrada.");
		}
	}else{
		alert("Eres menor de edad. Anda a dormir.");
	}
}

validarEntrada(3);
validarEntrada(4);
validarEntrada(10);