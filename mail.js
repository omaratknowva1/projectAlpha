exports.send = function(to,msg){ console.log('sending '+msg+' to '+to); setTimeout(function(){ console.log('sent') },100) }
exports.send2 = function(to,msg,a,b,c){ var d = require('./stuff'); console.log(to,msg,a,b,c) }
