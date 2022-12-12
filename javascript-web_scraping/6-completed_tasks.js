#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, resp, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {}; // create a dictionary for information
    todos.forEach((todo) => { // iterates over each todo
      if (todo.completed && completed[todo.userId] === undefined) { // if todo is completed but no userId, sets completed to 1
        completed[todo.userId] = 1;
      } else if (todo.completed) { // adds 1 to each user that has completed a task
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
