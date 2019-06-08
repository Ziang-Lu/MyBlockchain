# Blockchain Simple Implementation

## Blockchain的哲学意义

Blockchain是一个优美的distrbuted DB, 使得<u>互相不信任的个体</u>间, 对某种状态机能够达到稳定的共识.

从而<u>不依靠任何"链下"中心化权威机构</u>, 制造了<u>对这个共同维护的状态机的高强度信任 ("链上"信任体)</u>.

=> **"链上"信任制造机**

<br>

## 区块链应用: 鹰? 猪? 鉴别三原则

1. 是否试图在区块链上<u>制造"链上信任体"</u>?

   途径:

   * 通过把"链下信任体" 区块化
   * 通过创建全新的信任体

   如果答案是否, 那么背后的本质依然是利用"链下信任体", 只是"链下信任体"把blockchain当做一个distributed DB使用, CRUD完全依然由"链下信任体"控制 => 没有利用blockchain的核心价值

2. <u>"链下信任体"是否可区块化</u>?

   即 被区块化的链下信任体的逻辑是否可以用客观程序逻辑表示?

   => 当"链下信任体"的功能设计复杂的主观判断逻辑, 而非简单的客观判断逻辑的时候, 区块化基本不可能完成

3. 区块化所带来的有点是否能抵消使用区块链所带来的代价?

   即 区块化净收益>0?

<br>

## 架构设计

Check out this great article: https://blog.csdn.net/hui_yong/article/details/81111088

<br>

## License

This repo is distributed under the <a href="https://github.com/Ziang-Lu/MyBlockchain/blob/master/LICENSE">MIT license</a>.

