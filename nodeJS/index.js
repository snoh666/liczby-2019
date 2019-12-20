const fs = require('fs');

const fileBuffer = fs.readFileSync('./liczby.txt', (err, fd) => {
  if (err) throw err;
  fs.close(fd, (err) => {
    if (err) throw err;
  });
});

const numbersFile = fileBuffer.toString().split('\n');

numbersFile.forEach(number => {
  let wholeSum = 0;
  // let factorial = 0;
  [...number].forEach(eachNumber => {
    let factorial = 0;
    for(let i = 1; i <= eachNumber; i++) {
      if(factorial == 0) {
        factorial = Number(i);
      } else {
        factorial *= Number(i);
      }
    }
    wholeSum += factorial;
  });

  if(wholeSum == Number(number)) {
    console.log(wholeSum, number)
  }

});