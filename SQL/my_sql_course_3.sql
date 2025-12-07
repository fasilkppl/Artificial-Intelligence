CREATE TABLE exercise_logs
    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT,
    minutes INTEGER, 
    calories INTEGER,
    heart_rate INTEGER);

INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("biking", 30, 100, 110);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("biking", 10, 30, 105);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("dancing", 15, 200, 120);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("tree climbing", 30, 70, 90);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("tree climbing", 25, 72, 80);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("rowing", 30, 70, 90);
INSERT INTO exercise_logs(title, minutes, calories, heart_rate) VALUES ("hiking", 60, 80, 85);

SELECT * FROM exercise_logs WHERE title = "biking" OR title = "hiking" OR title = "tree climbing" OR title = "rowing";

/* IN */
SELECT * FROM exercise_logs WHERE title IN ("biking", "hiking", "tree climbing", "rowing");


#another table
CREATE TABLE drs_favorites
    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT,
    reason TEXT);

INSERT INTO drs_favorites(title, reason) VALUES ("biking", "Improves endurance and flexibility.");
INSERT INTO drs_favorites(title, reason) VALUES ("hiking", "Increases cardiovascular health");

SELECT title FROM drs_favorites;

SELECT * FROM drs_favorites;

SELECT * FROM exercise_logs WHERE title IN (
    SELECT title FROM drs_favorites);
    
SELECT * FROM exercise_logs WHERE title IN (
    SELECT title FROM drs_favorites WHERE reason = "Increases cardiovascular health");
    
/* LIKE */

SELECT * FROM exercise_logs WHERE title IN (SELECT title FROM drs_favorites WHERE reason LIKE "%cardiovascular%");





CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT);
    
CREATE TABLE diary_logs (
    id INTEGER PRIMARY KEY auto_increment,
    user_id INTEGER,
    date TEXT,
    content TEXT
    );
    
/* After user submitted their new diary log */
INSERT INTO diary_logs (user_id, date, content) VALUES (1, "2015-04-01",
    "I had a horrible fight with OhNoesGuy and I buried my woes in 3 pounds of dark chocolate.");
    
INSERT INTO diary_logs (user_id, date, content) VALUES (1, "2015-04-02",
    "We made up and now we're best friends forever and we celebrated with a tub of ice cream.");

SELECT * FROM diary_logs;

UPDATE diary_logs SET content = "I had a horrible fight with OhNoesGuy" WHERE id = 2;

SELECT * FROM diary_logs;

DELETE FROM diary_logs WHERE id = 1;

SELECT * FROM diary_logs;



