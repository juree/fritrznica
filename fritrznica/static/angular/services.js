angular.module('ipriServices', ['ngResource']).
    factory('Offer', function($resource){
        return $resource('/api/v1/offers', {}, {
            query: {method:'GET', isArray:false}
        });
    });
