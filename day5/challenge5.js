const fs = require("node:fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const [rawRules, rawUpdates] = input.split("\n\n");
const rules = [];
const updates = [];
for (let line of rawRules.split("\n")) {
  let [a, b] = line.split("|");
  rules.push([a, b]);
}
for (let line of rawUpdates.split("\n")) {
  updates.push(line.split(","));
}
function solution() {
  function followsRules(update) {
    let idx = new Map();
    for (let [id, val] of update.entries()) {
      idx.set(val, id);
    }
    for (let [before, after] of rules) {
      if (idx.has(before) && idx.has(after) && idx.get(before) > idx.get(after))
        return false;
    }
    return true;
  }
  let res = 0;
  for (let update of updates) {
    if (followsRules(update)) {
      res += Number(update[Math.floor(update.length / 2)]);
    }
  }
  return res;
}
function solution2() {
  function topoSort(update) {
    let set = new Set(update);
    let indegree = new Map();
    let graph = new Map();
    let q = [];
    let res = [];
    for (let key of set) {
      graph.set(key, []);
      indegree.set(key, 0);
    }
    for (let [before, after] of rules) {
      if (set.has(before) && set.has(after)) {
        graph.get(before).push(after);
        indegree.set(after, indegree.get(after) + 1);
      }
    }
    for (let [key, val] of indegree.entries()) {
      if (val === 0) q.push(key);
    }
    while (q.length > 0) {
      const node = q.shift();
      res.push(node);
      for (let nei of graph.get(node)) {
        indegree.set(nei, indegree.get(nei) - 1);
        if (indegree.get(nei) === 0) {
          q.push(nei);
        }
      }
    }
    return res;
  }
  function followsRules(update) {
    let idx = new Map();
    for (let [id, val] of update.entries()) {
      idx.set(val, id);
    }
    for (let [before, after] of rules) {
      if (idx.has(before) && idx.has(after) && idx.get(before) > idx.get(after))
        return false;
    }
    return true;
  }
  let res = 0;
  for (let update of updates) {
    if (!followsRules(update)) {
      res += Number(topoSort(update)[Math.floor(update.length / 2)]);
    }
  }
  return res;
}
