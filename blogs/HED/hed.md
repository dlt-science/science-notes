# Understanding the Transactional Capabilities of Hedera Hashgraph

<!-- ![Industry Perspective](images/IP.svg) -->
<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- Hedera Hashgraph's unique protocol and algorithm ensure a fast, secure, and fair platform for real-time applications and services.
- The Hedera Consensus Service streamlines consensus processes, fostering trust and decentralization for various applications.
- Hedera Token Service streamlines tokenization, supporting secure asset conversion, and promoting interoperability.
- Hedera transaction fees are designed for specific network operations and are fixed in USD to maintain stability, thereby minimizing the effects of HBAR's price volatility on transaction costs. This design ensures a predictable and steady cost structure for network users.
```

## Introduction

<!-- = Briefly introduce Hedera Hashgraph, its mission, and its unique features. -->
Hedera Hashgraph is a distributed ledger technology designed to offer a secure, fair, and fast platform for a new generation of real-time applications and services {cite}`decentralization2023`. In the Hedera network, a user initiates a transaction, which is then quickly disseminated among nodes through an efficient "gossip" protocol. Nodes gossip messages to each other about transactions randomly. Consensus on transactions is achieved independently by nodes using a virtual voting algorithm, which calculates a consensus timestamp based on the median timestamp when the majority of nodes received the transaction. This mechanism ensures transaction fairness and security, as no single node can significantly manipulate the order, thereby providing resilience against malicious activities.

The transaction recording process using Hedera hashgraph and its benefits can be seen in {numref}`hed_diagram`.

```{figure} images/hashgraph.png
---
width: 733px
height: 400px
name: hed_diagram
---
Hedera Hashgraph Transaction Recording Process & Its Key Benefits.
```

Since Hedera Hashgraph launched in August 2018, it offers unique transactional capabilities through its native HBAR cryptocurrency, used both for network security and as fuel for network services. As a proof-of-stake network, HBARs help safeguard the network by representing voting power; thus, wider distribution of HBARs prevents potential attacks by making it prohibitively expensive for a malicious entity to control one-third of the coins. In addition, HBARs serve as fuel for network services, compensating nodes for providing computing resources, and ensuring low, stable transaction fees. For example, a cryptocurrency transfer currently costs USD $0.0001 (paid in HBARs) {cite}`consensus2019`.

## Hedera Cryptocurrency Service

Hedera hashgraph provides two distincet services related to digital assets: the Hedera cryptocurrency service and token service. The Cryptocurrency Service pertains specifically to the use of HBAR for transactions and fees on the network, while the Token Service provides a platform for users to create and manage their own custom tokens. Hedera's cryptocurrency is engineered for speed, resulting in minimal network fees and enabling feasible microtransactions. When Hedera is fully operational, every user will have the capability to manage a network node and receive cryptocurrency payments for this contribution. Creating an account simply requires generating a key pair, without any necessity for a linked name or address. However, users have the option to connect hashes of identity certificates from any third-party certificate or identity authority of their choice. This feature is designed to facilitate compliance with regulatory requirements in jurisdictions with Know Your Customer (KYC) or Anti-Money Laundering (AML) laws. Additional information is available in the section on Regulatory Compliance {cite}`Baird2020`.

## Fees Associated with Hedera Transactions

Hedera's network fees are designed for specific network operations. The fees are payable in HBAR, but are also fixed in USD for stability.

```{note} **HBAR Denominations and Abbreviations**

Hedera denominates HBAR into various units:

    1 gigabar (Gℏ) = 1 billion HBAR
    1 megabar (Mℏ) = 1 million HBAR 
    1 kilobar (Kℏ) = 1,000 HBAR 
    1 hbar (ℏ) = 1 HBAR 
    1 millibar (mℏ) = 0.001 HBAR 
    1 microbar (μℏ) = 0.000001 HBAR
    1 tinybar (tℏ) = 0.00000001 HBAR.

```

Fee structures for various operations are as follows:

- Cryptocurrency Service: The cost for creating a crypto account is $0.05, for auto-renewing an account is $0.00022, and for transferring cryptocurrency is $0.0001, amongst others.
- Consensus Service: Fees for creating a topic on the Consensus Service is $0.01, for updating a topic is $0.00022, and for submitting a message is $0.0001, etc.
- Token Service: The cost to create a token is $1.00, to update a token is $0.001, and to associate a token with an account is $0.05, amongst others.
- File Service: The fee for creating a file is $0.05, updating a file is $0.05, and deleting a file is $0.007, etc.
- Smart Contract Service: Fees for creating a contract is $1.0, updating a contract is $0.026, and making a contract call is $0.05, etc.

Exact service fees will be visible once finalized through the [pricing calculator](https://docs.hedera.com/hedera/networks/mainnet/fees). 

## Hedera Consensus Service

<!-- = Explain what the Hedera Consensus Service is and its role in the Hedera ecosystem. -->
The Hedera Consensus Service (HCS) is one of the core services offered by the Hedera public network. Its role is to offer a trust layer for any application or permissioned network that needs a decentralized and verifiable log of events. In simpler terms, HCS allows a group of participants to agree on the order and the exact time (to the second) that a series of transactions happened. This can be important in many different scenarios, such as tracking provenance across supply chains, logging asset transfers between blockchain networks, counting votes in a Decentralized Autonomous Organization (DAO), monitoring Internet of Things (IoT) devices, verifying the sequence of financial transactions, or ensuring fair gameplay in a multiplayer game {cite}`consensus2019`. HCS is a crucial part of the Hedera ecosystem as it enables decentralized applications and other systems to enjoy the benefits of decentralization, security, and fairness without having to handle the complexities of consensus on their own.
<!-- = Discuss the architecture of the Consensus Service, including how it's exposed via SDKs and the Hedera API (HAPI), and how applications can access the network services. -->
### Hedera Consensus Service Architecture
As the fourth core service offered by Hedera, HCS provides an essential underpinning for the platform's architecture. This service is exposed through a multitude of software development kits (SDKs) in popular programming languages, as well as the Hedera API (HAPI), which employs protobufs. Such design enables applications to interact with the network services using both high-level SDK abstractions and low-level APIs.

Conceptually, the HCS operates by allowing a client application to submit a byte string message tied to a specific topic (identified by an ID number). This message, encapsulating transactional information like a financial asset bid or a data hash, is processed upon payment of a transaction fee in HBARs, Hedera's native currency. Upon successful processing, the Hedera ledger delivers a record affirming consensus attainment, timestamp, sequence number for the event corresponding to the given topic, and a running hash reflecting all preceding messages related to that topic. Sequence numbers and running hashes are integral for applications to determine message order and verify message integrity, respectively.

The process of creating 'Topics' is simplified by a specific type of transaction made through the Hedera API, or HAPI. This transaction defines who owns the topic and who has permission to add or remove information from it, and it also provides a unique identification number for the topic. As expected, the Hedera Consensus Service is particularly useful for operators of mirror nodes and applications that deal with confidential information. These users need the advantages of a public ordering service, such as fast processing times, trust derived from decentralisation, and a permanent record of transactions.
### Configuration of Hedera Consensus Service
To configure this system, organisations need to create mirror nodes, program applications, and define unique keys that let authorised users monitor their activities. They also need to generate a unique 'topic' to identify relevant transactions. Each transaction created includes a message and topic, facilitated by the Hedera SDK. These transactions, which require a fee, can be sent to one or many mainnet nodes. The nodes then verify the transaction, confirm the payment of the transaction fee, and distribute its information across the network, thereby determining a consensus timestamp. Mirror nodes receive all data from the mainnet, including transaction details, consensus order, and timestamps. They can also create 'state proofs', providing a verifiable record of messages received for a topic, their order, and timestamps. These nodes run software that further processes transactions according to the application's business logic, producing application-specific results.

The system provides robust distribution via both the mirror and Hedera public networks. Users can obtain records from multiple mirror nodes and verify state proofs, ensuring mainnet agreement on transaction order and timestamp. Consequently, this architecture allows real-time auditing of mirror nodes and immediate validation of ordering and correct conclusions for any user running a mirror node.
<!-- = Discuss the benefits of the Consensus Service, such as fast, fair, secure, and decentralized consensus, reduced cost of operating private networks, improved trust model, and the potential for a network of interconnected applications. -->
### Benefits Hedera Consensus Service
Hedera's Consensus Service (HCS) offers a transformative solution to blockchain-based networks. It provides quick, fair, secure, and decentralized consensus, greatly enhancing the operational efficiency and trust model of private networks. By leveraging the hashgraph consensus algorithm, HCS settles transactions in seconds, ensuring fairness with its transparent, time-stamped process. It's a cost-effective solution, eliminating the high expenses of maintaining private networks while bolstering trust through its decentralized nature. The service also fosters a collaborative ecosystem, enabling interconnected applications. With HCS, Hedera sets the foundation for the next generation of decentralized applications (dApps), significantly bolstering the promise of distributed ledger technology.


## Hedera Token Service

<!-- = While the whitepaper does not explicitly mention the Hedera Token Service, you can discuss the general concept of tokenization on the Hedera network, and how it enables organizations and individuals to issue and trade tokens. -->
Hedera Hashgraph has revolutionized the process of tokenization, the method of converting tangible assets and ownership rights into digital tokens registered on a distributed ledger. Hedera Hashgraph addresses these needs through the introduction of the Hedera Token Service (HTS), providing two distinct models for token deployment {cite}`tokenization2020`. The HTS enables native token creation on the Hedera platform, storing information on the public Hedera ledger and offering pseudonymous privacy. This model is governed by the Hedera Governing Council and allows for limited customization.

On the other hand, the Hedera Consensus Service (HCS) allows for token creation on a permissioned network that benefits from public trust. In this model, storage occurs on a permissioned blockchain or database, and privacy levels can be public or encrypted. While this approach allows for custom governance and significantly more customization, including logic and roles, its distinguishing characteristic lies in its ability to combine the security and transparency of a public network with the control and flexibility of a private network.

### Benefits of Hedera Token Service

HTS offers a myriad of advantages for developers and businesses. With HTS, token deployment is uncomplicated and doesn't require any additional infrastructure. The service is cost-effective, facilitating token transfers at less than $0.01, making it ideal for various high-throughput use cases. In terms of performance, HTS enables thousands of transactions per second, with finality achieved within 3-5 second. It also ensures interoperability, allowing tokens to function seamlessly within the Hedera ecosystem and other distributed ledger networks. HTS tokens inherit the decentralized trust model of the Hedera network, ensuring transparent, verifiable transactions. Furthermore, the ease of integration with third-party services promotes adoption and liquidity for tokens issued on Hedera.

### Use Cases of Hedera's Tokenization Model

With these benefits, Hedera's tokenization model is capable of supporting a wide array of token use cases. Utility tokens offer the holder access to some product or service, while security tokens represent trading of value and must comply with relevant securities and other financial laws. Here's some key uses:

1. Financial Services: Tokenization can help in creating stablecoins, securities, and digital representations of financial assets like bonds, commodities, or stocks. This facilitates faster, more efficient trading and settlement.
2. Supply Chain: Tokens can be used to represent physical goods, tracking their movement, ownership, and provenance across a supply chain. This increases transparency and helps combat fraud and counterfeiting.
3. Real Estate: Fractional ownership of property can be enabled through tokenization, reducing barriers to entry and making real estate investment more accessible.
4. Art and Collectibles: Non-fungible tokens (NFTs) can represent unique pieces of art or collectibles, enabling proof of ownership, provenance tracking, and easier trading.
5. Decentralized Finance (DeFi): Tokenization forms the backbone of DeFi, enabling smart contract-driven financial products and services, such as lending platforms, decentralized exchanges, and yield farming.
6. Gaming: In-game assets can be tokenized to provide gamers with true ownership, enhancing the player economy and potentially creating cross-game compatibility for certain items.
7. Loyalty Programs: Businesses can tokenize loyalty rewards, making them more flexible, transferable, and potentially tradable.
8. Identity Verification: Personal identities can be tokenized to simplify and secure digital interactions, reducing fraud and enhancing user privacy.


## Hedera Smart Contract Service

Hedera's Smart Contract service revolutionizes the world of blockchain programming by introducing exceptional features that enhance performance, reduce costs, ensure security and fairness, and promote interoperability with Ethereum. The service allows the development of smart contracts using Solidity, a common language in Ethereum, simplifying the transition for developers familiar with Ethereum's ecosystem {cite}`Clarke2022`. The Besu EVM, tailored for the Hedera network and hashgraph consensus, enables high-speed transactions, predictable low fees, a negative carbon footprint, and exceptional performance with 15 million gas per second {cite}`Hedera`. By leveraging the hashgraph consensus algorithm, the service offers rapid transaction finality and optimizes contract execution, surpassing the capabilities of traditional block-based systems. It is designed to maintain low and predictable costs, significantly benefiting developers compared to Ethereum's fluctuating fees. The platform's robust security features and the governance of an esteemed council of industry leaders assure platform stability and continuous improvements. Furthermore, the service supports easy migration of existing Ethereum contracts to Hedera, showcasing its adaptability and convenience for developers.

```{seealso}
\
The full documentation for the Smart Contract service and a "Deploy Your First Smart Contract" tutorial [here](https://docs.hedera.com/hedera/tutorials/smart-contracts/deploy-a-contract-using-the-hedera-token-service).
Additionally, there's a code example below for creating a very first smart contract transaction on Hedera.
```javascript
{
....
//Create the transaction

const transaction = new ContractCreateTransaction()

    .setGas(100_000_000)
    .setBytecodeFileId(bytecodeFileId)
    .setAdminKey(adminKey);

//Modify the default max transaction fee (default: 1 hbar)

const modifyTransactionFee = transaction.setMaxTransactionFee(new Hbar(16));

//Sign the transaction with the client operator key and submit to a Hedera network

const txResponse = await modifyTransactionFee.execute(client);

//Get the receipt of the transaction

const receipt = await txResponse.getReceipt(client);

//Get the new contract ID

const newContractId = receipt.contractId;

console.log("The new contract ID is " +newContractId);
....
}
```

## Hedera File Service

Hedera Hashgraph's File Service provides a resilient, secure, and efficient system for data storage in a decentralized environment. It functions like a transaction graph, processing data in parallel and storing files across all network nodes in Merkle Trees and Merkle Directed Acyclic Graphs, ensuring tamper-proof, regionally accessible, and 100% available data. A unique feature is the provision of 'proof-of-deletion,' allowing businesses to comply with General Data Protection Regulations (GDPR) requirements. Files in the system have a set expiration date and are deleted automatically, while the storage service costs are based on the file size and the desired storage duration. Furthermore, Hedera offers controlled mutability via wACL keys, providing flexible data management and ensuring consensus for any changes. Transactions on Hedera are limited to 4KB, ensuring efficiency, although larger files can be accommodated through the appending of additional data. The service supports various transactions including creating, appending, deleting, and updating files, offering comprehensive and flexible options for developers and users. In essence, Hedera's File Service is a robust, secure, and efficient solution for decentralized data storage, embodying the low-cost and high-performative advantages of the platform {cite}`Wong2019`.

The architecture of Hedera's core services can be seen in {numref}`hed_service_diagram`.

```{figure} images/servicesarchitecture.png
---
width: 700px
height: 450px
name: hed_service_diagram
---
Architecture of Hedera's core service
```

## Conclusion

<!-- = Summarize the key points discussed in the blog.
= Discuss the potential impact of Hedera's transactional capabilities on the broader blockchain and DLT landscape. -->
Hedera Hashgraph has emerged as a pioneer in the realm of blockchain and Distributed Ledger Technology (DLT) by harnessing unique transactional capabilities. With its core services - the Hedera Consensus Service (HCS) and Hedera Token Service (HTS), it has profoundly altered how consensus and tokenization are handled in the DLT landscape.

The HCS leverages the hashgraph consensus algorithm for rapid, transparent, and secure transaction settlements. By reducing the cost and complexity of maintaining private networks, HCS improves their trust models and operational efficiency. Moreover, it lays the foundation for a network of interconnected applications, potentially revolutionizing the scope of decentralized applications. Simultaneously, the HTS enables straightforward tokenization on the Hedera network, with native token creation and flexible control mechanisms. The resulting tokens offers an array of benefits, such as cost-effectiveness, high performance, and ease of integration, making it a fitting choice for various high-throughput use cases.


<div style="text-align: right;font-weight: bold;">Ruoyi Zhao</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
