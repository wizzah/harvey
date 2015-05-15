#!/usr/bin/env python2.7

import config.config as config
import sys
print sys.path

if __name__ == '__main__':
    
    con = config.con
    
    db = con.harvey
    
    people = db.people
    
    #insert syntax for direct JSON
    #people.insert({'name': 'Shane','food': 'Chinese', 'location': 'Orlando, FL'})
    #people.insert({'name': 'Dustin','food': 'Real Chinese'})
    #people.insert({'name': 'Tony','type': 'Real Woman', 'location': 'Orlando, FL'})
    
    peeps = people.find()
    
    names = peeps[0]['name']
    #peeps = people.find({'name': {'$regex': '.*[Sh].*'}})
    
    print names
    
    #person = people.find_one({'food': 'Chinese'})
    #person['food']
    #people.save(person)
    
    print "INSERT & FIND TEST"
    for person in peeps:
        print person
        
    #for person in people.find():
    #    people.remove(person)