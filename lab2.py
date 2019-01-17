#echo
#!/usr/bin/env python3

#import socket
#
#HOST = ""
#PORT = 8081
#BUFFER_SIZE = 1024
#
#def main():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#        s.bind((HOST,PORT))
#        s.listen(1) #1 means true, listen incoming connection
#        conn, addr = s.accept() #accept incoming connection
#        full_data = b""
#        while True:
#            print("check")
#            data = conn.recv(BUFFER_SIZE)#receive info that connection sends
#            if not data:
#                print("1")
#                break
#            full_data += data
#        print(full_data)
#
#
#if __name__ == "__main__":
#    main()

import socket

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}
""".format(HOST=HOST)

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        
        full_data = b""
        while True:
            print("2")
            data = s.recv(BUFFER_SIZE) # No Stoping!!!!!!
            print("1")
            if not data:
                break
            full_data += data
        
        print(full_data)
# print(data)
    except:
        pass
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    for addr_tup in addr_info:
        conn_socket(addr_tup)



# Makes sure when the module is imported doesn't run any code that isn't in a function
if __name__ == "__main__":
    main()
