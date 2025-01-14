from __future__ import annotations

import boto3
from botocore.exceptions import ClientError
from pydantic import BaseModel, HttpUrl

from deciphon_sched.settings import Settings


class Storage:
    def __init__(self, settings: Settings):
        self._s3 = boto3.client(
            "s3",
            endpoint_url=settings.s3_url.unicode_string(),
            aws_access_key_id=settings.s3_key,
            aws_secret_access_key=settings.s3_secret,
        )
        self._bucket = settings.s3_bucket
        if not self._bucket_exists():
            self._s3.create_bucket(Bucket=self._bucket)

    def _bucket_exists(self):
        try:
            self._s3.head_bucket(Bucket=self._bucket)
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False
            raise e

    def presigned_upload(self, file: str) -> PresignedUpload:
        x = self._s3.generate_presigned_post(self._bucket, file)
        return PresignedUpload(url=HttpUrl(x["url"]), fields=x["fields"])

    def presigned_download(self, file: str) -> PresignedDownload:
        params = {"Bucket": self._bucket, "Key": file}
        x = self._s3.generate_presigned_url("get_object", Params=params)
        return PresignedDownload(url=HttpUrl(x))

    def delete(self, file: str):
        self._s3.delete_object(Bucket=self._bucket, Key=file)

    def has_file(self, file: str) -> bool:
        try:
            self._s3.head_object(Bucket=self._bucket, Key=file)
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False
            raise e


class PresignedUpload(BaseModel):
    url: HttpUrl
    fields: dict[str, str]


class PresignedDownload(BaseModel):
    url: HttpUrl
