
import array as arr

sharath= arr.array("i",[1,2,3,4,5,0,44,66,99,2,2])

sharath.append(3)  # to add the element at last 

sharath.insert(4,99) # to add element at specific index

sharath.remove(4)   # will remove the firs occurance of the number 4 

sharath.pop(1)          # will remove the respectiuve index

sharath.extend([7,8,9])  # will be used for add multiple elemebts

sharath1=sharath[4:7]   # will create annew arrey by slcing

sharath.reverse()  # will reverese the order of the elements in shatrath

print(len(sharath)) # will be used to find length of array
print(sharath)
print(sharath1)

print(sharath.count(2)) # will return how many times 2 appears in sharath


sam=arr.array("i",[1,2,3,4,5,6,7])
for i in sam:
    print(i, end="," )
