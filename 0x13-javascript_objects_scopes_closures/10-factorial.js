#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

function factorial(n) {
    if (n == 1){
        return (1);
    } else {
        return (n * factorial(n - 1));
    }
}

if (isNaN(x)){
    console.log("1");
} else {
    console.log(factorial(x))
}