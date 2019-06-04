#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Blockchain driver module.
"""

__author__ = 'Ziang Lu'

import random
from datetime import datetime
from typing import Any

from block import Block


def create_genesis_block() -> Block:
    """
    Creates the genesis block.
    :return: Block
    """
    return Block(
        index=0, prev_hash='None', data='Genesis Block',
        timestamp=datetime.now()
    )


def get_next_block(prev_block: Block, data: Any) -> Block:
    """
    Gets the next block from the given previous block.
    :param prev_block: Block
    :param data: Any
    :return: Block
    """
    index = prev_block.index + 1
    prev_hash = prev_block.hash
    return Block(index, prev_hash, data, timestamp=datetime.now())


def main():
    # Initialization
    blockchain = [create_genesis_block()]
    prev_block = blockchain[0]

    num_of_blocks_to_add = 20

    for _ in range(num_of_blocks_to_add):
        block_to_add = get_next_block(
            prev_block, f'Transaction {random.randint(100, 200)} BitCoins'
        )
        blockchain.append(block_to_add)
        print(f'Block #{block_to_add.index} has been added to the chain!')
        print(block_to_add)

        prev_block = block_to_add


if __name__ == '__main__':
    main()
