SELECT * FROM posts 
WHERE user_id = 13;


SELECT * FROM posts;


-- Query to delete users to test on delete action which was set to CASCADE
DELETE FROM users 
WHERE id = 15;


SELECT * FROM posts;
