<?php

$num = readline();

function factorial($num){
    $result = 1;
    for ($i=1;$i<=$num;$i++){
        $result*=$i;
    }
    return $result;
}

echo factorial($num);