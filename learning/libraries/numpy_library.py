import numpy as np
from numpy import random

""" Numerical Python (NumPy)
Python library used for working with arrays and also has functions for working 
in domain of linear algebra, fourier transform, and matrices. NumPy aims to 
provide an array object that is faster than traditional Python lists by storing 
at one continuous place in memory unlike lists, so processes can access and 
manipulate them very efficiently. This behavior is called locality of reference 
in computer science. It supports interacting with massive multidimensional array 
structures.

Install it using this command: pip install numpy
Once NumPy is installed, import it in your applications by adding the 
import numpy as np
"""

""" Overview
Import NumPy
import numpy as np

Creating Arrays
From a Python list:
arr = np.array([1, 2, 3, 4])
Using arange:
arr = np.arange(10)  # Creates an array from 0 to 9
Zeros and ones:
zeros_arr = np.zeros((3, 4))  # Create a 3x4 array of zeros
ones_arr = np.ones((2, 2))  # Create a 2x2 array of ones
Random arrays:
random_arr = np.random.rand(5)  # Create an array of 5 random numbers between 0 
and 1

Array Attributes
Shape:
shape = arr.shape  # Returns a tuple of array dimensions
Data type:
dtype = arr.dtype  # Returns the data type of the elements
Size:
size = arr.size  # Returns the total number of elements
Dimension:
ndim = arr.ndim  # Returns the number of dimensions

Array Indexing and Slicing
Indexing:
element = arr[2]  # Accesses the third element
Slicing:
subarr = arr[1:4]  # Creates a subarray from index 1 to 3 (exclusive)

Array Operations
Arithmetic:
addition = arr + 2  # Adds 2 to each element
multiplication = arr * 3  # Multiplies each element by 3
Comparison:
greater_than = arr > 2  # Returns a boolean array
Universal functions:
sin_arr = np.sin(arr)  # Applies sin function to each element

Array Manipulation
Reshaping:
reshaped_arr = arr.reshape(2, 2)  # Reshapes the array
Transposing:
transposed_arr = arr.T  # Transposes the array
Concatenation:
joined_arr = np.concatenate((arr1, arr2))  # Joins arrays along an existing axis
Stacking:
stacked_arr = np.stack((arr1, arr2), axis=1)  # Stacks arrays along a new axis

Other Useful Functions
Sum:
total = np.sum(arr)  # Calculates the sum of all elements
Mean:
mean_value = np.mean(arr)  # Calculates the mean of the array
Standard deviation:
std_dev = np.std(arr)  # Calculates the standard deviation
Dot product:
dot_product = np.dot(arr1, arr2)  # Calculates the dot product 
"""

""" Creating NumPy arrays
Pass a list, tuple or any array-like object into the array() method, and it will 
be converted into an ndarray
arr = np.array([1, "car", 3, 4, 5])
arr2 = np.array((1, 2, 3, 4, 5)) 
print(type(arr))
<class 'numpy.ndarray'>
"""

""" Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays). Nested array: 
arrays that have arrays as their elements.

0-D Arrays (Scalars) are the elements in an array. Each value in an array is a 
0-D array.
zeroD = np.array(10)

1-D or uni-dimensional Arrays is an array that has 0-D arrays as its elements.
oneD = np.array([1, 2, 3, 4, 5])

2-D Arrays is an array that has 1-D arrays as its elements. These are often used 
to represent matrix or 2nd order tensors.
twoD = np.array([[1, 2, 3], [4, 5, 6]])
print(twoD)
>>>[[1 2 3]
   [4 5 6]]

3-D arrays is an array that has 2-D arrays(matrices) as its elements. These are 
often used to represent a 3rd order tensor.
threeD = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(threeD)
>>>[[[1  2  3]
    [4  5  6]]
   [[7  8  9]
    [10 11 12]]]

When the array is created, the number of dimensions can be defined by using the 
ndmin argument. It can also tell how many dimensions arrays have.

fiveD = np.array([1, 2, 3, 4], ndmin=5)
print(fiveD, fiveD.ndim) 
>>>[[[[[1 2 3 4]]]]] 5
fiveDD = np.array([1,2,3,4])
print(fiveDD, fiveDD.ndim)
>>>[1 2 3 4] 1
"""

""" Array Indexing
1-D: Access an array element by referring to its index number.
oneD = np.array([1, 2, 3, 4, 5])
print(oneD[0])
>>>1

2-D: Use comma separated integers representing the dimension and the index of 
the element. Think of a table with rows and columns, where the dimension 
represents the row and the index represents the column.
twoD = np.array([[1, 2, 3], [4, 5, 6]])
print(twoD[1, 2])
>>>6
print(twoD[1, -2])
>>>5

3-D: To access elements from 3-D arrays, use comma separated integers 
representing the dimensions and the index of the element.
threeD = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(threeD[0, 1, 2])
>>>6, since the 0 captures[1, 2, 3], [4, 5, 6], the 1 [4, 5, 6] and the 2 
results in 6 
"""

""" Slicing arrays
Syntax of slicing is [start:end] or [start:end:step]. If start isn't passed, 
it's considered 0, end is considered length of array in the dim and step is 
considered 1

slicingOneD = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(slicingOneD[1:8:2])
>>>[2 4 6 8]

slicingTwoD = np.array([[1, 2, 3], [4, 5, 6]])
print(slicingTwoD[1, 0:2])
>>>[4 5]
"""

""" Data types
The NumPy array object has a property called dtype that returns the data type 
of the array. List of all data types in NumPy and the characters used to
represent them:
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type(void)

Creating Arrays With a Defined Data Type
array() function can take an optional argument: dtype to define the expected 
data type of the array elements:
arrDT = np.array([1, 2, 3, 4, 20000], dtype='S')
print(arrDT) 
>>>[b'1' b'2' b'3' b'4' b'20000'] (b = byte string)
print(arrDT.dtype) 
>>>S5 (5 bytes integer)

Converting Data Type on Existing Arrays
Make a copy of the array with the astype() method to copy the array, and specify 
the data type as a parameter.
arrType = np.array([1.1, 2.1, 3.1])
newarr = arrType.astype('i')
print(newarr)
>>>[1 2 3]
print(newarr.dtype)
>>>int32 
"""

""" Copy vs View
The main difference between a copy and a view of an array is that the copy is a 
new array, and the view is just a view of the original array. The copy owns the 
data and any changes made to the copy will not affect original array, and any 
changes made to the original array will not affect the copy. The view does not 
own the data and any changes made to the view will affect the original array, 
and any changes made to the original array will affect the view.

arrCV = np.array([1, 2, 3, 4, 5])
x = arrCV.copy()
y = arrCV.view()
arrCV[0] = 42
print(arrCV)
>>>[42  2  3  4  5]
print(x)
>>>[1  2  3  4  5]
print(y)
>>>[42  2  3  4  5]

Check if Array Owns its Data
Every NumPy array has the attribute "base" that returns None if the array owns 
the data. Otherwise, the base  attribute refers to the original object.
print(x.base)
>>>None
print(y.base)
>>>[42 2 3 4 5] which is the original array
"""

""" Shape and reshape
Attribute called shape returns a tuple with each index having the number of 
corresponding elements in each dimension.
arrShape = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arrShape)
>>>[[1, 2, 3, 4],
    [5, 6, 7, 8]]
print(arrShape.shape)
>>>(2, 4) there are 2 rows (the outer brackets) and 4 columns (the elements 
within each inner bracket).

By reshaping using reshape() we can add or remove dimensions or change number of 
elements in each dimension. reshape(<rows>, <columns>)
arrReshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arrReshape.reshape(4, 3)
print(newarr)
>>>[[ 1  2  3]
    [ 4  5  6]
    [ 7  8  9]
    [10 11 12]]

Flattening array is also possible by converting a multidimensional array into a 
1D array using reshape(-1).
arrFlat = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arrFlat.reshape(-1)
print(newarr)
>>>[1 2 3 4 5 6]
"""

""" Iterating and enumerating
Iterating: going through elements one by one. If n-D array is iterated on, it 
will go through n-1th dimension one by one. To return the actual values, the 
scalars, iterate the arrays in each dimension.

2-D example:
arr = np.array([[1,2,3,4],[2,3,4,5]])
for x in arr:
    for y in x:
        print(y)
>>>1
2
3
4
2
3
4
5

3-D example:
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)

Or by using the nditer() function
for x in np.nditer(arr):
    print(x)

Enumerating
for idx, x in np.ndenumerate(arr):
    print(idx, x)
"""

"""Joining, stacking and splitting
Joining: putting contents of two or more arrays in a single array.
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
joinarr = np.concatenate((arr1, arr2))
print(joinarr)
>>>[[1 2]
    [3 4]
    [5 6]
    [7 8]]

Joining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is that concatenate is 
used to join arrays along existing dimensions, while stack is used to create a 
new dimension for the combined arrays.
stackarr = np.stack((arr1, arr2), axis = 1)
print(stackarr)
>>>[[[1 5] [2 6]]
    [[3 7] [4 8]]]

Stacking along rows
stackrowarr = np.hstack((arr1, arr2))
print(stackrowarr)
>>>[[1 2 5 6]
    [3 4 7 8]]

Stacking along columns
stackcolarr = np.vstack((arr1, arr2)) 
print(stackcolarr)
>>>[[1 2]
    [3 4]
    [5 6]
    [7 8]]

Stacking along height (depth)
stackdeptharr = np.dstack((arr1, arr2)) 
print(stackdeptharr)
>>>[[[1 5]
    [2 6]]

    [[3 7]
    [4 8]]]

Key Differences:
Shape: Concatenation preserves the original shape of the arrays along the other 
axes, while stacking introduces a new axis.
Dimensionality: Concatenation can change the shape of the resulting array, while 
stacking always increases the dimensionality.

Splitting: splitting array(s) into multiple. In this example, newarr is split 
into 3 arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
>>>[array([1, 2]), array([3, 4]), array([5, 6])]
print(newarr[0])
>>>[1 2]
print(newarr[1])
>>>[3 4]
print(newarr[2])
>>>[5 6]
"""

"""Searching, sorting and filtering
Search an array for a certain value, and return the indexes that get a match 
using where() 
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
>>>(array([3, 5, 6], dtype=int64),)
Which means that the value 4 is present at indexes 3, 5, and 6.

Perform a binary search in the array and return the index where the specified 
value would be inserted to maintain the search order with searchsorted()
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, 7)
print(x)
>>>3 The output 3 indicates the value 7 would be inserted at index 3 to maintain 
sorted order of the array arr. 7 should be placed after the element at index 2 
(which is 5) to preserve the ascending order of the array.

By default the left most index is returned, but side='right' to return the right 
most index instead is also possible.
x = np.searchsorted(arr, 7, side ="right")
To search for more than one value, use an array with the specified values.
x = np.searchsorted(arr, [2, 4, 6])
print(x)
>>>[1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the 
original array to maintain the order.

Sorting Arrays
Putting elements in an ordered sequence. Ordered sequence is any sequence that 
has an order corresponding to elements, like numeric or alphabetical, ascending 
or descending.
arr = np.array([[5, 100, 2, 15], [2, 1, 10, 9]])
print(np.sort(arr))
>>>[[  2   5  15 100]
    [  1   2   9  10]]

Filtering Arrays
Getting some elements out of an existing array and creating a new array out of 
them. Filtering an array using a boolean index list (True or False). If the 
value at an index is True that element is included in the filtered array, if the 
value at that index is False that element is excluded from the filtered array.
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
[41 43]

Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
>>>[False False  True  True]
>>>[43 44]
"""

""" ufuncs
ufuncs stands for "Universal Functions" which are NumPy functions that operate 
on the ndarray object. ufuncs are used to implement vectorization in NumPy which 
is way faster than iterating over elements. Vectorization: converting iterative 
statements into a vector based operation. They also provide broadcasting and 
additional methods like reduce, accumulate etc. that are very helpful for 
computation.

ufuncs also take additional arguments, like:
where - boolean array/condition defining where the operations should take place.
dtype - defining the return type of elements.
out - output array where the return value should be copied.

Example: add the Elements of Two Lists
list 1: [1, 2, 3, 4]
list 2: [4, 5, 6, 7]

One way of doing it is to iterate over both of the lists and then sum each 
elements with for loop and append

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)
>>>[5, 7, 9, 11]

NumPy has a ufunc for this, called add(x, y) that will produce the same result.

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)
"""

""" Create ufunc
Define a function like with normal functions in Python, then add it to NumPy 
ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:
function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
>>>[6 8 10 12]

Check if a function is a ufunc:
print(type(np.add))
>>><class 'numpy.ufunc'>
"""

""" Arithmetic operators in ufunc 
Arithmetic Conditionally: means that we can define conditions where the 
arithmetic operation should happen.

Example arrays:
array1 = np.array([10,21,34,421,51])
array2 = np.array([6,7,8,9,10])

Addition
The add() function sums the content of two arrays, and return the results in a 
new array.

result = np.add(array1, array2)
print(result)
>>>[ 16  28  42 430  61]

Subtraction
The subtract() function subtracts the values from one array with the values from 
another array, and return the results in a new array.

result = np.subtract(array1, array2)
print(result)
>>>[  4  14  26 412  41]

Multiplication
The multiply() function multiplies the values from one array with the values 
from another array, and return the results in a new array.

result = np.multiply(array1, array2)
print(result)
>>>[  60  147  272 3789  510]

Division
The divide() function divides the values from one array with the values from 
another array, and return the results in a new array.

result = np.divide(array1, array2)
print(result)
>>>[ 1.66666667  3.          4.25       46.77777778  5.1       ]

Power
The power() function rises the values from the first array to the power of the 
values of the second array, and return the results in a new array.

result = np.power(array1, array2)
print(result)
>>>[   1000000 1801088541 -912490240 -747530235  695354697]

Remainder
Both the mod() and the remainder() functions return the remainder of the values 
in the first array corresponding to the values in the second array, and return 
the results in a new array.

result = np.remainder(array1, array2)
# result = np.mod(array1, array2)
print(result)
>>>[4 0 2 7 1]

Quotient and Mod
The divmod() function return both the quotient and the the mod. The return value 
is two arrays, the first array contains the quotient and second array contains 
the mod.

result = np.divmod(array1, array2)
print(result)
>>>(array([ 1,  3,  4, 46,  5]), array([4, 0, 2, 7, 1]))

Absolute Values
Both the absolute() and the abs() functions do the same absolute operation 
element-wise but we should use absolute() to avoid confusion with python's 
inbuilt math.abs()

result = np.absolute(array1)
print(result)
>>>[ 10  21  34 421  51]
"""

""" Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

Truncation
Remove decimals, return float number closest to zero. 
Use the trunc() and fix() functions.
arr = np.trunc([1.129, 29.567])
# arr = np.fix([1.129, 29.567])
print(arr)
>>>[ 1. 29.]

Rounding
The around() function increments preceding digit or decimal by 1 if >=5 else 
do nothing.
E.g. Round off 1.519 to 2 decimal places:
arr = np.around(1.519,2)
print(arr)
>>>2.0

Floor
The floor() function rounds off decimal to nearest lower integer.
E.g. floor of 3.166 is 3.
arr = np.floor([-3.12, 3.15])
print(arr)
>>>[-4.  3.]

Ceil
The ceil() function rounds off decimal to nearest upper integer.
E.g. ceil of 3.166 is 4.
arr = np.ceil([-3.1, 3.2])
print(arr)
>>>[-3.  4.]
"""

""" Logs
NumPy provides functions to perform log at the base 2, e and 10. All of the log 
functions will place -inf or inf in the elements if the log can not be computed.

Log at Base 2
Use the log2() function to perform log at the base 2.

Example
Find log at base 2 of all elements of following array:
arr = np.arange(1, 10)
print(np.log2(arr))
>>>[0.         1.         1.5849625  2.         2.32192809 2.5849625
 2.80735492 3.         3.169925  ]
The arange(1, 10) function creates a NumPy array containing numbers from 1 up 
to, but not including, 10. E.g. Create an array from 0 to 10 with a step of 2
arr = np.arange(0, 11, 2)
print(arr) output: [0 2 4 6 8 10]
print(np.log(arr)) calculates the natural logarithm of each element in the 
arr array.

Log at Base 10
Use the log10() function to perform log at the base 10.
arr = np.arange(1, 10)
print(np.log10(arr))

Natural Log, or Log at Base e
Use the log() function to perform log at the base e.
arr = np.arange(1, 10)
print(np.log(arr))

Log at Any Base
NumPy does not provide any function to take log at any base, therefore use
frompyfunc() along with inbuilt function math.log() with two input parameters 
and one output parameter:

Example
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
This line creates a NumPy universal function (ufunc) from the built-in Python 
log function.
np.frompyfunc takes three arguments:
log: The Python function to be converted into a ufunc.
2: The number of input arguments for the function.
1: The number of output arguments for the function.
print(nplog(100, 15))
The output will be the logarithm of 100 to the base 15.
"""

""" Summations
Difference between summation and addition
Addition is done between two arguments, summation happens over n elements.
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new = np.add(arr1,arr2)
print(new)
>>>[5 7 9]
new2 = np.sum([arr1,arr2])
print(new2)
>>>21
Specifying axis=n will sum the numbers in n arrays.
new3 = np.sum([arr1,arr2], axis=1)
print(new3)
>>>[ 6 15]

Cummulative Sum
Cummulative sum using cumsum() means partially adding the elements in array.
E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = 
[1, 3, 6, 10].
arr = np.array([1,2,3])
new = np.cumsum(arr)
print(new)
>>>[1 3 6]
"""

""" Products
To find the product of the elements in an array, use the prod() function.
arr = np.array([1,4,8,10])
prodarr = np.prod(arr)
print(prodarr)
>>>320 (1*4*8*10)

Find the product of the elements of two arrays:
arr1 = np.array([10,11,12])
arr2 = np.array([19,20,21])
prodarr = np.prod([arr1,arr2])
print(prodarr)
>>>10533600 (10*11*12*19*20*21)

Specifying axis=n will sum the numbers in n arrays.
prodarr = np.prod([arr1,arr2],axis=1)
print(prodarr)
>>>[1320 7980]

Cummulative Product
Cummulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = 
[1, 2, 6, 24]
arr1 = np.array([10,11,12])
prodarr = np.cumprod(arr1)
print(prodarr)
>>>[  10  110 1320]
"""

""" Differences
Differences
A discrete difference means subtracting two successive elements.
To find the discrete difference, use the diff() function.
E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

Compute discrete difference of the following array:
arr = np.array([120,122,150,1])
newarr = np.diff(arr)
print(newarr) 
>>>[   2   28 -149]

This operation can be performed repeatedly by giving parameter n.
E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be 
[2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the 
new result: [1-1, 1-1] = [0, 0]

newarr2 = np.diff(arr, n=2)
print(newarr2)
>>>[  26 -177]
[122-120, 150-122, 1-150] = [2 28 -149]. [28-2, -149-28] = [26 -177]
"""

""" LCM Lowest Common Multiple
Lowest Common Multiple is the smallest number that is a common multiple of
two numbers.

Find the LCM of the following two numbers:
num1 = 10
num2 = 14
x = np.lcm(num1,num2)
print(x)
>>>70 
10*7 = 70 and 14*5 = 70

Finding LCM in Arrays
To find the Lowest Common Multiple of all values in an array, use reduce().
The reduce() method will use the ufunc, in this case the lcm() function, on each 
element, and reduce the array by one dimension.

Find the LCM of the values of the following array:
arr = np.array([3,5,9])
x = np.lcm.reduce(arr)
print(x)
>>>45 
3*15 = 45, 5*9 = 45, 9*5 = 45
"""

""" GCD Greatest Common Denominator
The GCD (Greatest Common Denominator), or HCF (Highest Common Factor), is the 
biggest number that is a common factor of both of the numbers.

Find the HCF of the following two numbers:

arr = np.arange(2,8,2)
x = np.gcd(arr)
print(x)
>>>2
[2/2 = 1, 4/2 = 2, 6/2 = 3]
"""

""" Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and 
produce the corresponding sin, cos and tan values.

Find sine value of PI/2:
x = np.sin(np.pi/2)
print(x) 
>>>1.0

Convert Degrees Into Radians
By default all of the trigonometric functions take radians as parameters but 
radians can be converted to degrees and vice versa as well in NumPy.
Radians values are pi/180 * degree_values.

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
>>>[1.57079633 3.14159265 4.71238898 6.28318531]

Radians to Degrees
Convert all of the values in following array arr to degrees:
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)
>>>[ 90. 180. 270. 360.]

Finding Angles
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse 
(arcsin, arccos, arctan). NumPy provides ufuncs arcsin(), arccos() and arctan() 
that produce radian values for corresponding sin, cos and tan values given.

Find the angle of 1.0:
x = np.arcsin(1.0)
print(x)
>>>1.5707963267948966

Angles of Each Value in Arrays
Find the angle for all of the sine values in the array
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
>>>[ 1.57079633 -1.57079633  0.10016742]

Hypotenues
Finding hypotenues using pythagoras theorem in NumPy using hypot() that takes 
the base and perpendicular values and produces hypotenues based on pythagoras 
theorem.

Find the hypotenues for 4 base and 3 perpendicular:
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
>>>5.0
"""

""" Hyperbolic Functions
NumPy provides the ufuncs hyperbolic sinh(), cosh() and tanh() that take values 
in radians and produce the corresponding sinh, cosh and tanh values.

Find sinh value of PI/2:
x = np.sinh(np.pi/2)
print(x) 
>>>2.3012989023072947

Find cosh values for all of the values in arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)
>>>[2.50917848 1.60028686 1.32460909 1.20397209]

Finding Angles
Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and 
tanh inverse (arcsinh, arccosh, arctanh) using ufuncs arcsinh(), arccosh() and 
arctanh() that produce radian values for corresponding sinh, cosh and tanh 
values given.

Find the angle of 1.0:
x = np.arcsinh(1.0)
print(x)
>>>0.881373587019543

Find the angle for all of the tanh values in array:
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
>>>[0.10033535 0.20273255 0.54930614]
"""

""" Set Operations
A set in mathematics is a collection of unique elements. Sets are used for 
operations involving frequent intersection, union and difference operations.

Create Sets in NumPy using NumPy's unique() method to find unique elements from 
any array. E.g. create a set array, but remember that the set arrays should 
only be 1-D arrays.

Convert following array with repeated elements to a set:
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
>>>[1 2 3 4 5 6 7]

To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
>>>[1 2 3 4 5 6]

To find only the values that are present in both arrays, use the intersect1d() 
method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
>>>[3 4]

To find only the values in the first set that is NOT present in the seconds set, 
use the setdiff1d() method.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
>>>[1 2]

To find only the values that are NOT present in BOTH sets, use the setxor1d() 
method.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
>>>[1 2 5 6]
"""

""" Random Numbers in NumPy
Random number does NOT mean a different number every time. Random means 
something that can not be predicted logically. NumPy offers the random module to 
work with random numbers. 

Working with the random library is either possible by using the command:
from numpy import random
or if import numpy as np is existing, type np.random while using functions

Computers work on programs, and programs are 
definitive set of instructions. So it means there must be some algorithm to 
generate a random number as well. If there's a program to generate random number 
it can be predicted, thus it is not truly random. Random numbers generated 
through a generation algorithm are called pseudo random.

In order to generate a truly random number on computers, get the random data 
from some outside source, generally keystrokes, mouse movements, data on network 
etc. Truly random numbers is necessary for use cases related to security (e.g. 
encryption keys) or when the basis of application is the randomness (e.g. 
Digital roulette wheels).

The randint() method takes a size parameter where you can specify the shape of 
an array.
x = random.randint(100)
print(x)
>>>37

1-D array containing 5 random integers from 0 to 100
x = random.randint(100, size= 5)
print(x)
>>>[ 4 30 93  1 15]

2-D array with 3 rows, each row containing 5 random integers from 0 to 100
x = random.randint(100, size=(3,5))
print(x)
>>>[[12 39 30 71 77]
    [35  9 44 58  9]
    [46 93 73 43 43]]

The rand() method also allows you to specify the shape of the array.
1-D array containing 5 random floats
x = random.rand(5)
print(x)
>>>[0.70450945 0.37376285 0.20690139 0.56921465 0.69592152]

Create a 2-D array with 3 rows, each row containing 5 random numbers
x = random.rand(3, 5)
print(x)
>>>[[0.22029937 0.37159398 0.66667137 0.28715107 0.5775001 ]
    [0.74578634 0.49256406 0.80929795 0.29202197 0.16508555]
    [0.92880499 0.0448327  0.8419925  0.82750211 0.03468751]]

The choice() method takes an array as a parameter and randomly returns one of 
the values.
x = random.choice([1,2,3,4,5])
print(x)
>>>1

Create a 2-D array that consists of the values in the array parameter of 
variable x
x = random.choice([1,2,3,4,5], size= (3,5))
print(x)
>>>[[2 1 5 4 2]
    [2 1 5 5 2]
    [2 1 1 5 4]]
"""

""" Random Data Distribution
Data Distribution is a list of all possible values, and how often each value 
occurs. The random module offer methods that return randomly generated data 
distributions.

A random distribution is a set of random numbers that follow a certain 
probability density function: a function that describes a continuous 
probability. i.e. probability of all values in an array. 

The choice() method allows to specify the probability for each value. The 
probability p is set by a number between 0 and 1, where 0 means that the value 
will never occur and 1 means that the value will always occur. The sum of all 
probability numbers should be 1.

Generate a 1-D array containing 100 values, where each value has to be 
3, 5, 7 or 9
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(10))
print(x)
>>>[7 7 7 7 7 7 5 5 7 7]

Generate a 2-D array with 3 rows, each containing 5 values
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
>>>[[5 7 5 5 5]
    [5 7 5 5 7]
    [7 7 5 5 7]]
 """

""" Random Permutations
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a 
permutation of [1, 2, 3] and vice-versa.
NumPy Random module provides two methods for this: shuffle() and permutation().

shuffle() is changing arrangement of elements in the original array.
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

permutation() returns re-arranged array (and leaves original array unchanged).
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
"""
