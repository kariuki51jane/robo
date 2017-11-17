var app=angular.module('myApp', ['googlechart']);


app.controller('myController', function($scope,socket) {

        var chart1 = {};
        chart1.type = "Gauge";
        chart1.displayed = false;
        chart1.data = [
            ['Label', 'Value'],
            ['Speed', 80],
            ['k', 55],
            ['Temperature', 68],
            ['Remaining Energy', 80],

        ];

        chart1.options = {
            width: 400,
            height: 120,
            redFrom: 90,
            redTo: 100,
            yellowFrom: 75,
            yellowTo: 90,
            minorTicks: 5
        };

        $scope.checkboxModel = {
            value1 : false,
            value2 : false
         };


        $scope.myChart = chart1;

        $scope.start_stop=function() {
            console.log("button cliecked");
            if($scope.checkboxModel.value2==true) {
                socket.emit('to_server', { switch: 0});
            }
            else{
                socket.emit('to_server', { switch: 1});
            }

        };


        socket.on('to_app', function (data) {

            if($scope.checkboxModel.value1==false) {
                $scope.myChart.data[1][1]=data.speed;
            }

        });







});


app.factory('socket', function ($rootScope) {
    var socket = io.connect();

    return {
        on: function (eventName, callback) {
            socket.on(eventName, function () {
                var args = arguments;
                $rootScope.$apply(function () {
                    callback.apply(socket, args);
                });
            });
        },
        emit: function (eventName, data, callback) {
            socket.emit(eventName, data, function () {
                var args = arguments;
                $rootScope.$apply(function () {
                    if (callback) {
                        callback.apply(socket, args);
                    }
                });
            })
        }
    };
});

/*
var socket = io();
var recieved_data;


setInterval(function(){
    message = {"switch":"ON", "simulate":1,"energy": 70,"speed": 80,"distance" :100,"temp" : 27}
    socket.emit('to_server', message);

}, 1000);


socket.on('to_app', function(msg){

    recieved_data=msg;
    console.log(recieved_data)
    data.setValue(0, 1, recieved_data.speed);
    chart.draw(data, options);

    data.setValue(1, 1, recieved_data.temp);
    chart.draw(data, options);

    data.setValue(2, 1, recieved_data.energy);
    chart.draw(data, options);

});

*/