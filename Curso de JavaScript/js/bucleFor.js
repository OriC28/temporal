let numeros = [1,2,3,4,5,6,7,8];
let nombres = ["Maria",
				"Pedro",
				numeros,
				"Carlos",
				"Miguel",
				"Lisa",
				"Mariana",
				"Luis"];
forPrincipal: //label
for (nombre in nombres){
	if (nombre == 2){
		for(numero of numeros){
			document.write(numero + "<br>");
			if(numero == 5){
				break;
			}
		}
	}else{
		document.write(nombres[nombre] + "<br>")
	}
}

//For in: mostrará las posiciones de los elementos que recorre.
//Fo of: mostrará los valores de los elementos que recorre.