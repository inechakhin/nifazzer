#!/usr/bin/perl
use warnings;
use strict;
use JSON;
use Data::Dumper;

use URI ();

use Mojo::URL;
use Mojo::Util qw(decode url_unescape);

sub parse_url_regex {
    my $url_string = shift;
    my %parsed;
    while ($url_string) {
        if (!exists($parsed{scheme})) {
            $url_string =~ s!^((?:[[:alnum:]]+:)?[[:alnum:]]+):!!;
            $parsed{scheme} = $1;
            return \%parsed unless $url_string =~ s!^//!!;
        }
        elsif (!exists($parsed{host}) && $url_string =~ s!^(?:((?:[\d\w]+:)?(?:[\d\w]+)?)@)?([\d\w\.]+)(?::([\d]+))?!!u) {
            $parsed{userinfo} = $1 // "";
            $parsed{host} = $2 // "";
            $parsed{port} = $3 // "";
        }
        elsif (!exists($parsed{path}) && $url_string =~ s!^/((?:[\d\w\.\/]*)+)!!u) {
            $parsed{path} = "/" . ( $1 // "" );
        }
        elsif (!exists($parsed{query}) && $url_string =~ s!^\?((?:[\d\w\[\]%\"\']+)=(?:[\d\w\[\]%\"\']+))*!!u ) {
            $parsed{query} = $1 // "";
        }
        elsif (!exists($parsed{fragment}) && $url_string =~ s!^#([\d\w\[\]%\"\']+)!!u) {
            $parsed{fragment} = $1 // "";
        }
        else {
            return undef;
        }
    }
    return \%parsed;
}

sub test_parse_url_regex {
    my $url_string = shift;
    my $part_url = shift;
    my $parsed_regex = parse_url_regex($url_string);
    if (!defined($parsed_regex)) {
        return;
    }
    if (defined($part_url->{"scheme"})) {
        if (defined($parsed_regex->{scheme})) {
            if ($parsed_regex->{scheme} ne $part_url->{"scheme"}) {
                print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\n".$parsed_regex->{scheme}."\n")
            }
        } else {
            print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"userinfo"})) {
        if (defined($parsed_regex->{userinfo})) {
            if ($parsed_regex->{userinfo} ne $part_url->{"userinfo"}) {
                print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\n".$parsed_regex->{userinfo}."\n")
            }
        } else {
            print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\nNot parsing\n")
        }
    }
    if ($part_url->{"host"} ne "") {
        if (defined($parsed_regex->{host})) {
            if ($parsed_regex->{host} ne $part_url->{"host"}) {
                print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\n".$parsed_regex->{host}."\n")
            }
        } else {
            print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"port"})) {
        if (defined($parsed_regex->{port})) {
            if ($parsed_regex->{port} ne $part_url->{"port"}) {
                print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\n".$parsed_regex->{port}."\n")
            }
        } else {
            print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\nNot parsing\n")
        }
    }
    if ($part_url->{"path-abempty"} ne "") {
        if (defined($parsed_regex->{path})) {
            if ($parsed_regex->{path} ne $part_url->{"path-abempty"}) {
                print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\n".$parsed_regex->{path}."\n")
            }
        } else {
            print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"query"})) {
        if (defined($parsed_regex->{query})) {
            if ($parsed_regex->{query} ne $part_url->{"query"}) {
                print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\n".$parsed_regex->{query}."\n")
            }
        } else {
            print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"fragment"})) {
        if (defined($parsed_regex->{fragment})) {
            if ($parsed_regex->{fragment} ne $part_url->{"fragment"}) {
                print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\n".$parsed_regex->{fragment}."\n")
            }
        } else {
            print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\nNot parsing\n")
        }
    }
}

sub test_uri {
    my $url_string = shift;
    my $part_url = shift;
    my $parsed_uri = URI->new($url_string);
    if (!defined($parsed_uri)) {
        return;
    }
    if (defined($part_url->{"scheme"})) {
        if (defined($parsed_uri->scheme)) {
            if ($parsed_uri->scheme ne $part_url->{"scheme"}) {
                print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\n".$parsed_uri->scheme."\n")
            }
        } else {
            print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"userinfo"})) {
        if (defined($parsed_uri->userinfo)) {
            if ($parsed_uri->userinfo ne $part_url->{"userinfo"}) {
                print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\n".$parsed_uri->{userinfo}."\n")
            }
        } else {
            print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"host"}) && $part_url->{"host"} ne '') {
        if (defined($parsed_uri->host)) {
            if ($parsed_uri->host ne $part_url->{"host"}) {
                print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\n".$parsed_uri->host."\n")
            }
        } else {
            print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"port"})) {
        if (defined($parsed_uri->port)) {
            if ($parsed_uri->port ne $part_url->{"port"}) {
                print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\n".$parsed_uri->port."\n")
            }
        } else {
            print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"path-abempty"}) && $part_url->{"path-abempty"} ne '') {
        if (defined($parsed_uri->path)) {
            my $path = decode('UTF-8', url_unescape($parsed_uri->path));
            if (defined($path)) {
                if ($path ne $part_url->{"path-abempty"}) {
                    print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\n".$path."\n")
                }
            }
        } else {
            print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"query"})) {
        if (defined($parsed_uri->query)) {
            my $query = decode('UTF-8', url_unescape($parsed_uri->query));
            if (defined($query)) {
                if ($query ne $part_url->{"query"}) {
                    print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\n".$query."\n")
                }
            }
        } else {
            print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"fragment"})) {
        if (defined($parsed_uri->fragment)) {
            if ($parsed_uri->fragment ne $part_url->{"fragment"}) {
                print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\n".$parsed_uri->fragment."\n")
            }
        } else {
            print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\nNot parsing\n")
        }
    }
}

sub test_mojo {
    my $url_string = shift;
    my $part_url = shift;
    my $parsed_mojo = Mojo::URL->new($url_string);
    if (!defined($parsed_mojo)) {
        return;
    }
    if (defined($part_url->{"scheme"})) {
        if (defined($parsed_mojo->scheme)) {
            if ($parsed_mojo->scheme ne $part_url->{"scheme"}) {
                print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\n".$parsed_mojo->scheme."\n")
            }
        } else {
            print("Problem in scheme:\n".$url_string."\n".$part_url->{"scheme"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"userinfo"})) {
        if (defined($parsed_mojo->userinfo)) {
            if ($parsed_mojo->userinfo ne $part_url->{"userinfo"}) {
                print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\n".$parsed_mojo->{userinfo}."\n")
            }
        } else {
            print("Problem in userinfo:\n".$url_string."\n".$part_url->{"userinfo"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"host"}) && $part_url->{"host"} ne '') {
        if (defined($parsed_mojo->host)) {
            if ($parsed_mojo->host ne $part_url->{"host"}) {
                print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\n".$parsed_mojo->host."\n")
            }
        } else {
            print("Problem in host:\n".$url_string."\n".$part_url->{"host"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"port"})) {
        if (defined($parsed_mojo->port)) {
            if ($parsed_mojo->port ne $part_url->{"port"}) {
                print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\n".$parsed_mojo->port."\n")
            }
        } else {
            print("Problem in port:\n".$url_string."\n".$part_url->{"port"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"path-abempty"}) && $part_url->{"path-abempty"} ne '') {
        if (defined($parsed_mojo->path)) {
            my $path = decode('UTF-8', url_unescape($parsed_mojo->path));
            if (defined($path)) {
                if ($path ne $part_url->{"path-abempty"}) {
                    print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\n".$path."\n")
                }
            }
        } else {
            print("Problem in path-abempty:\n".$url_string."\n".$part_url->{"path-abempty"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"query"})) {
        if (defined($parsed_mojo->query)) {
            my $query = decode('UTF-8', url_unescape($parsed_mojo->query));
            if (defined($query)) {
                if ($query ne $part_url->{"query"}) {
                    print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\n".$query."\n")
                }
            }
        } else {
            print("Problem in query:\n".$url_string."\n".$part_url->{"query"}."\nNot parsing\n")
        }
    }
    if (defined($part_url->{"fragment"})) {
        if (defined($parsed_mojo->fragment)) {
            if ($parsed_mojo->fragment ne $part_url->{"fragment"}) {
                print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\n".$parsed_mojo->fragment."\n")
            }
        } else {
            print("Problem in fragment:\n".$url_string."\n".$part_url->{"fragment"}."\nNot parsing\n")
        }
    }
}

print("Enter number:\n"."0 - Use parse url regex\n"."1 - Use uri lib\n"."2 - Use mojo lib\n");
my $num = <>;
chomp($num);
# Open/close Json file
open(my $fh, '../fuzz/fuzz.json') or die $!;
my $json_text = do { local $/; <$fh> };
close($fh);
# Parse Json file
my $data = JSON::decode_json($json_text);
# Test
for my $item (@$data) {
    my @array = @$item;
    my $url_string = $array[0];
    my $part_url = $array[1];
    if ($num == 0) {
        test_parse_url_regex($url_string, $part_url);
    } elsif ($num == 1) {
        test_uri($url_string, $part_url);
    } else {
        test_mojo($url_string, $part_url);
    }
}