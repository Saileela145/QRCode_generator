
#datatypes

num=5
type(num)

#here the 5 value we are assigning to the variable called num
#output:int   [type which tells the datatype of that assigned value]

num=23569762555076356367287
type(num)

#output:int
/*In Python 3, the distinction between int and long no longer exists. All integers are treated as int and can grow to arbitrary size. Therefore,
there's no need to explicitly check for long*/

num=5.3
type(num)
#output:float

num=2+5j
type(num)
#output:complex

#to get above complex value seperately with real and imaginary part
 num.real
 #output:2.0
 num.imag
 #output:5.0

 num=-5467.965
 num
 #output:-5467.965

 num1=10
 num2=2
 print(num1+num2)
 #output:12
 print(num1-num2)
 #output:8
 print(num1*num2)
 #output:20
 print(num1/num2)
 #output:5.0 [we got float type output here]
 print(10/3)
 #output:3.333333333333335 [output we get will be in decimal value not whole number]
 /* if you want output in whole number use floor division*/
 
 print(10//3)
 #output:3

print(num1%num2)
 #output:0
print(num1**num2)
#output:100 [we get 10**2  which is 10^2]

/*conversions*/
x="192"
type(x)
#output:str 
#though the value is in x but the value is in double quotes so it will consider the type as string

int(x)
#ouput:192

x=int(x)
type(x)
#output:int

x=float(x)
print(x)
#output:192.0

x=complex(x)
print(x)
#output:(192+0j)

print(complex(2,6))
#output:2+6j

/* Functions */
x=-7.5
print(abs(x))
#output:7.5 [absolute value]

import math
x=20
print(math.exp(x))
#output:22026.465794806718[exp is the exponent value ]

math.e
#output:2.718281828459045 [in this e give constant value]

math.pi 
#output:3.141592653589793

print(math.sqrt(6))
#output:2.449489742783178

max(1,34,65,378,36,2221)
#output:2221
min(1,33,4555,5677,322,0)
#output:0
