zeros = 0
ones = 0

num = [0, 0, 1, 1, 1, 1]

num.forEach(e => {
    if (e == 0) {
        zeros += 1;
    } else if (e == 1) {
        ones += 1;
    }
});
return ones > zeros
}

zeros = 0
ones  = 0

num = [0, 0, 1, 1, 1, 1]

for (n of num) {
    if (n == 0) {
        zeros += 1;
    } else if (n == 1) {
        ones  += 1;
    }
}
return ones  > zeros
