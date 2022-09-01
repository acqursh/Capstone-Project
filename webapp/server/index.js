var mysql = require('mysql');
const express = require('express');

const app = express();

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "kunal1234",
  database: 'capstone',
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected to database!");
});



app.listen(3001, ()=>{console.log("Server started on port 3001")});

// dotenv.config({path: "./config.env"});
// const PORT = process.env.PORT;

//paths to apis

//app.use(require("./APIS/----------"));