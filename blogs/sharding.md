# Sharding: A Panacea for Blockchain Scalability Challenges?
As the adoption of blockhain technology increases, scalability remains the central challenge and a major obstacle for blockchain to be adopted by mainstream industries. Bitcoin can only process 7 transactions per second (TPS), while the Ethereum blockchain can only process 15 TPS . Although, after the merger of Ethereum 1.0 and Ethereum 2.0, the TPS of Ethereum 2.0 is expected to reach 100,000 TPS, gas fees still remains a major issue. Ethereum has been relying on ZK-rollups to scale the network, but rollups are not a long-term solution. Therefore, the blockchain community is actively looking for a solution to the scalability problem.


`````{margin} **ZK-Rollups**
ZK-Rollups in Ethereum are a Layer 2 scaling solution that uses zero-knowledge proofs to bundle multiple transactions into a single proof on the main chain. This reduces on-chain data storage and gas costs while maintaining security. ZK-Rollups enable higher throughput, lower fees, and faster confirmations for Ethereum transactions, while preserving privacy and decentralization.
`````

## What is Sharding?
Sharding, originally a database design principle, is now being considered a promising solution to overcome the scalability challenges of blockchain systems. Sharding is a scaling technique that divides the blockchain network into smaller partitions called shards. Each shard is responsible for processing a subset of transactions. This allows the blockchain to process more transactions in parallel, thereby increasing the throughput of the system.

There are 2 common techniques blockchains implement to improve throughput:
- Delegate all the computation to a small set of powerful nodes. (eg - Algorand, Solana)
- Each node in the network only do a subset of the total amount of work. This is called Sharding (eg - Ethereum, Near, Ziliqa).

Traditional
databases assume the crash-failure model, in which a faulty
node simply stops sending and responding to requests. On
the other hand, blockchain systems operate in a more hostile
environment, therefore they assume a stronger failure model,
namely Byzantine failure, to account for malicious attackers

First, high-performance consensus protocols used in distributed databases [29, 41], cannot be applied to blockchains.
Instead, blockchains rely on Byzantine Fault Tolerance (BFT)
consensus protocols which have been shown to be a scalability bottleneck [21].
Thus, the first challenge is to scale BFT
consensus protocols. Second, in a distributed database any
node can belong to any shard, but a blockchain must assign
nodes to shards in a secure manner to ensure that no shard
can be compromised by the attacker. The second challenge,
therefore, is to achieve secure and efficient shard formation.
Third, the distributed database relies on highly available
transaction coordinators to ensure atomicity and isolation,
but coordinators in the blockchain may be malicious. Consequently, the third challenge is to enable secure distributed
transactions even when the coordinator is malicious

Examples of
sharded blockchains include Elastico [33], OmniLedger [27]
and RapidChain [47]. These systems, however, are limited to
cryptocurrency applications in an open (or permissionless)
setting. Since they focus on a simple data model, namely the
unspent transaction output (UTXO) model, these approaches
do not generalize to applications beyond Bitcoin.


## Different Sharding Approaches
We will discuss two different approaches to sharding by comparing the techniques used in Ethereum and Near Blockchain.

```{figure} images/sharding.png
---
width: 720px
height: 330px
name: sharding
---
Sharding in Ethereum vs Near Blockchain
```

### Sharding in Ethereum

### Sharding in Near Blockchain


## Sharding Challenges

### Security
### Cross-Shard Communication
```{figure} images/cross-shard.png
---
width: 350px
height: 230px
name: sharding
---
Cross-Shard Communication
```

## Conclusion
Whether sharding will be able to