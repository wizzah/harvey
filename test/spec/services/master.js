'use strict';

describe('Service: master', function () {

  // load the service's module
  beforeEach(module('harveyApp'));

  // instantiate service
  var master;
  beforeEach(inject(function (_master_) {
    master = _master_;
  }));

  it('should do something', function () {
    expect(!!master).toBe(true);
  });

});
