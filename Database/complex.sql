-- Joins
-- Left Join, Right Join, Inner Join, Outer Join
SELECT * FROM posts LEFT JOIN users ON posts.owner_id = users.id;

SELECT posts.id, email FROM posts LEFT JOIN users ON posts.owner_id = users.id;

SELECT posts.*, email FROM posts LEFT JOIN users ON posts.owner_id = users.id;

SELECT posts.*, email, users.id FROM posts LEFT JOIN users ON posts.owner_id = users.id;

-- Right Join it's going to include all the user's even if there have no posts created
SELECT posts.*, email, users.id FROM posts RIGHT JOIN users ON posts.owner_id = users.id;

-- Count the number of post for each user (LEFT)
SELECT users.id, COUNT(*) FROM posts LEFT JOIN users ON posts.owner_id = users.id 
GROUP BY users.id;

-- Count the number of post for each user (RIGHT)
SELECT users.id, users.email, COUNT(posts.id) AS user_post_count FROM posts RIGHT JOIN users ON posts.owner_id = users.id 
GROUP BY users.id;




