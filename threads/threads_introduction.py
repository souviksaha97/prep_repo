import threading
import time

start = time.perf_counter()



def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping...')


# Create a thread
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

# Start a thread
t1.start()
t2.start()

# To execute all threads before executing the following statements
t1.join()
t2.join()

finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s)')