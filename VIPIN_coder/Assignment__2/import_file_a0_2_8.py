"""
8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py
"""

x="wellocome"
y="hello"
z=22
#print(x,y,z)

"""frist tarika, ye module ke ek variable ko hi import karta hai
jaise ki b"""
import import_file_a1_2_8
print(import_file_a1_2_8.b)
print()

#second tarika, ye ek hi variable ko import karta hai jaise ki a 
from import_file_a1_2_8 import a
print(a)
print()

#thrd tarika, ye pure module ko import karta hai
from import_file_a1_2_8 import*
print(c)
