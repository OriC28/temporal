const jsonDeserializado = {nombre: "José", apellido: "Martínez", edad: 20};
const jsonSerializado = `{"telefono": "0412639543", "direccion":"París"}`;

//JSON deserializado (string) --> JSON serializado (object)
const deserializado = JSON.parse(jsonSerializado); 
//JSON serializado (object) --> JSON deserializado (string)
const serializado = JSON.stringify(jsonDeserializado); 

console.log(deserializado);