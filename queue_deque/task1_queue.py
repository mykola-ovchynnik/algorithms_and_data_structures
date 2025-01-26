from queue import Queue
import random
import time


request_queue = Queue()


def generate_request():
    request_id = random.randint(100, 9999)
    print(f"Generated request ID: {request_id}")
    request_queue.put(request_id)


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processing request ID: {request_id}")
        time.sleep(1)
    else:
        print("The queue is empty, no requests to process.")


def main():
    while True:
        generate_request()
        process_request()


if __name__ == "__main__":
    main()
