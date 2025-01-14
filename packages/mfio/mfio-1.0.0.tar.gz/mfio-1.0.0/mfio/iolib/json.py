# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Author:       yunhgu
# Date:         2023/8/3
# -------------------------------------------------------------------------------
from json import load
from .base import IO


class Json(IO):
    @classmethod
    def read(cls, path) -> dict:
        with open(path, mode='r', encoding="utf-8") as f:
            return load(f)

    @classmethod
    def write(cls, path, content):
        with open(path, mode="w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def name():
        """
        :return: string with name of geometry
        """
        return "json"
