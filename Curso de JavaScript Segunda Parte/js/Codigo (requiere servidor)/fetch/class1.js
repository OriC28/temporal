const getName = async () => {
    let request = await fetch("./informacion.txt");
    let answer = await request.json();
    let div = document.createElement("DIV");
    div.classList.add("result");
    let data = `Nombre: ${answer.Nombre} ${answer.Apellido}<br> `;
    div.innerHTML = data;
    document.body.appendChild(div);
    console.log(answer);
};

const getData = async () => {
    let request = await fetch("./informacion.txt");
    let answer = await request.json();
    let div = document.createElement("DIV");
    div.classList.add("result-data");
    let data = `Edad: ${answer.Edad}<br>
                Ciudad: ${answer.Ciudad}`;
    div.innerHTML = data;
    document.body.appendChild(div);
    console.log(answer);
};

let boton = document.getElementById("show");
let boton2 = document.getElementById("data")
boton.addEventListener("click", getName);
boton2.addEventListener("click", getData);