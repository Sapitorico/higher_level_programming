-- create table
CREATE TABLE IF NOT EXISTS unique_id (
    id INT(1) NOT NULL,
    name VARCHAR(256),
    UNIQUE KEY (id)
)