""" pytest tests for people dictionary"""
from people import setup_people


def test_jerry():
    jerry = setup_people()['Jerry_Smith']
    assert jerry.first_name == 'Jerry'
    assert jerry.age == 50
    assert jerry.hobbies == []


def test_fry():
    fry = setup_people()['Philip_Fry']
    assert fry.first_name == 'Philip'
    assert fry.age == 2040
    assert fry.hobbies == []


def test_cartman():
    cartman = setup_people()['Eric_Cartman']
    assert cartman.first_name == 'Eric'
    assert cartman.age == 10
    assert cartman.hobbies == []


def test_bat_man():
    bat_man = setup_people()['Bat_Man']
    assert bat_man.first_name == 'Bat'
    assert bat_man.age == 58
    assert bat_man.hobbies == ['Justice', 'Seed']


def test_eeyore():
    eeyore = setup_people()['Eeyore_Milne']
    assert eeyore.first_name == 'Eeyore'
    assert eeyore.age == 98
    assert eeyore.hobbies == ['Being gloomy, eating thistles and sugar cubes, playing Poohsticks, going to birthday parties, flowers, stars, sad stories and poems, looking over his hill']


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


def test_scooby():
    scooby = setup_people()['Scoobert_Doo']
    assert scooby.first_name == 'Scoobert'
    assert scooby.age == 7
    assert scooby.pet == ''
    assert scooby.hobbies == ['Eating Scooby Snacks']


def test_archer():
    archer = setup_people()['Sterling_Archer']
    assert archer.first_name == 'Sterling'
    assert archer.pet == 'Babou'
    assert archer.age == 36
    assert archer.hobbies == ['Drinking', 'Being an ass', 'Super Spy']


def test_all_keys_match_names():
    for key, person in setup_people().items():
        assert key == f'{person.first_name}_{person.surname}'


def test_muttley():
    muttley = setup_people()['Muttley_Dog']
    assert muttley.first_name == 'Muttley'
    assert muttley.age == 71
    assert muttley.hobbies == 'Laughing'
