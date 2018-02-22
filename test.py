from base56 import encode, decode

def test_end_to_end():
    for data in [ 'hi', 'there', "let's try Unicode", 'μ', 'Α α',
            'Β β', 'Γ γ', 'Ξ ξ', '[ð]', 'εγγεγραμμένος', '𐀆', '𐀅']:
            assert decode(encode(data)) == data

