
var express = require('express');
var app=express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var socket=require('net');
var path=require('path');

http.listen(3000);


app.use(express.static(path.join(__dirname, 'public')));


app.get('/', function(req, res){
    res.sendFile(__dirname + '/public/index.html');
});

var global_socket_io;

io.on('connection', function(socket){

    global_socket_io=socket;

    console.log('a user connected');
    socket.on('disconnect', function(){
        console.log('user disconnected');
    });

    socket.on('to_server', function(msg){
        console.log(JSON.stringify(msg));
        global_socket.write(JSON.stringify(msg));
    });


});

var global_socket;


socket.createServer(function (socket) {

    console.log("connected");

    global_socket=socket;

    socket.on('data', function (data) {
        //console.log(data);
        obj=JSON.parse(data);
        console.log(obj);
        global_socket_io.emit('to_app',obj);

        obj.simulate=1
        obj.switch="OFF"

    });
}).listen(5002);











