const input = document.querySelector(".input");


//  	                EVENTO KEYDOWN:
input.addEventListener("keydown", (e)=>{
    console.log("Una tecla fue presionada.");
});

//                      EVENTO KEYPRESS:
input.addEventListener("keypress", (e)=>{
    console.log("Una tecla fue presionada y soltada.");
});

//                      EVENTO KEYUP:
input.addEventListener("keyup", (e)=>{
    console.log("Una tecla fue soltada.");
});