import socket
import sys
import os
from util import *

def main():
    try:
        if (len(sys.argv) < 3):
            raise Exception("Incorrect usage, expected more arguments")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = sys.argv[1]
        port = int(sys.argv[2])
        action = sys.argv[3]
        filename = "x"
        if action in ("put", "get"):
            filename = sys.argv[4]
            if not len(filename.split(".")) >1:
                raise Exception("Incorrect filename, please include file extension")
            if filename.split()[1] not in FILETYPE:
                raise Exception("Filetype not supported")

        sock.connect((hostname, port))
        print("connection to server sucsseful")
    except ValueError:
        print(f"Invalid port number: {port}")
    except Exception as e:
        print(f"Error occured while connecting... Error: {e}")
    else:
        error_msg = ""
        if action=="list":
            header = create_header("list")
            sock.sendall(header)
            header, error_str = recv_header(sock)
            error_msg += error_str
            if error_str=="":
                data = recv_all(header[2])
            print(data.decode())
        elif action=="get":
            header = create_header("get", filename)
            sock.sendall(header)
            header, error_str = recv_header(sock)
            error_msg += error_str
            if header[0]=="error":
                error_msg += header[1]
            else:
                data = recv_all(header[2]).decode()
                error_msg += write_file(filename, data)
        else:
            if read_file(filename):
                data, data_size = read_file(filename)
                header = create_header("put", filename, data_size)
                sock.sendall(header)
                sock.sendall(data)
                header, error_str = recv_header()
                error_msg += header[0]
                error_msg += error_str
            else:
                error_msg += f"Could not find file named: {filename}"
        print(f"Completed {action} request sucssefully " if error_msg == "" else f"Errors occured while during {action} request from server: {hostname} : {error_msg}")
        

if __name__ == '__main__':
    main()