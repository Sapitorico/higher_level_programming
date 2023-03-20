-- Database + tables to test
DROP DATABASE IF EXISTS test_7;
CREATE DATABASE IF NOT EXISTS test_7;
USE test_7;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York");