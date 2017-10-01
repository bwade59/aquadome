'use strict';

exports.conditionsGET = function(args, res, next) {
  /**
   * Gets `condition` objects. Optional query param of **size** determines size of returned array 
   *
   * returns List
   **/
  var examples = {};
  examples['application/json'] = [ {
  "feed" : true,
  "watertemp" : 6.02745618307040320615897144307382404804229736328125,
  "currenttime" : "aeiou",
  "vent" : true,
  "fan" : true,
  "waterheat" : true,
  "waterph" : 0.80082819046101150206595775671303272247314453125,
  "ambienttemp" : 1.46581298050294517310021547018550336360931396484375,
  "lastfeeding" : "aeiou",
  "pump1" : true,
  "airheat" : true,
  "pump2" : true
} ];
  if (Object.keys(examples).length > 0) {
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(examples[Object.keys(examples)[0]] || {}, null, 2));
  } else {
    res.end();
  }
}

