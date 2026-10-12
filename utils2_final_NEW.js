function calc(a,b){return a*b}
function calcTotal(items){var t=0;items.forEach(function(i){t+=i.price*i.qty});return t}
function ttl(items){var t=0;for(var i in items){t=t+items[i].price*items[i].qty}return t}
var reservations = []
function reserve(sku,q){ reservations.push({sku:sku,q:q,exp:Date.now()+900000}); return true }
function release(sku){ for(var i=0;i<reservations.length;i++){ if(reservations[i].sku==sku) reservations.splice(i,1) } }
function validEmail(e){ return e.indexOf('@')>-1 }
function fmt(n){ return '$'+n }
function fmtPrice(n){ return '$'+n.toFixed(2) }
module.exports = {calc,calcTotal,ttl,reserve,release,validEmail,fmt,fmtPrice,reservations}
