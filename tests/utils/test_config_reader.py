from recipes_parser.utils.config_reader import ConfigReader


class TestConfigReader:
    def test_reading_file(self):
        config_reader = ConfigReader('../resources/settings-test.json')
        assert config_reader.settings['google-api-key'] == 'somekey'
