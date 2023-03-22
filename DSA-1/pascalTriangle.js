function generatePascalTriangle(numRows) {
  let final = []
  let rowNum = 0
  while (numRows) {
    let current = []
    for (let i = 0; i <= rowNum; i++) {
      if (i === 0 || i === rowNum) {
        current.push(1)
      } else {
        current.push(final[rowNum - 1][i - 1] + final[rowNum - 1][i])
      }
    }
    final.push(current)
    numRows--;
    rowNum++;
  }
  return final
};

console.log(generatePascalTriangle(5))