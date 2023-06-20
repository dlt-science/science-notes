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



## Solutions and Future Directions

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


```{bibliography}
:filter: docname in docnames
```
