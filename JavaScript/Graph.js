//TODO: fix the bfs
class Vertex {
  constructor(value) {
    this.value = value;
    this.neighbours = {};
  }
  getValue() {
    return this.value;
  }
  setValue(value) {
    this.value = value;
  }
  getNeighbours() {
    return this.neighbours;
  }
  retrieveNeighbour(key) {
    return this.neighbours[key];
  }
  addNeighbour(node) {
    this.neighbours[node.getValue()] = node;
  }
}
class Graph {
  constructor() {
    this.vertices = {};
    this.size = 0;
    this.root = null;
  }
  add(value) {
    var newVertex = new Vertex(value);
    this.vertices[value] = newVertex;
    if (this.size == 0) {
      this.root = newVertex;
    }
    this.size++;
  }
  connect(first, second) {
    if (!(first in this.vertices)) {
      this.vertices[first] = new Vertex(first);
      if (this.size == 0) {
        this.root = this.vertices[first];
      }
      this.size++;
    }
    if (!(second in this.vertices)) {
      this.vertices[second] = new Vertex(second);
      this.size++;
    }
    this.vertices[first].addNeighbour(this.vertices[second]);
    this.vertices[second].addNeighbour(this.vertices[first]);
  }

  dfs(value = null, output = []) {
    if (this.size == 0) {
      return null;
    }
    if (value == null) {
      var node = this.root;
    } else {
      var node = this.vertices[value];
    }
    output.push(node.getValue());
    for (var neighbour in node.getNeighbours()) {
      if (!(neighbour in output)) {
        output = this.dfs(neighbour, output);
      }
    }
    return output;
  }
  bfs(value = null) {
    if (this.size == 0) {
      return null;
    }
    if (value == null) {
      value = this.root.getValue();
    }
    var node;
    var queue = [this.vertices[value]];
    var output = [];
    while (queue.length > 0) {
      node = queue.pop();
      output.push(node.getValue());
      for (var neighbour in node.getNeighbours()) {
        if (!(neighbour in output)) {
          queue.unshift(this.vertices[neighbour]);
        }
      }
    }
    return output;
  }
}

var graph = new Graph();
graph.connect(1, 2);
graph.connect(2, 3);
graph.connect(1, 5);
console.log(graph.dfs());
console.log(graph.bfs());
