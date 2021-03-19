import morse


def test_read_from_file():
    morse.read_from_file("text.txt") == "Ala ma kota"


def test_encryption(benchmark):
    lines = ["Ala ma kota"]
    encrypted = ".-  .-..  .-  /  --  .-  /  -.-  ---  -  .-"
    assert benchmark(morse.encryption, lines) == encrypted

def test_encryption_multiline():
    assert morse.encryption(["Aa", "aA"]) == ".-  .-\n.-  .-"
