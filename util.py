import os
import socket

FILETYPE = ['jpg', 'jpeg', 'png']

#6 methods for both server and client

def create_header(action, **args):
    if len(args)==0:
        return f"({action})"
    elif len(args)==1:
        filename = args[0]
        return f"({action}, {filename})"
    else:
        filename = args[0]
        filesize = args[1]
        return f"({action}, {filename}, {filesize})"

def recv_header(sock):
    msg = ""
    error_str = ""
    action = ""
    header = []
    try:
        while True:
            msg += sock.recv(1024).decode()
            if msg.endswith(")"):
                msg = msg.replace("(", "").replace(")", "")
                break
        header = list(msg.split(", "))
    except Exception as e:
        error_str += e.__str__() + " || "
    finally:
        return header, error_str
                
def write_file(filename, data):
    if os.path.isfile(filename):
        return f"{filename} already exists || "
    else:
        with open(filename, 'wb') as file:
            file.write(data)
        return ""
    
def read_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            data = file.read().encode()
            data_size = len(data)
        return data, data_size
    return False

def file_list():
    return str([x for x in os.listdir() if len(element:=x.split('.')) > 1 and element[1] in FILETYPE]).strip(" ")

def recv_all(sock, amount_of_data):
    data = b''
    while len(data) < amount_of_data:
        data += sock.recv(amount_of_data - len(data))
    return data