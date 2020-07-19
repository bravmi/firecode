from firecode.utils import *


def generate_ip_address(s):
    n = len(s)

    @cached
    def go(i, d):
        """
        i is the current s index, d is the ip depth
        """
        if i == n and d == 0:
            return [[]]
        if i >= n:
            return []
        if d <= 0:
            return []

        ans = []
        for j in range(1, 4):
            p = s[i : i + j]
            if p and int(p) <= 255:
                ans.extend([p] + r for r in go(i + j, d - 1))
        return ans

    ips = ['.'.join(ip) for ip in go(0, 4)]
    return ips


if __name__ == '__main__':
    ans = generate_ip_address('1921682040')
    assert ans == [
        '19.216.82.040',
        '192.16.82.040',
        '192.168.2.040',
        '192.168.20.40',
        '192.168.204.0',
    ]
