import time

class ExecutionTimeLogger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter_ns()

    def stop_and_log(self, message="Execution time", nums = 1):
        if self.start_time is None:
            raise ValueError("Timer was not started. Call start() before stop_and_log().")

        # Calculate elapsed time in nanoseconds
        end_time = time.perf_counter_ns()
        elapsed_time_ns = end_time - self.start_time
        
        # Reset start time
        self.start_time = None
        message_total = message + f"total time: {elapsed_time_ns} nanoseconds.\n"
        message_avg = message + f"average time: {elapsed_time_ns/nums} nanoseconds.\n"
        # Log the elapsed time to the file
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(message_total)
            log_file.write(message_avg)
            log_file.write("\n")

# # Example usage
# logger = ExecutionTimeLogger('log.txt')

# # Start timing
# logger.start()

# # Code snippet to measure
# result = sum([x * x for x in range(1000)])  # Replace this with your actual code

# # Stop timing and log the result
# logger.stop_and_log("Summation execution time")

# print(f"Result of the code snippet: {result}")
