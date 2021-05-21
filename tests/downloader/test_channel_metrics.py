import pytest

from datetime import datetime as dt

from recipes_parser.downloader.model.short_desc_video import ShortDescVideo


class TestChannelMetrics:
    def test_adding_channel_metrics(self, channel_result):
        channel_metrics = ChannelMetrics()
        metrics = channel_metrics.parse(channel_result)
        assert metrics == [MetricLong('channel.videos.found', 5),
                           MetricDate('channel.videos.date.max', dt(2021, 8, 9, 17, 0, 3)),
                           MetricDate('channel.videos.date.min', dt(2019, 12, 9, 17, 0, 2))]

    @pytest.fixture
    def channel_result(self):
        return [ShortDescVideo('video_id', '2019-12-09T17:00:02Z', 'title'),
                ShortDescVideo('video_id', '2019-12-09T17:00:02Z', 'title'),
                ShortDescVideo('video_id', '2020-12-09T17:00:02Z', 'title'),
                ShortDescVideo('video_id', '2020-12-09T17:00:02Z', 'title'),
                ShortDescVideo('video_id', '2021-08-09T17:00:03Z', 'title')]
