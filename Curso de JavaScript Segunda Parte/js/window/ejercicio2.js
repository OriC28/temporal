/*SISTEMA PARA MOSTRARLE A COFLA LOS DATOS DEL SITIO WEB EN EL QUE SE ENCUENTRA.*/ 

let href = window.location.href;
let hostname = window.location.hostname;
let pathname = window.location.pathname;
let protocol = window.location.protocol;

//MOSTRAR INFORMACIÓN:

document.write(`<b>URL COMPLETA:</b> ${href}<br>
                <b>PATHNAME:</b>${pathname}<br>
                <b>HOSTNAME:</b> ${hostname}<br>
                <b>PROTOCOL:</b> ${protocol}<br>`);