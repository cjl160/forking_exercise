""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.hobbies == []


def test_road_runner():
    road_runner = setup_people()['Road_Runner']
    assert road_runner.first_name == 'Road'
    assert road_runner.age == 71
    assert road_runner.hobbies == ['running', 'seed']


def test_squanchy():
    squanchy = setup_people()['squanchy_smith']
    assert squanchy.first_name == 'squanchy'
    assert squanchy.age == 21
    assert squanchy.hobbies == ['squanching', 'running']
    
    
def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
