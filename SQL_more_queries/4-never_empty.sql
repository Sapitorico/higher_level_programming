-- create a table
CREATE TABLE IF NOT EXISTS id_not_null.mysql (
    id INT NOT NULL AUTO_INCREMENT DEFAULT 1,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);