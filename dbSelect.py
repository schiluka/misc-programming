import peewee as pw
from peewee import *
from db import TopProfiles, myDB

try:
    profile = TopProfiles.select().where(TopProfiles.profileId == '123').get()
    print 'got select'
    print profile.profiles
except Exception as e:
    print 'exception'
    print e
