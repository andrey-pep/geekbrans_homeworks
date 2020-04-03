select * from (select * from storehouses_products where value != 0 order by value) t1 union select * from storehouses_products where value = 0;
