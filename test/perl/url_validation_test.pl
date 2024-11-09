#!/usr/bin/perl
use warnings;
use strict;
use JSON;
use Data::Dumper;

use Data::Validate::URI qw(is_web_uri);

use URI;

use Regexp::Common qw /URI/;

use Data::Validate::URI qw(is_uri);


sub url_validator1 {
    my $url_string = shift;
    if (is_web_uri($url_string)) {
        return 1;
    } else {
        return 0;
    }
}

sub url_validator2 {
    my $uri = URI->new(shift, 'http');
    if ($uri->scheme) { 
        return 1; 
    } else { 
        return 0; 
    }
}

sub url_validator3 {
    my $url_string = shift;
    if ($url_string =~ /$RE{URI}{HTTP}/) { 
        return 1; 
    } else { 
        return 0; 
    }
}

sub url_validator4 {
    my $url_string = shift;
    if (is_uri($url_string)) {
        return 1;
    } else {
        return 0;
    }
}

# Open/close Json file
open(my $fh, '../fuzz/fuzz.json') or die $!;
my $json_text = do { local $/; <$fh> };
close($fh);
# Parse Json file
my $data = JSON::decode_json($json_text);
# Test
my %res;
my $count_full = 0;
my $count_true1 = 0;
my $count_true2 = 0;
my $count_true3 = 0;
my $count_true4 = 0;
for my $item (@$data) {
    my @array = @$item;
    my $url_string = $array[0];
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
    if (url_validator4($url_string)) {
        $count_true4++;
    }
}
$res{'Data::Validate::URI(is_web_uri)'} = ($count_true1 / $count_full) * 100;
$res{'URI'} = ($count_true2 / $count_full) * 100;
$res{'Regexp::Common'} = ($count_true3 / $count_full) * 100;
$res{'Data::Validate::URI(is_uri)'} = ($count_true4 / $count_full) * 100;
print Dumper(\%res);
