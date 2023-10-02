# The Symbiotic Relationship between Blockchain and Artificial Intelligence

<ins>**Innovation & Ideation**</ins>

```{admonition} Key Insights
:class: tip
- Blockchain and AI are fundamentally different - the former is decentralized, transparent, and deterministic, while the latter functions within centralized systems and relies on probabilistic computations.
- Despite their differences, they can empower each other, with blockchain addressing some of AI's shortcomings like privacy and control of data, while AI can enhance blockchain systems' efficiency, security, and effectiveness.
- Blockchain for AI involves using blockchain to promote data sharing, provide transparency, enable secure data marketplaces, foster decentralized AI architectures, and enhance swarm systems.
- AI for Blockchain suggests AI can augment smart contract capabilities and optimize the blockchain mining process.
- AI with Blockchain refers to applications that use both technologies in synergy, creating novel applications like enhancing human resources management, securing collaborative recommender systems, and automating process in SMEs with IoT data.
- However, the convergence of AI and blockchain faces challenges like scalability, security and privacy, and the data collaboration between on-chain and off-chain storage.
```

## Introduction

Artificial intelligence and blockchain are two progressive technologies that hold great potential in stimulating the intelligent evolution of various industries. Each possesses inherent strengths but also faces its own unique challenges. AI is gradually transforming industries by introducing advanced capabilities but struggles with issues such as interpretability and effectiveness. It operates based on three key elements: algorithms, computational power, and data {cite}`zhang2021recent`. On the other hand, blockchain, despite being an advantageous foundation for trustworthy transactions, grapples with hurdles concerning energy consumption, scalability, security, privacy, and efficiency {cite}`zhang2021recent`. Despite these separate research directions and associated challenges, AI and blockchain exhibit a natural synergy due to shared requirements for data analysis, security, and trust. This intersection between the two technologies can significantly amplify their respective strengths. According to the estimations of Spherical Insights, the Blockchain AI Market, valued at USD 230.10 million in 2021, is projected to grow to USD 980.70 million by 2030 {cite}`sphericalinsights2022blockchain`. The merger of these two technologies is an area that still calls for in-depth exploration. Moving forward, we'll examine AI in the context of blockchain, investigating in detail the possible intersections and inherent value these two technologies may possess when coalesced.


## Technology Explianed

`````{margin} **Proof of Work**
PoW involves nodes competing for bookkeeping rights by comparing computing power.
`````
`````{margin} **Proof of Stake**
PoS is where the length and amount of digital currency held increases the likelihood of obtaining bookkeeping rights and rewards.
`````
`````{margin} **Delegated Proof of Stake**
DPoS indicating where representative nodes are selected for proxy verification and accounting
`````

### Blockchain Technology
Blockchain can be conceptualized as an unalterable, collectively maintained digital register that facilitates instantaneous, transparent, and collaborative data exchange via encrypted transactions initiated and completed by multiple parties. The capability of Blockchain networks extends to the tracking of an assortment of operations, encompassing order processing, financial transactions, account management, and manufacturing procedures. As the authorized members have a unified view of the facts, they accrue a sense of trust and assurance in engaging in transactions with fellow businesses. This, in turn, augments operational efficiency and engenders the emergence of novel business opportunities.

The concept of blockchain is grounded in four core technologies {cite}`zhang2021recent`: consensus mechanism, data structure, cryptography, and distributed storage. The consensus mechanism encourages nodes to keep accounts; common mechanisms include proof of work (PoW), proof of stake (PoS), and delegated proof of stake (DPoS). The data structure of the blockchain resembles a chain, linking each block via a hash pointer in the block header, creating an interconnected chain. The use of cryptography, specifically symmetric and asymmetric encryption, provides confidentiality, integrity, and authentication to ensure the security of transactions, while the distributed storage mechanism prevents data tampering by requiring consensus from a majority of nodes. The emerging cross-chain technology aims to enable blockchain interconnection and enhance scalability, enabling operations like digital asset transfer and communication between chains.

### AI Technology
As mentioned in the literature review by Karger {cite}`inproceedings`, artificial intelligence technology was sparked by the introduction of machine learning in 1959 and was further driven by focused research in the USA and Japan during the '80s and '90s. Breakthroughs in deep learning and reinforcement learning algorithms, along with the rapid growth of network data and significant advances in computing power, have propelled AI's development. Key AI technologies such as natural language processing, adaptive learning, and computational vision already have vast applications in various industries. Recently, the advent of ChatGPT seems to push human society toward the technological point of singularity.

As a dominant power in the technological realm, artificial intelligence (AI) has introduced an array of benefits and conveniences into our daily lives. Yet, it's impossible to turn a blind eye to the accompanying risks and challenges that AI brings along. Some of these potential threats could be significant enough to impact the future trajectory of humanity. Recently, a notable development that has sparked further contemplation on the growth and inherent risks of AI is the departure of Geoffrey Hinton from Google. His unexpected move away from Google prompts us to scrutinize the future of AI more closely, raising questions about the direction AI research might take, the potential risks associated with the rapid advancement of this technology, and the measures we need to adopt for responsible AI development and usage.


## The mutual empowerment between blockchain and AI technology
Rohan Pinto, the CTO of 1Kosmos BlockID, with over two decades of experience in the field of cryptography, has shed light on the fundamental contrasts between AI and blockchain {cite}`pinto2018next`:

1.	AI largely functions within centralized systems, in contrast to blockchain that is rooted in a decentralized and distributed environment.
2.	Where most AI technologies are under the ownership and operation of centralized organizations, most blockchain advocates opt for open-source codebases, enabling anyone to review and inspect their codes freely.
3.	AI is often perceived as a 'black-box' approach in its current form, whereas blockchain provides clear visibility into each transaction it processes.
4.	AI is built on the basis of probabilistic computations, while blockchain is guided by a more deterministic methodology.

Nevertheless, He also pointed out that the centralized AI can lead to misuse, including extensive surveillance via facial recognition and computer vision technology. Moreover, developing solutions in a centralized setting necessitates businesses to relinquish privacy and control of their data to third parties. Here, blockchain technology plays a crucial role by potentially addressing several drawbacks associated with AI. 

AI algorithms excel at handling vast amounts of data and mimicking cognitive processes akin to the human brain. Utilizing complex neural networks, they recognize patterns, predict outcomes, and make decisions. Conversely, blockchain networks offer a transparent, decentralized, and tamper-resistant transaction layer. Anyone connected to the network can use it, and once data is stored, it becomes unalterable. This allows users to interact with the blockchain in a trust-minimized, permission-less manner.

Blockchain's inherent qualities of decentralization, immutability, and anonymization can address some of AI's key needs. It can break data silos and facilitate the free flow of algorithms, computational power, and data resources. Additionally, blockchain can ensure the integrity of original data and enhance the audit credibility and traceability of AI's operations. It can document AI's decision-making processes, thereby increasing transparency, explicability, and trust in AI's actions.


Conversely, AI can reciprocate by improving the architecture of blockchain systems, making them more secure, energy-efficient, and effective. In essence, the convergence of AI and blockchain technologies results in an autonomous, credible, and intelligent system, leveraging the benefits of both while mitigating their respective shortcomings.
 

## Application Scenario

In this section, we will discuss the combination of AI and blockchain technology in detail. At the 2020 International Conference on Information Systems, Erik Karger proposed a detailed review on the combination of blockchain and AI {cite}`inproceedings`. According to his research, the integration of AI and blockchain can be categorized into three main areas, each with its own subdivisions.

```{note} **AI & Blockchain Combination Classification**

- Blockchain for AI: Blockchain for AI pertains to scenarios and applications in which blockchain technology is utilized to bolster or amplify pre-existing AI applications.
- AI for Blockchain: AI for Blockchain encompasses situations where AI applications strive to enhance blockchain technology. This can be seen in areas like mining processes and smart contract execution.
- AI with Blockchain: AI with Blockchain refers to systems and platforms that concurrently employ AI and blockchain technology, with neither being solely reliant on or used as a leveraging tool for the other.

```
```{figure} images/ai_oracle_interact.png
---
width: 550px
height: 300px
name: AIB-fig
---
Integration of Blockchain and AI
``` 

### Blockchain for AI 

Most commonly, research and applications have explored the potential of using blockchain to augment AI. These applications can be subdivided into the following sections {cite}`inproceedings`:

- Data management based on blockchain

The availability of vast data is a key driver behind the AI revolution, but access to this data is often hindered by factors such as dominance by big players like Facebook and Google and growing concerns about privacy following instances of data misuse. This deters competition among AI researchers and companies, and increases fear and mistrust among users {cite}`8481263`. Blockchain technology can offer a solution by promoting data sharing, providing transparency, accountability, and giving users control over their data. 
In e-healthcare {cite}`Tagde2021`, blockchain can be used to securely store patient data. Each patient's health data could be stored in a block and added to the blockchain. This provides secure, immutable records that can easily be tracked and traced, ensuring patient data integrity and confidentiality. This can boost user confidence and enable better data use for societal benefits, such as faster discovery of cures for diseases.

- Data marketplaces that utilize blockchain

Blockchain could facilitate the creation of secure, private data marketplaces via smart contracts, eliminating the need for intermediaries. This would lower entry barriers for smaller players, encourage innovation, and allow for the search of relevant information while maintaining user privacy {cite}`8481263`. The primary aim of Ocean Protocol is to democratize the access to data, making it universally accessible for AI training and analysis {cite}`oceanprotocol2022`. They do this by providing a platform that allows individuals and organizations to monetize and share their data without losing control over it. This ensures data privacy and security while enabling the data to be used to its fullest potential.

- AI architectures that rely on blockchain

SingularityNET {cite}`singularitynet2019` exemplifies an AI architecture that leverages blockchain. It's a decentralized marketplace, powered by a blockchain protocol, for buying and selling AI services. This unique setup fosters an environment where anyone can create, share, and monetize AI tools. Developers can use the platform to sell AI services, while buyers can test these services before purchase. The decentralization provided by blockchain ensures that the marketplace is not dominated by any single entity. Additionally, blockchain's inherent transparency and immutability boost user trust and data security. The platform also uses smart contracts to automate transactions, making exchanges efficient and trustless. The platform even supports interoperability, enabling different AI services to collaborate and form complex models. By combining AI and blockchain, SingularityNET democratizes access to AI, fosters innovation, and promotes a transparent, secure AI ecosystem.

- Swarm systems enhanced by blockchain

Ferrer {cite}`10.1007/978-3-030-02683-7_77` discussed how blockchain technology can provide innovative solutions to emergent issues in the swarm robotics research field. Blockchain technology can significantly enhance swarm systems by increasing safety, supporting distributed decision making, and differentiating individual robot behaviors. Security threats can arise from insecure communication channels or manipulated swarm members. Blockchain addresses these vulnerabilities by providing a reliable peer-to-peer communication channel for each swarm agent. Using public-key cryptography, robots can securely exchange information, and message authorship can be easily verified. Moreover, a coordination mechanism using blockchain for various purposes has been developed. Each robot acts as a node and a miner in the blockchain network, enabling knowledge exchange, voice capture, and decision strategy application via smart contracts. Furthermore, blockchain can support decentralized decision-making algorithms in swarm systems, with benchmark tests showing improved consensus time and exit probability compared to non-blockchain methods.

### AI for Blockchain

- Intelligent Smart Contract

According to Almasoud et al. {cite}`8592662`, AI can significantly augment the capabilities of smart contracts by serving as recommendation systems during contract negotiations. They can analyse archived smart contracts, evaluate past negotiation strategies, propose effective language and clauses, and identify factors to consider in future contracts. Furthermore, AI can be programmed to negotiate conditions that affect the price or quality of goods. Nguyen and Bailey {cite}`nguyen2018usejournal` propose that AI can determine the optimal time to trigger a smart contract using supervised or unsupervised learning techniques. AI can also assist in providing dynamic, tailored solutions during contract failures. Omohundro {cite}`10.1145/2685328.2685334` argues that the integration of AI methods could make smart contracts operational in Internet of Things (IoT) environments, aiding the translation of sensor information into precise terms to which smart contracts can respond.

- Improvement of the Mining Process

Singh and Hafid {cite}`10.1007/978-3-030-23813-1_16` suggest that machine learning can improve the blockchain mining process by predicting transaction confirmation times on the Ethereum blockchain. This assists users in understanding the acceptance and timing of their transactions. Chen et al. {cite}`unknown` propose an AI-based consensus mechanism, "Proof of Artificial Intelligence" (PoAI), that ranks blockchain network nodes based on criteria such as computing power or security aspects, thereby allowing only the best nodes to conduct mining. This reduces competition for computing power, saves energy, and promotes fairness and decentralization. Although this field is still in its infancy, it holds substantial potential for future research and development.

### AI with Blockchain

Erik proposeed a third category of use cases for the combination of AI and blockchain, which create entirely new applications through their synergistic use, a concept termed 'blockchain with AI'. {cite}`inproceedings`

In the context of human resources management, Markopoulos et al. {cite}`inbook` describe an approach combining AI and blockchain to enhance the Democratic Teaming Model (DTM) for selecting project personnel. Expert systems in AI can recommend ideal team compositions based on employee data, while blockchain can secure the data and transactions for optimal analysis. Arora et al. {cite}`10.1007/978-981-13-8618-3_51` propose combining deep learning and blockchain to enhance the security of collaborative recommender systems, especially in industries where data privacy is paramount. Li et al. {cite}`8649758` present a customer service approach using blockchain and automated machine learning (AutoML) to analyse data from IoT devices securely. This process automation can particularly benefit small and medium-sized enterprises (SMEs). Mylrea {cite}`MYLREA2019217` investigates the potential of blockchain, AI, and machine learning in forming Distributed Autonomous Energy Organizations (DAEOs), improving security, speed, and reducing the need for intermediaries. Autonomous smart contracts could facilitate automatic value or service exchanges, and the blockchain can function as a secure storage medium for sensitive data.

## Challenges

As we look to the future of technological advancements, the integration of AI and blockchain holds tremendous promise. This convergence could revolutionize many fields around us. However, this promise is not without its challenges:

1. Scalability: The performance and scalability of the existing blockchain platform is crucial to the successful implementation of smart blockchain applications. Challenges include consistency issues, network delays, and performance limitations. Pursuing scalability may decrease the consistency requirements of the distributed network, leading to blockchain bifurcation. The peer-to-peer nature of the blockchain results in network delays, especially for nodes with longer delays. Also, the transaction performance limits the scalability of the blockchain, as to ensure security and eventual consistency, transactions can't be performed in parallel, making it hard to increase transaction throughput.

2. Security and Privacy: Blockchain's transparency is a double-edged sword. On one hand, it is one of its main selling points. On the other hand, this very transparency poses a significant challenge: how do we protect user privacy in an open system? Currently, common privacy protection methods in blockchain include information hiding and identity confusion. Yet, these measures often require increased computational processes, leading to reduced system efficiency. The challenge here is leveraging AI to improve this low efficiency, while also adapting existing algorithms for application in a distributed environment.

3. Data Collaboration between On-Chain and Off-Chain Storage: The effective combination of blockchain technology and traditional information systems is crucial to ensure the relevance and consistency of data both on-chain and off-chain. Challenges like poor data quality, data monopoly, and data abuse can be given new development opportunities with the intervention of blockchain. Ensuring the correct combination of on-chain and off-chain data is necessary for the practical application of the blockchain and AI combination in the real economy.

## Conclusion

In conclusion, the integration of artificial intelligence and blockchain promises exciting potential across various applications. However, realizing this potential still remains challenging. The existing taxonomy of AI and blockchain synergy may not remain static in the coming years. As technological boundaries continue to be pushed, the fusion of artificial intelligence and blockchain is set to significantly transform our digital and commercial landscape. 

<div style="text-align: right;font-weight: bold;">Ruoyi Zhao</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
