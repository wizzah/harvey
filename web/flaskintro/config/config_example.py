global config

from pymongo import Connection

# URI for Mongo
con = Connection("mongodb://<user>:<password>@<info>.mongolab.com:<info>/<databasename>")
