function evenOdd() {
    var startNum = [1, 2, 3, 4, 5, 6, 7, 8];
    startNum.forEach(function (e) {
        if (e != 0) {
            if (e % 2 == 0) {
                console.log(e + ": Even")
            } else {
                console.log(e + ": Odd")
            }
        }
    })
}

// function evenOdd() {
//     num = 24
//     startNum = 1;

//     while (startNum < num) {
//         if (startNum != 0) {
//             if (startNum % 2 == 0) {
//                 console.log(`${startNum} : Even`)
//             } else {
//                 console.log(`${startNum} : Odd`)
//             }
//         }
//         startNum += 1;
//     }



// }

evenOdd()
