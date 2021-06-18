import threading
import time

start = time.perf_counter()



def do_something(seconds):
	print(f'Sleeping {seconds} second(s)...')
	time.sleep(seconds)
	print('Done sleeping...')

# Create a list of threads
threads = []

# Create thread, append it to list
for _ in range(10):
	t = threading.Thread(target=do_something, args=[_])
	t.start()
	threads.append(t)

# Join threads
for thread in threads:
	thread.join()

finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s)')