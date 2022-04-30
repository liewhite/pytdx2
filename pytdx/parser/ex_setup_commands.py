# coding=utf-8

from pytdx.parser.base import BaseParser
from pytdx.helper import get_datetime, get_volume, get_price
from collections import OrderedDict
import struct


class ExSetupCmd1(BaseParser):

    def setup(self):
        self.send_pkg = bytearray.fromhex("010148650001520052005424e5bb1c2fafe525941f32c6e5d53dfb415b734cc9cdbf0ac92021bfdd1eb06d22da3bfcac1354076b3092c4f924cfd2d31f32c6e5d53dfb411f32c6e5d53dfb4124288302ea5fc63df443512c51847720")

    def parseResponse(self, body_buf):
        pass