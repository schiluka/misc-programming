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
        self.gender = gender
    def addRelation(self, name, gender, id):
        r = Relation(name, gender, id)
        self.relations.append(r)
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

print 'classes defined'
r1 = Relation('Name1','M','123')
r2 = Relation('Name2','F','234')
r3 = Relation('Name3','M','345')
rs = []
rs.append(r1)
rs.append(r2)
rs.append(r3)
p = Profile('ID1', 'google.com', 'Name', rs, 'M')
p.addRelation('Name1','M','123')
p.addRelation('Name2','F','234')
p.addRelation('Name3','M','345')
#jsonOut = json.dumps(p.__dict__)
jsonOut = p.toJson()
print 'json output'
print jsonOut
publicUrl = 'http://www.geni.com/people/{name}/{guid}'
geniFile = open('./geni.json','r')
contents = geniFile.read()
#print contents
jsoncontents = json.loads(contents)
firstName = jsoncontents['focus']['first_name']
lastName = jsoncontents['focus']['last_name']
publicUrl = publicUrl.replace('{name}', firstName + '-' + lastName)
publicUrl = publicUrl.replace('{guid}', jsoncontents['focus']['guid'])
p = Profile(jsoncontents['focus']['id'], publicUrl,
            firstName + ' ' + lastName, [], jsoncontents['focus']['gender'])
#print jsoncontents['focus']['id']
contents = jsoncontents['nodes']
for node in contents:
    #print node['id']
    if node.startswith('profile') and jsoncontents['focus']['id'] != contents[node]['id']:
        p.addRelation(contents[node]['first_name'] + ' ' + contents[node]['last_name'],
                      contents[node]['gender'], contents[node]['id'])
print p.id
print p.toJson()