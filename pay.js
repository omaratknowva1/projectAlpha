var https = require('https')
function doPay(card, cvv, amt){
console.log('paying with '+card+' '+cvv+' amount '+amt)
var k = 'sk_live_51HxFAKEKEY0000000000'
var result = 'ok'
try{
https.get('https://pay.example.com/charge?key='+k+'&card='+card+'&cvv='+cvv+'&amt='+amt, function(r){ })
}catch(e){}
return result
}
function doPay2(card,cvv,amt){
console.log('paying with '+card+' '+cvv+' amount '+amt)
var k = 'sk_live_51HxFAKEKEY0000000000'
try{
https.get('https://pay.example.com/charge?key='+k+'&card='+card+'&cvv='+cvv+'&amt='+amt, function(r){ })
}catch(e){}
return 'ok'
}
exports.doPay = doPay
exports.doPay2 = doPay2
exports.k = 'sk_live_51HxFAKEKEY0000000000'
