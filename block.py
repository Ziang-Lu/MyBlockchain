#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Block definition module.
"""

__author__ = 'Ziang Lu'

import hashlib
import pprint
from datetime import datetime

from typing import Any


class Block:
    """
    Block class on a blockchain.
    """
    __slots__ = ['_prev_hash', '_data', '_timestamp', '_hash']

    def __init__(self, prev_hash: str, data: list):
        """
        Constructor with parameter.
        :param prev_hash: str
        :param data: list
        """
        self._prev_hash = prev_hash
        self._data = data
        self._timestamp = datetime.now()
        self._hash = None

    def add_data(self, data_piece: Any) -> None:
        """
        Adds a piece of data to this block.
        :param data_piece: Any
        :return: None
        """
        self._data.append(data_piece)
        self._timestamp = datetime.now()

    def hash_block(self, nonce: int) -> None:
        """
        Hashes this block with the given nonce.
        :param nonce: int
        :return: None
        """
        content = f'{self._prev_hash}{self._data}{nonce}{self._timestamp}'
        sha256 = hashlib.sha256()
        sha256.update(str.encode(content))
        self._hash = sha256.hexdigest()

    @property
    def hash(self) -> str:
        """
        Accessor of hash.
        :return: str
        """
        return self._hash

    def print_block(self) -> None:
        """
        Prints this block.
        :return: None
        """
        pprint.pprint({
            'prev_hash': self._prev_hash,
            'data': self._data,
            'timestamp': self._timestamp,
            'hash': self._hash
        })
