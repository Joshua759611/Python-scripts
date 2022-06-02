import random
import string
#total = string.ascii_letters + string.digits + string.punctuation
total=string.hexdigits+string.ascii_letters+string.punctuation+string.digits
length = 15
password = "".join(random.sample(total, length))
print(password)
