import json

class Relation:
    def __init__(self, name, gender, id):
        self.name = name
        self.id = id
        self.gender = gender

class Profile:
    relations = []
    def __init__(self, id, geniLink, name, relations, gender):
        self.id = id
        self.name = name
        self.geniLink = geniLink
        self.relations = relations
    def addRelation(self, name, gender, id):
        r = Relation(name, gender, id)
        self.relations.append(r)
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

print 'classes defined'
r1 = Relation('Name1','M','123')
r2 = Relation('Name2','F','234')
r3 = Relation('Name3','M','345')
rs = []
#rs.append(r1)
#rs.append(r2)
#rs.append(r3)
p = Profile('ID1', 'google.com', 'Name', rs, 'M')
p.addRelation('Name1','M','123')
p.addRelation('Name2','F','234')
p.addRelation('Name3','M','345')
#jsonOut = json.dumps(p.__dict__)
jsonOut = p.to_JSON()
print 'json output'
print jsonOut