"""print("program start")
try:
    result=10/0
    print("result:",result)
except:
    print("an error occurred.division by zero is not aloowed.")
    print("program end")"""


"""try:
    number=int(input("enter a number:"))
    print("you entered:",number)
except valueError:
    print("Error:please enter a valid integer value.")"""

"""try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero.")
except ValueError:
    print("Error:please enter only integers.")"""

"""try:
    a=10
    b=0
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Error:division by zero.")
finally:
    print("this line always runs(finallu block)")"""


"""try:
    user_number=int(input("enter a number:"))
    result=100/user_number
except ValueError:
    print("error:invalid number format.")
except ZeroDivisionError:
    print("cannot divide by zero.")
else:
    print("success!result:",result)"""


try:
    f=open("student.txt","R")
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("error:student.txt file not found.")