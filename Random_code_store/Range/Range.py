##Range
#The range function creates a sequential list of numbers. usually starts from the least to the max
numbers=list(range(10))
print(numbers)
#The call to list is necessary because range by itself will create a range object. 
# This will be needed to be converted to a list for it to be used later.

nums=list(range(5))
print(nums[4])

# this is alot different because the normal way of counting is len(nums) with a total of 5 items (0,1,2,3,4,5)
nums[0]=0
nums[1]=1
nums[2]=2
nums[3]=3
nums[4]=4

#If a range is called with one argument. It produces an object with values from 0 to that argument. in other words an argument 10 will have an output of 0 to 10
#If a range is called with two arguments. It produces values from the first to the second.

numbers=list(range(3,8))
print(numbers)

print(range)==range(0,20)

num=20
print(range(num))
print(list(range(num)))


#the range always starts with the first argument and stops at a value below the last argument
nums=list(range(5,8))
print(len(nums))


#A range can have a third argument, this determines the interval of the sequence produced.
#the third argument must always be an integer.

numbers=list(range(5,20,2))
print(numbers)


nums= list(range(3,15,3))
print(nums[2])



#Counter Loops: Range
list(range(0,5)), list(range(2,5)), list(range(0,10,2))

list(range(-5,5))
list(range(5,-5,-1))

for i in range(3):
    print( i, ('python'))


master=[3,5,8,4,1,5,9,3,5,0]
s=xrange(len(master))
print(s)


master=[3,5,8,4,1,5,9,3,5,0]
for i in range(len(master)):
    print(i)
#Notice that range does not return the contents of the list but their indexes
#Result/output
0
1
2
3
4
5
6
7
8
9

nums=[2,5,3,7,5,8]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        print(i,j)
#this solution does not repeat based on order. The pairs are unique
#But it does all possible solutions  
#Result/output
0 1
0 2
0 3
0 4
0 5
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5