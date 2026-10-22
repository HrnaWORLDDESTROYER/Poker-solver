import os
import sys

path = sys.argv[1]

dir_list = os.listdir(path)

print(dir_list)

last_state = {}

def should_reload (path):
    result = False
    for (root, dirs, files) in os.walk(path, topdown=True):
        for f in files:
            key = root + '/' + f
            if last_state[key] != os.path.getmtime(key):
                last_state[key] = os.path.getmtime(key)
                result = True
    return result


while True:



