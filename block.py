#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Block definition module.
"""

__author__ = 'Ziang Lu'

import hashlib
from datetime import datetime

from typing import Any


class Block:
    """
    Data block.
    """
    __slots__ = ['_index', '_prev_hash', '_data', '_timestamp', '_hash']

    def __init__(self, index: int, prev_hash: str, data: Any,
                 timestamp: datetime):
        """
        Constructor with parameter.
        :param index: int
        :param prev_hash: str
        :param data: Any
        :param timestamp: datetime
        """
        self._index = index
        self._prev_hash = prev_hash
        self._data = data
        self._timestamp = timestamp
        self._hash = self._hash_block()

    def _hash_block(self) -> str:
        """
        Private helper method to hash this block.
        :return: str
        """
        content = f'{self._index}{self._prev_hash}{self._data}{self._timestamp}'
        sha256 = hashlib.sha256()
        sha256.update(str.encode(content))
        return sha256.hexdigest()

    @property
    def index(self) -> int:
        """
        Accessor of index.
        :return: int
        """
        return self._index

    @property
    def hash(self) -> str:
        """
        Accessor of hash.
        :return: str
        """
        return self._hash

    def __repr__(self):
        s = f'Block #{self._index}:\n'
        s += f'Previous hash: {self._prev_hash}\n'
        s += f'Data: {self._data}\n'
        s += f'Time: {self._timestamp}\n'
        s += f'Hash: {self._hash}\n'
        return s
