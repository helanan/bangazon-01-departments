import shelve
from employee import employee
from manager import Manager

bob = Person...
sue = ...
tom = ...

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()
