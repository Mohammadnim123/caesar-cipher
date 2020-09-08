from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_a_string_with_a_given_shift():
    expected = 'ifmmp nz gsjfoe'
    actual = encrypt('hello my friend',27)
    assert expected == actual

def test_decrypt_a_string_with_a_given_shift():
    expected = 'hello my friend'
    actual = decrypt('ifmmp nz gsjfoe',27)
    assert expected == actual


def test_encryption_upper_and_lower_case_letters():
    expected = 'Ifmmp Nz Gsjfoe'
    actual = encrypt('Hello My Friend',1)
    assert expected == actual



def test_including_white_space():
    expected = 'Rovvy Wi Pbsoxn'
    actual = encrypt('Hel----())(()@@@lo My Fri-------end',10)
    assert expected == actual

def test_hacking():
    expected = 'It was the best of times it was the worst of times'
    actual = hacking('Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc')
    assert expected == actual