from firecode.utils import *


def generate_ip_address(s):
    ips = [[]]
    for c in s:
        new_ips = []
        for addr in ips:
            # add new octet
            if len(addr) < 4:
                new_ips.append(addr + [c])
            # or extend previous one
            if addr and len(addr[-1]) < 3 and int(addr[-1] + c) <= 255:
                new_ips.append(addr[:-1] + [addr[-1] + c])
        ips = new_ips
    return ['.'.join(ip) for ip in ips if len(ip) == 4]


if __name__ == '__main__':
    assert generate_ip_address('1921682040') == [
        '19.216.82.040',
        '192.16.82.040',
        '192.168.2.040',
        '192.168.20.40',
        '192.168.204.0',
    ]
