from base56 import encode, decode
from string import printable


def test_printable_letters():
    for char in printable:
        assert decode(encode(char)) == char


def test_unicode():
    for data in ['hi', 'there', "let's try Unicode", 'μ', 'Α α',
                 'Β β', 'Γ γ', 'Ξ ξ', '[ð]', 'εγγεγραμμένος', '𐀆', '𐀅']:
        assert decode(encode(data)) == data


def test_binary():
    for data in b'\x80\x81\x99\x10\x54':
        assert decode(encode(bytes([data]))) == bytes([data])
