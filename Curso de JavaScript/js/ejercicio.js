/*
Robert tiene $1.5
Pedro tiene $1.7
Cofla tiene $3

Los precios de los helados son los siguientes:
Palito de helado de agua: $0.6
Palido de helado de crema: $1
Bombón helado marca heladix: $1.6
Bombón helado marca heladovich: $1.7
Bombón helado marca helardo: $1.8
Potecito de helado con confites: $2.9
Pote de 1/4kg -> $2.9

CREAR SOLUCIONES:
1. Pedirles que ingresen el monto que tienen y mostrarles helado más caro.
2. Si hay 2 o más con el mismo precio, mostrarlos.
3. Cofla quiere saber cuánto es el vuelto.
*/

let montoRoberto = prompt("Ingrese su monto, Roberto: ");
let montoPedro = prompt("Ingrese su monto, Pedro: ");
let montoCofla = prompt("Ingrese su monto, Cofla: ");

let montoTotal = Number.parseFloat(montoRoberto) 
				+ Number.parseFloat(montoPedro) + 
				Number.parseFloat(montoCofla);

if (montoTotal>=2.9){
	let vuelto = montoTotal - 2.9;
	alert("Ustedes podrán comprar un potecito de helado con confetis o un pote de 1/4 KG.")
	alert(`Su vuelto es de: ${vuelto.toPrecision(2)}$.`);
}
