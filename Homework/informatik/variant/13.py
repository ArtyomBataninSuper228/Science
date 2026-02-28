from ipaddress import *

ip = ip_address('212.154.18.0')
mx = 0
for mask in range(9, 33):

    net = ip_network(f"212.154.18.25/{mask}", 0)
    if ip in net and ip != net[0] and ip != net[-1]:
        print(mask, len(list(net)))
        mx = max(len(list(net)), mx)
print(mx)