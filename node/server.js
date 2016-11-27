var http = require('http').Server();
var io = require('socket.io')(http);
var redis = require('redis');

var redisClient = redis.createClient(6379, 'redis')

io.on('connection', function(socket){
    console.log('A user has connected ...');
    socket.on('subscribe', function(celeryTaskId){
        console.log('A user has succribe');
        redisClient.subscribe(celeryTaskId);
    });

    redisClient.on('message', function(channel, message){
        console.log('Connect to redis cliente');
        socket.emit('result', message);
    })
})

http.listen(3000, function(){
    console.log('Listen in port 3000 ...');
});