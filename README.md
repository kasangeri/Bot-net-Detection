# Bot-net-Detection
A bot-net is a network of infected hosts (bots) that works independently under the control of aBotmaster(Bot herder), which issues commands to bots usingcommand and control   (C&amp;C)servers.   Traditionally,   bot-nets   used   acentralized   client-server architecturewhich had a single point of failure but with the advent of peer-to-peer technology, the problem of single point of failure seems to have been resolved. Gaining advantage of the decentralized  nature  of  the  P2P  architecture,  botmasters  started  using  P2P  based communication  mechanism.P2P  bot-netsare  highly  resilient  against  detection  even  after some bots are identified or taken down. P2P bot-nets provide central frameworks for different cyber-crimes  which  include  DDoS  (Distributed  Denial  of  Service),  email  spam,  phishing, password sniffing, etc. So, the objective is to develop a tool for identifying P2P bot-nets using network traffic analysis.Also, the developers should detect the hosts involved in P2P traffic and then the detected hosts are further analyzed to detect bot-nets.

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
