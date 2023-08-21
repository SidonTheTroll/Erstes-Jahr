# 19/08/23

- Search for database named 'school'

```
mysql> show databases like 'school';
        Empty set (0.00 sec)
```

- Create database named 'school'

```
mysql> create database school;
        Query OK, 1 row affected (0.10 sec)
```

- Search database named 'school'

```
mysql> show databases like 'school';
        +-----------------+
        |Database (school)|
        +-----------------+
        |School           |
        +-----------------+
        1 row in set (0.00 sec)
```

- Delete database named 'school'

```
mysql> drop database school;
        Query OK, 0 row affected (0.09 sec)
```

- Search database named 'school'

```mysql> show database like 'school';
        Empty set (0.00 sec)
```
