#! /usr/bin/env

import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Test remote connection')
    parser.add_argument('--host', action="store", dest="host", required=True)
    parser.add_argument('--port', action="store", dest="port", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e, sys.exit(1))

    try:
        s.connect((host, port))
    except socket.error as e:
        print("Address related error connecting to server: %s" % e, sys.exit(1))


if __name__ == '__main__':
    main()