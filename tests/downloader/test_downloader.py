import json
from recipes_parser.downloader.youtube_description_downloader import YoutubeDownloader


class TestDownloader:
    def test_parse_channel_response(self):
        with open('../resources/sample_channel_response.json', 'r') as f:
            response = json.load(f)
        downloader = YoutubeDownloader("somekey")
        videos = downloader.extract_video_ids(response)
        assert len(videos) == 5
        assert videos[0] == 'DUDKIcYltZA'
