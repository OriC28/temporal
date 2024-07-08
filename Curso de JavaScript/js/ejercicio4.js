/*
SOLUCIONES:
1. CREAR UN SISTEMA QUE LE PERMITA A COFLA VER LAS PARTICULARIDADES
	DE LOS 3 CELULARES.
2. CADA CELULAR DEBE TENER: COLOR, PESO, RESOLUCIÓN DE PANTALLA,
	RESOLUCIÓN DE CÁMARA Y MEMORIA RAM.
3. CADA CELULAR DEBE PODER: ENCENDER, REINICIAR, APAGAR, TOMAR FOTOS
	Y GRABAR.
*/

class Celular{
	constructor(color, peso, rp, rc, ram){
		this.color = color;
		this.peso = peso;
		this.rp = rp;
		this.rc = rc;
		this.ram = ram;
		this.encendido = false;
	}
	
	presionarBotonEncender(){
		if (this.encendido==false){
			alert("El teléfono se está prendiendo...");
			this.encendido = true;
		}else{
			alert("El teléfono se está apagando...");
			this.encendido = false;
		}
	}
	reset(){
		if(this.encendido==true){
			alert("El teléfono se está reiniciando...");
		}else{
			alert("El teléfono se encuentra apagado.");
		}
	}

	takePhoto(){
		alert(`Foto tomada. Resolución de ${this.rc}`);
	}
	record(){
		alert("Grabando...");
	}
	
	mostrarInfo(){
		return `<b>DATOS DEL TELÉFONO</b><br>
				<b>Color:</b> ${this.color}<br>
				<b>Peso:</b> ${this.peso}<br>
				<b>Resolución de Pantalla:</b> ${this.rp}<br>
				<b>Resolución de Cámara:</b> ${this.rc}<br>
				<b>Memoria RAM:</b> ${this.ram}<br>`;
	}
}

const A55 = new Celular("Morado", "8.5g", "15'", "1920x1080", "16GB");
const RedmiNote12 = new Celular("Blanco", "14'", "2300x1080", "1920x1080", "8GB");
const iPhone15 = new Celular("Azul claro", "15'", "2556x1179", "2300x1080", "16GB");


class AltaGama extends Celular{
	constructor(color, peso, rp, rc, ram, rCamaraExtra){
		super(color, peso, rp, rc, ram);
		this.rCamaraExtra = rCamaraExtra;
	}
	
	grabarLento(){
		alert("Estás grabando en cámara lenta.");
	}
	
	reconomientoFacial(){
		alert("Vamos a iniciar un reconocimiento facial. No te muevas.");
	}
	infoAltaGama(){
		return this.mostrarInfo() + `<b> Resolución segunda camára:</b> ${this.rCamaraExtra}`;
	}
}

const celularAltaGama1 = new AltaGama("Azul", "7.6g", "16'", "1980x1080", "16GB", "2556x1179");
const celularAltaGama2 = new AltaGama("Rosado", "8.6g", "15'", "1080x720", "8GB", "1980x1080");


document.write(`${celularAltaGama1.infoAltaGama()} <br>
				<br>${celularAltaGama2.infoAltaGama()} <br>`);
