# Database

## psql commands

```
# conntect to database
psql -U admin -d mydb

# show tables
\dt

# describe tables
\d products

# test insert and select
insert into products (name) values ('first name');
select * from products;
```

## APIs
```sh
# list all items
curl --location --request GET 'http://127.0.0.1:8888/api/products'

# add item
curl --location --request POST 'http://127.0.0.1:8888/api/product' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "boy"
}'
```