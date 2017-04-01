/*angular.module('TLEapp', []).controller('TodoController', function($scope) {
    $scope.Name = "",
    $scope.Line1 = "",
	$scope.Line2 = "",
    $scope.fullTLE = function() {
        return $scope.Name + " " + $scope.Line1+ " " + $scope.Line2;
    }
});*/

var zerorpc = require("zerorpc");

define(function () {
    function TodoController($scope) {
        
		$scope.Name = "Name",
		$scope.Line1 = "Line 1",
		$scope.Line2 = "Line 2",
		
		$scope.fullTLE = function() {
			alert($scope.Name);
			console.log($scope.Name);
			console.log($scope.Line1);
			console.log($scope.Line2);
		
			return $scope.Name + " " + $scope.Line1+ " " + $scope.Line2;
			
			
    	 };
		 
		$scope.sendTLE = function(){
			var client = new zerorpc.Client();
			client.connect("tcp://127.0.0.1:4242");
			
			client.invoke("hello", "RPC", function(error, res, more) {
				console.log(res);
			});
			
		}
		 
    }
	
	return TodoController;
});

/*angular.module('TodoController', [])
  .controller('TodoController', ['$scope', TodoController]);

function TodoController($scope){
	
	$scope.Name = "Name";
	$scope.Line1 = "Line 1";
	$scope.Line2 = "Line 2";
	
	$scope.fullTLE = function(){
		alert(Name);
		
	};
	
}*/
