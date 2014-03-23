import peewee as pw
from peewee import *
from db import TopProfiles, myDB

try:
        myDB.connect()
        # Check if existing profile
        profile = TopProfiles.select().where(TopProfiles.profileId == '6000000024671758100').get()
        if(profile.profiles < 23):
            # existing record, update counts
            #uq = UpdateQuery(TopProfiles, steps=4, profiles=23).where(
                        #TopProfiles.profileId =='6000000024671758100')
            #uq.execute()
            q = TopProfiles.update(steps=4, profiles=23).where(TopProfiles.profileId =='6000000024671758100')
            q.execute()
except Exception as e:
        # No worries. duplicate profile
        print str(e)
myDB.close()