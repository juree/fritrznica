function OffersCtrl($scope, Offer) {
    $scope.offers = Offer.query();
}

function PonudiCtrl($scope, Parsedoffer) {
    $scope.parsedoffers = Parsedoffer.query();
}
