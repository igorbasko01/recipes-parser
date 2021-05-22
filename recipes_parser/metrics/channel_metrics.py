from typing import List
from datetime import datetime as dt
from recipes_parser.downloader.model.short_desc_video import ShortDescVideo
from recipes_parser.metrics.model.metrics import MetricDate, MetricLong


class ChannelMetrics:
    def parse(self, channel_results: List[ShortDescVideo]):
        max_published = None
        min_published = None
        count = 0
        for result in channel_results:
            published = self._str2date(result.published_at)
            max_published = published if max_published is None or published > max_published else max_published
            min_published = published if min_published is None or published < min_published else min_published
            count += 1
        return self._create_metrics(max_published, min_published, count)

    @staticmethod
    def _str2date(str_date: str) -> dt:
        return dt.strptime(str_date, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def _create_metrics(max_published: dt, min_published: dt, count: int):
        return [
            MetricLong('channel.videos.found', count),
            MetricDate('channel.videos.date.max', max_published),
            MetricDate('channel.videos.date.min', min_published)
        ]
