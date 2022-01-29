somelist= [1,2,3,4,5]

newlist1= [x for x in somelist if x%2 == 0]
print(newlist1)

newlist2 = [x if x %2 == 0 else "odd" for x in somelist]
print(newlist2)

# newlist = [expression for item in iterable if condition == True]

# customized sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

