/*
En la fábrica de juguetes del Polo Norte, cada juguete
tiene un número de identificación único. Sin embargo,
debido a un error en la máquina de juguetes, algunos
números han sido asignados a más de un juguete.

Encuentre el primer número de identificación que se ha
repetido, ¡donde la segunda aparición tiene el índice
más pequeño! En otras palabras, si hay más de un número
repetido, debes devolver el número cuya segunda aparición
aparece primero en la lista. Si no hay números repetidos,
devuelve -1.

Ejemplo:

const giftIds = [2, 1, 3, 5, 3, 2]
const firstRepeatedId = findFirstRepeated(giftIds)
console.log(firstRepeatedId) // 3
// Even though 2 and 3 are repeated
// 3 appears second time first


*/



const findFirstRepeated = (array)=>{
	let step = 0;
	let total_step = [];
	let i = 0;
	let a = array[0];
	while(i<array.length){
		if(a!=array[i]){
			step++;
		}else{
			total_step.push(step);
			step = 0;
			a = array[i];
		}
	}
	alert(total_step);
}


findFirstRepeated([2, 1, 3, 5, 3, 2]);