from socket import *

def port_scan(host, port):
    s = socket(AF_INET, SOCK_STREAM) # Setting up TCP protocol
    try: # Exception Handling
        s.connect((host, port)) # Connecting to port
        print("[+] {} port is open".format(port))
    except: # If connection fails
        print("[+] Port is closed")