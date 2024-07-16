//HACIENDO PETICIONES (POST) A UNA API DE REQUESTS.
let request;
if(window.XMLHttpRequest) request = new XMLHttpRequest();
else request = new ActiveXObject("Microsoft.XMLHTTP"); //Se utiliza para Internet Explorer o navegadores que no tengan XMLHttpRequest
const imagen = document.querySelector(".image");
request.addEventListener("load", ()=>{
    let answer;
    if (request.status == 200 || request.status == 201){
        answer = request.response; //Answer 200 or 201(GREAT)
    }
    else answer = "No se ha encontrado el archivo."; // Error 404 Not Found (ERROR)
    console.log(JSON.parse(answer));
});

request.open("POST", "https://reqres.in/api/users");

request.setRequestHeader("Content-type", "application/json;charset=UTF-3");

request.send(JSON.stringify({
    "name": "morpheus",
    "job": "leader"
}));
