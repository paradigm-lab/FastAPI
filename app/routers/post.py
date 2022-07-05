from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()


@router.get("/posts", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()

    return posts  # FastAPI is going to serialize into JSON


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,
                 db: Session = Depends(get_db)):  # Extracts all of the fields from the body and convert to dictionary
    """
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    """

    # This helps to be vulnerable from SQL injection cursor.execute("""INSERT INTO posts(title, content, published)
    # VALUES(%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))

    # new_post = cursor.fetchone()

    # Committing to the database to actually commit the changes (By using the database connection Instance)
    # conn.commit()

    # print(**post.dict())
    new_post = models.Post(**post.dict())  # Unpacking the model to a regular python dictionary
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # Returning back the post to new_post

    return new_post


# Path parameter(id)
@router.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    """
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} was not found"}
    """

    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()

    # We don't use the all() method because it's going to keep searching for all the data instead we use first() method.
    post = db.query(models.Post).filter(models.Post.id == id).first()   # More efficient

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")

    return post


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # Deleting post
    # Find the index in the array that has required ID
    # my_posts.pop(index)

    """
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    my_posts.pop(index)
    """

    # Using raw SQL
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    '''
    deleted_post = cursor.fetchone()
    print(deleted_post)
    conn.commit()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    '''

    # Using ORM
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):

    """
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    """

    # Raw SQL query
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #               (post.title, post.content, post.published, str(id)))

    '''
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    '''

    # ORM Approach
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    else:
        post_query.update(updated_post.dict(), synchronize_session=False)
        db.commit()

    return post_query.first()
