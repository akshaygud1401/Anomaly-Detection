import requests
from tqdm import tqdm
import time
import numpy as np

test_application = {
	"std_local_source_degrees": 3.252, 
    "avg_global_source_degrees": 9650.47687,
    "max_global_dest_degrees": 21087,
    "max_global_source_degrees": 24016,
    "std_global_source_degrees": 6476.3258,
    "min_global_source_degrees": 350,
    "avg_global_dest_degrees": 7649.4788,
    "n_connections": 83,
    "min_global_dest_degrees": 104
}

url = "http://0.0.0.0:8989/"
timesarr = []
# Send 1000 requests and measure latency in ms
for i in tqdm(range(1000)):
    t0 = time.time_ns() // 1_000_000
    resp = requests.post(url, json=test_application)
    t1 = time.time_ns() // 1_000_000
    time_taken = t1 - t0
    timesarr.append(time_taken)
	
# Results
print("Response time in ms:")
print("Median:", np.quantile(timesarr, 0.5))
print("95th precentile:", np.quantile(timesarr, 0.95))
print("Max:", np.max(timesarr))

# Response time in ms:
# Median: 7.0
# 95th precentile: 14.0
# Max: 108