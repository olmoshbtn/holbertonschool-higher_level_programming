#!/usr/bin/node
exports.esrever = function (list) {
  const esrever = [];
  for (let i = list.length - 1; i >= 0; i--) {
    esrever.push(list[i]);
  }
  return esrever;
};
