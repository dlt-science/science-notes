# Understanding the Transactional Capabilities of Hedera

<!-- ![Industry Perspective](images/IP.svg) -->
<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- Hedera's unique protocol and algorithm ensure a fast, secure, and fair platform for real-time applications and services.
- Hedera's native cryptocurrency, HBAR, bolsters network security and powers transactions at low, stable fees.
- Hedera's USD-fixed transaction fees, tailored for network operations, counteract HBAR price fluctuations to provide a stable and predictable cost framework for users.
- The Hedera Consensus Service streamlines consensus processes, fostering trust and decentralisation for various applications.
- The Hedera Token Service streamlines tokenisation, supporting secure asset conversion, and promoting interoperability.
```

## Introduction

 `````{margin} **Gossip about gossip**
  The "Gossip about Gossip" protocol is a fundamental part of the consensus algorithm, which disseminates transactions across network nodes through random information exchange, similar to social gossip. Beyond transaction data, this protocol also conveys the timeline and pathway of data propagation, enabling an efficient consensus on transaction order without a laborious proof-of-work process.
`````

<!-- = Briefly introduce Hedera, its mission, and its unique features. -->
Hedera is a distributed ledger technology designed to offer a secure, fair, and fast platform for a new generation of real-time applications and services {cite}`decentralization2023`. In the Hedera network, a user initiates a transaction, which is then quickly disseminated among nodes through an efficient "gossip" protocol. Nodes gossip messages to each other about transactions randomly. Consensus on transactions is achieved independently by nodes using a virtual voting algorithm, which calculates a consensus timestamp based on the median timestamp when the majority of nodes received the transaction. This mechanism ensures transaction fairness and security, as no single node can significantly manipulate the order, thereby providing resilience against malicious activities.

The transaction recording process using Hedera and its benefits can be seen in {numref}`hed_diagram`.

```{figure} images/hashgraph.png
---
width: 733px
height: 400px
name: hed_diagram
---
Hedera Transaction Recording Process & Its Key Benefits.
```

Since Hedera launched in August 2018, it offers unique transactional capabilities through its native HBAR cryptocurrency, used both for network security and as fuel for network services. As a proof-of-stake network, HBARs help safeguard the network by representing voting power; thus, wider distribution of HBARs prevents potential attacks by making it prohibitively expensive for a malicious entity to control one-third of the coins. In addition, HBARs serve as fuel for network services, compensating nodes for providing computing resources, and ensuring low, stable transaction fees. For example, a cryptocurrency transfer currently costs \$0.0001 (paid in HBARs) {cite}`consensus2019`.

## Hedera Cryptocurrency Service

Hedera provides two distinct services related to digital assets: the Hedera Cryptocurrency Service and Token Service. The Cryptocurrency Service pertains specifically to the use of HBAR for transactions and fees on the network, while the Token Service provides a platform for users to create and manage their own custom tokens. Hedera's cryptocurrency is engineered for speed, resulting in minimal network fees and enabling feasible micro-transactions. When Hedera is fully operational, every user will have the capability to manage a network node and receive cryptocurrency payments for this contribution. To create an account, all that is needed is to generate a key pair; there is no need for a linked name or address. However, users are given the flexibility to link hashes of identity credentials from any selected third-party certificate or identity authority. This function is purposefully constructed to aid in adhering to legal standards in regions enforcing Know Your Customer (KYC) or Anti-Money Laundering (AML) regulations. Further details can be found in the Regulatory Compliance section {cite}`Baird2020`.

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

- Cryptocurrency Service: The cost for creating a crypto account is \$0.05, for auto renewing an account is \$0.00022, and for transferring cryptocurrency is \$0.0001, amongst others.
- Consensus Service: Fees for creating a topic on the Consensus Service is \$0.01, for updating a topic is \$0.00022, and for submitting a message is \$0.0001, etc.
- Token Service: The cost to create a token is \$1.00, to update a token is \$0.001, and to associate a token with an account is \$0.05, amongst others.
- File Service: The fee for creating a file is \$0.05, updating a file is $0.05, and deleting a file is \$0.007, etc.
- Smart Contract Service: Fees for creating a contract are $1.0, for updating a contract are \$0.026, and for making a contract call are \$0.05, etc.

Exact service fees will be visible once finalized through the [pricing calculator](https://docs.hedera.com/hedera/networks/mainnet/fees). 

## Hedera Consensus Service

The Hedera Consensus Service (HCS) is an essential component of the Hedera network that provides a decentralised, secure, and verifiable log of events. It facilitates agreement on transaction order and timing across diverse applications, ranging from supply chains to multiplayer gaming. More than just a transactional ledger, HCS revolutionises the blockchain ecosystem by offering swift, fair, and decentralised consensus. Utilising the hashgraph consensus algorithm, HCS expedites transaction settlements, fostering transparency with a timestamped process. It not only bolsters efficiency and the trust model of private networks but also significantly reduces operational costs. Moreover, it promotes a collaborative environment for interconnected applications, paving the way for the next wave of decentralised applications{cite}`consensus2019`.

### HCS Architecture and Configuration

HCS is made accessible through various SDKs and the Hedera API (HAPI). It processes byte string messages from client applications tied to unique topics. These messages, carrying transactional details, are processed against a fee in HBARs, Hedera's native currency. Upon successful processing, the Hedera ledger returns a record with consensus details, timestamps, sequence numbers, and running hashes reflecting previous messages. To configure this service, organisations set up mirror nodes, program applications, and define unique keys and topics for transactions to configure HCS. After verification and confirmation of the transaction fee payment, the transaction information is disseminated across the network to establish a consensus timestamp. Mirror nodes receive this information, facilitating the creation of state proofs and further transaction processing. This configuration ensures robust record distribution and real-time auditing, fostering transparency and immediate validation of transaction order and accuracy.

## Hedera Token Service

The Hedera Token Service (HTS) enables native token creation on the Hedera platform, storing information on the public Hedera ledger and offering pseudonymous privacy. This model is governed by the Hedera Governing Council and allows for limited customisation {cite}`tokenization2020`. HTS makes token deployment straightforward and cost-effective, without the need for additional infrastructure. It can support high throughput applications with thousands of transactions per second, achieving transaction finality in 3-5 seconds. The interoperability of tokens across the Hedera ecosystem and decentralised trust model ensures transparent, verifiable transactions.

### Applications of Hedera's Tokenisation Model

Hedera's tokenisation model can support various token use cases {cite}`tokenization2020`. In financial services, it can facilitate efficient trading and settlement of assets like bonds, stocks, or commodities. Tokens can also track physical goods in supply chains, enable fractional ownership in real estate, represent unique art pieces as Non-fungible tokens, and form the backbone of Decentralised Finance. Other applications include tokenising in-game assets, loyalty rewards, and personal identities for enhanced security and user privacy.


## Hedera Smart Contract Service

Hedera's Smart Contract Service revolutionises the world of blockchain programming by introducing exceptional features that enhance performance, reduce costs, ensure security and fairness, and promote interoperability with Ethereum. The service allows the development of smart contracts using Solidity, a common language in Ethereum, simplifying the transition for developers familiar with Ethereum's ecosystem {cite}`Clarke2022`. The Besu EVM, tailored for the Hedera network and hashgraph consensus, enables high-speed transactions, predictable low fees, a negative carbon footprint, and exceptional performance with 15 million gas per second {cite}`Hedera`. By leveraging the hashgraph consensus algorithm, the service offers rapid transaction finality and optimises contract execution, surpassing the capabilities of traditional block-based systems. It is designed to maintain low and predictable costs, significantly benefiting developers compared to Ethereum's fluctuating fees. The platform's robust security features and the governance of an esteemed council of industry leaders assure platform stability and continuous improvements. Furthermore, the service supports easy migration of existing Ethereum contracts to Hedera, showcasing its adaptability and convenience for developers.

```{seealso}
\
The full documentation for the Smart Contract Service and a "Deploy Your First Smart Contract" tutorial [here](https://docs.hedera.com/hedera/tutorials/smart-contracts/deploy-a-contract-using-the-hedera-token-service).
Additionally, a JavaScript code snippet is provided below for creating a very first smart contract transaction on Hedera.
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

 `````{margin} **Merkle Directed Acyclic Graph**
  Merkle DAG is a unique form of DAG where each node is identified by a cryptographic hash, composed of the node's content and the identifiers of its children nodes. They are self-verifying structures, immutable by nature, and constructed from the leaves up, meaning children nodes are added before their parents, with each node essentially serving as the root of its own sub-Merkle DAG.
`````
Hedera's File Service provides a resilient, secure, and efficient system for data storage in a decentralised environment. It functions like a transaction graph, processing data in parallel and storing files across all network nodes in Merkle Trees and Merkle Directed Acyclic Graphs, ensuring tamper-proof, regionally accessible, and 100% available data. A unique feature is the provision of 'proof-of-deletion,' allowing businesses to comply with General Data Protection Regulations (GDPR) requirements. Files in the system have a set expiration date and are deleted automatically, while the storage service costs are based on the file size and the desired storage duration. Furthermore, Hedera offers controlled mutability via WACL(WriteAccess Control) keys, providing flexible data management and ensuring consensus for any changes. Transactions on Hedera are limited to 4KB, ensuring efficiency, although larger files can be accommodated through the appending of additional data. The service supports various transactions including creating, appending, deleting, and updating files, offering comprehensive and flexible options for developers and users. In essence, Hedera's File Service is a robust, secure, and efficient solution for decentralised data storage, embodying the low-cost and high-performance advantages of the platform {cite}`Wong2019`.

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
Hedera has emerged as a pioneer in the realm of blockchain and Distributed Ledger Technology (DLT), leveraging unique transactional capabilities. It has significantly transformed the DLT landscape through its core services such as the Hedera Cryptocurrency Service, Hedera Consensus Service, Hedera Token Service, Smart Contract Service, and File Service, altering the handling of consensus and tokenisation. The advanced transactional capabilities of Hedera, coupled with its suite of innovative services, position it as a substantial disruptor in the blockchain and DLT arena. Its commitment to cost-effectiveness, high performance, secure operations, and transparency has the potential to redefine how businesses and individuals interact with distributed ledger technology, thus paving the way for the next wave of decentralised applications.


<div style="text-align: right;font-weight: bold;">Ruoyi Zhao</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
