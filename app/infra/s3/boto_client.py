from dataclasses import dataclass
from uuid import UUID

from infra.s3.base import (
    AsyncS3ClientProtocol,
    S3DeleteObjectResponse,
    S3GetObjectResponse,
    S3PutObjectResponse,
    S3ListObjectsV2Response,
)


@dataclass
class BotoClient:
    client: AsyncS3ClientProtocol
    bucket_name: str

    async def get_content(self, content_uid: UUID) -> S3GetObjectResponse:
        response: dict = await self.client.get_object(Bucket=self.bucket_name, Key=str(content_uid))
        # todo добавить обработку ошибок
        return self._map_get_object(response)

    async def put_content(self, content_uid: UUID, body: bytes) -> S3PutObjectResponse:
        response: dict = await self.client.put_object(
            Bucket=self.bucket_name,
            Key=str(content_uid),
            Body=body,
        )
        return self._map_put_object(response)

    async def delete_content(self, content_uid: UUID) -> S3DeleteObjectResponse:
        response: dict = await self.client.delete_object(
            Bucket=self.bucket_name,
            Key=str(content_uid),
        )
        return self._map_delete_object(response)

    async def list_contents(self, prefix: str) -> S3ListObjectsV2Response:
        response: dict = await self.client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=prefix,
        )
        return self._map_list_objects(response)

    @staticmethod
    def _map_get_object(data: dict) -> S3GetObjectResponse:
        return S3GetObjectResponse(
            body=data["Body"],
            content_length=data.get("ContentLength"),
            content_type=data.get("ContentType"),
            etag=data.get("ETag"),
            last_modified=data.get("LastModified"),
            metadata=data.get("Metadata"),
            version_id=data.get("VersionId"),
            storage_class=data.get("StorageClass"),
            server_side_encryption=data.get("ServerSideEncryption"),
        )

    @staticmethod
    def _map_put_object(data: dict) -> S3PutObjectResponse:
        return S3PutObjectResponse(
            etag=data.get("ETag"),
            version_id=data.get("VersionId"),
            server_side_encryption=data.get("ServerSideEncryption"),
        )

    @staticmethod
    def _map_delete_object(data: dict) -> S3DeleteObjectResponse:
        return S3DeleteObjectResponse(
            delete_marker=data.get("DeleteMarker"),
            version_id=data.get("VersionId"),
            request_charged=data.get("RequestCharged"),
        )

    @staticmethod
    def _map_list_objects(data: dict) -> S3ListObjectsV2Response:
        return S3ListObjectsV2Response(
            contents=data.get("Contents"),
            common_prefixes=data.get("CommonPrefixes"),
            delimiter=data.get("Delimiter"),
            encoding_type=data.get("EncodingType"),
            is_truncated=data.get("IsTruncated"),
            key_count=data.get("KeyCount"),
            max_keys=data.get("MaxKeys"),
            name=data.get("Name"),
            next_continuation_token=data.get("NextContinuationToken"),
            prefix=data.get("Prefix"),
            start_after=data.get("StartAfter"),
        )
