from time import perf_counter 

def measure_time(func):
    def modified_function(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'{end - start}')
        return result
    return modified_function


@measure_time
def foo (a):
    return [x**2 + a for x in range(1000)]


if __name__ == '__main__':
    foo(0)