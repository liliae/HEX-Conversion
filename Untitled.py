from numpy import *

fcoord = open("/Users/Lily/Desktop/coord.txt", 'r+')
coord = fcoord.read()
fcoord.close()
xy = coord.strip()
xy = xy.split("\n")


salad = []

for line in xy:
        if line[:9] == '0000 0000':
            salad.append(line)

for no in salad:
    for line in xy:
        if line == no:
            xy.insert(xy.index(line), '0000 0000 0000 0000 0000 0000 0000 0000')
            xy.remove(line)
stitches = []

' Establish arrays for changing from little endian to dec'
for row in xy:
    stitches.append(int(row[2:4]+row[:2], 16))
    stitches.append(int(row[12:14]+row[10:12], 16))
    stitches.append(int(row[22:24]+row[20:22], 16))
    stitches.append(int(row[32:34]+row[30:32], 16))

stitches_arr = array(stitches)
stitches_arr = reshape(stitches_arr, (len(xy),4))

savetxt('final_stitches.txt', stitches_arr,fmt ='%d', header='Stitches')