# Flash Loan Attacks in Decentralized Finance: A Comprehensive Review

<ins>**Academic insights**</ins>

## Key insights

- Flash loans, a distinct DeFi feature, offer uncollateralized loans within a single transaction, providing liquidity for various strategies. Flash loan attacks exploit DeFi vulnerabilities, aiming for high profits with minimal risk, resulting in substantial financial losses across multiple DeFi platforms.

- Attackers use methods like oracle and governance manipulation, front running, and liquidity removal to exploit protocol vulnerabilities.

- Notable flash loan attack cases involve price oracles, governance manipulation, and liquidity drainage, showcasing the challenges in securing DeFi protocols. 

- Defensive strategies, such as transaction monitoring, requiring approval for flash loan usage, and improved oracle designs, aim to mitigate flash loan attacks. However, the evolving nature of attacks continues to challenge their effectiveness.

- Ongoing research in monitoring, analytics, incentive mechanisms, and oracle designs is crucial to achieve stability in DeFi and maximize its potential. Security challenges persist due to the open and interconnected nature of DeFi protocols.

## Abstract

Flash loans, a unique feature of decentralized finance (DeFi), facilitate uncollateralized loans within a single blockchain transaction. However, they also introduce a new class of attacks that have stolen millions from DeFi protocols. This blog provides an in-depth review of academic literature on flash loan attacks, analyzing attack incentives, methods, notable cases, and emerging defensive techniques. The aim is to shed light on the complexities of securing business logic and economic incentives within an open DeFi ecosystem.

## Introduction

Decentralized finance (DeFi) seeks to replicate traditional financial services, such as lending and trading, using blockchain smart contracts. One notable feature is flash loans—uncollateralized loans that must be repaid within the same transaction [[1]](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_11). Flash loans alleviate liquidity constraints for arbitrage and hedging strategies. However, they also equip potential attackers with capital for market manipulation.

In a flash loan attack, the borrower exploits vulnerabilities to extract profits exceeding the small loan fee. For instance, manipulating oracle prices to secure loans larger than what collateral would permit [[2]](https://arxiv.org/abs/2011.13260). Flash loan attacks have resulted in over $750 million in losses across various DeFi platforms [[3]](https://defiyield.app/incidents). 

This blog reviews academic literature that analyzes flash loan attacks in DeFi. First, we discuss attacker incentives and common methods. Next, we delve into prominent attack cases and their measurable impacts. Finally, we explore emerging defensive techniques and the remaining challenges. This examination highlights the novel risks posed by flash loans and the difficulties in balancing innovation and security in decentralized systems.

Flash loans leverage the atomicity of blockchain transactions—either all state changes succeed, or all are reverted. This ensures loan repayment before changes take effect [[1]](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_11). Collateral is unnecessary since no counterparty risk is involved. Borrowers only need to pay a small fee (e.g., 0.09%) to the lending pool, making loans capital efficient.

```{figure} images/flow.png
---
width: 801px
height: 611px
name: Flashloan_attack
---
Flashloan attack.
```

Lenders benefit from fee revenue, and borrowing demand boosts overall pool liquidity. However, attackers exploit the fact that flash loans provide almost unlimited capital for market manipulation within a single transaction. Successful attacks yield profits far exceeding the fractional loan fee.

## Attack Incentives and Methods

The central incentive for flash loan attacks is to gain substantial profits with minimal risk. Attacks extract value from DeFi protocols before changes are reverted due to failed repayment. Importantly, there is essentially no cost to attempting attacks repeatedly [[4]](https://www.mdpi.com/2624-6511/21/1/7). 

Typical attack methods include:

- **Oracle manipulation:** Borrowed assets are utilized to manipulate price feeds before acquiring undercollateralized loans or liquidations [[5]](https://arxiv.org/abs/2201.08621).

- **Governance manipulation:** Flash-borrowed assets enhance voting power to approve adverse proposals [[6]](https://arxiv.org/abs/1904.05234).

- **Front running:** Detecting arbitrage transactions and front-running them with more favorable rates for the attacker [[7]](https://eprint.iacr.org/2020/1272). 

- **Removal of liquidity:** Draining pooled reserves through flash borrowing to disable markets or deposit contracts [[8]](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_11).

These techniques combine borrowed capital with issues in incentive design, oracle integrity, and contract logic. Successful attacks across multiple protocols demonstrate how interconnectivity amplifies vulnerabilities.

## Prominent Attack Cases

Flash loan attacks emerged in 2020, coinciding with the growth of DeFi lending. Early cases involving price oracles include bZx (February 2020, \$1 million), Harvest Finance (October 2020, \$24 million), and PancakeBunny (May 2021, $200 million) [[3]](https://defiyield.app/incidents)[[7]](https://eprint.iacr.org/2020/1272). The persistence of oracle attacks highlights the challenges in designing secure oracles. 

Governance attacks have also been demonstrated via flash loans, as seen in the manipulation of Yam voting (August 2020) [[6]](https://arxiv.org/abs/1904.05234). Recent attacks like Beanstalk (April 2022, $182 million) reveal how flash loans can swiftly drain liquidity from deposit pools by exploiting redemption calculations.

In total, 12 of the top 20 DeFi exploits by profit involved flash loans [[3]](https://defiyield.app/incidents), with estimated losses exceeding $750 million. These incidents underscore how flash loans enable complex manipulation that is challenging to anticipate. Attacks are growing in sophistication by combining multiple techniques.

## Emerging Defensive Techniques

In response to rampant flash loan attacks, several defensive techniques have emerged. One approach involves transaction monitoring and the detection of common attack patterns, such as rapid pumping and dumping of oracles [[10]](https://arxiv.org/abs/2104.15068). This allows for preemptive action against the attack and transaction reversals.

Another mitigation strategy is to require approval for flash loan usage in a protocol's smart contracts [[11]](https://ieeexplore.ieee.org/abstract/document/9908104). While this restricts manipulation using flash loans, it may also compromise the intended flexibility of flash loans. 

At the protocol level, leveraging time-weighted average pricing via oracles helps reduce manipulation, as does using the maximum across multiple oracles [[12]](https://makerdao.com/en/whitepaper/#oracle-price-feeds). However, oracle designs remain a challenge. Additionally, proposals to share liquidity across central and decentralized exchanges can mitigate the impact of liquidity attacks [[13]](https://dl.acm.org/doi/10.5555/3481544.3481549).

Despite these defenses, the effectiveness remains elusive as attacks continue to grow more sophisticated. Inherent challenges persist in securing economic protocols atop public blockchains that permit open access. 

## Conclusion

In summary, flash loans offer both capital efficiency and the potential for manipulation. Numerous DeFi protocols and users have fallen victim to sophisticated attacks, resulting in damages exceeding $750 million to date. Technical and economic solutions are still evolving. Ongoing research in monitoring, analytics, and incentive mechanisms is crucial to achieving stability and unlocking the potential of DeFi.

<div style="text-align: right;font-weight: bold;">Arafath Shariff</div>
<div style="text-align: right;font-style: italic;">October 2023</div>

## References

[1] K. Qin et al., "Attacking DeFi Ecosystem with Flash Loans for Fun and Profit," Proc. of FC, 2021.

[2] Y. Marcus et al., “DeFi Attacks: Flash Loans and Centralization,” arXiv:2011.13260, 2020. 

[3] DeFiYield, “DeFi Hacks/Exploits Tracker,” DeFiYield, Accessed Feb. 2023.

[4] N. Melab et al., “Ethereum Smart Contract Security: a Survey,” Intl. J. of Services Computing, 2021.

[5] X. Li et al., “Statistical Model Checking of Ethereum-Based DeFi Flash Loan Attacks,” arXiv:2201.08621, 2022.

[6] P. Daian et al., “Flash Boys 2.0: Frontrunning in DeFi,” arXiv:1904.05234, 2019.

[7] L. Zhou et al., “High-Frequency Trading on Decentralized On-Chain Exchanges,” Proc. of S&P, 2021. 

[8] K. Qin et al., “Attacking the DeFi Ecosystem with Flash Loans for Fun and Profit,” Proc. of FC, 2021. 

[9] DeFiYield, “DeFi Attacks 2020,” DeFiYield, 2020.

[10] S. Wu et al., “DefiRanger: Detecting Price Manipulation Attacks on DeFi Applications,” arXiv:2104.15068, 2021.

[11] B. Liu et al., “Guarding DeFi Against Flash Loan Attacks,” Proc. of ICCCN, 2022. 

[12] MakerDAO, “Oracles V2,” MakerDAO Whitepaper, 2019.

[13] K. Croman et al., “On Combining Privacy and Decentralization in Distributed Ledger Technology,” Proc. of FC, 2022.