from threading import Thread
import time
class MyNewThread(Thread):
    def __init__(self,threadName,counter):
        Thread.__init__(self)
        self.threadName=threadName
        self.counter=counter

    def print_thread(self):
        while(self.counter>=0):
            self.counter-=1
            print '%d : %s ' %(self.counter,self.threadName)
        localtime=time.asctime(time.localtime(time.time()))
        print localtime
        print '\n %s is ended'%self.threadName

    def run(self):
        self.print_thread()

thread1=MyNewThread("thread1",50)
print "Thread1 started"
thread2=MyNewThread("thread2",60)
print "Thread1 started"

thread1.start()
thread2.start()
            
