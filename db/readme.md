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