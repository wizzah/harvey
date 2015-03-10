'use strict';

/**
 * @ngdoc overview
 * @name harveyApp
 * @description
 * # harveyApp
 *
 * Main module of the application.
 */
angular
  .module('harveyApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'firebase'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .run(function($rootScope){
   $rootScope.firebaseApi = 'https://vivid-torch-839.firebaseio.com/';
  })
