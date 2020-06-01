from .models import Post
from file_upload.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime

def upload_and_create(request, file_to_upload):
    #create client
    session = Session(
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
        region_name = AWS_S3_REGION_NAME
    )

    s3 = session.resource('s3')

    #file upload
    now = datetime.now().strftime("%Y%H%M%S")

    img_object= s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key = request.POST['title'] + '/'+now + file_to_upload.name,
        #pk 쓰기 '1/' +now + file_to_upload.name
        Body = file_to_upload
    )

    #create post
    s3_url = "https://django-file-upload-yeongbeom.s3.ap-northeast-2.amazonaws.com/"
    post = Post.objects.create(
        title = request.POST['title'],
        img = s3_url + request.POST['title']+'/'+now + file_to_upload.name
        #pk 추가할 곳
        # s3_url+'1/'+now+file_to_upload.name
    )


