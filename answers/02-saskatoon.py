# sadservers.com/scenario/saskatoon

import re

ips = {}
winner = {"ip": None, "count": None}

with open("access.log", "r", encoding="utf-8") as file:
    for i in file.readlines():
        line = i.rstrip()
        ip = re.search(r"\d+\.\d+\.\d+\.\d+", line).group()

        if ips.get(ip) is None:
            ips[ip] = 1
        else:
            current = ips[ip]
            ips[ip] = current + 1

for ip, count in ips.items():
    current_winner_ip = winner["ip"]

    if current_winner_ip is None:
        winner["ip"] = ip
        winner["count"] = count

    if count > winner["count"]:
        winner["ip"] = ip
        winner["count"] = count

print(winner)
