<?php

$option = 7;
/*
switch($option){
    case 1:
        echo "Seleccionada primera opción.";
        break;
    case 2:
        echo "Seleccionada segunda opción.";
        break;
    default:
        echo "Por favor, seleccione una opción válida.";
        break;
}*/

echo match($option){
  1 => "Seleccionada primera opción.\n",
  2 => "Seleccionada segunda opción.\n",
  default => "Por favor, seleccione una opción válida.\n"
};