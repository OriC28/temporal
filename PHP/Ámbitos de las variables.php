<?php

$num = readline();

function modify(){
    global $num; //Accediendo a una variable global
    $num++; //Modificando la variable global
}

modify();
echo "$num\n\n";

// --------- Paso de parámetros por referencia -----------
function test(&$n){ 
    $n+=10;
}

$t = 4;
test($t);
echo $t;