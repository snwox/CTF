from pwn import *
from time import *
r=remote("2020.redpwnc.tf",31039)
context.log_level="debug"
sleep(10)

# 0 1 2 3 4 5 6 7 8 9
# 1 a 3 2 5 9 8 7 4 6 -> 1
# 1 3 a 2 5 9 8 7 4 6 -> 2
# 1 3 2 a 5 9 8 7 4 6 -> 1
# 1 2 3 a 5 9 8 7 4 6 -> 3
# 1 2 3 5 a 9 8 7 4 6 -> 4
# 1 2 3 5 9 a 8 7 4 6 -> 5
# 1 2 3 5 9 8 a 7 4 6 -> 6
# 1 2 3 5 9 8 7 a 4 6 -> 7
# 1 2 3 5 9 8 7 4 a 6 -> 5
# 1 2 3 5 9 7 8 4 a 6 -> 6
# 1 2 3 5 9 7 4 8 a 6 -> 5
# 1 2 3 5 9 4 7 8 a 6 -> 4
# 1 2 3 5 4 9 7 8 a 6 -> 3
# 1 2 3 4 5 9 7 8 a 6 -> 8
# 1 2 3 4 5 9 7 8 6 a -> 7
# 1 2 3 4 5 9 7 6 8 a -> 6
# 1 2 3 4 5 9 6 7 8 a -> 5
# 1 2 3 4 5 6 9 7 8 a -> 6
# 1 2 3 4 5 6 7 9 8 a -> 7
# 1 2 3 4 5 6 7 8 9 a  done (9)
#pay load is 1 2 1 3 4 5 6 7 5 6 5 4 3 8 7 6 5 6 7

#r.sendline("1 2 1 3 4 5 6 7 5 6 5 4 3 8 7 6 5 6 7 9")

bubble=[1,0xa,3, 2, 5, 9, 8, 7, 4, 6]
for i in range(len(bubble)):
    for j in range(len(bubble)-1):
        if bubble[j]>bubble[j+1]:
            r.sendline(j)
            t=bubble[j]
            bubble[j]=bubble[j+1]
            bubble[j+1]=t

print bubble
r.sendline(10)
r.interactive()

