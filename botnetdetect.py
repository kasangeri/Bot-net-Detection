#!/usr/bin/env python
# coding: utf-8

# In[6]:

import sys
from scapy.all import rdpcap
import numpy as np
import csv, os
import pickle

inp_file = sys.argv[1]
packets = rdpcap(inp_file)
prev_ts = 0
num_packets = len(packets)
for i in range(len(packets)):
    try:
        host0 = packets[5][1].src
        host1 = packets[5][1].dst
    except:
        continue
host = ""  
for i in range(len(packets)):
    try:
        src = packets[i][1].src
        dst = packets[i][1].dst
    except:
        continue
    if src!=host0 and dst!=host0:
        host = host1
        break
    elif src!=host1 and dst!=host1:
        host = host0
        break
sent_packets = 0   
rec_packets = 0
sent_bytes = 0
rec_bytes = 0
pack_max = 0
pack_min = packets[5].len
pack_total = 0
init_time = packets[0].time
final_time = packets[-1].time
total_duration = final_time - init_time
packet_freq = num_packets/total_duration
forward_ts = []
backward_ts = []
inter_time = []
count=0
for i in range(len(packets)):
    try:
        l = packets[i].len
    except:
        continue
    ts = packets[i].time
    if i>0:
        inter_time.append(ts-prev_ts)
    prev_ts = ts
    pack_max = max(pack_max,l)
    pack_min = min(pack_min,l)
    pack_total+=l
    if packets[i][1].src==host:
        sent_packets+=1
        sent_bytes+=len(packets[i][1])
        forward_ts.append(ts)
    else:
        rec_packets+=1
        rec_bytes+=len(packets[i][1])
        backward_ts.append(ts)
forward_inter_time = [forward_ts[i]-forward_ts[i-1] for i in range(1,len(forward_ts))]
backward_inter_time = [backward_ts[i]-backward_ts[i-1] for i in range(1,len(backward_ts))]

features = []
features.append(np.mean(inter_time))
features.append(sent_packets)
features.append(rec_packets)
features.append(sent_bytes)
features.append(rec_bytes)
features.append(pack_total)
features.append(pack_min)
features.append(pack_max)
features.append(max(inter_time))
features.append(min(inter_time))
features.append(total_duration)
features.append(packet_freq)
features.append(np.mean(forward_inter_time))
features.append(np.mean(backward_inter_time))
features.append(max(forward_inter_time))
features.append(min(forward_inter_time))
features.append(max(backward_inter_time))
features.append(min(backward_inter_time))

with open('rf_model', 'rb') as f:
    rf = pickle.load(f)
list = []
list.append(features)
output=rf.predict(np.array(list))
if output[0]==1.0:
    print("botnet")
else:
    print("benign")


# In[ ]:




