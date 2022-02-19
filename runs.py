import os




p1s = range(0,5)
p2s = range(0,5)

#This is a driver

for p1 in p1s:
    for p2 in p2s:
        print(f"logging experiment for p1 {p1} and p2 {p2}")
        os.system(f"python demo.py -p1 {p1}   -p2 {p2}")
