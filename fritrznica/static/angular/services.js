var app = angular.module('ipriServices', ['ngResource']);

app.factory('Offer', function($resource){
    return $resource('/api/v1/offers?!user='+USER_ID+'&version='+VERSION+'&offered=true&closed=false', {}, {
        query: {method:'GET', isArray:false}
    });
});

app.factory('Parsedoffer', function($resource){
    return $resource('/api/v1/parsedoffers?user='+USER_ID+'&version='+VERSION+'&offered=false&closed=false', {}, {
        query: {method:'GET', isArray:false}
    });
});

app.factory('Offeredoffer', function($resource){
    return $resource('/api/v1/parsedoffers?user='+USER_ID+'&version='+VERSION+'&offered=true&closed=false', {}, {
        query: {method:'GET', isArray:false}
    });
});

app.factory('Swap', function($resource){
    return $resource('/api/v1/swaps', {}, {
        query: {method:'GET', isArray:false}
    });
});
