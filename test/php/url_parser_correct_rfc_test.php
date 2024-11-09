<?php

function test_parse_url($url_str, $part_url)
{
    $parsing_url = parse_url($url_str);
    if ($parsing_url == false) {
        return;
    }
    // scheme
    if (!isset($parsing_url['scheme']) && isset($part_url['scheme']) && strcmp($part_url['scheme'], "") != 0) {
        echo "Problem in scheme:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['scheme']) && !isset($part_url['scheme'])) {
        echo "Problem in scheme:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['scheme']) && isset($part_url['scheme']) && strcmp($parsing_url['scheme'], $part_url['scheme']) != 0) {
        echo "Problem in scheme:\n" . $url_str . "\n" . $part_url['scheme'] . "\n" . $parsing_url['scheme'] . "\n";
    }
    // userinfo
    if (isset($parsing_url['user'])) {
        if (isset($parsing_url['pass'])) {
            $userinfo = $parsing_url['user'] . ":" . $parsing_url['pass'];
        } else {
            $userinfo = $parsing_url['user'];
        }
    } else {
        $userinfo = null;
    }
    if (!isset($userinfo) && isset($part_url['userinfo']) && strcmp($part_url['userinfo'], "") != 0) {
        echo "Problem in userinfo:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($userinfo) && !isset($part_url['userinfo'])) {
        echo "Problem in userinfo:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($userinfo) && isset($part_url['userinfo']) && strcmp($userinfo, $part_url['userinfo']) != 0) {
        echo "Problem in userinfo:\n" . $url_str . "\n" . $part_url['userinfo'] . "\n" . $userinfo . "\n";
    }
    // host
    if (!isset($parsing_url['host']) && isset($part_url['host']) && strcmp($part_url['host'], "") != 0) {
        echo "Problem in host:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['host']) && !isset($part_url['host'])) {
        echo "Problem in host:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['host']) && isset($part_url['host']) && strcmp($parsing_url['host'], $part_url['host']) != 0) {
        echo "Problem in host:\n" . $url_str . "\n" . $part_url['host'] . "\n" . $parsing_url['host'] . "\n";
    }
    // port
    if (!isset($parsing_url['port']) && isset($part_url['port']) && strcmp($part_url['port'], "") != 0) {
        echo "Problem in port:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['port']) && !isset($part_url['port'])) {
        echo "Problem in port:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['port']) && isset($part_url['port']) && strcmp($parsing_url['port'], $part_url['port']) != 0) {
        echo "Problem in port:\n" . $url_str . "\n" . $part_url['port'] . "\n" . $parsing_url['port'] . "\n";
    }
    // path
    if (!isset($parsing_url['path']) && isset($part_url['path-abempty']) && strcmp($part_url['path-abempty'], "") != 0) {
        echo "Problem in path:\n" . $url_str . "\n" . $part_url['path-abempty'] . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['path']) && !isset($part_url['path-abempty'])) {
        echo "Problem in path:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['path']) && isset($part_url['path-abempty']) && strcmp($parsing_url['path'], $part_url['path-abempty']) != 0) {
        echo "Problem in path:\n" . $url_str . "\n" . $part_url['path-abempty'] . "\n" . $parsing_url['path'] . "\n";
    }
    // query
    if (!isset($parsing_url['query']) && isset($part_url['query']) && strcmp($part_url['query'], "") != 0) {
        echo "Problem in query:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['query']) && !isset($part_url['query'])) {
        echo "Problem in query:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['query']) && isset($part_url['query']) && strcmp($parsing_url['query'], $part_url['query']) != 0) {
        echo "Problem in query:\n" . $url_str . "\n" . $part_url['query'] . "\n" . $parsing_url['query'] . "\n";
    }
    // fragment
    if (!isset($parsing_url['fragment']) && isset($part_url['fragment']) && strcmp($part_url['fragment'], "") != 0) {
        echo "Problem in fragment:\n" . $url_str . "\n" . "It is NOT parsed" . "\n";
    }
    if (isset($parsing_url['fragment']) && !isset($part_url['fragment'])) {
        echo "Problem in fragment:\n" . $url_str . "\n" . "It is parsed" . "\n";
    }
    if (isset($parsing_url['fragment']) && isset($part_url['fragment']) && strcmp($parsing_url['fragment'], $part_url['fragment']) != 0) {
        echo "Problem in fragment:\n" . $url_str . "\n" . $part_url['fragment'] . "\n" . $parsing_url['fragment'] . "\n";
    }
}

$file = file_get_contents("../fuzz/fuzz.json");
$data = json_decode($file, true);

foreach ($data as $full_url) {
    $url_string = $full_url[0];
    $part_url = $full_url[1];
    test_parse_url($url_string, $part_url);
}
