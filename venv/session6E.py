#keyword arguments
def fun(**kwargs):
    print(kwargs)  #kwargs = keyword arguments which can be any name
    print(type(kwargs))
fun(a=10, b=20, name="john")
# fun(10="john", 20="jennie", 30="hello") #error