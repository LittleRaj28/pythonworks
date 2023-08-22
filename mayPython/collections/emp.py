employee = {"id":100,"name":"vijay","department":"hr","salary":250000}
#create a function for returning employee name

def get_name(emp):
    return emp.get("name")
print(get_name(employee))

#create a lambda function for returning  the salary

salary = lambda emp:emp.get("salary")
print(salary(employee))

#*args  positional arguments takes anynumber of parameter type tuple

def addition(*args):
    return sum(args)
print(addition(10,20))
print(addition(10,20,30,40))

#lambda
addition = lambda *args:sum(args)
print(addition(10,50))

max_fn = lambda *args:max(args)
print(max_fn(25,65,235))

