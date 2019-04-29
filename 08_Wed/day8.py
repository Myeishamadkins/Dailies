# ex = [1, 0, -1, -2, 0, 1, 0]
# ex = [1, -2, 2, -2, 2, -2, 0, 1, 0]
# ex = []
# ex =[1, 2, 3]

el = 0
step = 0
ae = True

for i in ex:
    el += i
    if el < 0 and ae == True:
        step +=1
        ae = False
    elif el >= 0 and ae == False:
        ae = True
print(step)
