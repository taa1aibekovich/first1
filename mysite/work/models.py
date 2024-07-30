from django.db import models


class UserProfile(models.Model):
    nickname = models.CharField(max_length=32, unique=True)
    biografi = models.TextField()
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    website = models.URLField()

    def __str__(self):
        return self.nickname


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} - {self.following}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_image')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='like_post')
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} - {self.created_at}'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replise', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.post} - {self.created_at}'
