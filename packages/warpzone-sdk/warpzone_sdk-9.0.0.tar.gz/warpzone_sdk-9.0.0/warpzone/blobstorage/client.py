""" Module w.r.t. Azure blob storage logic."""
from dataclasses import dataclass
from typing import Optional

import pandas as pd
from azure.core.exceptions import (
    HttpResponseError,
    ServiceRequestError,
    ServiceResponseError,
)
from azure.storage.blob import BlobServiceClient

from warpzone.healthchecks import HealthCheckResult, HealthStatus
from warpzone.transform import data


@dataclass
class BlobData:
    content: bytes
    name: str
    metadata: Optional[dict] = None

    def __post_init__(self):
        self.metadata = self.metadata if self.metadata else {}

    @classmethod
    def from_pandas(
        cls,
        df: pd.DataFrame,
        name: str,
        metadata: Optional[dict] = None,
        schema: Optional[dict] = None,
    ):
        content = data.pandas_to_parquet(df, schema=schema)
        return cls(content, name, metadata=metadata)

    def to_pandas(self) -> pd.DataFrame:
        return data.parquet_to_pandas(self.content)


class WarpzoneBlobClient:
    """Class to interact with Azure Blob Service"""

    def __init__(self, blob_service_client: BlobServiceClient):
        self._blob_service_client = blob_service_client

    @classmethod
    def from_connection_string(cls, conn_str: str):
        blob_service_client = BlobServiceClient.from_connection_string(conn_str)
        return cls(blob_service_client)

    def download(self, container_name: str, blob_name: str) -> BlobData:
        blob_client = self._blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_name,
        )
        stream_downloader = blob_client.download_blob()
        return BlobData(
            content=stream_downloader.content_as_bytes(),
            name=blob_name,
            metadata=stream_downloader.properties.metadata,
        )

    def upload(
        self,
        container_name: str,
        blob_data: BlobData,
        overwrite: bool = False,
    ):
        blob_client = self._blob_service_client.get_blob_client(
            container=container_name,
            blob=blob_data.name,
        )
        blob_client.upload_blob(
            data=blob_data.content,
            metadata=blob_data.metadata,
            overwrite=overwrite,
        )

    def check_health(self) -> HealthCheckResult:
        """
        Pings the connection to the client's associated storage ressources in Azure.
        """
        try:
            container_iterator = self._blob_service_client.list_containers()
            next(container_iterator, None)
        except (ServiceRequestError, ServiceResponseError, HttpResponseError) as ex:
            return HealthCheckResult(
                status=HealthStatus.UNHEALTHY,
                description="Unable to connect to blob storage.",
                exception=ex,
            )

        return HealthCheckResult.healthy()
