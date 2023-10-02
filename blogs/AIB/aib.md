# The Symbiotic Relationship between Blockchain and Artificial Intelligence

<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- Blockchain and AI present a synergistic relationship, where each technology can address the inherent challenges of the other, leading to the creation of a secure, efficient, and intelligent system.
- AI technology can enhance blockchain-based Decentralized Finance (DeFi) operations by providing advanced analytic tools, thus allowing for more sophisticated fund management and yield optimization.
- An exemplary application of AI in DeFi is SingularityDAO, which uses AI for managing liquidity, predicting market movements, and rebalancing portfolios.
- Challenges such as proving the origin of AI-generated content and computations in blockchain can potentially be addressed with technologies like Zero-Knowledge Machine Learning (ZKML) and blockchain-NFTs for AI models, though these solutions still have limitations and areas for further research and development.
```

## Introduction

Artificial intelligence and blockchain are two progressive technologies that hold great potential in stimulating the intelligent evolution of various industries. Each possesses inherent strengths but also faces its own unique challenges. AI is gradually transforming industries by introducing advanced capabilities but struggles with issues such as interpretability and effectiveness. It operates based on three key elements: algorithms, computational power, and data {cite}`zhang2021recent`. On the other hand, blockchain, despite being an advantageous foundation for trustworthy transactions, grapples with hurdles concerning energy consumption, scalability, security, privacy, and efficiency {cite}`zhang2021recent`. Despite these separate research directions and associated challenges, AI and blockchain exhibit a natural synergy due to shared requirements for data analysis, security, and trust. This intersection between the two technologies can significantly amplify their respective strengths. According to the estimations of Spherical Insights, the Blockchain AI Market, valued at USD 230.10 million in 2021, is projected to grow to USD 980.70 million by 2030 {cite}`sphericalinsights2022blockchain`. The merger of these two technologies is an area that still calls for in-depth exploration. Moving forward, we'll examine AI in the context of blockchain, investigating in detail the possible intersections and inherent value these two technologies may possess when coalesced.

## The mutual empowerment between blockchain and AI technology

Rohan Pinto, the CTO of 1Kosmos BlockID {cite}`pinto2018next` pointed out that the centralized AI can lead to misuse, including extensive surveillance via facial recognition and computer vision technology. Moreover, developing solutions in a centralized setting necessitates businesses to relinquish privacy and control of their data to third parties. Here, blockchain technology plays a crucial role by potentially addressing several drawbacks associated with AI.

AI algorithms excel at handling vast amounts of data and mimicking cognitive processes akin to the human brain. Utilizing complex neural networks, they recognize patterns, predict outcomes, and make decisions. Conversely, blockchain networks offer a transparent, decentralized, and tamper-resistant transaction layer. Anyone connected to the network can use it, and once data is stored, it becomes unalterable. This allows users to interact with the blockchain in a trust-minimized, permission-less manner.

Blockchain's inherent qualities of decentralization, immutability, and anonymization can address some of AI's key needs. It can break data silos and facilitate the free flow of algorithms, computational power, and data resources {cite}`samani2023convergence`. Additionally, blockchain can ensure the integrity of original data and enhance the audit credibility and traceability of AI's operations. It can document AI's decision-making processes, thereby increasing transparency, explicability, and trust in AI's actions.

Conversely, AI can reciprocate by improving the architecture of blockchain systems, making them more secure, energy-efficient, and effective. In essence, the convergence of AI and blockchain technologies results in an autonomous, credible, and intelligent system, leveraging the benefits of both while mitigating their respective shortcomings.

## Enhancing DeFi Operations with AI

Most commonly, research and applications have explored the potential of using blockchain to augment AI {cite}`inproceedings`. However, our focus is on exploring how AI can enhencing Decentralized Finance. As a core application of blockchain, Decentralised Finance (DeFi) has consistently been a subject of keen interest in both academic and commercial research.

Raheman et al. {cite}`9686345` designed an infrastructure of AI agents or "Oracles" for portfolio management, liquidity provision, and price prediction in various decentralized financial markets. As shown in Figure 1, these Oracles will increase investment value and returns by offering liquidity. They serve end business applications, smart contracts, and other agents. A key aspect is the distinction between an "inventory/portfolio" that comprises multiple assets and a "DEX swap pool" or "DEX balancing pool," which is one of several portfolio maintenance strategies. Therefore, a single "inventory/portfolio" may contain multiple "DEX swap pools" or "DEX balancing pools" with various strategies.

```{figure} images/defi&ai.png
---
width: 450px
height: 551px
name: defi&ai
---
Figure 1: the business functions (at the top) served by AI Oracles (at the bottom).
```

Figure 2 is the diagram showing how the AI oracles interact with each other and the data sources.

```{figure} images/ai_oracle_interact.png
---
width: 564px
height: 652px
name: ai_oracle_interact
---
Figure 2: AI Oracles (in the middle) serving business functions/applications (at the top) relying on data scalping services (at the bottom).
```
AI oracles are being developed for a comprehensive portfolio management system, utilizing on-chain data and predictive analytics.
Key components include:
- A Portfolio Planner Oracle for long-term investment strategies,
- A Strategy Evaluator Oracle for assessing competitive strategies
- A Pool Weighting Oracle for adjusting short-term risks
- A Signal Generator Oracle for real-time trading and liquidity advice
- A Sentiment Watcher Oracle for monitoring social and online media buzz about specific tokens

These components are informed by the Price Predictor, which predicts price trends and volatility using AI and machine learning. Data is sourced from various channels, including centralized exchanges and live Ethereum Nodes. The architecture is currently under construction, with primary components being the Strategy Evaluator, Price Predictor, Portfolio Planner, and Pool Weighter. The research {cite}`9686345` also indicate that there are opportunities to improve the predictor model's efficiency, such as sharing models across similar markets or using pre-trained models that match expected market conditions. For more detail of the architecture and test result, please see [here](https://docs.singularitydao.ai/research-papers/artificial-intelligence/architecture-of-automated-crypto-finance-agent).

In general, DeFi allows user to access financial services without intermediaries. Comparing to traditional finance, DeFi allows users to have greater control over their assets and avoid the fees associated with centralized exchanges.

- With help of AI, DeFi platforms can analyze vast amounts of data to provide personalized investment and minimizes risks. Machine Learning Algorithms (MLA) can help identify investment opportunities and optimize smart contracts. These can help user to make more informed decisions to increase profits.

Yield aggregator and dencentralised exchange (DEX) are specific applications under the DeFi ecosystem.

- Yield Aggregators automatically shift their users' funds between different DeFi protocols to seek out the highest yield. This process is typically based on complex algorithms and strategies, and the goal is to maximize return on investment, taking into account factors such as gas fees and potential risks. AI can significantly improve the efficiency and performance of yield aggregators by helping to analyze market trends and determine the optimal strategies for funds allocation.

- DEXs are decentralized platforms where cryptocurrencies can be traded directly between users. AI can contribute to DEXs in several ways, including optimizing liquidity provision, predicting market movements, improving price matching algorithms, and detecting abnormal trading behaviors.


SingularityDAO is an representative application of AI within the decentralized finance (DeFi) ecosystem. It is a decentralized protocol that facilitates user-friendly crypto asset management, employing advanced risk management and analytic tools. This non-custodial system nurtures a new network of Digital Asset Managers, providing automated trading strategies powered by AI-enhanced data analytics. {cite}`singularitydao2020lightpaper`.

- In the context of SingularityDAO, AI is applied to manage liquidity and predict market movements. AI algorithms dynamically manage portfolios, execute efficient asset allocation, and provide liquidity to high-quality tokens in decentralized exchanges (DEXs). This essentially optimizes the performance of the token sets (or DynaSets) within complex markets.

- Yield aggregators in DeFi automatically move their users' funds between different liquidity pools to maximize returns. SingularityDAO applies AI to this concept through their DynaSets, which are actively managed portfolios (or baskets) of utility tokens from early-stage AI projects. AI models help in the management and rebalancing of these DynaSets, optimizing for the best possible returns.

SingularityDAO is not solely a DEX, a liquidity pool, or a yield aggregator in the traditional sense, it leverages AI to bring sophisticated fund management and yield optimization techniques to these areas within the DeFi ecosystem.

## Challenges and Solutions

With AI technology becoming increasingly sophisticated, the line between AI-generated content and human-created content is blurring. As such, there is a growing need to ascertain the origin of content—whether it was generated by applying a specific AI model to a particular input. Zero-knowledge cryptography could provide a solution, offering a method to validate the outputs from these models without revealing any sensitive information about the input or the model itself—a process often referred to as ZKML (Zero-Knowledge Machine Learning). This capability could be extremely useful in sensitive fields like healthcare, where the confidentiality of patient data is paramount. However, it's important to note that ZKML currently focuses on creating zero-knowledge proofs for the inference (or output) of machine learning models, not the training phase, which is a highly computationally demanding task {cite}`dcbuilder2023zkml`.

Battah et al. {cite}`9924181` proposed a solution using blockchain and NFTs addresses the limitations of existing methods in managing AI model ownership, trading, and access by providing traceability, transparency, auditability, security, and trustful features . It leverages blockchain technology to create a decentralized and transparent system where ownership rights and exchanges of AI models can be managed in a trustworthy manner . By using NFTs linked to AI models, smart contracts are employed to enforce ownership, ease of access, and exchange policies . This ensures that the ownership of AI models is clearly defined and can be easily transferred between parties . Additionally, the system tracks information regarding all assets and provides provenance of data, overcoming trust concerns . Overall, the solution aims to provide a secure and reliable framework for managing AI model ownership, trading, and access. This system keeps track of all assets and provides provenance of data, could potentially addressing the trust concerns that can arise with AIGC NFTs.

While blockchain technology does not natively recognize or comprehend real-world events, it could be advantageous if it were cognizant of such incidents. This understanding could enable the transfer of value in accordance with real-world situations. Oracles provide a solution to this by serving as intermediaries that fetch and verify real-world data for blockchains. However, they may not suffice in all cases because some real-world data requires computation before it's sent to the blockchain. For instance, a yield aggregator aiming to transfer deposits between different pools to maximize yield in a trust-minimized way would need to compute the current yields and risks of all available pools. This forms an optimization problem that machine learning is well-equipped to tackle. Nevertheless, executing machine learning computations on the blockchain is costly. This presents an opportunity for ZKML, this would allows machine learning computations to be conducted off-chain but verified on-chain in a zero-knowledge manner, which could potentially reduce costs and increase efficiency {cite}`samani2023convergence`.

## Conclusion

The symbiotic relationship between blockchain and artificial intelligence can pave the way for transformative developments in various industries. The strengths of these technologies address each other's challenges, resulting in a more secure, efficient, and intelligent system. Decentralized finance (DeFi), a prominent application of blockchain, has particularly benefited from this convergence, with AI enhancing analytic capabilities and optimizing yields. Yet, challenges remain, such as proving the origins of AI-generated content and computations in the blockchain environment. Emerging solutions like Zero-Knowledge Machine Learning (ZKML) and blockchain-backed NFTs for AI models offer promising possibilities but require further exploration. As research and development continue, we can anticipate a future where these powerful technologies seamlessly intertwine, driving innovative solutions across a multitude of sectors.

<div style="text-align: right;font-weight: bold;">Ruoyi Zhao</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```