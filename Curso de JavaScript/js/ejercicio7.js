class Calculadora{
	constructor(numero1, numero2){
		this.num1 = numero1;
		this.num2 = numero2;
	}
	
	sumar(){return this.num1 + this.num2;}
	
	restar(){return this.num1 - this.num2;}
	
	multiplicar(){return this.num1*this.num2;}
	
	dividir(){return this.num1/this.num2;}
	
	potencia(){return this.num1**this.num2;}
	
	raizCuadrada(){
		let raizC = Math.sqrt(this.num1);
		let raizC2 = Math.sqrt(this.num2);
		let raices = [raizC, raizC2];
		return raices;
	}
	raizCubica(){
		let raizCU = Math.cbrt(this.num1);
		let raizCU2 = Math.cbrt(this.num2);
		let raices = [raizCU, raizCU2];
		return raices;
	}
}

let num1Int = parseInt(prompt("Ingrese el número 1: "));
let num2Int = parseInt(prompt("Ingrese el número 2: "));
let opcion = parseInt(prompt(`Elige una una operación:
1. Suma 
2. Resta
3. Multiplicación
4. División 
5. Potencia 
6. Raíz Cuadrada 
7. Raíz Cúbica `));

let calculadora = new Calculadora(num1Int, num2Int);

switch(opcion){
	case 1:
		alert(`La suma es: ${calculadora.sumar()}`);
		break;
	case 2:
		alert(`La resta es: ${calculadora.restar()}`);
		break;
	case 3:
		alert(`la multiplicación es: ${calculadora.multiplicar()}`);
		break;
	case 4:
		alert(`La división es: ${calculadora.dividir()}`);
		break;
	case 5:
		alert(`${num1Int} elevado a la ${num2Int} es: ${calculadora.potencia()}`);
		break;
	case 6:
		raices = calculadora.raizCuadrada();
		alert(`La raíz cuadrada de ${num1Int} es ${raices[0]} y la raíz cuadrada de ${num2Int} es ${raices[1]}`);
		break;
	case 7:
		raices = calculadora.raizCubica();
		alert(`La raíz cuadrada de ${num1Int} es ${raices[0]} y la raíz cuadrada de ${num2Int} es ${raices[1]}`);
		break;
	default:
		alert("Opción incorrecta.");
	
}

