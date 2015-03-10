'use strict';

/**
 * @ngdoc service
 * @name harveyApp.master
 * @description
 * # master
 * Service in the harveyApp.
 */
angular.module('harveyApp')
  .service('master', function ($rootScope, $firebaseObject, $log, $routeParams) {
  	var master = this;
  	if($routeParams.test){
  		master.ref = new Firebase($rootScope.firebaseApi + '/tests/' + $routeParams.test);
  	}else{
  		master.ref = new Firebase($rootScope.firebaseApi + '/tests');
  	}
  	
  	master.object = $firebaseObject(master.ref);
  	$log.info(master.object);

  	return master;
  });
