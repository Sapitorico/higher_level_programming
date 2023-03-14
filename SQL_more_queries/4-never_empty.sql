-- create a table
CREATE TABLE IF NOT EXISTS hbtn_test_db_4.id_not_null (
    id INT NOT NULL AUTO_INCREMENT DEFAULT 1,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);