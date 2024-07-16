const getInfo = async ()=>{
    let result;
    let div = document.querySelector(".container")
    div.style.background = "#000";
    try{
        result = await axios("dataEjercicio1.txt");
        div.innerHTML = `<p><strong class="green">Estudiantes aprobados:</strong>
                    ${result.data.aprobados}</p><br>
                    <p><strong class="red">Estudiantes desaprobados:</strong>
                    ${result.data.desaprobados}</p>`;
    }catch(e){
        div.innerHTML = `<p class="error">Ha ocurrido un error</p>`;
        console.log(e);
    }
    
};

let boton = document.getElementById("getInfo");
boton.addEventListener("click", getInfo);