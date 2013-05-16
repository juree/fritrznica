angular.module('trznica', ['ipriServices']).
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.
            when('/firstFromUcilnica', {templateUrl: 'templates/firstFromUcilnica.html',   controller: OffersCtrl}).
            when('/ponudi', {templateUrl: 'templates/ponudi.html', controller: PonudiCtrl}).
            when('/cakalnica', {templateUrl: 'templates/cakalnica.html', controller: SwapsCtrl}).
            otherwise({redirectTo: '/'});
    }]);
