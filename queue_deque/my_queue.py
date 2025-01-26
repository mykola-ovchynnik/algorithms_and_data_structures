import random
import time
import sys
from queue import Queue
from threading import Thread


class RequestHandler:
    def __init__(self):
        self.request_queue = Queue()
        self.running = True
        self.processed_count = 0

    def generate_request(self):
        for _ in range(10):
            request_id = random.randint(1000, 9999)
            print(f"Generated request ID: {request_id}")
            self.request_queue.put(request_id)
            time.sleep(0.5)
        self.running = False

    def process_request(self):
        while self.running or not self.request_queue.empty():
            if not self.request_queue.empty():
                request_id = self.request_queue.get()
                print(f"\nProcessing request ID: {request_id}")
                self.processed_count += 1
            else:
                print("\nThe queue is empty, no requests to process.")
            time.sleep(1.5)

    def stop(self):
        self.running = False


def main():
    handler = RequestHandler()
    generator_thread = Thread(target=handler.generate_request)
    processor_thread = Thread(target=handler.process_request)

    generator_thread.start()
    processor_thread.start()

    generator_thread.join()
    processor_thread.join()

    print("\nAll request successfully processed.")
    print(f"\nTotal requests processed: {handler.processed_count}")
    sys.exit(0)


if __name__ == "__main__":
    main()
