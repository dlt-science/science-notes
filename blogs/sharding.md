# Sharding: A Panacea for Blockchain Scalability Challenges?
As the adoption of blockhain technology increases, scalability remains the central challenge and a major obstacle for blockchain to be adopted by mainstream industries. Bitcoin can only process 7 transactions per second (TPS), while the Ethereum blockchain can only process 15 TPS . Although, after the merger of Ethereum 1.0 and Ethereum 2.0, the TPS of Ethereum 2.0 is expected to reach 100,000 TPS, gas fees still remains a major issue. Ethereum has been relying on ZK-rollups to scale the network, but rollups are not a long-term solution. Therefore, the blockchain community is actively looking for a solution to the scalability problem.


`````{margin} **ZK-Rollups**
ZK-Rollups in Ethereum are a Layer 2 scaling solution that uses zero-knowledge proofs to bundle multiple transactions into a single proof on the main chain. This reduces on-chain data storage and gas costs while maintaining security. ZK-Rollups enable higher throughput, lower fees, and faster confirmations for Ethereum transactions, while preserving privacy and decentralization.
`````

## What is Sharding?
Sharding, originally a database design principle, is now being considered a promising solution to overcome the scalability challenges of blockchain systems. It is a scaling technique that divides the blockchain network into smaller partitions called shards. Each shard is responsible for processing a subset of transactions. This allows the blockchain to process more transactions in parallel, thereby increasing the throughput of the system.

There are 2 common techniques blockchains implement to improve throughput:
- Delegate all the computation to a small set of powerful nodes. (eg - Algorand, Solana)
- Each node in the network only do a subset of the total amount of work (Sharding). Ethereum, Near, Ziliqa use this technique.

```{note} **Sharding in Blockchains vs Traditional Databases**

The sharding techniques used in traditional databases cannot be directly applied to blockchains because of following reasons:
- Blockchains rely on Byzantine Fault Tolerance (BFT) consensus protocols which have been shown to be a scalability bottleneck.
- Distributed databases depend on highly available transaction coordinators for atomicity and isolation assurance; however, blockchain coordinators could potentially exhibit malicious behavior.
- In a distributed database, any node can belong to any shard, but a blockchain must assign nodes to shards in a secure manner to ensure that no shard can be compromised by the attacker.
```


There have been a few proposed sharded blockchains such as Elastico {cite}`luu2016secure`, OmniLedger {cite}`kokoris2018omniledger` and RapidChain {cite}`zamani2018rapidchain`. Nonetheless, such systems are predominantly constrained to cryptocurrency use cases in open (or permissionless) environments. Owing to their reliance on the unspent transaction output (UTXO) model—a simplistic data structure—these methods lack generalizability for applications beyond Bitcoin {cite}`dang2019towards`. So we will focus on more general purpose blockchains such as Ethereum and Near Blockchain.


## Different Sharding Approaches
We will discuss two different approaches to sharding by comparing the techniques used in Ethereum and Near Blockchain.

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
### Cross-Shard Communication
As the network gets divided up into multiple shards, it is important to ensure that the shards can communicate with each other to maintain consistency and interoperability. As seen in [{numref}`cross-sharding`], this can be problematic if there is forking within the shards and the block issuing the transaction is not included in the canonical chain. Both Near and Ethereum overcome this challenge by exchanging receipts between the shards. The receipts are used to prove that a transaction has been executed on a shard {cite}`nearruntimespec` and the corresponding transaction can be executed on the other shard.


```{figure} images/cross-shard.png
---
width: 350px
height: 230px
name: cross-sharding
---
Cross-Shard Communication
```

### Smart Contracts

## Conclusion
Whether sharding will be able to

## References

```{bibliography}
:filter: docname in docnames
```