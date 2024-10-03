<?php

declare(strict_types=1); /* Especifica que el tipado será estricto, esto significa que
las funciones no intentarán convetir un tipo de dato a otro sino que directamente arrojará error.
*/

/*Se puede especificar el tipo de dato para cada parámetro de la función, esto
lo que hará es convetir cualquier otro tipo de dato en el asignado.*/

function sum(int $num1, int $num2): int | float //Tipo de retorno de la función (entero o flotante)
{
    return $num1/2 + $num2;
}

echo sum(5,6);


