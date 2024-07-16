//HACIENDO PETICIONES (GET) A UNA API DE DRAGON BALL.

let request;
if(window.XMLHttpRequest) request = new XMLHttpRequest();
else request = new ActiveXObject("Microsoft.XMLHTTP"); //Se utiliza para Internet Explorer o navegadores que no tengan XMLHttpRequest
const imagen = document.querySelector(".image");
request.addEventListener("load", ()=>{
    let answer;
    if (request.status == 200) answer = request.response; //Answer 200 (GREAT)
    else answer = "No se ha encontrado el archivo."; // Error 404 Not Found (ERROR)
    let transformationsGoku = JSON.parse(answer).transformations;
    console.log(transformationsGoku);
    let imageGokuSS1 = transformationsGoku[2].image;
    imagen.setAttribute("src", imageGokuSS1);
});

request.open("GET", "https://dragonball-api.com/api/characters/1");
request.send();
