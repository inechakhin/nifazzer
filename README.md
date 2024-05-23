# nifazzer
nifazzer is a tool for generating payloads using the ABNF grammar, which is used in RFC to describe various data types and structures. It is possible to add individual parts of a complex rule so that they are tracked when generating values. This tool can be used as an add-on, pre-generation element for your fuzzer or an existing fuzzer.

### Usage
Python version 3 is required to run the tool. To run help, enter
```
python3 pre_fuzz.py -h
```
To easily generate 1000 values of the URI rule according to RFC 3986, enter
```
python3 pre_fuzz.py -r 3986 -f URI -c 1000
```
The generated values by default will be in the 'fuzz.json' file. To change the output file, enter
```
python3 pre_fuzz.py -r 3986 -f URI -c 1000 -o rfc3986
```
To generate values that track individual parts of the rule, enter
```
python3 pre_fuzz.py -r 3986 -f URI -c 1000 -p scheme,userinfo,host,port,path,query,fragment
```

### Test
The tool was tested using libraries for validating and parsing URL-addresses of the following programming languages:
* [Python](test/)
* [Go](https://github.com/inechakhin/nifazzer-test-go)
* [Java](https://github.com/inechakhin/nifazzer-test-java)
* [NodeJS](https://github.com/inechakhin/nifazzer-test-nodejs)
* [PHP](https://github.com/inechakhin/nifazzer-test-php)
* [Perl](https://github.com/inechakhin/nifazzer-test-perl)
* [Ruby](https://github.com/inechakhin/nifazzer-test-ruby)