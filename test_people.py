""" pytest tests for people dictionary"""
from people import setup_people


def test_oliver():
    oliver = setup_people()['Oliver_Smart']
    assert oliver.first_name == 'Oliver'
    assert oliver.age == 21
    assert oliver.hobbies == []

def test_eeyore():
	eeyore = setup_people()['Eeyore_Milne']
	assert eeyore.first_name == 'Eeyore'
	assert eeyore.age == 98
	assert eeyore.hobbies == ['Being gloomy, eating thistles and sugar cubes, Poohsticks, birthday parties, flowers, stars, sad stories and poems, looking over his hill']

def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'
