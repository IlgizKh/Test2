from unittest import TestCase

from main import YaUploader

path = "test"
token = ""

class TestSummarize(TestCase):
    def setUp(self):
        self.ya = YaUploader(token)
    def test_upload_folder(self):
        self.assertEqual(self.ya.upload_folder(path), "True")