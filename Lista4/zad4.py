from inspect import getfullargspec
import math

class Func:
    def __init__(self,name,func):
        self.name = name
        self.func = func

    def __call__(self, *args):
        return self.func(*args)   

dict = {}

def overload(f):
    name = str(len(getfullargspec(f).args)) + ' ' + f.__name__
    dict[name] = Func(name,f)

    def modified_function(*args):
        return dict[str(len(args)) + ' ' + f.__name__](*args)
    return modified_function

@overload
def norm(x,y):
   return math.sqrt(x*x + y*y)
  
@overload
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)

if __name__ == "__main__":
    x = norm(2,4)
    y = norm(2,3,4)
    print(x)
    print(y)