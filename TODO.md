## Voting/Likes System Requirements
* Users should be able to like a post
* Should only be able to like a post once 
* Retrieving posts should also fetch the total number of likes

## Vote Model 
* Column referencing post id
* Column referencing id of user who liked the post
* A user should only be able to like a post once so this means we need to ensure every post_id/voter_id is a unique combination

## Composite Keys
* Primary key that spans multiple columns
* Since Primary Keys must be unique, this will ensure no user can like a post twice.
