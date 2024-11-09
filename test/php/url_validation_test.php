<?php

function url_validator1($url_str)
{
    if (filter_var($url_str, FILTER_VALIDATE_URL) === FALSE) {
        return false;
    } else {
        return true;
    }
}

function url_validator2($url_str)
{
    if (preg_match("/^http[s]?:\/\/[^\s\/$.?#].[^\s]*$/i", $url_str)) {
        return true;
    } else {
        return false;
    }
}

function url_validator3($url_str)
{
    $parsed_url = parse_url($url_str);
    if ($parsed_url && isset($parsed_url['scheme']) && isset($parsed_url['host'])) {
        return true;
    } else {
        return false;
    }
}

$file = file_get_contents("../fuzz/fuzz.json");
$data = json_decode($file);

$count_full = 0;
$count_true1 = 0;
$count_true2 = 0;
$count_true3 = 0;
foreach ($data as $full_url) {
    $url_string = $full_url[0];
    $count_full++;
    if (url_validator1($url_string)) {
        $count_true1++;
    }
    if (url_validator2($url_string)) {
        $count_true2++;
    }
    if (url_validator3($url_string)) {
        $count_true3++;
    }
}
echo "filter_var: ", ((float) $count_true1 / $count_full) * 100, "%\n";
echo "regex: ", ((float) $count_true2 / $count_full) * 100, "%\n";
echo "parse_url: ", ((float) $count_true3 / $count_full) * 100, "%\n";
