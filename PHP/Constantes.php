<?php

define('PI', 3.14); //Definiendo una constante (valor inmutable)
echo "The Pi value is: " . PI ."\n\n"; //Se accede al valor de la constante sin anteponer "$"

define('ANIMALS', ['DOG','CAT','DUCK','BUNNY']); //Definiendo una constante de tipo array
echo ANIMALS[3] . " IS CUTE\n";

//Verificar si una constante ha sido definida
if(defined('PI')){
    echo "\nPI IS DEFINED\n";
}else{
    echo "PI ISN'T DEFINED, YOU MUST TRY DEFINE IT.\n";
}