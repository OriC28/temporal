class App{
	constructor(puntuacion, descargas, peso){
		this.puntuacion = puntuacion;
		this.descargas = descargas;
		this.peso = peso;
		this.iniciado = false;
		this.instalada = false;
	}
	
	abrir(){
		if(this.iniciado == false && this.instalada == true){
			alert("App iniciada.");
			this.iniciado = true;
		}
	}
	
	cerrar(){
		if(this.iniciado == true && this.instalada == true){
			alert("Cerrando la app...");
			this.iniciado = false;
		}else{
			alert("No se puede cerrar esta app porque no se encuentra abierta.");
		}
	}
	instalar(){
		if(this.instalada == false){
			alert("Instalando app...");
			this.instalada = true;
		}else{
			alert("La app ya se encuentra instalada en este dispositivo.");
		}
	}
	desinstalar(){
		if(this.instalada == true){
			alert("Desinstalando app...");
		}else{
			alert("La app no se encuentra instalada en este dispositivo.");
		}
	}
	
	appInfo(){
		return `<b>Puntuación: </b> ${this.puntuacion} <br>
				<b> Descargas: </b> ${this.descargas} <br>
				<b>Peso: </b> ${this.peso} <br>`;
	}
}

const app = new App("6.7", "200.000", "5MB");
const app2 = new App("7.8", "1.000.000", "16MB");

document.write(`${app2.appInfo()}`);