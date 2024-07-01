#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);
const y = parseInt(args[3]);

function add(a, b) {
    if (isNaN(a) || isNaN(b)) {
        console.log("NaN")
    } else {
        return a + b;
    }
}

const total = add(x, y);
console.log(total);