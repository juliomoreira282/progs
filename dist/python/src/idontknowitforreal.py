import time

y = 1
while True:
    print(y)
    time.sleep(0.5)
    y += 1
    if y > 20:
        y = 1