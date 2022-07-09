## Voting/Likes System Requirements
* Users should be able to like a post
* Should only be able to like a post once 
* Retrieving posts should also fetch the total number of likes

#### Vote Model 
* Column referencing post id
* Column referencing id of user who liked the post
* A user should only be able to like a post once so this means we need to ensure every post_id/voter_id is a unique combination

#### Composite Keys
* Primary key that spans multiple columns
* Since Primary Keys must be unique, this will ensure no user can like a post twice.

#### Vote Route
* Path will be at "/vote"
* The user id will be extracted from the JWT token 
* The body will contain the id of the post the user is voting on as well as the directio of the vote.

    ``
        {
            post_id: 1432
            vote dir: 0
        }
    ``
* A vote direction(dir) of 1 means we want to add a vote, a direction of 0 means we want to delete a vote.
