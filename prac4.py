import ipaddress
ip = input("Enter network address with prefix (e.g. 192.168.1.0/24) : ")
network = ipaddress.ip_network(ip)
subnets = list(network.subnets(new_prefix=26))

for i, subnet in enumerate(subnets, 1):
    print(f"Subnet {i} = {subnet} Mask = {subnet.netmask}")