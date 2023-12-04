import boto3
import gzip
from io import BytesIO
import json
from datetime import datetime

from .models import SegmentObjects

def sync_aws_s3_data():
    boto3.setup_default_session(profile_name='s3user')
    s3_client = boto3.resource('s3')
    my_bucket = s3_client.Bucket('segment-tiny')

    for file in my_bucket.objects.all():
        if file.key.endswith(".gz"):
            gzipped_content = file.get()['Body'].read()
            file_content = gzip.GzipFile(fileobj=BytesIO(gzipped_content)).read().decode('utf-8')
            try:
                json_data = json.loads(file_content)
                if not SegmentObjects.objects.filter(message_id=json_data.get("messageId")).first():
                    SegmentObjects.objects.create(
                        anonymous_user_id=json_data["anonymousId"],
                        user_id=json_data.get("userId"),
                        message_id=json_data.get("messageId"),
                        page_path=json_data["properties"].get("path"),
                        page_title=json_data["properties"].get("title"),
                        source_element_id=json_data["properties"].get("element_id"),
                        event_name=json_data.get("event"),
                        event_type=json_data.get("type"),
                        received_at=datetime.strptime(json_data["sentAt"].split(".")[0], "%Y-%m-%dT%H:%M:%S"),
                    )
            except:
                pass
