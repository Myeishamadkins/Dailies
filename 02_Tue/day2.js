function isFactor() {
    var startNum = 12;
    var factor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

    factor.forEach(function(e) {
        if (e != 0) {
            if (startNum % e == 0) {
                console.log(`${e} is a factor of ${startNum}`);
            } else {
                console.log(`${e} is not a factor of ${startNum}`);
            }
        }
    });
}

function isFactor() {
    num = 12;
    startNum = 1;

    while (startNum < num) {
        if (startNum != 0) {
            if (num % startNum == 0) {
                console.log(`${startNum} is a factor of ${num}`);
            } else {
                console.log(`${startNum} is not a factor of ${num}`);
            }
        }
        startNum += 1;
    }
}

isFactor();
