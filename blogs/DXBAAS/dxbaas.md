# Developing with Blockchain-as-a-Service and its Impacts on Developer Experience

<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- Blockchain-as-a-Service (BaaS) simplifies development complexity, fostering a more accessible infrastructure, notably driving Developer eXperience (DX).
- Developer Experience (DX), akin to User Experience (UX), profoundly influences software development, impacting performance and quality across various aspects.
- Docstone, a blockchain-based architecture, offers asset registration services, aiming to expand capabilities by integrating Decentralized Finance (DeFi) modules.
- The assessment of Developer eXperience (DX) will be crucial in understanding how BaaS affects the ease, usefulness, and overall effectiveness of Docstone's integration, shaping possible improvements for BaaS in the future.
```

## Introduction

Blockchain technology has taken a prominent role in various sectors, owing to its potential to meet the requirements of integrity, authenticity, security, access control, transparency, and availability necessary for many solutions. In essence, blockchain combines cryptography, data management, and incentive mechanisms to facilitate the verification, execution, and recording of transactions among different parties without the centralized control of any trusted third party {cite}`xu2019architecture`. Despite the promising outcomes of using blockchain, there are barriers to its progress and acceptance {cite}`kotha2023complexity`. Implementing blockchain and decentralized applications (dApps) can be intricate and error-prone due to the need to consider network infrastructure components and commercial regulations of smart contracts across several software architecture aspects {cite}`song2022research`.

Furthermore, deployment challenges and high operational expenses in maintaining a distributed blockchain system hinder its adoption in the market {cite}`li2021services`. In summary, we still face (i) a scarcity of experienced developers, (ii) complex implementation and usage, and (iii) expensive maintenance. In this regard, to promote blockchain adoption and facilitate its use, "Blockchain-as-a-Service" (BaaS) platforms have emerged, enabling developers to solely focus on coding business rules while leveraging cloud services for infrastructure deployment and network monitoring {cite}`onik2019performance`. Blockchain as a Service (BaaS) holds promise in enhancing the efficiency of developing blockchain applications. Simplified and expedited deployment is the core service current BaaS platform providers provide. In a short period, blockchain technology has significantly advanced. Despite the high demand for professionals, who are still in short supply, solutions like BaaS can facilitate implementation by "traditional" developers, consequently fostering the adoption of blockchain across various domains. However, despite the great potential of these platforms, the literature is scarce regarding studies that assess the use of these platforms by developers and the actual impact on their development experience.

Given the context, this project aims to evaluate the developer experience using Blockchain-as-a-Service platforms to analyze their impacts on different software development aspects. To conduct this assessment, we will perform a Case Study based on a BaaS currently under development by the author of this proposal. The case study will use Docstone as the research object, a BaaS that allows the storage of documentary information in a personalized and flexible manner, from the initial configuration of parameters for creating document templates to their storage and validation in one or more blockchains. This proposal is part of a major project that has already been published in conferences {cite}`soares2022blockchain, soares2022docstone, fernandes2023proposta` and journals {cite}`soares2023extending`. In addition, a version designed for the government won first and third place in two challenges in the Web3 Hackathon - Tokenization of the Union's Heritage of Brazil.

This tool focused only on asset management to verify documents and asset integrity in the versions presented. In order to evolve the proposal for this project, the goal is to expand the architecture to integrate with Decentralized Finance (DeFi) services. In this sense, the relevance of this project lies in the following contributions:
1. Identification and mapping of the main challenges faced by blockchain developers when using BaaS, creating guidelines for possible solutions and development standards.
2. Remodeling of Docstone to improve the developer experience when integrating blockchains with document and financial management services with a proposed DeFi Module.
3. Evaluating BaaS usage considering different aspects of the developer experience through real experiments with Docstone.


## Blockchain-as-a-Service & Developer eXperience

The different current architectures of BaaS originate from both the industry and academia {cite}`song2022research`.
Figure 1 lists some of the providers that offer this service in a private manner. For instance, Alibaba supports three different blockchain technologies (Hyperledger Fabric, Enterprise Ethereum, and Quorum). The platform supports various basic BaaS services, including general resource creation, resource management, operation, and security management. Another system is IBM ADEPT, which allows the initial use of Hyperledger Fabric in IoT support. ADEPT enables the creation of CIs instead of writing them from scratch, providing a simple layer and business-level abstraction. Various academic works have also presented BaaS solutions. In the Unified Blockchain as a Service (uBaaS) {cite}`lu2019ubaas`, for example, users can create a blockchain environment and design applications through a uBaaS user interface that interacts with various backend services and API gateways, including blockchain deployment and CI services.

```{figure} images/baas.png
---
width: 1200px
height: 220px
name: baas
---
The BaaS architectures of Alibaba, IBM, Microsoft, Oracle, and Amazon.
```

Blockchain-as-a-Service (BaaS) simplifies the complexity of development, offering a more accessible infrastructure. This simplification drives Developer experience (DX) by allowing developers to focus more on business logic and creating innovative solutions, positively impacting the usability of the developed applications. The concept of User Experience (UX) influenced the concept of DX. DX is defined as a way to capture how developers think and feel about their activities within their work environments, assuming that improving the developer's experience has positive impacts on software development project outcomes {cite}`fagerholm2012developer`. 

Several studies indicate that human factors are the most relevant in software development, both in terms of performance and quality, impacting the success of software projects {cite}`dutra2021human`. The DX plays a crucial role in various areas of software development and encompasses technical and social aspects. For instance, when attempting to create a developer ecosystem for applications and services, it allows the design of a development experience that makes the platform and ecosystem more appealing to developers. On the other hand, in the context of software project management, DX can be used to assess the alignment of plans and goals with the motivation and commitment of developers. Furthermore, it provides essential insights to sustain the development team's performance by identifying the factors that impact their work {cite}`fagerholm2012developer`. 

## Case Study: Docstone

In summary, Docstone is a blockchain-based architecture providing registration and validation services for assets such as documents, processes, and NFTs, as depicted in Figure 3. The architecture is divided into three main layers: Application, Service, and Persistence.

```{figure} images/architecture_v1.png
---
width: 1200px
height: 240px
name: architecture_v1
---
Docstone Architecture Overview.
```

The Application Layer is where client applications connect and utilize Docstone. This layer provides a user-readable interface for interacting with the available resources and endpoints. Following, there's the Service Layer, which implements and executes all functionalities related to managing Documents, Processes, and NFTs. This process is carried out through four main classes that interact with each other: Client, Model, Smart Contract (SC), and Assets.
Finally, there's the Persistence Layer, which consists of three modules supporting document content storage: Off-chain Module, EVM Module, and Private Network Module. These layers encompass storage in a relational database, distributed file system storage (IPFS), smart contract execution on an Ethereum Virtual Machine (EVM), and integration with private networks based on Hyperledger Fabric.

Figure 4 illustrates registering information related to copyright certificates for artworks on the blockchain using Docstone. In Step 1, the flow involves the creation of an artwork certificate template by the client (the document's structure to be stored), followed by deploying a smart contract on the chosen blockchain (Ethereum, Polygon, Binance, etc.) in Step 2. The smart contract is of the "documents" type and is associated with the created template.

```{figure} images/demonstration_flow.png
---
width: 1000px
height: 300px
name: demonstration_flow
---
Demonstration Flow of Docstone.
```

In Step 3, the artwork certificate's metadata is inserted into the blockchain using the previously defined template and smart contract. The data includes attributes such as the author's identification, artwork identification, description, and type. Additionally, it is possible to submit the digital file representing the artwork to be stored on IPFS while the metadata is stored on the blockchain. Finally, in Step 4, it is possible to query the artwork certificate's metadata on the blockchain and retrieve the artwork file from IPFS. Moreover, other requests, such as document validation, can be initiated by comparing the hash of the submitted file with the hash previously recorded on the blockchain, enabling verification of the file's integrity. This process demonstrates how Docstone is used to register, store, and retrieve information regarding certificates of artworks on the blockchain.


### Integrating Decentralized Finances (DeFi) to the Docstone

As a step forward in developing this technology, the integration of a DeFi Module has been proposed. Thus, to introduce DeFi protocols into Docstone, the main focus will be adaptations within the Service Layer. This adaptation will involve integrating functionalities and smart contracts that enable decentralized financial operations. Consequently, Docstone will be capable of utilizing services such as:

- **Lending and Borrowing:** Integration of solutions where users lend and borrow without the need for intermediaries {cite}`paliwal2022analysis`. e.g., Compound, Aave, and MakerDAO.

- **Decentralized Exchanges (DEXs):** Integration with systems that facilitate direct cryptocurrency exchanges without needing a centralized exchange. They function through smart contracts, liquidity pools, and AMM algorithms {cite}`xu2021sok`. e.g., Uniswap, SushiSwap, and PancakeSwap.

- **Staking:** Integration with systems that allow cryptocurrency holders to lock their assets on a platform to support blockchain network security and operations. In return, they receive rewards in additional tokens.

- **Oracles:** Integration with oracles to supply real-world data to smart contracts within the DeFi ecosystem. They act as bridges between external information (such as asset prices, exchange rates, weather data, etc.) {cite}`liu2021first`. e.g., Chainlink and Band Protocol.

As depicted in Figure 5, the DeFi Module is added to the Docstone architecture. Initially, the aim is to implement DEX, Lending and Borrowing, Staking, and Oracles services. To achieve this goal, we propose an interface for integration with SDKs and APIs the platforms provide or even custom smart contracts for communication with such services.


```{figure} images/architecture_v2.png
---
width: 1052px
height: 360px
name: architecture_v2
---
Service Layer introducing DeFi Module.
```

For instance, within the DEX ecosystem, Uniswap offers its SDK  for developers to integrate operations such as Fetching a Quote and Executing a Trade, among other functionalities. Conversely, Curve, a more complex DEX enabling the exchange of more than three tokens, provides extensive documentation for proper integrations with its smart contracts. In the context of Lending & Borrowing platforms, Compound, Aave, and MakerDAO also offer their SDKs through which they perform various functionalities. 

Protocols like Bake, PancakeSwap, and Nexo offer robust features through their SDKs within the Staking realm. These tools empower developers to incorporate functionalities such as Token Delegation, Reward Claiming, and Governance Participation, adding value to the Docstone ecosystem. Regarding Oracles, integrating reliable external data sources is essential for secure and accurate operations. Prominent platforms like Chainlink and Band Protocol play significant roles. The former provides detailed documentation for consuming Data Feeds, for instance. Meanwhile, the latter positions itself as a cross-chain data oracle aiming to supply trustworthy, secure, and real-time data to smart contracts across multiple blockchain networks.

Considering an example of a DEX, as stated by Uniswap's SDK, to execute a trade on Uniswap using the provided SDK, several steps need to be undertaken, such as:
1. Using a wallet extension,
2. Constructing a route from pool information,
3. Creating a Route,
4. Constructing an unchecked trade and finally
5. Executing a trade.

For Docstone, the aim is to further reduce the number of steps for the end developer, who might not necessarily require in-depth blockchain knowledge, needing only to 'Execute a trade' (the final step).

```{seealso}
\
**Illustrative Scenario:**
\
Platform A enables users to convert Token A, based on Ethereum (ETH), to Token B, facilitating swift and direct transactions between different cryptocurrencies. This integration streamlines the process for platform A users, allowing them to access the Uniswap environment without leaving the platform's ecosystem. Additionally, developers simplify the integration process by using Docstone to facilitate the integration. The developer can call a route /execute_trade and send the following body in the request.
```json
{
    "protocol": "UNISWAP",
    "service": "execute_trade"
    "token_a": "ETH",
    "token_b": "ABC",
    "amount": "0.0001"
}
```

We abstract architectural and technological details for such examples as they are yet to be remodeled and specified. Therefore, as presented in the following section, we intend to use the methodological procedures below.

## Methodology Overview

`````{margin} **Design Science Research (DSR)**
DSR aims to generate knowledge about the project and develop solutions to enhance systems, solve problems, and create new artifacts.
`````

This applied research project follows the protocol of Design Science Research (DSR) {cite}`vaishnavi_design_nodate`. The five stages of this research are (i) Awareness of the Problem, (ii) Suggestion, (iii) Development, (iv) Evaluation, and (v) Conclusion.

`````{margin} **Multivocal Literature Review (MLR)**
MLR process includes both peer-reviewed literature and grey literature, encompassing different perspectives among professionals and academic researchers
`````
In the **Awareness of the Problem** phase, considering the scarcity of studies in the literature related to the theme, we intend to conduct a Multivocal Literature Review (MLR) {cite}`garousi2019guidelines` to identify the main discussions about Developer eXperience and blockchain. Additionally, we will perform Software Repository Mining on StackOverflow to identify the key challenges discussed by developers using blockchain to guide the redesign and improvements that will be made in the API Docstone in its Docstone version.

The **Suggestion** phase starts immediately after the first stage. Based on a deeper understanding and well-defined delimitation of the problem and all the theoretical foundations raised, this stage focuses on articulating the theoretical assumptions and proposed concepts. With such data as an initial representation of the proposed artifact, iterative versions must be generated until the tentative design, in the form of an API or service, is achieved. In turn, the **Development** phase proposes the artifact itself in its final version. In this case, the integration of the DeFi Module is considered.

Once developed, the artifact must be evaluated to validate it and illustrate how it functions in practice. Thus, the **Evaluation** phase aims to evaluate the API through a Case Study. The goal is to assess the API's different aspects and quality requirements, as well as its adaptation to different use cases. Additionally, evaluation is planned with different profiles (software architect and developer) focused on blockchain development. Specifically, the plan is to evaluate the developer's experience using the API through different implementations. The last step of the design cycle is the Conclusion, where we analyze, consolidate, and adequately document the results. 


## Potential Implications

- **Simplified Development:** Developers can easily leverage various third-party services or focus more on business logic than infrastructure complexity, potentially speeding up development.
- **Reduced Learning Curve:** BaaS can make entry into blockchain development more accessible for developers without experience in this domain.
- **Improved API Usability:** Developers may find integrating specific functionalities into their applications more accessible.
- **Increased Innovation:** Encouragement for creating new blockchain-based solutions and applications, resulting in a more diversified ecosystem.
- **Enhanced Software Quality:** A better understanding of developers' challenges and needs may lead to the emergence of standards and guidelines improving overall software quality in this environment.
- **Wider Blockchain Adoption:** With the simplification offered by BaaS services, more companies may consider integrating blockchain technology into their operations.
- **Cost and Complexity Reduction:** Decrease in costs and complexity associated with building and maintaining blockchain infrastructures, making them more accessible to businesses of different sizes.
- **Diversification of Services:** Availability and more varied options to cater to specific business needs.
- **Expansion of Blockchain Applications:** New applications and use cases may emerge in sectors that previously did not consider blockchain technology viable.

## Potential Open Challenges

- **Education and Training:** Despite the simplification offered by BaaS, the need for trained professionals to effectively use these services may need to be addressed.
- **Scalability and Efficiency:** Similarly to the scalability of blockchains and the efficiency in executing smart contracts that still need improvements to handle a higher volume of transactions and users, BaaS architectures must also be designed to support such demand.
- **Standardization and Interoperability:** Pursuing common standards and interoperability among different BaaS platforms could be challenging to ensure a more efficient integration.
- **Security and Privacy:** Ensuring the security and privacy of data, especially in a semi-decentralized environment, when using APIs.

## Conclusion
The introduction of Blockchain-as-a-Service (BaaS) brings significant potential benefits for developers, institutions, and society. Enhancements in developer blockchain experience open doors for broader and more efficient use of blockchain technology across all sectors. However, challenges remain, including ongoing education and professional training, ensuring scalability and efficiency, standardization and interoperability among BaaS platforms, and critical concerns such as data security and privacy in a semi-decentralized environment. Overcoming these challenges is crucial to fully harness the potential of BaaS solutions and further expand their utility and impact on businesses and society.


<div style="text-align: right;font-weight: bold;">Pamella Soares</div>
<div style="text-align: right;font-style: italic;">December 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```




