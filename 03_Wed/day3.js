function getString() {
    s1 = "hello";
    s2 = "pillow";

    return s1 && s2;
}

function getStrings(s1, s2) {
    s1List = [];
    s2List = [];

    i = 0;
    sameLetter = "";
    for (s in s1) {
        s1List.push(s);
    }
    for (s in s2) {
        s2List.push(s);
    }

    while (i < s1List.length && i < s2List.length) {
        if (s1List[i] != s2List[i]) {
            sameLetter += ".";
        } else {
            sameLetter += s1List[i];
        }
        i += 1;
        return sameLetter;
    }
}

function work() {
    s1 = getString();
    s2 = getString();
    console.log(getStrings(s1, s2));
}

work();
