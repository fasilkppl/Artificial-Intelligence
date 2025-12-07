x = input("enter num 1: ")
y = input("enter num 2: ")


try:
    z=(int(x)/int(y))
except Exception as e:
    print("exception occured : ",e)
    print("exception Type : ",type(e).__name__)
    z='Not Possible'
except ValueError as n:
    print('Exception: ',n)


print('division : ', z)

