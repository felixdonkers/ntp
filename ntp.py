import ntplib
import time
from time import ctime

c = ntplib.NTPClient()

# https://gist.github.com/mutin-sa/eea1c396b1e610a2da1e5550d94b0453
ntp_servers = ["time.esa.int", "time.nist.gov", "pool.ntp.org", "ntp.time.nl", "time.google.com", "time.facebook.com", "time.apple.com", "time.windows.com"]
ntp_errors = [0] * len(ntp_servers)
ntp_ok = [0] * len(ntp_servers)
ntp_duration = [0.0] * len(ntp_servers)

i = 0
while True:
    i += 1
    for s in ntp_servers:
        try:
            t = time.time()
            response = c.request(s, version=3)
            ntp_duration[ntp_servers.index(s)] += float(time.time() - t)
            avg_duration = ntp_duration[ntp_servers.index(s)] / (i - ntp_errors[ntp_servers.index(s)])
            ntp_ok[ntp_servers.index(s)] += 1
            print(f"{ntp_ok[ntp_servers.index(s)]}/{i}: {ctime(response.tx_time)}, {avg_duration}, {s}")
        except:
            ntp_errors[ntp_servers.index(s)] += 1
            print(f"{ntp_errors[ntp_servers.index(s)]}/{i}: not able to get ntp time from {s}")
    time.sleep(60)
    print()
