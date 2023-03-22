function matrixReshape(mat, r, c) {
  let m = mat.length
  let n = mat[0].length
  if (m * n !== r * c) return mat
  let nums = []
  let newMat = []
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      nums.push(mat[i][j])
    }
  }
  let k = 0
  for (let i = 0; i < r; i++) {
    let curr = []
    for (let j = 0; j < c; j++) {
      curr.push(nums[k])
      k++
    }
    newMat.push(curr)
  }
  return newMat
};

console.log(matrixReshape([[1, 2], [3, 4]], 1, 4))