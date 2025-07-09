import socket

ip = input("Enter IP: ")
port_start = int(input("Enter a Start Port: "))
port_end = int(input("Enter an End Port: "))

if port_start < port_end:
    for port in range(port_start, port_end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
else:
    print("Start port must be less than end port.")
