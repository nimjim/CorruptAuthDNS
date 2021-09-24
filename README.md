# CorruptAuthDNS

## Introduction

CorruptAuthDNS is a simple authoritative DNS server that returns a response that is not RFC compliant or a corrupted response.
It was made to verify the functions of DNS full service resolver.
It is based on [SimpleAuthDNS](https://github.com/nimjim/SimpleAuthDNS.git) and is designed to alter the response during the name resolution process.

## Requirement

- Python 3
- dnspython (http://www.dnspython.org/)

## Installation and Usage

```bash
pip3 install dnspython
git clone https://github.com/nimjim/CorruptAuthDNS.git
cd CorruptAuthDNS
python3 main.py -d -c
```

```bash
$ python3 main.py -h
usage: main.py [-h] [-s SERVER] [-p PORT] [-v] [-d] [-f FILE] [-c]

This is a simple authoritative dns that returns a corrupted response.

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        IP address for listen. Default: all addresses
  -p PORT, --port PORT  Port for listen. Default: 53
  -v, --verbose         Print verbose output
  -d, --debug           Same as "--verbose"
  -f FILE, --file FILE  The zone file to use. Default: "./corrupt.com.zone"
  -c, --corrupt         Corrupt test mode
```

## Note

See [SimpleAuthDNS](https://github.com/nimjim/SimpleAuthDNS.git) for more information on what you can do as an authoritative DNS server.
It is possible to modify the response in corrupt_response.py.
As an example, it is implemented to make a response with the wrong case if the qname is starts with case_rand_test.
This allows us to see how a DNS full resolver implementing qname case randomization behaves when it receives an answer with wrong case.

