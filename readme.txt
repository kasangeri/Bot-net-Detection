usage:
python3 final.py <pcap-file address>

Libraries:
pickle, scipy, scapy, numpy, csv, os, sys (use python3, pip install for pickle, scapy, scipy, numpy)
pip3 instll scipy
pip3 install scapy
pip3 install pickle
pip3 install numpy
(use a prefarably fresh installation of python3 or a fresh virtualenv)

Output format : "benign" - if benign
                "botnet" - if botnet

We assumed there is a single host only and continued our detection process
Detection would take some time because of the slowness of scapy tool. But that's the best tool we could find
