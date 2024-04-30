from queue import Queue
import time

queue = Queue()

def generate_unique_id():
    return int(time.time() * 1000000)

def generate_request():
    request_id = generate_unique_id()  
    request = {"id": request_id} 
    queue.put(request) 
    print(f"Request {request_id} is added to the queue.")

def process_request():
    if not queue.empty():
        request = queue.get() 
        print(f"Request {request['id']} is processed.")
    else:
        print("The queue is empty. No tasks to execute.")

while True:
    generate_request() 
    process_request() 
    time.sleep(1)

