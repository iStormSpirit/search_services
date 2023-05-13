from models.post import PostModel
from schemas.schemas import Post, PostCreate, PostUpdate
from .post import PostService


class RepositoryPost(PostService[PostModel, PostCreate, PostUpdate]):
    pass


post_crud = RepositoryPost(PostModel)
