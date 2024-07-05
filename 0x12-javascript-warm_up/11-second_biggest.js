#!/usr/bin/node

const args = process.argv;

if (!args || args.length <= 2) {
    console.log("0");
} else {
    const arr = [];
    let j = 0;
    for (let i = 2; i < args.length; i++) {
        arr[j++] = parseInt(args[i]);
    }
    
    const max = Math.max(...arr);
    const finalArr = [];

    for (let i = 0, j = 0; i < arr.length; i++) {
        if (arr[i] === max) {
            continue;
        }
        finalArr[j++] = arr[i];
    }

    const secondMax = Math.max(...finalArr);
    console.log(secondMax);
}