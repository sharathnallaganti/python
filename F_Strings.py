"""
=> F-String was introduced in Python 3.6, and is now the preferred way of formatting strings. 
Before Python 3.6 we had to use the format() method.


| Code   | Meaning               |
| ------ | --------------------- |
| `%s`   | String                |
| `%d`   | Integer               |
| `%f`   | Float                 |
| `%.2f` | Float with 2 decimals |


"""


import math
radius =10
dia = 2* radius

Area_of_triangle = 2* math.pi * radius
print(f"Area of the circle is : {Area_of_triangle:.2f}")

