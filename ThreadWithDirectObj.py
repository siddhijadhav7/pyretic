from threading import Thread
import time
class MyNewThread:
    def __init__(self,threadName,counter):
        self.threadName=threadName
        self.counter=counter
        #Creating object of Thread class without inheriting it
        obj=Thread(target=self.print_thread())
        obj.start()

    def print_thread(self):
        while(self.counter>0):
            self.counter-=1
            print '%d : %s ' %(self.counter,self.threadName)
        localtime=time.asctime(time.localtime(time.time()))
        print localtime
        print '\n %s is ended'%self.threadName

    """def run(self):
        self.print_thread()"""

thread1=MyNewThread("thread1",20)
print "Thread1 started"
thread2=MyNewThread("thread2",15)
print "Thread1 started"


            
