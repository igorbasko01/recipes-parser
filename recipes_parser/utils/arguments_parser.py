import argparse


class ArgumentsParser(object):
    def __init__(self,
                 youtube_downloader_name,
                 ingredients_parser_name,
                 arguments=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('--settings-path', default='../settings.json')
        parser.add_argument('--download', dest='components', action='append_const', const=youtube_downloader_name)
        parser.add_argument('--parse', dest='components', action='append_const', const=ingredients_parser_name)
        self.args = parser.parse_args(arguments)
