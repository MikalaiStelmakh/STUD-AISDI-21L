def find_n(substring: str, text: str):
    """
    Parameters:
        substring: substring to be found
        text: text to be searchedP
    Returns:
        List of positions in ascending ordeer of the beginnings
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


def find_kmp(substring: str, text: str):
    """
    Parameters:
        substring: substring to be found
        text: text to be searchedP
    Returns:
        List of positions in ascending ordeer of the beginnings
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


def find_kr(substring: str, text: str):
    """
    Parameters:
        substring: substring to be found
        text: text to be searchedP
    Returns:
        List of positions in ascending ordeer of the beginnings
        of ``substring`` in ``text``.
    """
    pass
