# return the greatest common factor, GCF
'''
https://divisible.info/Modulo/What-is-16-mod-64.html'''
import pdb

def gcf(a, b):
#    pdb.set_trace()
   if a == 0:
      return b
   print(b%a, a)
   return gcf(b%a, a)

a = 64
b = 16

print(f"GCF({a} , {b}) = {gcf(a, b)}")