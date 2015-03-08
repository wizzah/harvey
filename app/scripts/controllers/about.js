'use strict';

/**
 * @ngdoc function
 * @name harveyApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the harveyApp
 */
angular.module('harveyApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
