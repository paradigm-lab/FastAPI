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



-- Explanations:
	-- The first table refferenced is the LEFT table and the second table referenced is the RIGHT tables


-- Posts over votes(LEFT)
SELECT * FROM posts LEFT JOIN votes ON posts.id = votes.post_id;

-- Posts over votes(RIGHT)
SELECT * FROM posts RIGHT JOIN votes ON posts.id = votes.post_id; 

-- Count the number of votes
SELECT posts.*, COUNT(votes.post_id) AS LIKES FROM posts LEFT JOIN votes ON posts.id = votes.post_id 
GROUP BY posts.id; 

-- Count the number of votes
SELECT posts.*, COUNT(votes.post_id) AS LIKES FROM posts LEFT JOIN votes ON posts.id = votes.post_id 
WHERE posts.id = 7
GROUP BY posts.id; 
