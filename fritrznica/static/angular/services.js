var app = angular.module('ipriServices', ['ngResource']);

app.factory('Offer', function($resource){
    return $resource('/api/v1/offers', {}, {
        query: {method:'GET', isArray:false}
    });
});

app.factory('Parsedoffer', function($resource){
    return $resource('/api/v1/parsedoffers', {}, {
        query: {method:'GET', isArray:false}
    });
});
