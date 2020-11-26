import random
import string
import time

colorString = '\033['+str(32)+'m'

while True:
    text = ""
    for i in range(194):
        skip = random.randint(0, 6)
        if not skip:
            text += ''.join(random.choice(string.ascii_uppercase +
                                          string.digits) for _ in range(1))
        else:
            text += ' '

    time.sleep(0.01)
    print(colorString + text)
