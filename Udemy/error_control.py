# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:17:47 2017

@author: wlunareve
"""
import sys
"""13
while True:
    try:
        x=int(input("Plz enter a number:"))
        break
    except ValueError:
        print("input error")
        

try:
    f=open('mysql.py')
    s=f.readline()
    i=int(s.strip())

except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])
"""

def displaySalary(salary):
    if salary<0:
        raise ValueError("薪水必須為負")
    print("薪水="+str(salary))

try:
    Salary=eval(input("請輸入薪水:"))
    displaySalary(Salary)
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("錯誤:薪水為正")
except:
    print("Unexpected error:",sys.exc_info()[0])