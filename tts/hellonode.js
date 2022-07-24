//load HTTP module
const http = require("http");
const hostname = '127.0.0.1';
const port= 3000;
//create HTTP server and listen on port 3000 for request 
const server= http.createServer((req,res) =>{ 
    //Set the response HTTP header with HTTP status and Content type
    res.statusCode=200;
    res.setHeader('Content-Type', 'text/plain');
    res.end("Manpreet\n");
});
//listen for request on port 3000 and as a callback function have the port listened on logged
server.listen(port,hostname,()=> {
    console.log(`Server running at http://${hostname}:${port}/`);
});
