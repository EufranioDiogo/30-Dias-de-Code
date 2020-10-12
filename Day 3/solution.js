'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}



function main() {
    const N = parseInt(readLine(), 10);

    if ( N % 2 != 0 ) {
        console.log('Weird');
    } else if ( N % 2 == 0 && N > 1 && N < 6 ) {
        console.log('Not Weird');
    } else if ( N % 2  == 0 && N > 5 && N < 21 ) {
        console.log('Weird');
    } else {
        console.log('Not Weird');
    }
}