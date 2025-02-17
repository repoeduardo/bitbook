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
