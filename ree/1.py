flag=[0]*35
box = [
 253, 194, 15, 13, 82,
 129, 244, 80, 193, 233,
 36, 54, 199, 69, 219,
 74, 136, 6, 190, 144,
 68, 57, 156, 153, 240,
 65, 95, 135, 61, 179,
 159, 183, 182, 130, 107]
target = [
 174, 178, 102, 127, 22,
 245, 143, 226, 245, 131,
 65, 105, 135, 48, 94,
 21, 185, 188, 225, 211,
 116, 11, 178, 184, 248,
 18, 47, 205, 79, 38,
 235, 244, 149, 196, 185]

state = target
for i in range(0, 35, 5):
    # state[i] = flag[i] ^ box[i]
    # state[i + 1] = flag[(i + 1)] ^ box[(i + 1)]
    # state[i + 2] = ((state[i] ^ state[(i + 1)] ^ flag[(i + 2)]) - box[(i + 2)]) & 255
    # state[i + 3] = flag[(i + 3)] ^ box[(i + 3)]
    # state[i + 4] = flag[(i + 4)] ^ state[(i + 3)]

    flag[i+4]=state[i+4]^state[i+3]
    flag[i+3]=state[i+3]^box[i+3]
    flag[i+2]=((state[i+2]+box[i+2])&255)^state[i+1]^state[i]
    flag[i+1]=state[i+1]^box[i+1]
    flag[i]=state[i]^box[i]

print(bytes(flag))