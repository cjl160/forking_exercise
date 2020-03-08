#!/usr/bin/env python
"""people dictionary to showoff namedtuple"""
from collections import namedtuple
PERSON = namedtuple('person', 'first_name surname age pet hobbies')


def setup_people():
    """returns a dictionary of people with
       key firstname_surname: value: namedtuple PERSON
       that has firstname, surname, age, pet, hobbies items
    """
    people = {}
    _add_oliver(people)
    _add_road_runner(people)
    _add_squanchy(people)
    _add_eeyore(people)
    _add_bat_man(people)
    _add_muttley(people)
    _add_scooby(people)
    return people


def _add_oliver(people):
    """ adds oliver """
    new_p = PERSON(first_name='Oliver', surname='Smart',
                   age=21, pet='Rat', hobbies=[])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_road_runner(people):
    """ adds Road Runner """
    new_p = PERSON(first_name='Road', surname='Runner',
                   age=71, pet=None, hobbies=['running', 'seed'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_squanchy(people):
    """ adds squanchy """
    new_p = PERSON(first_name='squanchy', surname='smith',
                   age=21, pet='Rat', hobbies=['squanching', 'running'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_eeyore(people):
    """Adds eeyore"""
    new_p = PERSON(first_name='Eeyore', surname='Milne',
                    age=98, pet='', hobbies=['Being gloomy, eating thistles and sugar cubes, playing Poohsticks, going to birthday parties, flowers, stars, sad stories and poems, looking over his hill'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_bat_man(people):
    """ adds oliver """
    new_p = PERSON(first_name='Bat', surname='Man',
                   age=58, pet=None, hobbies=['Justice', 'Seed'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_muttley(people):
    """ adds muttley"""
    new_p = PERSON(first_name='Muttley', surname='Dog',
                   age=71, pet='Dick Dastardly', hobbies='Laughing')
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def _add_scooby(people):
    """ adds Scooby Doo """
    new_p = PERSON(first_name='Scoobert', surname='Doo',
                   age=7, pet='', hobbies=['Eating Scooby Snacks'])
    key = new_p.first_name + '_' + new_p.surname
    people[key] = new_p


def main():
    """ main function run as script """
    people = setup_people()
    print(people)


if __name__ == '__main__':
    main()
