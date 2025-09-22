""" 
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()  # calling the original function
        print("After the function runs")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # run the actual function
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished slow task")

slow_function() """
def increment(per=5):
    print(f"i am getting : {per}")
    a=input(f"student performance:")
    if a=="average":
        print(f"i am getting :{7}")
    elif a=="exceed":
         print(f"i am getting :{10}")
    else:
        print(f"i am getting :{8}")    
increment()
"""increment(7)
increment(f"exceed:{10}")
increment(f"ok:{8}")
increment() """