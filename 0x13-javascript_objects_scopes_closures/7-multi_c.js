#!/usr/bin/node

const args = process.argv.slice(2);
const x = args[0];

if (isNaN(parseInt(x))){
    console.log("Missing number of occurrences");
} else {
    j = parseInt(x);
    for (i = 0; i < j; i++){
        console.log("C is fun");
    }
}