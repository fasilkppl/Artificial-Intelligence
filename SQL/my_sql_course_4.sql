/* What we used to originally create the table */
CREATE TABLE users (
    id INTEGER PRIMARY KEY auto_increment,
    name TEXT);
    
CREATE TABLE paragraphs (
    id INTEGER PRIMARY KEY auto_increment,
    user_id INTEGER,
    date TEXT,
    content TEXT
    );
    
/* After user submits a diary log */
INSERT INTO paragraphs (user_id, date, content) VALUES (1, "2015-04-02",
    "OhNoesGuy and I made up and now we're best friends forever and we celebrated with a tub of ice cream.");
    
ALTER TABLE paragraphs ADD emotion TEXT default "unknown";

INSERT INTO paragraphs (user_id, date, content, emotion) VALUES (1, "2015-04-03",
    "We went to Disneyland!", "happy");
    
SELECT * FROM paragraphs;
