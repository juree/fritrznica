function OffersCtrl($scope, Offer) {
    $scope.offers = Offer.query();
}
