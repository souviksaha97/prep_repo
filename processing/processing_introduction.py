import multiprocessing
import time

start = time.perf_counter()



def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping...')


# Create a process
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# Start a thread
p1.start()
p2.start()

# To execute all processes before executing the following statements
p1.join()
p2.join()

finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s)')