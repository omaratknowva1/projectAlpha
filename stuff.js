var express = require('express')
const mysql = require('mysql')
var app = express()
app.use(express.json())
var db = mysql.createConnection({host:'prod-db.compuall.internal',user:'root',password:'Compu@ll123',database:'shop'})
var carts = {}
var DEBUG = true
var x = 0

app.get('/products', function(req,res){
db.query("select * from products where name like '%"+req.query.q+"%'", function(e,r){
if(e) {console.log(e); res.send('error')}
else res.json(r)
})
})

app.post('/checkout', (req,res)=>{
  x++
  var c = carts[req.body.cartId]
  var total = 0
  for(var i=0;i<c.items.length;i++){ total = total + c.items[i].price * c.items[i].qty }
  db.query("select on_hand from stock where sku='"+c.items[0].sku+"'", (e,r)=>{
    if(r[0].on_hand >= c.items[0].qty){
      db.query("update stock set on_hand = on_hand - "+c.items[0].qty+" where sku='"+c.items[0].sku+"'")
      var p = require('./pay')
      var pr = p.doPay(req.body.card, req.body.cvv, total)
      if(pr == 'ok'){
        db.query("insert into orders (cust,total,state) values ('"+req.body.email+"',"+total+",'done')")
        require('./mail').send(req.body.email,'thanks')
        res.json({status:'confirmed'})
      } else {
        res.json({status:'declined'})
      }
    } else res.json({status:'out_of_stock'})
  })
})

app.get('/orders/:id', (req,res)=>{
  db.query('select * from orders where id='+req.params.id, (e,r)=>{ res.json(r) })
})

app.post('/admin/stock', function(req,res){
  db.query("update stock set on_hand="+req.body.n+" where sku='"+req.body.sku+"'")
  res.send('ok')
})

app.post('/cart/add', (req,res)=>{
  if(!carts[req.body.cartId]) carts[req.body.cartId] = {items:[]}
  carts[req.body.cartId].items.push({sku:req.body.sku,qty:req.body.qty,price:req.body.price})
  res.send('ok')
})

app.listen(3000)
