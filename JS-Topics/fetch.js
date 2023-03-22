import fetch from 'node-fetch'

const promise = new Promise(async (resolve, reject) => {
  const x = await fetch("https://api.openweathermap.org/data/2.5/weather?q=" + 'denver' +
    "&appid=b59e476dfdfb802022387977c6b4ceb1")
  resolve(x)
})

promise
  .then(data => console.log(data.json()))

// data.then(data => console.log(data))
// const x = await fetch("https://api.openweathermap.org/data/2.5/weather?q=" + 'denver' +
//   "&appid=b59e476dfdfb802022387977c6b4ceb1")
//   .then(async (data) => await data.json())
// console.log(x)

function abc(script, callback) {
  script.onload => callback(id)
}

abc('https://abc.com/posts/123', function (id) {
  console.log(id)
})

const res = await new Promise(async (resolve, reject) => {
  if (true) {
    resolve(pageYOffset)
  }
})

