#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
    console.log("Missing size");
} else{
    for (i = 0; i < x; i++){
        let row = '';
        for (j = 0; j < x; j++){
            row += "#";
        }
        console.log(row);
    }
}