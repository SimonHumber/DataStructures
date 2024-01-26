import random

f = open("10,000.txt", "w")
for x in range(0, 10000):
    f.write(str(random.randint(0, 10000)))
    f.write("\n")
f.close()

f = open("1m.txt", "w")
for x in range(0, 1000000):
    f.write(str(random.randint(0, 1000000)))
    f.write("\n")
f.close()
