-- create table
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
);