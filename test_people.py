""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.hobbies == []

def test_fry():
    fry = setup_people()['philip_fry']
    assert fry.first_name == 'philip'
    assert fry.age == 2040
    assert fry.hobbies == []

def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
