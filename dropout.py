""" opens a socket to a DNS server.
    When it fails, it prints a timestamp and a description of the failure.
"""
import socket
import time
from random import random

def socket_to_host(host="8.8.8.8", port=53, timeout=3):
    """ Attempt to open a socket.
        Return bool for success and a string of info.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True, ''
    except socket.error as ex:
        return False, f'{ex}'

def str_now():
    """ Return a timestamp string
    """
    return time.strftime('%b-%d %H:%M:%S', time.localtime())

HOST_IPS = [
    '8.8.8.8',          # google DNS server
    '208.67.222.222',   # open DNS
    '208.67.220.220',   # open DNS
    # '192.168.2.3',    # test IP that I know will not respond
    ]

TICKER = '|/-\\'

if __name__ == '__main__':
    print(f'{__file__} starting at {str_now()}')
    i, j = 0, 0
    while True:
        i, j = i+1, j+1
        i, j = i % len(HOST_IPS), j % len(TICKER)
        b_good, e_str = socket_to_host(HOST_IPS[i])
        if not b_good:
            print(f'FAILED at {str_now()} to {HOST_IPS[i]} {e_str}')
        else:
            print(TICKER[j]+'\r', end=' ', flush=True)
        time.sleep(2 + random() * 2)
