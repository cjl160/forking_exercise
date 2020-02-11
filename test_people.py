""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.pet == 'Rat'
    assert oliver.hobbies == []


def test_archer():
    archer = setup_people()['Sterling_Archer']
    assert archer.first_name == 'Sterling'
    assert archer.pet == 'Babou'
    assert archer.age == 36
    assert archer.hobbies == ['Drinking', 'Being an ass', 'Super Spy']


def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
