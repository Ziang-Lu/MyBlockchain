#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Miner definition module.
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

    def mine(self, prev_hash: str, data: list, difficulty: int,
             q: Queue) -> None:
        """
        Mines a block at the given index of the given difficulty.
        :param prev_hash: str
        :param data: list
        :param difficulty: int
        :param q: Queue
        :return: None
        """
        block = Block(prev_hash, data)
        block.hash_block(nonce=random.randint(0, 99999))
        while q.empty():
            if self._mined_valid_block(block, difficulty):
                q.put(block, block=False)
                # Non-blocking
                # i.e., As soon as one miner mines a valid block, the others
                # don't wait.
                break
            block.hash_block(nonce=random.randint(0, 99999))
