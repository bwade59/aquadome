'use strict';

var url = require('url');

var Default = require('./DefaultService');

module.exports.conditionsGET = function conditionsGET (req, res, next) {
  Default.conditionsGET(req.swagger.params, res, next);
};
