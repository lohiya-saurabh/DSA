import fetch from 'node-fetch'
const promises = []

function createReq(id) {
  const req = fetch(`https://jsonplaceholder.typicode.com/todos/${id}`)
    .then(res => res.json())
  return req
}

let i = 197
while (i < 202) {
  promises.push(createReq(i))
  i += 1
}

const result = Promise.all(promises)
result.then(res => console.log(res))
