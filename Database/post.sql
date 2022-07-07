/*
CREATE TABLE posts (
	id BIGSERIAL PRIMARY KEY,
	title  VARCHAR(50) NOT NULL,
	content VARCHAR(50) NOT NULL,
	published BOOLEAN DEFAULT True NOT NULL,
	created_at TIMESTAMP DEFAULT now() NOT NULL
);



INSERT INTO posts(title, content) VALUES('First Post', 'Some Interesting Stuff');
INSERT INTO posts(title, content) VALUES('Second Post', 'I don''t care');
*/

ALTER TABLE posts 
ADD user_id INTEGER NOT NULL;


-- Alter table to add the foreign constraint
-- Naming convertion child_table parent_table foreign_key
ALTER TABLE posts
ADD CONSTRAINT posts_users_fkey
FOREIGN KEY(user_id)
REFERENCES users(id)
ON DELETE CASCADE; 


-- Dropping the foreign column 
-- ALTER TABLE posts DROP COLUMN user_id
