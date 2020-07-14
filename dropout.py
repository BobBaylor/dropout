""" opens a socket to a DNS server.
    When it fails, it prints a timestamp and a description of the failure.
"""
import socket
import time
from random import random
from itertools import cycle

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

    ticks = cycle(TICKER)   # circular list of spinning line characters
    host_ips = cycle(HOST_IPS)  # circular list of ip addresses
    while True:
        a_host = next(host_ips)
        b_good, e_str = socket_to_host(a_host)
        if not b_good:
            print(f'FAILED at {str_now()} to {a_host} {e_str}')
        else:
            print(next(ticks)+'\r', end=' ', flush=True)
        time.sleep(2 + random() * 2)
