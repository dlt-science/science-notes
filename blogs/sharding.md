# Sharding: A Panacea for Blockchain Scalability Challenges?

<ins>**Innovation & Ideation**</ins>

```{admonition} Key Insights
:class: tip
- Sharding is a promising scaling technique for blockchains, dividing the network into smaller partitions called shards to process transactions in parallel, thus increasing throughput.
- Sharding approaches in blockchain systems vary, with solutions like Ethereum 2.0 using multiple shard chains coordinated by a beacon chain, and others, such as Near Protocol's Nightshade, opting for processing data chunks in a single blockchain with different validator sets.
- Sharding implementation faces challenges such as security, cross-shard communication, and data availability, which require solutions like random validator assignment, transaction receipts, and erasure coding.
- While sharding offers potential scalability improvements, layer 2 solutions like ZK-Rollups and Optimistic Rollups remain the preferred short-term scaling methods until sharding proves its ability to handle high transaction volumes.
```

As the adoption of blockhain technology increases, scalability remains the central challenge and a major obstacle for blockchain to be adopted by mainstream industries. Bitcoin can only process 7 transactions per second (TPS), while the Ethereum blockchain can only process 15 TPS . Although, after the merger of Ethereum 1.0 and Ethereum 2.0, the TPS of Ethereum 2.0 is expected to reach 100,000 TPS, gas fees still remains a major issue. Ethereum has been relying on ZK-rollups to scale the network, but rollups are not a long-term solution. Therefore, the blockchain community is actively looking for a solution to the scalability problem.


`````{margin} **ZK-Rollups**
ZK-Rollups in Ethereum are a Layer 2 scaling solution that uses zero-knowledge proofs to bundle multiple transactions into a single proof on the main chain. This reduces on-chain data storage and gas costs while maintaining security. ZK-Rollups enable higher throughput, lower fees, and faster confirmations for Ethereum transactions, while preserving privacy and decentralization.
`````

## What is Sharding?
Sharding, originally a database design principle, is now being considered a promising solution to overcome the scalability challenges of blockchain systems. It is a scaling technique that divides the blockchain network into smaller partitions called shards. Each shard is responsible for processing a subset of transactions. This allows the blockchain to process more transactions in parallel, thereby increasing the throughput of the system.

There are 2 common techniques blockchains implement to improve throughput:
- Delegate all the computation to a small set of powerful nodes. (eg - Algorand, Solana)
- Each node in the network only do a subset of the total amount of work (Sharding). Ethereum, [Near](https://near.org/), [Hedera](https://hedera.com/) use this technique.

```{note} **Sharding in Blockchains vs Traditional Databases**

The sharding techniques used in traditional databases cannot be directly applied to blockchains because of following reasons:
- Blockchains rely on Byzantine Fault Tolerance (BFT) consensus protocols which have been shown to be a scalability bottleneck.
- Distributed databases depend on highly available transaction coordinators for atomicity and isolation assurance; however, blockchain coordinators could potentially exhibit malicious behavior.
- In a distributed database, any node can belong to any shard, but a blockchain must assign nodes to shards in a secure manner to ensure that no shard can be compromised by the attacker.
```
## Different Sharding Approaches

Huang et. al. {cite}`huang2022brokerchain` proposed a new cross-shard blockchain protocol called BrokerChain that aims to address the issue of hot shards and reduce the number of cross-shard transactions and outperforms other state-of-the-art sharding methods in terms of transaction throughput, confirmation latency, queue size of transaction pool.
Tennakoon et. al. {cite}`tennakoon2022dynamic` propose a blockchain sharding protocl with dynamic sharding where
smart contract invocations stored in blocks reconfigure the sharding. This protocol is effective in the sense that it improves the efficiency of blockchain by preventing resource wastage by closing the shard that are not processig as many transactions or are idle.
There have been a few proposed sharded blockchains such as Elastico {cite}`luu2016secure`, OmniLedger {cite}`kokoris2018omniledger` and RapidChain {cite}`zamani2018rapidchain`. Nonetheless, such systems are predominantly constrained to cryptocurrency use cases in open (or permissionless) environments. Due to their reliance on the unspent transaction output (UTXO) model—a simplistic data structure—these methods lack generalizability for applications beyond Bitcoin {cite}`dang2019towards`. So we will focus on more general purpose blockchains such as Ethereum and Near Blockchain.

`````{margin} **Hot Shards**
Hot shards are shards that are experiencing a high volume of transactions, which can negatively impact the performance and security of the blockchain system.
`````

```{figure} images/sharding.png
---
width: 720px
height: 330px
name: sharding-eth-near
---
Sharding in Ethereum vs Near Blockchain
```

### Sharding in Ethereum
 In ethereum, data is distributed among several shard chains ([{numref}`sharding-eth-near`]) and each of these shard chains submit a record of transactions to the beacon chain or coordinating layer which coordinates and manages the shards by maintaining synchronization and ensuring a common ledger. The shards receive sets of transactions from the mining pool. Under the Ethereum 2.0 proposal, these TX are split based on their transaction types. Miners then use an EVM to process shards' data into a block and update the Merkle tree’s state on the beacon chain {cite}`kudzin2022scaling`.

### Sharding in Near Blockchain
Near's sharding technique is called "Nightshade" {cite}`near2020nightshade`. Although the full implementation is still in progress, the idea is instead having multiple subchains with a single beacon chain, data is divided into smaller partitions called chunks. Each chunk is processed by a different set of validators. The validators are randomly assigned to chunks and the assignment is done in a way that the same validator is not assigned to multiple chunks as shown in [{numref}`sharding-eth-near`]. At present the Near blockchain has 4 shards and the eventual plan is to have 100 shards {cite}`nearroadmap`.

## Sharding Challenges
The main issue with sharding is that it is extremely complicated to implement as it opens up possibilities of new attack vectors and security challenges. The following are some of the challenges that need to be addressed before sharding can be implemented in a blockchain system.

### Security
In a 10-shard system, each shard's security is reduced by a factor of 10 due to separate validator sets. Upon hard-forking a non-sharded chain with X validators into a sharded chain, each shard has X/10 validators. Consequently, compromising one shard necessitates corrupting only 5.1% (51% / 10) of the total validators. This is a significant reduction in security. To overcome this challenge, Ethereum uses a random beacon chain to assign validators to shards. Blockchains like Near and Algorand use Verifiable Random Functions (VRFs) to assign validators to shards. This ensures that the validators are randomly assigned to shards and the same validator is not assigned to multiple shards.

Hafid et. al. {cite}`hafid2022tractable` propose a Probabilistic Generating Function Analysis (PGFA) approach as an effective and tractable method to analyze the security of sharding-based blockchain protocols. They conclude that an increase in the number of Sybil IDs, network size, and ID Selection Pool(comprising of honest IDs and sybil IDs) size results in a higher failure probability, compromises network security which can lead to shard takeover atacks.

`````{margin} **VRF**
Verifiable Random Functions (VRFs) are a cryptographic primitive that allows a user to generate a random number that can be verified by anyone.
`````
### Cross-Shard Communication
As the network gets divided up into multiple shards, it is important to ensure that the shards can communicate with each other to maintain consistency and interoperability. As seen in [{numref}`cross-sharding`], this can be problematic if there is forking within the shards and the block issuing the transaction is not included in the canonical chain. Both Near and Ethereum overcome this challenge by exchanging receipts between the shards. The receipts are used to prove that a transaction has been executed on a shard {cite}`nearruntimespec` and the corresponding transaction can be executed on the other shard. In Hedera Blockchain which uses a gossip protocol to exchange information between shards, each shard maintains a queue of outgoing messages for other shards. Messages are sent from one shard to another through nodes randomly contacting each other, along with proof of consensus. The process continues until the receiving shard confirms message processing with an updated sequence number in its shared state {cite}`hederawhitepaper`. Instead of receipts, Hedera uses sequence number which is maintained by a shard for each other shard as a proof of latest execution message.

```{figure} images/cross-shard.png
---
width: 350px
height: 230px
name: cross-sharding
---
Cross-Shard Communication
```
### Data Availability
The data availability problem relates to the difficulty of ensuring that all necessary data for verifying a block's validity is accessible to all participants in the network. For instance, a light client does not have access to full block data, and thus cannot
verify the validaity of data. To overcome this problem, erasure coding is used to verify the validity of data. If the light client is able to retrieve a sufficient number of chunks of data, it can reconstruct the original data and verify the validity of the block. This approach is being currently used by Ethereum and Near.

`````{margin} **Erasure Codes**
Erasure codes allow a piece of data M chunks long to be expanded into a piece of data N chunks long ("chunks" can be of arbitrary size), such that any M of the N chunks can be used to recover the original data.
`````


## Conclusion
Sharding seems to be the most promising solution to overcome the scalability challenges of blockchain systems. Although Ethereum and Near have made significant progress in implementing sharding, it is still not time-tested and it remains to be seen whether these blockchains will be able to bear the load of transactions volume when scenarios such as [DeFi boom](https://www.forbes.com/sites/tatianakoffman/2020/08/31/defi-the-hot-new-crypto-trend-of-2020/?sh=5576a8a05bce) or [NFT craze](https://qz.com/1145833/cryptokitties-is-causing-ethereum-network-congestion) happen again. Until then, layer 2 solutions such as ZK-Rollups and Optimistic Rollups will continue to be the preferred scaling solutions for blockchain systems.

<div style="text-align: right;font-weight: bold;">Parshant Singh</div>
<div style="text-align: right;font-style: italic;">May 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```