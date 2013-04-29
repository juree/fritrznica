angular.module('trznica', ['ipriServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/firstFromUcilnica', {templateUrl: 'templates/firstFromUcilnica.html',   controller: OffersCtrl}).
            otherwise({redirectTo: '/'});
    }]);
