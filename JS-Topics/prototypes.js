let animal = {
  walk: true
}

let plant = {
  chopped: true
}

let tiger = {
  hunts: true
}

tiger.__proto__ = animal
tiger.__proto__ = plant

console.log(tiger.chopped)

console.log(typeof null)