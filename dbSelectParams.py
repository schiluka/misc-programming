import peewee as pw
from peewee import *
from db import TopProfiles, myDB

try:
        myDB.connect()
        top = TopProfiles.select().order_by(TopProfiles.profiles.desc()).limit(1)
        steps = []
        count = 1
        for t in top:
            steps.append({'profileId':t.profileId,
                          'profileLink':t.profileLink,
                          'steps':t.steps,
                          'profiles':t.profiles
                          })
except:
        traceback.print_exc(file=sys.stdout)
myDB.close()
print steps
