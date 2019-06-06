#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Blockchain module.
"""

__author__ = 'Ziang Lu'

import json
import random
from multiprocessing import Process, Queue
from string import ascii_letters, digits

from block import Block
from mining import Miner


class BlockChain:
    """
    Blockchain class.
    """
    __slots__ = ['_chain', '_miners']

    _DIFFICULTY = 4
    # By setting difficulty = 4, we get around 1~2 seconds between generating
    # two valid blocks.

    @staticmethod
    def _gen_transaction() -> str:
        """
        Private helper method to randomly generates a transaction.
        :return: str
        """
        transaction = {
            'sender': ''.join(random.sample(ascii_letters + digits, 8)),
            'recipient': ''.join(random.sample(ascii_letters + digits, 8)),
            'amount': random.randint(100, 1000)
        }
        return json.dumps(transaction)

    def __init__(self):
        """
        Default constructor.
        """
        self._chain = []
        self.gen_block(genesis=True)

        # Set 6 miners
        self._miners = [Miner() for _ in range(6)]

    def gen_block(self, genesis=False) -> None:
        """
        Generates the next block and adds it to the chain.
        :param genesis: bool
        :return: None
        """
        if genesis:
            genesis_block = Block(index=0, prev_hash='0', data=[])
            genesis_block.hash_block()
            self._chain.append(genesis_block)
            return

        index = len(self._chain)
        prev_hash = self._chain[-1].hash
        transaction = self._gen_transaction()
        # Let the miners start mining
        processes = []
        result_q = Queue()
        for miner in self._miners:
            th = Process(
                target=miner.mine,
                args=(
                    index, prev_hash, [transaction], self._DIFFICULTY, result_q
                )
            )
            processes.append(th)
        for p in processes:
            p.start()
        for p in processes:
            p.join()

        new_block = result_q.get(block=False)
        self._chain.append(new_block)
        print(new_block)


if __name__ == '__main__':
    block_chain = BlockChain()
    for _ in range(10):
        block_chain.gen_block()
