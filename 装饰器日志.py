import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper


@log_execution_time
def calculate_similarity():
    time.sleep(2)

calculate_similarity()