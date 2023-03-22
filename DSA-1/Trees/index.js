class Nodes {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

export const node1 = new Nodes(3)
const node2 = new Nodes(1)
const node3 = new Nodes(2)
// const node4 = new Nodes(15)
// const node5 = new Nodes(7)

node1.left = node2
node1.right = node3
// node3.left = node4
// node3.right = node5