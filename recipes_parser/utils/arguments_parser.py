import argparse


class ArgumentsParser(object):
    def __init__(self,
                 extract_name,
                 transform_name,
                 load_name,
                 arguments=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('--settings-path', default='../settings.json')
        parser.add_argument('--extract', dest='components', action='append_const', const=extract_name)
        parser.add_argument('--transform', dest='components', action='append_const', const=transform_name)
        parser.add_argument('--load', dest='components', action='append_const', const=load_name)
        self.args = parser.parse_args(arguments)
