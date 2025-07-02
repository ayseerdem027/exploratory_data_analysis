import threading
import queue

file_name = "Information.txt"
data_queue = queue.Queue(maxsize=5)
SENTINEL = None  # Signal to tell the processing thread to stop


def extract_data_from_file():
    with open(file_name, "r") as file:
        for line in file:
            data_queue.put(line.strip())
            print(f"Extracted data: {line.strip()}")
    # Signal that we're done producing
    data_queue.put(SENTINEL)


def process_data_received():
    while True:
        try:
            data = data_queue.get()
            if data is SENTINEL:
                data_queue.task_done()
                break  # Exit the loop if sentinel is received
            if any(char.isdigit for char in data):
                print(f"Processed data: {data}")
            data_queue.task_done()
        except Exception as e:
            print(f"Error processing data: {e}")
            data_queue.task_done()


if __name__ == "__main__":
    extract_data_thread = threading.Thread(target=extract_data_from_file)
    process_data_thread = threading.Thread(target=process_data_received)

    extract_data_thread.start()
    process_data_thread.start()

    extract_data_thread.join()
    process_data_thread.join()
