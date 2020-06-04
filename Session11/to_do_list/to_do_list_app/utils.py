from .models import Post, Picture
from to_do_list.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime

def upload_and_save(request, file_to_upload, new_post):
    
    session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
    )

    s3 = session.resource('s3')
    now = datetime.now().strftime("%Y%H%M%S")

    img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key = str(new_post.pk)+'/' +new_post.title,
        Body = file_to_upload
    )

    #Post model 만들기
    s3_url = 'https://django-file-upload-yeongbeom.s3.ap-northeast-2.amazonaws.com/'
    picture = Picture.objects.create(
        post = new_post,
        author = new_post.author,
        content = s3_url+ str(new_post.pk)+'/' + new_post.title
    )