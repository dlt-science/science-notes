# Exploring the World of Maximal Extractable Value (MEV) in Blockchain

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
```
## Introduction

Maximal Extractable Value (MEV) also known as Miner Extractable Value (MEV), an increasingly crucial topic in the realm of blockchain research, refers to the monetary advantage a miner can acquire by strategically manipulating transactions in a block they produce. Recent studies have begun to shed light on the complexities of MEV, exposing both its potential threats and opportunities within the blockchain infrastructure. This blog post offers an in-depth analysis of recent academic findings, focusing on the operational dynamics of MEV, its implications on the fairness and security of blockchain networks, and the proposed solutions to mitigate its effects.

## Deconstructing MEV

The concept of Miner/Maximal Extractable Value (MEV) was coined by Daian et al. to define the maximum profit a miner can secure by strategically adjusting transaction sequences. This practice has evolved into a profitable industry, with specialized searchers identifying potential victims and constructing transactions to maximize MEV. The success of such operations hinges on the searcher's ability to precisely control the relative order of their transactions in comparison to the victim's transactions.

Although MEV is a relatively new field, it has already been the focus of substantial research regarding understanding, quantifying, and mitigating its effects. Below is a brief overview of common sources of MEV and the security concerns they pose.

MEV is prevalent in various financial applications, and extracting MEV typically involves the precise placement of transactions to maximize profit. 

**Frontrunning:** This involves placing the attacker’s transactions ahead of the victim's. For instance, an attacker may offer higher transaction fees to ensure their transaction gets executed first to exploit a rare market opportunity. Another approach is to sandwich the victim's transaction between the attacker's transactions.

**Backrunning:** In this scenario, the attacker places their transaction right after the victim's transaction to take advantage of the market change initiated by the victim. For instance, if a transaction on Exchange X significantly increases an asset's price, it opens an arbitrage opportunity. Here, the backrunner could purchase the same asset from another exchange, X', at a lower cost and then sell it on X, keeping the price difference (Yang et al.). In this scenario, the backrunner's transaction does not harm the user and aids in maintaining price consistency between the two exchanges. In a similar context, backrunning can also be used to capitalize on oracle updates for liquidation opportunities (Qin et al.).

**Sandwich Attacks:** Sandwich attacks present a more complex MEV extraction method where the attacker places two transactions, one before and one after the victim's regular trade. The goal is to manipulate asset prices in such a way that the attacker benefits from the victim's loss (Zhou et al.). However, executing sandwich attacks can be risky for the attacker as any deviation from the desired transaction order can lead to financial loss. In most cases, these attacks are executed via MEV auction platforms.

**Bribery Attacks:** Attackers may generate MEV to encourage miners to act in their favor, in what's known as a bribery attack. These attacks can range from incentivizing miners to temporarily delay a transaction by offering higher fees for a conflicting transaction to more complex schemes facilitated by smart contracts (Tsabary et al., Winzer et al.). The impact of bribery attacks varies depending on the specific application.
 
## Impact on Blockchain Fairness and Security Risks

Eskandari et al. highlighted a disconcerting aspect of economic inequality that MEV introduces into a system fundamentally designed for decentralization and equality. Their research showed that miners with more significant computational resources are advantaged, leading to an unequal distribution of wealth and power within the network. This core issue necessitates more rigorous examination and underscores the urgency for remedies that reestablish equilibrium and honor the essential principles of blockchain technology.

### Financial losses

Certain forms of MEV extraction can result in direct financial losses for users. A case in point is the predatory sandwich attacks, which led to profits exceeding $3 million for attackers in November 2022 alone (Eigen Phi). This substantial gain was, unfortunately, the result of monetary losses suffered by the victims.

### Inefficiencies Stemming from Coordination Deficit
The competitive pursuit of MEV by bots can lead to on-chain bidding battles. These contests may contribute to network traffic jams and inflate transaction costs. Some strategies intended to counter MEV can unintentionally trigger other forms of inefficiency. For instance, implementing a first-come-first-served transaction ordering can shift the competitive battleground to off-chain latency, thereby instigating off-chain latency wars among MEV searchers.

### Threat to Consensus Stability

Carlsten et al. demonstrated that when transaction fees surpass block rewards, miners may stray from honest mining practices. They could create forks with high-fee blocks to entice other miners to contribute to their fork. MEV can be seen as an expanded form of transaction fees directed to the miner, and a significant MEV can amplify this issue. Today, lucrative MEV extraction often outweighs block rewards (flashbots). 

Daian et al. detailed an additional attack method that leverages MEV, referred to as Time-bandit attacks. Essentially, this approach enhances reorganization or 51% attacks by supplementing them with financial support derived from MEV.

### A Catalyst for Centralization

Vitalik asserted that MEV could foster centralization given the notable economies of scale associated with uncovering complex MEV extraction opportunities. A future dominated by centralization and monopoly is undesirable as it undermines the principles of transparency and decentralization. There's also a concern that MEV could promote "vertical integration" (Hasu et al.) where miners and traders combine to establish exclusive systems. This development could potentially jeopardize the transparency and permissionless nature of the blockchain.

## Solutions and Future Directions

### MEV Auction Platforms 

MEV auction platforms serve to facilitate auctions that allocate block space to users who place bids for their transaction inclusion. They place a high emphasis on transaction privacy and atomicity. Their services are mostly availed by MEV searchers, who carry out their MEV extraction transactions covertly, and regular users who protect their transactions from being exposed to searchers (Yang et al.).

With the Ethereum merge, MEV auction platforms bifurcated into pre-merge and post-merge types. Pre-merge platforms like Flashbots and Eden Network use first-price sealed-bid auctions. Post-merge platforms are set to see native support in the form of a Proposer-Builder Separation (PBS) protocol in future Ethereum versions. However, an interim realization, MEV-Boost, continues to rely on trusted relays. For users exclusively interested in privacy, these platforms offer private channels that can be accessed via RPC endpoints (Yang et al.).

### Time-Based Transaction Ordering

Time-based ordering properties form a category of solutions aimed at preventing transaction order manipulation in the blockchain ecosystem. The concept, initially proposed by Kelkar et al., is built around "receive-order fairness," which is a first-come-first-served approach to transaction ordering. This notion has been further explored and improved upon by systems, which offer enhanced liveness and reduced communication complexity.

In the field of transaction ordering, relative fairness has also been a focus of exploration. Kursawe et al. propose the concept of relative fairness, stipulating that if all honest validators see transaction T before a given time and another transaction T' after this time, T should be scheduled before T'. Zhang et al. offer a similar concept called ordering-linearizability. While there are slight differences in these approaches, they can be integrated into a single property referred to as fair separability. 

Baird et al., in their exploration of Hashgraph, introduce a method that assigns each transaction a fair timestamp, derived from the median time that each node reports receiving the transaction first. A potential vulnerability in this method, however, is that a single adversary could manipulate a median-time-based order.

## Conclusion

MEV, while a challenging facet of the blockchain universe, offers valuable insights into the intricate dynamics of blockchain systems. Its study reveals critical areas of vulnerability, while also inspiring new strategies for enhancing system fairness and security. As the blockchain landscape continues to grow and evolve, addressing the issue of MEV will remain a pivotal focus in ongoing academic research and technological innovation.

<div style="text-align: right;font-weight: bold;">Ali Kathia</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

P. Daian, S. Goldfeder, T. Kell, Y. Li, X. Zhao, I. Bentov, L. Breiden- bach, and A. Juels, “Flash Boys 2.0: Frontrunning in Decentralized Exchanges, Miner Extractable Value, and Consensus Instability,” in 2020 IEEE Symposium on Security and Privacy (SP). IEEE, 2020, pp. 910–927.

Yang, S. et al. (2022) SOK: Mev countermeasures: Theory and practice, [2212.05111v1] SoK: MEV Countermeasures: Theory and Practice. Available at: http://export.arxiv.org/abs/2212.05111v1 (Accessed: 20 June 2023). 

K. Qin, L. Zhou, P. Gamito, P. Jovanovic, and A. Gervais, “An Empir- ical Study of DeFi Liquidations: Incentives, Risks, and Instabilities,” in Proceedings of the 21st ACM Internet Measurement Conference, 2021, pp. 336–350.

L. Zhou, K. Qin, C. F. Torres, D. V. Le, and A. Gervais, “High- Frequency Trading on Decentralized On-Chain Exchanges,” in 2021 IEEE Symposium on Security and Privacy (SP). IEEE, 2021, pp. 428–445.

I. Tsabary, M. Yechieli, A. Manuskin, and I. Eyal, “MAD-HTLC: because HTLC is crazy-cheap to attack,” in 2021 IEEE Symposium on Security and Privacy (SP). IEEE, 2021, pp. 1230–1248.

F. Winzer, B. Herd, and S. Faust, “Temporary Censorship Attacks in the Presence of Rational Miners,” in 2019 IEEE European Symposium on Security and Privacy Workshops (EuroS&PW). IEEE, 2019, pp. 357–366.

Eskandari, S., Moosavi, S. and Clark, J. (2019) Sok: Transparent dishonesty: Front-running attacks on Blockchain, arXiv.org. Available at: https://arxiv.org/abs/1902.05164 (Accessed: 20 June 2023). 

EigenPhi, “Sandwich overview | EigenPhi,” 2022. [Online]. Available: https://eigenphi.io/mev/ethereum/sandwich

M. Carlsten, H. Kalodner, S. M. Weinberg, and A. Narayanan, “On the Instability of Bitcoin Without the Block Reward,” in Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communi- cations Security, 2016, pp. 154–167.

Flashbots, “Transparency dashboard | Flashbots,” 2022. [Online]. Available: https://dashboard.flashbots.net/

Proposer/block builder separation-friendly fee market designs - eco- nomics - ethereum research. [Online]. Available: https://ethresear.ch/t/ proposer- block- builder- separation- friendly- fee- market- designs/9725

Hasu and S. Gosselin. Why run mev-boost? | Flashbots. [Online]. Available: https://writings.flashbots.net/why-run-mevboost/

M. Kelkar, F. Zhang, S. Goldfeder, and A. Juels, “Order-Fairness for Byzantine Consensus,” in Annual International Cryptology Confer-
ence. Springer, 2020, pp. 451–480.

K. Kursawe, “Wendy, the Good Little Fairness Widget: Achieving Order Fairness for Blockchains,” in Proceedings of the 2nd ACM Conference on Advances in Financial Technologies, 2020, pp. 25–36.

Y. Zhang, S. Setty, Q. Chen, L. Zhou, and L. Alvisi, “Byzantine Ordered Consensus without Byzantine Oligarchy,” in 14th USENIX Symposium on Operating Systems Design and Implementation (OSDI 20), 2020, pp. 633–649.

L. Baird, A. Luykx, and P. Madsen, “Hedera Tech- nical Insights: Fair Timestamping and Fair Ordering of Transactions,” 2022. [Online]. Available: https://hedera.com/blog/ fair- timestamping- and- fair- ordering- of- transactions


```{bibliography}
:filter: docname in docnames
```
