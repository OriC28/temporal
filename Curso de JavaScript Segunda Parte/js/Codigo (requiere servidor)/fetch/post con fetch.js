//PETICION POST CON FETCH:

const request = fetch("https://reqres.in/api/users",{
    method: "POST",
    body: JSON.stringify({"name": "morpheus","job": "leader"}),
    headers: {"Content-type" : "application/json"}
});
request.then(answer => answer.json())
        .then(answer => console.log(answer));