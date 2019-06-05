#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Block definition module.
"""

__author__ = 'Ziang Lu'

import random
from multiprocessing import Queue

from block import Block


class Miner:
    """
    Miner class.
    """

    @staticmethod
    def _mined_valid_block(block: Block, difficulty: int) -> bool:
        """
        Private helper method to check whether the given mined block satisfies
        the criteria: the first difficulty number of characters are '0'.
        :param block: Block
        :param difficulty: int
        :return: bool
        """
        for i in range(difficulty):
            if block.hash[i] != '0':
                return False
        return True

    def mine(self, index: int, prev_hash: str, data: list,
             difficulty: int, q: Queue) -> None:
        """
        Mines a block at the given index of the given difficulty.
        :param index: int
        :param prev_hash: str
        :param data: list
        :param difficulty: int
        :param q: Queue
        """
        block = Block(index, prev_hash, data)
        block.set_nonce(random.randint(0, 99999))
        block.hash_block()
        while q.empty():
            if self._mined_valid_block(block, difficulty):
                q.put(block, block=False)
                break
            block.set_nonce(random.randint(0, 99999))
            block.hash_block()
