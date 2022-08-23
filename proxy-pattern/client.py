from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any
import uuid


@dataclass
class BlotterFile:
    client: str
    date: str
    body: List[Dict[Any, Any]]
    metadata: List[Dict[Any, Any]] 


class BlotterFileRepo(ABC):
    """
    Represents inteface through which client code interacts
    with blotter files.
    """
    @abstractmethod
    def getFile(self, client: str, date: str) -> BlotterFile:
        """
        Get file from actual storage.
        """

    @abstractmethod
    def uploadFile(self, client: str, date: str, blotter: BlotterFile) -> str:
        """
        Upload blotter file to permanent storage.
        """
        

class S3Adapter:
    def __init__(self, region: str):
        self.region = region

    def download_file(self, bucket: str, object_name: str, file_name: str) -> BlotterFile:
        """
        This is a fake boto3 implementation.
        """
        print(f"In s3 adapter")


class S3BlotterFileRepo(BlotterFileRepo):
    """
    Implements access to s3 bucket.
    """
    def __init__(self, s3: S3Adapter):
        self.s3 = s3

    def getFile(self, client: str, date: str) -> BlotterFile:
        """
        Uses boto adapter to access filestore.
        """
        print(f"Getting {date}.parquet blotter file for {client}.")
        return BlotterFile("", "", [{}, {}], [{}])

    def uploadFile(self, client: str, date: str, blotter: BlotterFile) -> str:
        """
        Uses boto adapter to upload a file to filestore.
        """
        print(f"Uploading {date}.parquet file for {client}.")
        return uuid.uuid4()

class CachedS3BlotterFileRepo(BlotterFileRepo):
    """
    Implements cached access to s3 bucket.
    """
    def __init__(self, s3: S3Adapter):
        self.s3 = s3
        # Could also be redis...
        self._cache = {}


    def getFile(self, client: str, date: str) -> BlotterFile:
        """
        Uses boto adapter to access filestore.
        """
        print(f"Getting {date}.parquet blotter file for {client}.")
        if date in self._cache:
            return self._cache[date]
        
        file = BlotterFile("", "", [{}, {}], [{}])
        self._cache[date] = file
        return file

    def uploadFile(self, client: str, date: str, blotter: BlotterFile) -> str:
        """
        Uses boto adapter to upload a file to filestore.
        """
        pass


def client():
    s3 = S3Adapter(region="us-east-1")

    cached_repo = CachedS3BlotterFileRepo(s3=s3)

    cached_repo.getFile("Up Down Partners", "20220823")



client()