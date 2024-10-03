<?php

$num = -700;
$num2 = -$num; //El operador "-" se llama operador unario
$num3 = 70;
$saludo = "hola";
echo var_dump($saludo) ."\n"; //La función var_dump() retorna el tipo de dato y el valor asignado a la variable
echo "$num2\n";

//WARNING NOTE: $a++ != ++$a (al asignar dicho valor en otra variable)

/*
"..." permite pasar una cantidad indefinida de parámetros
Todos los parámetros se almacenan en el array $words
*/
function concat(...$words){ 
    $result = "";
    foreach($words as $word){
        $result = $result . $word . " ";
    }
    return $result;
}

echo concat("hola","como","estas");