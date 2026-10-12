create table products(id int, name varchar(255), price float, sku varchar(50), active int);
create table stock(sku varchar(50), on_hand int, reserved int);
create table orders(id int auto_increment primary key, cust varchar(255), total float, state varchar(20), card varchar(30));
insert into products values (1,'Laptop',999.99,'LAP1',1);
insert into stock values ('LAP1',10,0);
create table orders2(id int, cust varchar(255), total float, cardnum varchar(30), cvv varchar(4));
