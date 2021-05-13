from typing import List


def find_n(substring: str, text: str) -> List[int]:
    """
    Parameters:
        substring: substring to be found
        text: text to be searched
    Returns:
        List of positions in ascending order of the beginnings
        of ``substring`` in ``text``.
    """
    if not substring:
        return list(range(len(text)))
    naive_position = []
    if substring and text:
        for n in range(0, len(text) - len(substring) + 1):
            m = 0
            while m < len(substring) and text[n + m] == substring[m]:
                m += 1
                if m == len(substring):
                    naive_position.append(n)
    return naive_position


def find_kmp(substring: str, text: str) -> List[int]:
    """
    Parameters:
        substring: substring to be found
        text: text to be searched
    Returns:
        List of positions in ascending order of the beginnings
        of ``substring`` in ``text``.
    """
    if not substring:
        return list(range(len(text)))
    kmp_position = []
    if substring and text:
        prefix = [0 for i in range(len(substring))]
        i = 0
        j = 1
        while j < len(substring):
            if substring[i] == substring[j]:
                prefix[j] = i + 1
                i += 1
                j += 1
            elif i != 0:
                i = prefix[i - 1]
            else:
                j += 1
        print(prefix)
        n = 0
        m = 0
        while n < len(text):
            if text[n] == substring[m]:
                n += 1
                m += 1
            elif m != 0:
                m = prefix[m - 1]
            else:
                n += 1
            if m == len(substring):
                kmp_position.append(n - m)
                m = prefix[m - 1]
    return kmp_position


def find_kr(substring: str, text: str) -> List[int]:
    """
    Parameters:
        substring: substring to be found
        text: text to be searched
    Returns:
        List of positions in ascending order of the beginnings
        of ``substring`` in ``text``.
    """
    if not substring:
        return list(range(len(text)))
    d = 123456789
    q = 987654321
    n = len(text)
    m = len(substring)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    kr_position = []
    if substring and text and n >= m:
        for i in range(m):
            p = (d * p + ord(substring[i])) % q
            t = (d * t + ord(text[i])) % q
        for s in range(n - m + 1):
            if p == t:
                match = True
                for i in range(m):
                    if substring[i] != text[s+i]:
                        match = False
                        break
                if match:
                    kr_position = kr_position + [s]
            if s < n-m:
                t = (t - h * ord(text[s])) % q
                t = (t * d + ord(text[s+m])) % q
                t = (t + q) % q
    return kr_position
