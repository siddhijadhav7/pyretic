from thread import start_new_thread

def thread1(cnt1):
	while (cnt1)>0 :
		print "In thread 1\n"
		cnt1-=1

def thread2(cnt2):
	while (cnt2)>0 :
		print "In thread 2\n"
		cnt2-=1

start_new_thread(thread1,(39,))
start_new_thread(thread2,(29,))

