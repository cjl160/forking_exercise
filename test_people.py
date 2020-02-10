""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.pet == 'Rat'
    assert oliver.hobbies == []

def test_scooby():
    scooby = setup_people()['Scoobert_Doo']
    assert scooby.first_name == 'Scoobert'
    assert scooby.age == 7
    assert scooby.pet == ''
    assert scooby.hobbies == ['Eating Scooby Snacks']

def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
