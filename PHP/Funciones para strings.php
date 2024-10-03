<?php

$word = "abcdef peo %% HOLA";
// GET SIZE
$size_word = mb_strlen($word);
// GET INDEX 
$index_of = strpos($word, '%');
// GET INDEX SINCE RIGHT
$index_since_right = strrpos($word, '%');
// VERIFY IF SUBSTRING INTO STRING MAIN (RETURN TRUE O FALSE)
$substring = str_contains($word, 'peo');
// VERIFY IF STRING STARTS WITH A SPECIFY CHARACTER (RETURN TRUE O FALSE)
$startswith = str_starts_with($word, 'a');
// VERIFY IF STRING ENDS WITH A SPECIFY CHARACTER (RETURN TRUE O FALSE)
$endsswith = str_ends_with($word, '%%');

$w1 = "culo";
$w2 = "culo";

// VERIFIY IF TWO STRINGS ARE EQUALS (IT'S NOT SENSITIVE CASE)
# echo strcasecmp($w1, $w2) == 0 ? "Both words are equals" : "No equals";

// VERIFIY IF TWO STRINGS ARE EQUALS (IT'S SENSITIVE CASE)
# echo strcmp($w1, $w2) == 0 ? "Both words are equals" : "No equals";

// GET SUBSTRING SPECIFY RANGE (IT'S LIKE SLICING IN PYTHON)
$get_peo = substr($word, 7, 3);
// REPLACE A SUBSTRING OR CHARACTER IN STRING MAIN FOR OTHER SUBSTRING O CHARACTER SPECIFIED
$replace_word = str_replace("%%", "culote", $word);
// CHANGE ALL UPPER CASE TO LOWER CASE IN STRING SPECIFIED
$to_lower = strtolower($word);
// CHANGE ALL LOWER CASE TO UPPER CASE IN STRING SPECIFIED
$to_upper = strtoupper($word);
// CHANGE THE FIRST CHARACTER TO UPPER
$first_upper = ucfirst($word);
// CHANGE FIRST CHARACTER TO UPPER IN EACH WORD
$words_upper = ucwords($word);
