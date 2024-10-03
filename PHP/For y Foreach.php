<?php

$animals = ["Dog", "Cat", "Duck", "Bunny"];

foreach($animals as $index => $animal){
    echo "$index ----- $animal\n";
}

for ($i=0;$i<sizeof($animals); $i++){
    echo "$i ----- $animals[$i]\n";
}


