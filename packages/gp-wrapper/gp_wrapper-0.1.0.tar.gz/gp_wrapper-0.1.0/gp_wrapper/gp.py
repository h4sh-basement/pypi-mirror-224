from typing import Optional, Generator, Iterable
import requests
from requests.models import Response
from google.oauth2.credentials import Credentials  # type:ignore
from google_auth_oauthlib.flow import InstalledAppFlow  # type:ignore
# from googleapiclient.discovery import Resource  # type:ignore
# import googleapiclient.discovery  # type:ignore
from .media_item import GooglePhotosMediaItem
from .album import GooglePhotosAlbum
from .utils import UploadToken, Url, Path, declare, split_iterable

SCOPES = [
    'https://www.googleapis.com/auth/photoslibrary',
    "https://www.googleapis.com/auth/photoslibrary.appendonly",
    "https://www.googleapis.com/auth/photoslibrary.sharing"
]
EMPTY_PROMPT_MESSAGE = ""


class GooglePhotos:
    """A wrapper class over GooglePhotos API to get 
    higher level abstraction for easy use
    """
    ALBUMS_ENDPOINT = "https://photoslibrary.googleapis.com/v1/albums"
    UPLOAD_MEDIA_ITEM_ENDPOINT = "https://photoslibrary.googleapis.com/v1/uploads"
    CREATE_ENDPOINT = "https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate"

    @declare("Initializing Google Photos service")
    def __init__(self, client_secrets_path: str = "./client_secrets.json") -> None:
        flow: InstalledAppFlow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, SCOPES)  # noqa
        self.credentials: Credentials = flow.run_local_server(
            port=0,
            authorization_prompt_message=EMPTY_PROMPT_MESSAGE
        )
        self.session = requests.Session()
        self.session.credentials = self.credentials  # type:ignore

    def get(self, endpoint: Url, *args, **kwargs) -> Response:
        """wrapper function to create general purpose GET request with the current session

        Args:
            endpoint (Url): the endpoint to call

        Returns:
            Response: the response of the request
        """
        return self.session.get(endpoint, *args, **kwargs)

    def post(self, endpoint: Url, *args, **kwargs) -> Response:
        """wrapper function to create general purpose POST request with the current session

        Args:
            endpoint (Url): the endpoint to call

        Returns:
            Response: the response of the request
        """
        return self.session.post(endpoint, *args, **kwargs)

    def _construct_headers(self, additional_headers: Optional[dict] = None) -> dict:
        BASE_HEADERS: dict = {
            "Authorization": f"Bearer {self.credentials.token}"}
        res = dict(BASE_HEADERS)
        if additional_headers is not None:
            res.update(additional_headers)
        return res

    def json_headers(self) -> dict:
        return self._construct_headers({"Content-Type": "application/json"})

    @declare("Creating an Album")
    def create_album(self, album_name: str) -> GooglePhotosAlbum:
        headers = self.json_headers()
        payload = {
            "album": {
                "title": album_name
            }
        }
        response = self.post(
            GooglePhotos.ALBUMS_ENDPOINT,
            json=payload,
            headers=headers
        )
        dct = response.json()
        album = GooglePhotosAlbum(
            self,
            id=dct["id"],
            title=dct["title"],
            productUrl=dct["productUrl"],
            isWriteable=dct["isWriteable"],
            mediaItemsCount=0,
            coverPhotoBaseUrl="",
            coverPhotoMediaItemId=""
        )
        return album

    @declare("Getting all Albums")
    def get_albums(self) -> Generator[GooglePhotosAlbum, None, None]:
        headers = self._construct_headers()

        response = self.get(
            GooglePhotos.ALBUMS_ENDPOINT,
            headers=headers
        )
        albums_data = response.json().get('albums', [])
        for dct in albums_data:
            yield GooglePhotosAlbum(
                self,
                id=dct["id"],
                title=dct["title"],
                productUrl=dct["productUrl"],
                isWriteable=dct["isWriteable"],
                mediaItemsCount=dct["mediaItemsCount"] if "mediaItemsCount" in dct else 0,
                coverPhotoBaseUrl=dct["coverPhotoBaseUrl"],
                coverPhotoMediaItemId=dct["coverPhotoMediaItemId"] if "coverPhotoMediaItemId" in dct else "",
            )

    @declare
    def _upload_media_item(self, media_path: Path) -> UploadToken:
        headers = self.json_headers()
        image_data = open(media_path, 'rb').read()
        response = self.post(
            GooglePhotos.UPLOAD_MEDIA_ITEM_ENDPOINT,
            data=image_data,
            headers=headers
        )
        token = response.content.decode('utf-8')
        return token

    @declare
    def _get_media_item_id(self, upload_token: UploadToken) -> GooglePhotosMediaItem:
        headers = self._construct_headers()
        create_payload = {
            "newMediaItems": [
                {
                    "simpleMediaItem": {
                        "uploadToken": upload_token
                    }
                }
            ]
        }
        response = self.post(
            GooglePhotos.CREATE_ENDPOINT,
            json=create_payload,
            headers=headers
        )
        dct = response.json()['newMediaItemResults'][0]['mediaItem']
        return GooglePhotosMediaItem(
            self,
            id=dct["id"],
            productUrl=dct["productUrl"],
            mimeType=dct["mimeType"],
            mediaMetadata=dct["mediaMetadata"],
            filename=dct["filename"],
        )

    @declare("Uploading media to Album")
    def upload_media(self, album: GooglePhotosAlbum, media_path: Path) -> dict:
        """uploads a single image into an album

        Args:
            album (GooglePhotosAlbum): the album wrapper object
            media_path (Path): the path to the image

        Returns:
            dict: the result of the request. empty dict means success
        """
        media = self._get_media_item_id(self._upload_media_item(media_path))
        endpoint = f"https://photoslibrary.googleapis.com/v1/albums/{album.id}:batchAddMediaItems"
        headers = self._construct_headers()
        response = self.post(
            endpoint, headers=headers,
            json={
                "mediaItemIds": [media.id]
            }
        )
        return response.json()

    @declare("Uploading images in batches")
    def upload_media_batch(self, album: GooglePhotosAlbum, paths: Iterable[Path]) -> Iterable[Response]:
        """uploads media in batches of 50 images at once

        Args:
            album (GooglePhotosAlbum): the album wrapper object
            paths (Iterable[Path]): the iterable which has the paths to the media

        Yields:
            Generator[dict, None, None]: yields the results of each batch request. empty dict means success
        """
        MAX_SIZE: int = 50
        endpoint = f"https://photoslibrary.googleapis.com/v1/albums/{album.id}:batchAddMediaItems"
        responses = []
        for batch in split_iterable(paths, MAX_SIZE):
            media_ids = []
            for path in batch:
                media = self._get_media_item_id(
                    self._upload_media_item(path))
                media_ids.append(media.id)
            headers = self._construct_headers()
            response = self.post(
                endpoint, headers=headers,
                json={
                    "mediaItemIds": media_ids
                }
            )
            responses.append(response)
        return responses

    # def delete_album(self, album: GooglePhotosAlbum) -> Response:
    #     raise NotImplementedError(
    #         "The Google API does not support deleting albums")
    #     ALBUM_DELETE_ENDPOINT = f"https://photoslibrary.googleapis.com/v1/albums/{album.id}"
    #     headers = self.json_headers()
    #     response = self.session.delete(ALBUM_DELETE_ENDPOINT, headers=headers)
    #     return response


__all__ = [
    "GooglePhotos"
]
