-- Script that lists all records of the table second_table of the database hbtn_0c_0.
SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY score, name ORDER BY score DESC;
