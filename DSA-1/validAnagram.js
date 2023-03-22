/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram (s, t) {
  let sCount = {}
  let tCount = {}
  for (let letter of s) {
    sCount[letter] = sCount[letter] ? sCount[letter]++ : 1
  }
  for (let letter of t) {
    tCount[letter] = tCount[letter] ? tCount[letter]++ : 1
  }
  for (let letter of s) {
    if (sCount[letter] !== tCount?.letter) return false
  }
  console.log(sCount)
  console.log(tCount)
  return true
};