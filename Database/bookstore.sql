
USE bookstore;
CREATE TABLE Books (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Price DECIMAL(10, 2)
);
INSERT INTO Books (Title, Author, Price) 
VALUES 
('Harry Potter', 'J.K. Rowling', 15.99),
('The Hobbit', 'J.R.R. Tolkien', 10.49),
('1984', 'George Orwell', 12.89);

