# izmantojot laika zīmogu
import time
import random

laiks=time.time() # UNIX laisk - 1970 1,janv

parole=f"{int(time.time()*1000)}-{random.randint(1000,9999)}"

print(parole)