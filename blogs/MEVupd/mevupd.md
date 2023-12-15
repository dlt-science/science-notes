# Exploring the World of Maximal Extractable Value (MEV) in Blockchain

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
- MEV's impact extends beyond transaction ordering profits, influencing network congestion and fee inflation, with miners potentially altering their behavior to chase these extractable values.
- To reduce the manipulative impact of MEV on transaction order, proposals for including transactions based on objective metrics like gas prices or timestamps are being examined.
- The emergence of specialised roles, including arbitrage traders and bot operators, signifies the development of a sophisticated MEV ecosystem, focusing on the optimisation of transaction placement for maximum returns.
- To enhance the fairness of blockchain networks, new protocols are being developed that aim to level the playing field by minimising the advantages of MEV for miners with greater computational resources.
- To protect end users from predatory MEV strategies, such as sandwich attacks, solutions are being researched that would obscure transaction details from potential attackers.
- To maintain the integrity of consensus mechanisms in the face of MEV, strategies are being considered that could deter miners from deviating from honest practices for short-term gains.
```
## Introduction

Maximal Extractable Value (MEV) also known as Miner Extractable Value (MEV), an increasingly crucial topic in the realm of blockchain research, refers to the monetary advantage a miner can acquire by strategically manipulating transactions in a block they produce. Recent studies have begun to shed light on the complexities of MEV, exposing both its potential threats and opportunities within the blockchain infrastructure. This science note offers an in-depth analysis of recent academic findings, focusing on the operational dynamics of MEV, its implications on the fairness and security of blockchain networks, and the proposed solutions to mitigate its effects.

## Deconstructing MEV

```{figure} images/MEVflow.drawio.png
---
width: 720px
height: 325px
name: mev_diagram
---
Transaction Prioritisation in the Context of Miner Extractable Value (MEV).
```

The concept of Miner/Maximal Extractable Value (MEV) was coined by Daian et al. {cite}`daian2020flash` to define the maximum profit a miner can secure by strategically adjusting transaction sequences. This practice, prevalent in various financial applications, has evolved into a profitable industry dominated by specialised searchers like arbitrage traders and bot operators. These searchers focus on identifying opportunities and constructing transactions to maximise MEV, often involving the precise placement of transactions.

In blockchains supporting smart contracts, miners or validators prioritize transactions with higher fees for inclusion in blocks, impacting the mempool where unconfirmed transactions wait, often delaying those with lower fees. A common MEV scenario involves miners exploiting arbitrage opportunities on trading platforms, sometimes leading to bidding wars with bots for higher transaction fees {cite}`yash2022mev`.

The impact of MEV is significant, particularly on end users who pay transaction fees, and on miners who select transactions based on these fees to maximise profits. While MEV is a relatively new field, it has already seen substantial research focused on understanding, quantifying, and mitigating its effects, especially in terms of common sources of MEV and the security concerns they pose. Common strategies include front running, where transaction fees are exchanged for block space with non-miner MEV extractors, and back running, which involves manipulating transactions for profit from on-chain events {cite}`yash2022mev`.

**Frontrunning:** This involves placing the attacker’s transactions ahead of the victim's. For instance, an attacker may offer higher transaction fees to ensure their transaction gets executed first to exploit a rare market opportunity. Block space is sold to non-miner MEV extractors in return for transaction fees through Priority Gas Auctions. 

**Backrunning:** In this scenario, the attacker places their transaction right after the victim's transaction to take advantage of the market change initiated by the victim. For instance, if a transaction on Exchange X significantly increases an asset's price, it opens an arbitrage opportunity. Here, the backrunner could purchase the same asset from another exchange, X', at a lower cost and then sell it on X, keeping the price difference {cite}`yang2022sok`. In this scenario, the backrunner's transaction does not harm the user and aids in maintaining price consistency between the two exchanges. In a similar context, backrunning can also be used to capitalise on oracle updates for liquidation opportunities {cite}`qin2021empirical`.

**Sandwich Attacks:** Sandwich attacks present a more complex MEV extraction method where the attacker places two transactions, one before and one after the victim's regular trade. The goal is to manipulate asset prices in such a way that the attacker benefits from the victim's loss {cite}`zhou2021high`. However, executing sandwich attacks can be risky for the attacker as any deviation from the desired transaction order can lead to financial loss. In most cases, these attacks are executed via MEV auction platforms.

**Bribery Attacks:** Attackers may generate MEV to encourage miners to act in their favor, this is known as a bribery attack. These attacks can range from incentivizing miners to temporarily delaying a transaction by offering higher fees for a conflicting transaction to more complex schemes facilitated by smart contracts {cite}`tsabary2021mad` {cite}`winzer2019temporary`. The impact of bribery attacks varies depending on the specific application.
 
## Impact on Blockchain Fairness and Security Risks

Eskandari et al. {cite}`eskandari2020sok` highlighted a disconcerting aspect of economic inequality that MEV introduces into a system fundamentally designed for decentralisation and equality. Their research showed that miners with more significant computational resources are advantaged, leading to an unequal distribution of wealth and power within the network. This core issue necessitates more rigorous examination and underscores the urgency for remedies that reestablish equilibrium and honor the essential principles of blockchain technology.

### Financial Losses

Certain forms of MEV extraction can result in direct financial losses for users. A case in point is the predatory sandwich attacks, which led to profits exceeding $3 million for attackers in November 2022 alone {cite}`eigenphi2022sandwich`. This substantial gain was, unfortunately, the result of monetary losses suffered by the victims.

### Inefficiencies Stemming from Coordination Deficit
The competitive pursuit of MEV by bots can lead to on-chain bidding battles. These contests may contribute to network traffic jams and inflate transaction costs. Some strategies intended to counter MEV can unintentionally trigger other forms of inefficiency. For instance, implementing a first-come-first-served transaction ordering can shift the competitive battleground to off-chain latency, thereby instigating off-chain latency wars among MEV searchers.

### Threat to Consensus Stability

Carlsten et al. {cite}`carlsten2016instability` demonstrated that when transaction fees surpass block rewards, miners may stray from honest mining practices. They could create forks with high-fee blocks to entice other miners to contribute to their fork. MEV can be seen as an expanded form of transaction fees directed to the miner, and a significant MEV can amplify this issue. Today, lucrative MEV extraction often outweighs block rewards {cite}`flashbot2022transparency`. 

Daian et al. {cite}`daian2020flash` detailed an additional attack method that leverages MEV, referred to as Time-bandit attacks. Essentially, this approach enhances reorganisation of 51% attacks by supplementing them with financial support derived from MEV.

### A Catalyst for Centralisation

Vitalik {cite}`vitalik2021proposer` asserted that MEV could foster centralisation given the notable economies of scale associated with uncovering complex MEV extraction opportunities. A future dominated by centralisation and monopoly is undesirable as it undermines the principles of transparency and decentralisation. There's also a concern that MEV could promote "vertical integration" {cite}`hasu2022why` where miners and traders combine to establish exclusive systems. This development could potentially jeopardise the transparency and permissionless nature of the blockchain.

## Solutions and Future Directions

### MEV Auction Platforms 

MEV auction platforms serve to facilitate auctions that allocate block space to users who place bids for their transaction inclusion. They place a high emphasis on transaction privacy and atomicity. Their services are mostly availed by MEV searchers, who carry out their MEV extraction transactions covertly, and regular users who protect their transactions from being exposed to searchers {cite}`yang2022sok`.

With the Ethereum merge, MEV auction platforms bifurcated into pre-merge and post-merge types. Pre-merge platforms like Flashbots and Eden Network use first-price sealed-bid auctions. Post-merge platforms are set to see native support in the form of a Proposer-Builder Separation (PBS) protocol in future Ethereum versions. However, an interim realisation, MEV-Boost, continues to rely on trusted relays. For users exclusively interested in privacy, these platforms offer private channels that can be accessed via RPC endpoints {cite}`yang2022sok`.

### Time-Based Transaction Ordering

Time-based ordering properties form a category of solutions aimed at preventing transaction order manipulation in the blockchain ecosystem. The concept, initially proposed by Kelkar et al. {cite}`kelkar2020order`, is built around "receive-order fairness," which is a first-come-first-served approach to transaction ordering. This notion has been further explored and improved upon by systems, which offer enhanced liveness and reduced communication complexity.

In the field of transaction ordering, relative fairness has also been a focus of exploration. Kursawe et al. {cite}`kursawe2020wendy` propose the concept of relative fairness, stipulating that if all honest validators see transaction T before a given time and another transaction T' after this time, T should be scheduled before T'. Zhang et al. {cite}`zhang2020byzantine` offer a similar concept called ordering-linearizability. While there are slight differences in these approaches, they can be integrated into a single property referred to as fair separability. 

Baird et al. {cite}`hedera2022hederatech`, in their exploration of Hashgraph, introduce a method that assigns each transaction a fair timestamp, derived from the median time that each node reports receiving the transaction first. A potential vulnerability in this method, however, is that a single adversary could manipulate a median-time-based order.

## Conclusion

MEV, while a challenging facet of the blockchain universe, offers valuable insights into the intricate dynamics of blockchain systems. Its study reveals critical areas of vulnerability, while also inspiring new strategies for enhancing system fairness and security. As the blockchain landscape continues to grow and evolve, addressing the issue of MEV will remain a pivotal focus in ongoing academic research and technological innovation.

<div style="text-align: right;font-weight: bold;">Ali Kathia</div>
<div style="text-align: right;font-style: italic;">December 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```