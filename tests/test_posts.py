from typing import List
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts")

    # Validation using the schemas
    def validate(post):
        return schemas.PostOut(**post)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)

    # assert posts_list[0].Post.id == test_posts[0].id
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

