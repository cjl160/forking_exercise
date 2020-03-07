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


def main():
    """ main function run as script """
    people = setup_people()
    print(people)


if __name__ == '__main__':
    main()
