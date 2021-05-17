import pytest
import tempfile
from pathlib import Path
from recipes_parser.utils.file_ops import save_json_to_file


class TestFileOps:
    def test_creating_sub_dirs(self):
        sub_dirs = 'channels/videos'
        with tempfile.TemporaryDirectory() as tmpdirname:
            path = Path(tmpdirname, sub_dirs, 'channel_res.json')
            save_json_to_file({}, path)
            assert Path(tmpdirname, sub_dirs).exists()

    def test_creating_non_json_suffixed_file(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            path = Path(tmpdirname, 'channel_res.txt')
            with pytest.raises(ValueError, match="Please provide a file with a \'.json\' suffix"):
                save_json_to_file({}, path)

