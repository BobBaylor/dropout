
import socket
import time
from random import random

def socket_to_host(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True, ''
    except socket.error as ex:
        return False, f'{ex}'

def str_now():
    return time.strftime('%b-%d %H:%M:%S', time.localtime())

if __name__ == '__main__':
    host_ips = [
        '8.8.8.8',
        '208.67.222.222',
        '208.67.220.220',
        # '192.168.2.3',
        ]
    ticker = '|/-\\'
    print(f'starting at {str_now()}')
    i = 0
    j = 0
    while True:
        i = i+1
        i = i % len(host_ips)
        j = j+1
        j = j % len(ticker)
        b_good, e_str = socket_to_host(host_ips[i])
        if not b_good:
            print(f'FAILED at {str_now()} to {host_ips[i]} {e_str}')
        else:
            print(ticker[j]+'\r', end=' ', flush=True)
        time.sleep(2 + random() * 2)

