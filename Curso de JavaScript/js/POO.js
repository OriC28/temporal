class Animal{
	constructor(nombre, edad, color){
		this.nombre = nombre;
		this.edad = edad;
		this.color = color;
	}
	
	set setNombre(nuevoNombre){ //Setter
		this.nombre = nuevoNombre;
	}
	get getEdad(){ //Getter
		return this.edad;
	}
}

class Perro extends Animal { //Herencia
	constructor (nombre, edad, color, tamaño){
		super(nombre, edad, color);
		this.tamaño = tamaño;
	}
	ladrar (){
		alert("¡Guau!");
	}
}

const perro = new Perro("Tom", 12, "Negro", "Grande");
const gato = new Animal("Lisa", 8, "Blanco", "Pequeño");
perro.setNombre = "Lucas";
document.write(perro.getEdad + "<br>" +
				perro.nombre + "<br>");

