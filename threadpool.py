import thread
import time

MAX_THREADS = 5
CURRENT_THREADS = 0

def getNames():
    names = []
    print 'getting names'
    names.append('jack')
    names.append('hack')
    return names

def processJob(job):
    global CURRENT_THREADS
    print job + ' started'
    count = 0
    while count < 5:
        time.sleep(1)
        count += 1
        print "%s: %s" % ( job, time.ctime(time.time()) )
    CURRENT_THREADS = CURRENT_THREADS -1

if __name__ == '__main__':
    global CURRENT_THREADS
    global MAX_THREADS
    while True:
        names = getNames()
        if( (names != None) and (CURRENT_THREADS < MAX_THREADS) ):
            for name in names:
                print 'for loop'
                CURRENT_THREADS = CURRENT_THREADS + 1
                thread.start_new_thread( processJob, (name, ) )
        print 'main sleeping'
        time.sleep(120)