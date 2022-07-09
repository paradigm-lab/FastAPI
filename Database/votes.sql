-- Composite Keys
CREATE TABLE votes (
	post_id INTEGER,
	user_id INTEGER,
	PRIMARY KEY(post_id, user_id),

	CONSTRAINT votes_posts_fkey
		FOREIGN KEY(post_id)
		REFERENCES posts(id)
		ON DELETE CASCADE,

	CONSTRAINT votes_users_fkey
		FOREIGN KEY(user_id)
		REFERENCES users(id)
		ON DELETE CASCADE
);


INSERT INTO votes(post_id, user_id) VALUES(8, 14);
INSERT INTO votes(post_id, user_id) VALUES(7, 16);

-- Invalid Post Id and User Id (Error Expected)
INSERT INTO votes(post_id, user_id) VALUES(1000, 1000);
