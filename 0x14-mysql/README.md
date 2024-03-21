### Setting Up MySQL Database Slave-Master Replica System

**Introduction**

In this project, we'll be setting up a MySQL database slave-master replica system on two web servers. This setup is commonly used in production environments to improve database performance, reliability, and redundancy.
![image](https://github.com/LWSSIM/alx-system_engineering-devops/assets/127129101/47d493d8-086e-473d-8b07-799240ddb0f6)

### Installing mysql -5.7 on the web-servers

```bash
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```
I used bionic for this project.

If you have problems installing, follow this [guide](https://www.devart.com/dbforge/mysql/how-to-install-mysql-on-ubuntu/)

### What is the main role of a database?

A database serves as a centralized repository for storing, organizing, and managing data. It provides mechanisms for data retrieval, insertion, deletion, and modification, enabling applications to interact with structured data efficiently.

```sql
-- Example: Creating a database in MySQL
CREATE DATABASE my_database;
```

### What is a database replica?

A database replica is an exact copy of the primary database (master) that is created and maintained on another server (slave). This replica contains the same data as the master and is updated in near real-time to reflect changes made to the master database.

```sql
-- Example: Configuring replication in MySQL
-- On the master server:
GRANT REPLICATION SLAVE ON *.* TO 'replication_user'@'slave_ip' IDENTIFIED BY 'password';

-- On the slave server:
CHANGE MASTER TO MASTER_HOST='master_ip', MASTER_USER='replication_user', MASTER_PASSWORD='password';
START SLAVE;
```

### What is the purpose of a database replica?

The primary purposes of having a database replica include high availability, load balancing, and disaster recovery.

```php
// Example: Connecting to the database replica for read operations in PHP
$connection = new mysqli('replica_host', 'username', 'password', 'database_name');
```

### Why do database backups need to be stored in different physical locations?

Storing database backups in different physical locations provides protection against various risks such as hardware failure, natural disasters, and data corruption.

```bash
# Example: Backing up a MySQL database
mysqldump -u username -p database_name > backup.sql
```

### What operation should you regularly perform to make sure that your database backup strategy actually works?

Regularly testing database backups is crucial to ensure their reliability and effectiveness.

```bash
# Example: Restoring a MySQL database from a backup
mysql -u username -p database_name < backup.sql
```

## Tasks

### 0

Follow instalation guide.
(add checker public key in web-02 for ssh access)

TEST:
```bash
mysql --version
```

### 1

Configure sql for both servers to allow checker access, with the following:
Use a script or enter manually in `mysql`

```sql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
```
TEST:

```bash
mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
```

### 2

Create a minimum of 1 tables to configure replication;

```sql
CREATE DATABASE tyrell_corp;

USE tyrell_corp;

CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));

INSERT INTO nexus6 (name) VALUES (Leon);

GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
```
TEST:
```bash
mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
```

### 3

On web-01 create a new user for the replica server, and grant the right persmissions to the user.
```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';

GRANT REPLICATION SLAVE ON . TO 'replica_user'@'%';

GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
```
> [!NOTE]
> holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.


Test:
```bash
mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
```

### 4

In this task, we will configure the primary server to replicate to the replica server.

First, we need to set up the firewall rules on both servers to allow MySQL traffic.
```bash
sudo ufw allow 3306/tcp

sudo ufw reload
```


In my.cnf file on web-01, add the following lines to configure the server as a primary server:
```bash
server-id       = 1
# MySQL's Binary Log File
log_bin         = /var/log/mysql/mysql-bin.log
# Database we want to replicate
binlog_do_db    = tyrell_corp
```
In my.cnf file on web-02, add the following lines to configure the server as a replica server:
```bash
# Distinguish servers in a replication setup
server-id       = 2
# MySQL's Binary Log File
log_bin         = /var/log/mysql/mysql-bin.log
# Database we want to replicate
binlog_do_db    = tyrell_corp
# Defines the location of the replica's relay log
relay-log       = /var/log/mysql/mysql-relay-bin.log
```
Next, restart the MySQL service on both servers to apply the changes.
```bash
sudo service mysql restart
```

You can check the status of the MySQL service on web-01 and web-02 to ensure that it is running.
```bash
# in Web-01 mysql
SHOW MASTER STATUS;

# in Web-02 mysql
# set the proper values in the following command and run it in Web-02 mysql
CHANGE MASTER TO MASTER_HOST='master_ip', MASTER_USER='replica_user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.0000xx', MASTER_LOG_POS=INTEGER;

SHOW SLAVE STATUS\G
```

### Conclusion

Setting up a MySQL database slave-master replica system enhances database reliability, availability, and disaster recovery capabilities. By understanding the role of databases, the purpose of replicas, the importance of backup storage locations, and the need for regular backup testing, we can ensure the integrity and continuity of our data infrastructure.
