from apps.posts.models import Post

for i in range(100):
    Post.objects.create(title=f'Post created in bulk # {i}', text='Sample text for post created via ORM. I can create a lot of posts automatically in such way', status='p', author_id=1)
