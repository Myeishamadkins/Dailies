socks = ['b', 'b', 'b ', 'y', 'b', 'y', 'b', 'r']
# 3
singles = []
pairs = 0
for sock in socks:
    if sock in singles:
        socks.remove(sock)
        pairs += 1
    else:
        singles.append(sock)
print(pairs)
