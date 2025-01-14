import random
import socket

def check_port(host='10.1.16.211',port="11107"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((host,int(port)))
    ok =True
    if result == 0:
       print( f"Host {host} Port {port} is open")

    else:
       print (f"Host {host} Port {port} not open")
       ok =False
    sock.close()
    return ok

def check_ports (host,ports):
    for port in ports:
        check_port(host,port)

def create_list(r1, r2):
    return random.sample(range(r1, r2), min(100,r2-r1))

def line_to_host_port(line:str):
    host,ports_string = line.strip().split(",")
    _range =False
    if " " in ports_string:
       ports = ports_string.split(" ")
    elif "-" in ports_string:
        start, end = ports_string.split("-")
        ports = create_list(int(start),int(end))
        _range = True
    else:
        ports = [ports_string]
    return host, ports, _range

# host, ports  = line_to_host_port("10.1.44.16,8020 585")


# with open("example_check_port_list","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         host,ports = line_to_host_port(line)
#         check_ports(host,ports)


