/*
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de 
cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Escribir un 
programa que lea el número de payasos y muñecas vendidos en el último pedido y 
calcule el peso total del paquete que será enviado.
*/

class Paquete{
	constructor(cantMuñecas, cantPayasos){
		this.muñecas = cantMuñecas;
		this.payasos = cantPayasos;
	}
	
	validarPeso(){
		let paquetePeso = this.muñecas*112 + this.payasos*75;
		if (paquetePeso>=1000){
			let paqueteKG = paquetePeso/1000;
			alert(`El peso del paquete es de ${paqueteKG}kg.`);
		}else{
			alert(`El peso del paquete es de ${paquetePeso}g.`);
		}
	}
}


let muñecas = prompt("Ingrese la cantidad de muñecas: ");
let muñecasCant = parseInt(muñecas);

let payasos = prompt("Ingrese la cantidad de payasos: ");
let payasosCant = parseInt(payasos);

const paquete1 = new Paquete(muñecasCant, payasosCant);
paquete1.validarPeso();



/*

const validarPeso = (muñecas, payasos)=>{
	let paquetePeso = muñecas*112 + payasos*75;
	if (paquetePeso>=1000){
		let paqueteKG = paquetePeso/1000;
		alert(`El peso del paquete es de ${paqueteKG}kg.`);
	}else{
		alert(`El peso del paquete es de ${paquetePeso}g.`);
	}
}

let muñecas = prompt("Ingrese la cantidad de muñecas: ");
let muñecasCant = parseInt(muñecas);

let payasos = prompt("Ingrese la cantidad de payasos: ");
let payasosCant = parseInt(payasos);

validarPeso(muñecas, payasos);

*/