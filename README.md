# BITBOOK

Bitbook is a terminal-based book management system. The user interface is very simple, featuring only basic functions for listing, adding, updating, and deleting books, as shown in the image below.

![Menu](ASSETS/user_menu.png)

## REQUIREMENTS  

The requirements to use the system are as follows:  

- MySQL database  
- Python  
  - Libraries: rich and mysql-connector-python  
- Git (optional, only if you want to clone this repository)  

### DATABASE - MYSQL  

Install the database server on your computer (or local network), then run the following script to create the database:  

~~~sql
CREATE DATABASE bitbook;
USE bitbook;
CREATE TABLE books (
	id int primary key auto_increment,
    author varchar(100) not null,
    title varchar(255) not null,
    subtitle varchar(255),
    genre varchar(50) not null,
    book_year int not null,
    publisher varchar(100) not null,
    book_description text
);

/* Initial data, you can change this */
INSERT INTO books(author, title, subtitle, genre, book_year, publisher, book_description)
VALUES
('Machado De Assis', 'Dom Casmurro', '', 'literature', 1899, 'Principis', 'In Dom Casmurro, the narrator Bento Santiago revisits his childhood spent on Rua de Matacavalos and tells the story of the love and misadventures he experienced with Capitu'),
('Miguel De Cervantes', 'Don Quixote', '', 'literature', 1605, 'Pe de letra', 'After reading many novels of chivalry, a poor nobleman decides to become a knight-errant. He adopts the name Don Quixote de la Mancha, in homage to the region of Spain where he was born. He relies on the help of a peasant, Sancho Panza, who becomes his squire. His unbridled imagination makes him see everything in a crazy way: windmills become giants; herds become armies; inns, castles, and so on.');

SELECT * FROM books;
~~~

![Database](ASSETS/db.png)

### DOWNLOAD THE PROJECT TO YOUR COMPUTER  

**ATTENTION**: Before downloading, activate the virtual environment using Python and install the required libraries.  

Now clone this repository to your computer:  

~~~bash
git clone https://github.com/repoeduardo/bitbook.git
~~~

Edit the database parameters in the ``config.py`` file:  

~~~python
# Database configuration
DB_HOST = # Localhost or Database IP
DB_PORT = # Database port - default: 3306
DB_USER = # Database user
DB_PASSWORD = # Database password
DB_NAME = "bitbook" # Database name
MYSQL_VERSION = "8.0.41" # Version of MySQL

# Software
SOFT_VERSION = "1.0.0"
SOFT_NAME = "Bitbook"
SOFT_DESC = "terminal system for book management"
SOFT_CREATORS = ["Eduardo Araujo Da Silva"] # Change to your name
~~~

If the settings are correct, simply run the main project file:  
~~~bash
python main.py
~~~
