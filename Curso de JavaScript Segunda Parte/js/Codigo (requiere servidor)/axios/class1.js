const getName = async () => {
    let result = await axios("./informacion.txt");
    let div = document.createElement("DIV");
    div.classList.add("result");
    let datos = `Nombre: ${result.data.Nombre} ${result.data.Apellido}<br> `;
    div.innerHTML = datos;
    document.body.appendChild(div);
    console.log(result);
};

const getData = async () => {
    let result = await axios("./informacion.txt");
    let div = document.createElement("DIV");
    div.classList.add("result-data");
    let datos = `Edad: ${result.data.Edad}<br>
                Ciudad: ${result.data.Ciudad}`;
    div.innerHTML = datos;
    document.body.appendChild(div);
};

let boton = document.getElementById("show");
let boton2 = document.getElementById("data")
boton.addEventListener("click", getName);
boton2.addEventListener("click", getData);