import fetch from 'node-fetch'

// With  Promise you can call function first and define it later
// whereas in callback you've to define the function first

// let promise2 = new Promise(async (resolve, reject) => {
//   const y = await fetch('https://jsonplaceholder.typicode.com/todos/1')
//     .then(x => x.json())
//   resolve({ ...y, hi: 'bye' })
// })
// // promise2.then(async data => console.log(await data.json()))
// console.log(await promise2)

// let promise = await fetch('https://jsonplaceholder.typicode.com/todos/1')
//   .then(x => x.json())
//   .then(y => { ...y, hi: 'bye' })

// console.log(promise)

// const y = new Promise((resolve) =>
//   fetch('https://jsonplaceholder.typicode.com/todos/1')
//     .then(x => resolve(x))
// )
// y.then(async y => console.log(await y.json()))
// console.log(await y.json())

// console.log(promise2)

// 1.
// const y = fetch('https://jsonplaceholder.typicode.com/todos/1')
//   .then(x => return x.json())
// console.log(await y)

// 2.
// const x = await fetch('https://jsonplaceholder.typicode.com/todos/1')
//   .then(x => x.json())
//   .then(data => data)
// console.log(x)
// console.log('hellos')

// 3.
// const y = await fetch('https://jsonplaceholder.typicode.com/todos/1')
//   .then(x => x.json())
// console.log(y)

// 4.
// const y = new Promise(resolve =>
//   fetch('https://jsonplaceholder.typicode.com/todos/1')
//     .then(x => resolve(x.json()))
// )
// console.log(await y)

// 5
// const y = await fetch('https://jsonplaceholder.typicode.com/todos/1')
// console.log(await y.json())

// function promisify(func) {
//   return function (...args) {
//     return new Promise((resolve, reject) => {
//       try {
//         const result = func(...args)
//         resolve(result)
//       } catch (error) {
//         reject(error)
//       }
//     })
//   }
// }

// const max = promisify(Math.max)

// console.log(await max(3, 5, 7))