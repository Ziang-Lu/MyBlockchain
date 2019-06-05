#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Block definition module.
"""

__author__ = 'Ziang Lu'

import hashlib
import json
from datetime import datetime

from typing import Any


class Block:
    """
    Block class on a blockchain.
    """
    __slots__ = [
        '_index', '_prev_hash', '_data', '_difficulty', '_nonce', '_timestamp',
        '_hash'
    ]

    def __init__(self, index: int, prev_hash: str, data: list):
        """
        Constructor with parameter.
        :param index: int
        :param prev_hash: str
        :param data: list
        """
        self._index = index
        self._prev_hash = prev_hash
        self._data = data
        self._nonce = None
        self._timestamp = datetime.now()
        self._hash = None

    @property
    def hash(self) -> str:
        """
        Accessor of hash.
        :return: str
        """
        return self._hash

    def add_data(self, data_piece: Any) -> None:
        """
        Adds a piece of data to this block.
        :param data_piece: Any
        :return: None
        """
        self._data.append(data_piece)
        self._timestamp = datetime.now()

    def set_nonce(self, nonce: int) -> None:
        """
        Mutator of nonce.
        :param nonce: int
        :return: None
        """
        self._nonce = nonce

    def hash_block(self):
        """
        Hashes this block.
        """
        content = f'{self._prev_hash}{self._data}{self._nonce}{self._timestamp}'
        sha256 = hashlib.sha256()
        sha256.update(str.encode(content))
        self._hash = sha256.hexdigest()

    def __repr__(self):
        block_info = {
            'Index': self._index, 'Previous hash': self._prev_hash,
            'Data': self._data, 'Time': str(self._timestamp), 'Hash': self._hash
        }
        return json.dumps(block_info)
