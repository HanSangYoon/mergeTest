from django.db import models
from django.utils import timezone
from datetime import datetime


class FacebookInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    gender = models.CharField(max_length=255, null=True, default=None)
    phone_number = models.CharField(max_length=255, null=True, default=None)
    birthday = models.CharField(max_length=255, null=True, default=None)
    company1 = models.CharField(max_length=255, null=True, default=None)
    company2 = models.CharField(max_length=255, null=True, default=None)
    company3 = models.CharField(max_length=255, null=True, default=None)
    university1 = models.CharField(max_length=255, null=True, default=None)
    university2 = models.CharField(max_length=255, null=True, default=None)
    university3 = models.CharField(max_length=255, null=True, default=None)
    address1 = models.CharField(max_length=255, null=True, default=None)
    address2 = models.CharField(max_length=255, null=True, default=None)
    address3 = models.CharField(max_length=255, null=True, default=None)
    contact1 = models.CharField(max_length=255, null=True, default=None)
    contact2 = models.CharField(max_length=255, null=True, default=None)
    contact3 = models.CharField(max_length=255, null=True, default=None)
    contact4 = models.CharField(max_length=255, null=True, default=None)
    friends_cnt = models.IntegerField(null=True, default=None)
    insertedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class FacebookPost(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    post_text = models.TextField(null=True, default=None)
    post_info = models.CharField(max_length=255, null=True, default=None)
    post_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.post_text}'
        return template.format(self)


class FacebookFriends(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    friends_name = models.CharField(max_length=255, null=True, default=None)
    friends_info = models.CharField(max_length=255, null=True, default=None)
    friends_id = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.friends_name}'
        return template.format(self)


class InstagramInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    intro = models.CharField(max_length=255, null=True, default=None)
    homepage = models.CharField(max_length=255, null=True, default=None)
    company1 = models.CharField(max_length=255, null=True, default=None)
    post_cnt = models.IntegerField(null=True, default=None)
    follower_cnt = models.IntegerField(null=True, default=None)
    follow_cnt = models.IntegerField(null=True, default=None)
    insertedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class InstagramPost(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    post_text = models.TextField(null=True, default=None)
    post_place = models.CharField(max_length=255, null=True, default=None)
    post_info = models.CharField(max_length=255, null=True, default=None)
    post_like = models.IntegerField(null=True, default=None)
    post_view = models.IntegerField(null=True, default=None)
    post_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.post_text}'
        return template.format(self)


class InstagramFollower(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    follower_id = models.CharField(max_length=255, null=True, default=None)
    follower_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class InstagramFollow(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    follow_id = models.CharField(max_length=255, null=True, default=None)
    follow_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class TwitterInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_cnt = models.IntegerField(null=True, default=None)
    following_cnt = models.IntegerField(null=True, default=None)
    follower_cnt = models.IntegerField(null=True, default=None)
    joined_date = models.DateField(null=True, default=None)
    insertedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class TwitterTweet(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    tweet_name = models.CharField(max_length=255, null=True, default=None)
    tweet_page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_text = models.TextField(null=True, default=None)
    tweet_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.tweet_text}'
        return template.format(self)


class TwitterTrends(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    trends_name = models.CharField(max_length=255, null=True, default=None)
    trends_tweet_cnt = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.trends_name}'
        return template.format(self)


class TwitterFollower(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    follower_name = models.CharField(max_length=255, null=True, default=None)
    follower_page_id = models.CharField(max_length=255, null=True, default=None)
    follower_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class TwitterFollowing(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    following_name = models.CharField(max_length=255, null=True, default=None)
    following_page_id = models.CharField(max_length=255, null=True, default=None)
    following_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.following_name}'
        return template.format(self)


class YoutubeInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    subscribe_cnt = models.IntegerField(null=True, default=None)
    insertedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class YoutubeSubscribe(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    channel_name = models.CharField(max_length=255, null=True, default=None)
    channel_info = models.CharField(max_length=255, null=True, default=None)
    subscribe_cnt = models.IntegerField(null=True, default=None)
    channel_sub_cnt = models.IntegerField(null=True, default=None)
    channel_video_cnt = models.IntegerField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.channel_name}'
        return template.format(self)


class YoutubeRecentVideo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    video_channel_name = models.CharField(max_length=255, null=True, default=None)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.video_name}'
        return template.format(self)


class YoutubeCommentHistory(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_comment = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.video_name}'
        return template.format(self)


class GmailInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    mail_cnt = models.IntegerField(null=True, default=None)
    insertedTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id}'
        return template.format(self)


class GmailList(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    origin_ph = models.CharField(max_length=255, null=True, default=None)
    gmail_sender = models.CharField(max_length=255, null=True, default=None)
    gmail_sender_email = models.CharField(max_length=255, null=True, default=None)
    gmail_title = models.CharField(max_length=255, null=True, default=None)
    gmail_contents = models.TextField(null=True, default=None)
    gmail_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.gmail_title}'
        return template.format(self)
