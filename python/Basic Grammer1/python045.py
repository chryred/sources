import time
#import mylib
import mypackage.mylib

#time.sleep(1)
print(mypackage.mylib.add_txt("나는", "파이썬이다"))
print(mypackage.mylib.reverse1(1, 2, 3))

from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse1

print(mylib.add_txt("나는", "파이썬이다"))
print(reverse1(1, 3, 4))

import mypackage.mylib as ml
print(ml.add_txt("11", "22"))