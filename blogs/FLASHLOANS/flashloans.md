# Flash Loan Attacks in Decentralized Finance

<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- Flash loans, a distinct DeFi feature, offer uncollateralied loans within a single transaction, providing liquidity for various strategies. Flash loan attacks exploit DeFi vulnerabilities, aiming for high profits with minimal risk, resulting in substantial financial losses across multiple DeFi platforms.

- Attackers use methods like oracle and governance manipulation, front running, and liquidity removal to exploit protocol vulnerabilities.

- Notable flash loan attacks involve price oracles, governance manipulation, and liquidity drainage, showcasing the challenges in securing DeFi protocols. 

- Defensive strategies, such as transaction monitoring, requiring approval for flash loan usage, and improved oracle designs, aim to mitigate flash loan attacks. However, the evolving nature of attacks continues to challenge their effectiveness.

- Ongoing research in monitoring, analytics, incentive mechanisms, and oracle designs is crucial to achieve stability in DeFi and maximize its potential. Security challenges persist due to the open and interconnected nature of DeFi protocols.
```



## Abstract

Flash loans, a unique feature of decentralized finance (DeFi), facilitate uncollateralized loans within a single blockchain transaction. However, they also introduce a new class of attacks that have stolen millions from DeFi protocols. This blog provides an in-depth review of academic literature on flash loan attacks, analyzing attack incentives, methods, notable cases, and emerging defensive techniques. The aim is to shed light on the complexities of securing business logic and economic incentives within an open DeFi ecosystem.

## Introduction

Decentralized finance (DeFi) seeks to replicate traditional financial services, such as lending and trading, using blockchain smart contracts. One notable feature is flash loans—uncollateralized loans that must be repaid within the same transaction {cite}`aaveFlashLoans`. Flash loans alleviate liquidity constraints for arbitrage and hedging strategies. However, they also equip potential attackers with capital for market manipulation.

In a flash loan attack, the borrower exploits vulnerabilities to extract profits exceeding the small loan fee. For instance, manipulating oracle prices to secure loans larger than what collateral would permit {cite}`aaveFlashLoans`. Flash loan attacks have resulted in over $750 million in losses across various DeFi platforms {cite}`DeFi`. 

This blog reviews academic literature that analyzes flash loan attacks in DeFi. First, we discuss attacker incentives and common methods. Next, we delve into prominent attack cases and their measurable impacts. Finally, we explore emerging defensive techniques and the remaining challenges. This examination highlights the novel risks posed by flash loans and the difficulties in balancing innovation and security in decentralized systems.

Flash loans leverage the atomicity of blockchain transactions—either all state changes succeed, or all are reverted. This ensures loan repayment before changes take effect {cite}`aaveFlashLoans`. Collateral is unnecessary since no counterparty risk is involved. Borrowers only need to pay a small fee (e.g., 0.09%) to the lending pool, making loans capital efficient.
Lenders benefit from fee revenue, and borrowing demand boosts overall pool liquidity. However, attackers exploit the fact that flash loans provide almost unlimited capital for market manipulation within a single transaction. Successful attacks yield profits far exceeding the fractional loan fee.

## Attack Incentives and Methods
Flash lending made its debut in 2018 by the Marble Protocol and quickly found popularity with traders looking to profit off arbitrage opportunities between decentralized exchanges {cite}`aonFlashLoan`
The central incentive for flash loan attacks is to gain substantial profits with minimal risk. Attackerss extract value from DeFi protocols before changes are reverted due to failed repayment. Importantly, there is essentially no cost to attempting attacks repeatedly as long as the initial loan is repayed {cite}`coinledgerFlashLoans`. 

```{figure} images/floan.png
---
width: 550px
height: 330px
name: flashloan attack
---
Typical Flashloan Attack
```

Typical attack methods include:

- **Arbitrage:** Attackers can use flash loans to execute arbitrage transactions and profit from price differences between different decentralised exchanges (DEXs). Even though this attack may not be malevolent, reputable traders may nonetheless suffer losses as a result of it.

- **Price manipulation:** Attackers can use flash loans to manipulate the price of a cryptocurrency by artificially inflating or deflating its value. This can cause significant losses for traders who have placed orders based on manipulated prices.

- **Removal of liquidity/Smart contract exploits:** Draining pooled reserves through flash borrowing to disable markets or deposit contracts {cite}`acmdigitalloan`. Attackers can exploit DeFi smart contract vulnerabilities including reentrancy issues and integer overflow errors by using flash loans. They might be able to carry out more assaults or steal money from the protocol as a result{cite}`hackenFlashLoan`.

These techniques combine borrowed capital with issues in incentive design, oracle integrity, and contract logic. Successful attacks across multiple protocols demonstrate how interconnectivity amplifies vulnerabilities {cite}`aaveFlashLoans`.

## Prominent Attack Cases

Recent flash loan assaults have exposed the weaknesses and inherent risks of decentralised finance (DeFi) platforms. Euler Finance experienced a significant breach in March 2023, resulting in 197 million dollars in losses. The hacker was able to influence the platform's borrowing capabilities by exploiting a weakness in Euler's rate computation, notably within the eToken function. Similarly, Cream Finance had a flash loan attack in October 2021, resulting in losses of more than 130 million dollars. The attacker exploited flaws in Cream's yUSDVault in order to double the perceived value of particular tokens. Furthermore, in November 2021, bZx was subjected to a sophisticated hack that included two independent assaults that targeted flaws in the platform's reliance on a single oracle for pricing determination {cite}`hackenFlashLoan`.

In total, 12 of the top 20 DeFi exploits by profit involved flash loans {cite}`DeFi`, with estimated losses exceeding $750 million. These incidents underscore how flash loans enable complex manipulation that is challenging to anticipate. Attacks are growing in sophistication by combining multiple techniques. These real-world cases emphasize the utmost importance of fortifying security measures, including the implementation of multiple trusted oracles and robust risk management protocols, to fortify DeFi platforms against flash loan attacks and curtail potential financial losses.

## Emerging Defensive Techniques

In response to rampant flash loan attacks, several defensive techniques have emerged. One approach involves transaction monitoring and the detection of common attack patterns, such as rapid pumping and dumping of oracles. This allows for preemptive action against the attack and transaction reversals.

Another mitigation strategy is to require credit based approval for flash loan usage in a protocol’s smart contracts. While this restricts manipulation using flash loans, it may also compromise the intended flexibility of flash loans. Usage of models like the Recency, Frequency and Monetary model(RFM) which  is a marketing technique used to quantify user value based on recency, frequency, and monetary value of purchases. R measures how recently a user has made a purchase, F measures how often they purchase, and M measures how much money they spend. Users are segmented into groups based on their RFM scores to identify reliable users.

At the protocol level, leveraging time-weighted average pricing via oracles helps reduce manipulation, as does using the maximum across multiple oracles. However, oracle designs remain a challenge. Additionally, proposals to share liquidity across central and decentralized exchanges can mitigate the impact of liquidity attacks {cite}`springerTowardsSecure`.

Despite these defenses, the effectiveness remains elusive as attacks continue to grow more sophisticated. Inherent challenges persist in securing economic protocols atop public blockchains that permit open access{cite}`acmdigitalloan`. 

## Conclusion

In summary, flash loans offer both capital efficiency and the potential for manipulation. Numerous DeFi protocols and users have fallen victim to sophisticated attacks, resulting in damages exceeding $750 million to date. Technical and economic solutions are still evolving, but following best practices like third party auditing, re-entrancy guards and credit based checks can mitigate risks of such attacks immensely.

It is important to stay updated with the latest best practices and reports as the DeFi landscape is continuously evolving, by following best practices and being vigilant, we can help to build a safe DeFi landscape for everyone.

<div style="text-align: right;font-weight: bold;">Arafath Shariff</div>

## References

```{bibliography}
:filter: docname in docnames
```

