var express = require('express');
var app = express();
var path = require('path');
app.use(express.static(path.join(__dirname, 'HTML'))); //  "public" off of current is root
app.listen(3000);



console.log("Running at Port 3000");
