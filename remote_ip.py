#! /usr/bin/env python
# Find IP address of remote host 

import socket

def get_remote_machine_info():
    # Change this URL for any address you would like to query
    remote_host = 'www.pytgo.org'
    try:
        print("The IP address is: %s"
        %socket.gethostbyname(remote_host))
    except socket.error as err_msg:
        print("%s: %s" %(remote_host, err_msg))

if __name__ == '__main__':
    get_remote_machine_info()
