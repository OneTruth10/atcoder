import socket
import sys
import os
from util import *

def do_header(header):
    error_msg = ""
    if len(header)==1:
        action = header[0]
    elif len(header)==2:
        action, filename = header[0], header[1]
    else:
        action, filename, filesize = header[0], header[1], int(header[2])
    if action=="list":
        try:
            data = file_list().encode()
            data_size = len(file_list().encode())
            header = create_header("list", "list of files", data_size)
        except Exception as e:
            error_msg += e.__str__ + " || "
            header = create_header("error", error_msg)
    elif action=="put":
        data = recv_all(sock, filesize)
        error_msg += write_file(filename, data) + " || "
        header = create_header(error_msg)
        data = ""
    elif action=="get":
        try:
            if read_file(filename):
                data, data_size = read_file(filename)
            header = ("get", filename, data_size)
        except Exception as e:
            error_msg += e.__str__ + " || "
            header = create_header("error", error_msg)
            data = ""
    sock.sendall(header)
    sock.sendall(data)
    return error_msg
            
def main():
    sock = socket.socket()
    error = ""
    try: 
        port = int(sys.argv[1])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("", port))
        sock.listen(5)
        print("server started succsesfully")
    except ValueError:
        print("Invalid port number")
    except Exception as e:
        print(f"Errors occured while setting up server, probably bad port number: {e}") 
    else:
        try:
            while True:
                print("Waiting for client connection")
                cconn, caddr = sock.accept()
                print(f"succsesful connection from: {cconn.getsockname()}")
                header, error_str = recv_header(sock)
                error += do_header(header)
                print(f"Succesfully completed {header[0]} request." if error=="" else f"Error occured: {error}")
        except KeyboardInterrupt:
            print("KeyboardInterrupt, Stopping server...")
        except Exception as e:
            print(f"Error while accepting new clients: {e}")
        finally:
            sock.close()
 
if __name__ == '__main__':
    main()