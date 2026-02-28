import json
import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
m = set()
def f(x):
    return x[0]
i = 0
for dirpath, dirnames, filenames in os.walk("/Users/artembatanin/"):
    for dir in dirnames:
        if not os.path.islink(os.path.join(dirpath, dir)):
            sz = get_size(os.path.join(dirpath, dir))/1024/1024/1024
            m.add((sz, os.path.join(dirpath, dir)))
        i += 1
        prc = i/119722
        if (prc*100)%1 <= 100/119722:
            print(prc*100)
m = list(m)
m.sort()
print(len(m))
for i in m[-100:]:
    print(i)
m = m[-100:]
f = open("file.json", mode = "w")
json.dump(m, f)
f.close()