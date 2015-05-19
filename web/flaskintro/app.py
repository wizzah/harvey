from flask import Flask, request
app = Flask(__name__)
import config.config as config
import sys
print sys.path
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None, methods=['GET', 'POST']):
    return render_template('form_for_research.html', name=name)

@app.route('/')
def hello_world(name='WTF'):
    # get or make different parts of the form to pass
    # make a list of dictionaries, like what json is
    survey = dict()
    phone_carrier = ["one", "two", "three"]
    survey["phone_carrier"] = phone_carrier
    gender = ["female", "male", "don't want to disclose"]
    survey["gender"] = gender
    # etc
    print survey
    return render_template('form_for_research.html', name=name, survey=survey)

@app.route('/researcher/')
def researcher():
    return " <html><body><h1>Researcher Page</h1><pre>{0}</pre></body></html> ".format(search_database())

@app.route('/submit', methods=['GET', 'POST'])
def form():
    #email = request.form['emailAddress']
    #print "The email address is '" + email + "'"
    print "Hey, is this getting called, bro?:", request.form
    #import pdb;pdb.set_trace()
    #return render_template('form_for_research.html').replace("<!--verify-->", "<br>".join([var for var in request.form]))
    return "<html><body><h1>Your Mom THanks you</h1>{0}<pre>{1}</pre></body></html>".format(request.form.get('firstName', 'NA'), str(request.form))

def search_database():
    
    output = ""
    
    con = config.con
    db = con.harvey
    people = db.people
    #insert syntax for direct JSON
    #people.insert({'name': 'Shane','food': 'Chinese', 'location': 'Orlando, FL'})
    #people.insert({'name': 'Dustin','food': 'Real Chinese'})
    #people.insert({'name': 'Tony','type': 'Real Woman', 'location': 'Orlando, FL'})
    peeps = people.find()
    
    names = peeps[2]['name']
    #peeps = people.find({'name': {'$regex': '.*[Sh].*'}})
    
    # print names
    output += names + "\n"
    
    #person = people.find_one({'food': 'Chinese'})
    #person['food']
    #people.save(person)
    
    print "INSERT & FIND TEST"
    for person in peeps:
        # print person
        # If no value, prevents error, get method in Python
        output += str(person.get('type',"N/A")) + "\n" 
        
    #for person in people.find():
    #    people.remove(person)
    
    return output

if __name__ == '__main__':
    app.run(debug=True)