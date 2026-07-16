def logger(func):
    def wrapper(*args,**kwargs):
        print("Searting...")
        result=func(*args,**kwargs)
        print("Finished...")
        return result
    return wrapper
@logger
def add(x,y):
    return x+y
print(add(3,5))
