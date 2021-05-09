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
    pass


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
