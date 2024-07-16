//HACIENDO UNA PETICIÓN CON AXIOS (POST):

axios.post("https://reqres.in/api/users",{"name": "morpheus","job": "leader"})
    .then(answer=>console.log(answer));