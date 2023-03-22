/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
function isAnagram(s, t) {
  let sCount = {}
  let tCount = {}
  if (s.length !== t.length) return false
  for (let letter of s) {
    if (letter in sCount) sCount[letter]++
    else sCount[letter] = 1
    // sCount[letter] = sCount[letter] ? sCount[letter]++ : 1
  }
  for (let letter of t) {
    if (letter in tCount) tCount[letter]++
    else tCount[letter] = 1
  }
  for (let letter of s) {
    if (sCount[letter] !== tCount[letter]) return false
  }
  return true
};

console.log(isAnagram('anagram', 'gramana'))