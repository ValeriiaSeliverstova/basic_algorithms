import queue
import random
import time
import threading

stop_program = False
my_queue = queue.Queue()

#Додати заявку до черги
def generate_request(request_id):
    request_types = ["Login", "Purchase", "Logout", "Report", "Update"]
    request_type = random.choice(request_types)
    new_request = f"Request ID {request_id} - Type: {request_type}"
    my_queue.put(new_request)
    print(f"{new_request} added to the queue")

def process_request():
    if not my_queue.empty():
        request = my_queue.get()
        print(f"Processing request {request}")
        time.sleep(random.uniform(1, 3))
    else:
        print("Queue is empty")


def listen_for_enter():
    input()  # очікуємо на Enter
    global stop_program
    stop_program = True

def main():
    global stop_program
    request_id = 1

    stop_thread = threading.Thread(target=listen_for_enter)
    stop_thread.start()

    while not stop_program:
        generate_request(request_id)
        request_id += 1
        process_request()
        time.sleep(2)

    stop_thread.join()  #завершення потоку
    print("Program stopped.")

if __name__ == "__main__":
    main()