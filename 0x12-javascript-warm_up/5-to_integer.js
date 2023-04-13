#!/usr/bin/node
const myNum = math.floor(number(process.argv[2]));
console.log(isNaN(myNum) ? 'Not a number' : `My number: ${myNum}`);
