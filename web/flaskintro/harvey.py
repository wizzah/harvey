#!/usr/bin/env python

from pymongo import Connection
from config import *

if __name__ == '__main__':
    #todo - supply real database credentials from separate config file
    
    db = con.test_database
    
    people = db.people
    
    people.insert({'name': 'Shane','food': 'Chinese', 'location': 'Orlando, FL'})
    people.insert({'name': 'Dustin','food': 'Real Chinese'})
    people.insert({'name': 'Tony','type': 'Real Woman', 'location': 'Orlando, FL'})
    
    #peeps = people.find({'food': 'Chinese'})
    peeps = people.find({'name': {'$regex': '.*[Sh].*'}})
    
    person = people.find_one({'food': 'Chinese'})
    #person['food']
    people.save(person)
    
    print "INSERT & FIND TEST"
    for person in peeps:
        print person
        
    for person in people.find():
        people.remove(person)