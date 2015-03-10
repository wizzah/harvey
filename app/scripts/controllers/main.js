'use strict';

/**
 * @ngdoc function
 * @name harveyApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the harveyApp
 */
angular.module('harveyApp')
  .controller('MainCtrl', function ($scope, master) {
    $scope.tests = master.object;
  });
