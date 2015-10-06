# Working Bikes
Working Bikes volunteer tracking website

## Development

### Create the database (MySQL)
```sql
CREATE DATABASE the_database;
CREATE USER the_user IDENTIFIED BY 'the_password';
GRANT ALL PRIVILEGES ON working_bikes.* to 'the_user'@'%';
```

### Set up the environment
```shell
export WORKING_BIKES_DATABASE_NAME=the_database
export WORKING_BIKES_DATABASE_USER=the_user
export WORKING_BIKES_DATABASE_PASSWORD=the_password
export WORKING_BIKES_SECRET_KEY=foobarbaz
export WORKING_BIKES_DEBUG=TRUE
```

### Clone this repository
```shell
$ git clone https://github.com/working-bikes/working-bikes.git
```
### Install its dependencies
```shell
$ cd working-bikes
$ mkvirtualenv working-bikes
(working-bikes)$ pip install -r requirements.txt
```

### Run the server
```shell
(working-bikes)$ ./manage.py runserver
```