#!/usr/bin/node
const oldlist = require('./100-data').list;
const newlist = oldlist.map((item, index) => item * index);
console.log(oldlist);
console.log(newlist);
