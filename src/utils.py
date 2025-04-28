import os
from typing import List, Dict, Optional
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise EnvironmentError("YOUTUBE_API_KEY is required in environment variables.")

def get_youtube_service():
    """
    Returns an instance of the YouTube Data API client.
    """
    return build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def get_playlist_items(playlist_id: str, max_results: int = 300) -> List[str]:
    """
    指定したplaylist_idからvideo_id一覧を取得する。
    Returns a list of video IDs.
    """
    service = get_youtube_service()
    video_ids: List[str] = []
    next_page_token: Optional[str] = None
    while True:
        try:
            response = service.playlistItems().list(
                part="contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()
        except HttpError as e:
            raise RuntimeError(f"YouTube API error: {e}")
        for item in response.get("items", []):
            video_ids.append(item["contentDetails"]["videoId"])
            if len(video_ids) >= max_results:
                return video_ids
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    return video_ids

def get_video_meta(video_id: str) -> Dict[str, str]:
    """
    指定したvideo_idのメタデータ（title, publishedAt, duration, url）を取得する。
    Returns a dict with keys: video_id, title, published_at, duration, url
    """
    service = get_youtube_service()
    try:
        response = service.videos().list(
            part="snippet,contentDetails",
            id=video_id
        ).execute()
    except HttpError as e:
        raise RuntimeError(f"YouTube API error: {e}")
    items = response.get("items", [])
    if not items:
        raise ValueError(f"No metadata found for video_id: {video_id}")
    item = items[0]
    title = item["snippet"]["title"]
    published_at = item["snippet"]["publishedAt"]
    duration = item["contentDetails"]["duration"]
    url = f"https://www.youtube.com/watch?v={video_id}"
    return {
        "video_id": video_id,
        "title": title,
        "published_at": published_at,
        "duration": duration,
        "url": url,
    }
