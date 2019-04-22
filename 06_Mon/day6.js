
function letterPrac(set) {
    for (let i in set) {
        let n = set.toLowerCase().charCodeAt(i);
        let length = n - 96;
        let s = '';
        if (length >= 0 && length < 26) {
            for (let j = 0; j < length; j++) {
                s += set.charAt(i);
            }
        } else {
            s = '(' + set.charAt(i) + ')';
        }
        console.log(s);
    }

}
letterPrac("haha!");
