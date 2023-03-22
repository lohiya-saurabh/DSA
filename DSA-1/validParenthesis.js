function validParenthesis(s) {
  let stack = []
  let parenthesis = new Set(['(', '[', '{'])
  let match = { ')': '(', '}': '{', ']': '[' }
  for (let par of s) {
    if (parenthesis.has(par)) {
      stack.push(par)
    } else {
      let x = stack.pop()
      if (match[par] !== x) return false
    }
  }
  return stack.length === 0
};

console.log(validParenthesis('{[]()}()[[{}()]]'))