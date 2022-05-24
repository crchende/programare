const express = require('express');

const app = express();

//Middleware - functiile de mai jos se vor apela inainte de 'get'
app.use(function(req, res, next) {
  console.log("Middleware 1 - processing req.url:   ", req.url);
  next();
})

app.use(function(req, res, next) {
  console.log(req)
  console.log("Middleware 2 - processing req.params:", req.params);
  console.log("Middleware 2 - processing req.params:", req.query)
  next();
})

//ROUTER - asociere URL cu raspuns
app.get('/', function(req, res) {
  res.send("<html><body>Salut</body></html>");
});

app.get('/salut/:id', function(req, res) {
  console.log(req)
  console.log(req.params);
  console.log(req.params.id);
  let response = `<html><body> ${req.params.id} </body></html>`;
  res.send(response)
});




app.listen(5500, () => console.log("Server is running"))
