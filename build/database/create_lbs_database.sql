-- CREATES lbs database

DROP DATABASE lbs;

CREATE DATABASE IF NOT EXISTS lbs;

-- USE lbs;

-- -- CREATE TABLE user

-- CREATE TABLE IF NOT EXISTS user (
--     user_id INT AUTO_INCREMENT PRIMARY KEY,
--     full_name VARCHAR(100) NOT NULL,
--     email_address VARCHAR(60) UNIQUE,
--     phone VARCHAR(15),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- LIBRARY TABLE

-- CREATE TABLE IF NOT EXISTS librarian (
--     librarian_id INT AUTO_INCREMENT PRIMARY KEY,
--     full_name VARCHAR(100) NOT NULL,
--     email_address VARCHAR(60) UNIQUE,
--     secret_key VARCHAR(30) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- BOOK TABLE
-- CREATE TABLE IF NOT EXISTS book (
--     isbn_no VARCHAR(20) PRIMARY KEY UNIQUE,
--     bk_title TEXT NOT NULL,
--     bk_authors TEXT NOT NULL,
--     year_published INT,
--     publisher VARCHAR(60) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- ISSUED TABLE
-- CREATE TABLE IF NOT EXISTS issued (
--     issued_id INT AUTO_INCREMENT PRIMARY KEY,
--     issued_date DATETIME NOT NULL,
--     book_isbn VARCHAR(20) NOT NULL,
--     librarian_id INT NOT NULL,
--     user_id INT NOT NULL,
--     FOREIGN KEY (book_isbn) 
--         REFERENCES book (isbn_no) 
--         ON UPDATE RESTRICT 
--         ON DELETE CASCADE,
--     FOREIGN KEY (librarian_id) 
--         REFERENCES librarian (librarian_id) 
--         ON UPDATE RESTRICT 
--         ON DELETE CASCADE,
--     FOREIGN KEY (user_id) 
--         REFERENCES user (user_id) 
--         ON UPDATE RESTRICT 
--         ON DELETE CASCADE
-- );

-- -- RETURN TABLE

-- CREATE TABLE IF NOT EXISTS bk_return (
--     return_id INT AUTO_INCREMENT PRIMARY KEY,
--     issued_id INT NOT NULL,
--     isreturned ENUM('Yes', 'No'),
--     FOREIGN KEY (issued_id) 
--         REFERENCES issued (issued_id) 
--         ON UPDATE RESTRICT 
--         ON DELETE CASCADE
-- );
