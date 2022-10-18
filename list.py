#studymaterial = ["pens", "eraser", "books", "papers" ,"55"]
#print(studymaterial[4])

#list methods                                  # list is mutable  - can change the valuse
# this is sort methods                          #and [] show the square bracket

numbers = [4, 8, 7, 5, 6 ]
numbers.sort()
print(numbers)

# reverse sort 
#numbers = [4, 8, 7, 5, 6 ]
#numbers.sort()
#numbers.reverse()
#print(numbers)

"""
#extended slicing

numbers = [4, 8, 7, 5, 6 ]
print(numbers[::3])
#if we are add the 1 in print
#   like : [::1] ans is as well as same print [4, 8, 7, 5, 6,]
#then we enter the [::2] 2 is skeep the numbers
# ex : ans is [4, 7, 6]
 #then we enter the [::3] 3 is skeep the numbers
 # ex : ans is [4, 5]


 # if you are using nagative slicing u can used only -1
  #for ex  [::-1]# in string also use -1

numbers = [4, 8, 7, 5, 6 ]
print(numbers[1:5:2])
