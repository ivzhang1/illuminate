import random
d = {'box':5, 'sphere':3, 'torus':4, 'rotate': 'xyz', 'move': 3}

f = raw_input("how many randoms: ")
times = int(f)
out = ""
while times:
    r = random.choice(list(d.keys()))
    out += r + "\n"
    if d[r] == 'xyz':
        out += random.choice(["x","y","z"]) +" "+ str(random.randrange(0, 360)) + "\n"
    else:
        v = d[r]
        ran = 500
        if d[r] == 'move':
            ran = 100
        while v:
            out += str(random.randrange(0, ran)) + " "
            v -= 1
        if d[r] != 'move':
            out += str(random.randrange(0, 100)) + "\n"


    times -= 1

out += "display\nsave\nrandy.png"
f = open("script_rand", "w")
f.write(out)
f.close()
print("done")
