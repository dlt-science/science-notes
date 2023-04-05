# Governance In DeFi

```{admonition} Key Insights!
:class: tip
- The voting power in DeFi protocols becomes increasingly concentrated among a percentage of token holders over time in decentralised exchanges, lending protocols and yield aggregators.
- The paramount wallet addresses ranking within the top 5, 100, and 1000, exercise predominant influence over the voting power in the Balancer, Compound, Uniswap, and Yearn Finance protocols, with Compound displaying the least evidence of decentrality
- The most significant governance challenges identified by DeFi users are voter collusion, low participation rates, and voter apathy.
- To address vulnerabilities in DeFi governance, a novel voting mechanism resistant to sybil attacks called bond voting has been proposed.
- To enhance the manual parameter section, an AI-enabled adjustment solution has been demonstrated to automate governance mechanisms.
```

## Introduction

Decentralized finance (DeFi) has emerged as a potential substitute for traditional financial institutions, offering peer-to-peer transactions and a diverse range of services that democratize finance by enabling users to participate in protocol governance. However, several studies have suggested that the current governance mechanisms require improvements. This article provides an overview of findings associated with DeFi governance.

## Centralised Governance in DeFi Protocols

 `````{margin} **What are Lending Protocols ?**
  Lending protocols are decentralized finance (DeFi) applications built on top of blockchain technology that allow users to lend and borrow cryptocurrency assets without the need for intermediaries such as banks or traditional financial institutions.
`````
`````{margin} **What are Decentralised Exchanges ?**
  Decentralized exchanges (DeXs) are peer-to-peer trading platforms built on top of a blockchain that enable the direct exchange of cryptocurrency assets without the need for a central authority or intermediary.
`````
`````{margin} **What are Yield Aggregators ?**
  Yield aggregator are a decentralized finance (DeFi) applications that automate the process of seeking out the best yield opportunities for cryptocurrency assets, and provide users with a way to optimize their returns on investment.
`````

 Several studies have identified a significant level of centrality in the governance mechanisms of DeFi protocol. Barbereau et al., {cite}`barbereau2022defi` found that the decentrality of voting in DeFi is significantly low with a majority of the voting power concentrated among a percentage of governance token holders. As evidenced by their findings, there was a significant degree of centrality, in lending protocols, decentralisd exchanges and yield aggregators. This study used case studies to comprehend the governance mechanisms of these protocols.

Similarly, Jensen et al. {cite}`jensen2021decentralized` results demonstrate centrality in voting power with the protcols top 5, top 100, and top 1000 wallet addresses controlling majority of the voting power in Balancer, Compound, Uniswap and Yearn Finance protocols. In this study, the token holdings and users' wallets of protocols were analysed; Compound displayed the most evidence of centrality and Uniswap the least with the top 5 wallet addresses accounting for 42.1% and 12.05%, respectively.

Barbereau et al. {cite}`barbereau2022decentralised` ascertained that DeFi protocols become more centralized over time. In this longitudinal study, voting patterns demonstrated changes in the voting power dynamics over time. Furthermore, in analysing the governance structures of DeFi protocols, Stroponiati et al. {cite}`stroponiati5decentralized` ascribed reward-based economic incentives as the significant cause behind the development of centralized structures.

```{figure} images/Govern.drawio.png
---
width: 750px
height: 260px
name: gov_evolution
---
The Evolution of DeFi Governance.
```
 
## Challenges & Vulnerability In DeFi Governance

`````{margin} **What is Voter Collusion ?**
  Voter collusion refers to a situation where a group of voters collude together to manipulate the outcome of a voting process in their favor, typically by coordinating their votes to create a supermajority.
`````

`````{margin} **What is Voter Apathy ?**
  Voter apathy refers to a situation where token holders or members of the organization do not actively participate in the voting process due to a lack of interest
`````

In investigating governance challenges, Ekal et al., {cite}`ekal2022defi` identified voter collusion, low participation rates, and voter apathy as the most significant challenges. This empirical investigation utilised an interview survey approach to collect data from protocol users. Furthermore, to address vulnerabilities, Mohan et al. {cite}`mohan2022voting` proposed a novel voting mechanism resistant to sybil attacks called bond voting. This solution factors in time commitment to be resistant to plutocracy. 

## AI-enabled On-chain Governance

To enhance and automate governance mechanisms, Xu et al., {cite}`xu2023auto` demonstrated an AI-enabled parameter adjustment solution which is more efficent than current current implementations. Specifically, the study employed Deep Q-network (DQN) reinforcement learning to investigate for automated parameter selection in a DeFi environment. Although a lending protocol was employed in the study, the model's application can extend to other categories of DeFi protocols as well. In investigating DAOs, Nabben {cite}`nabben2023governance` observes that GitcoinDAO also employs algorithmic governance in various organizational components such as monitoring the compliance with organizsational rules.

observation is that GitcoinDAO employs algorithmic governance in various organizational components and at the same time necessitates the regulation of the algorithmic processes initiated by the community in an open and decentralized manner

## Conclusion

The vision of DeFi is to forster a democratic process of governance and sustain high levels of decentrality  finance in the process. However, recent studies have highlighted significant centrality in DeFi governance mechanisms, indicating the need for improvements in the existing governance models. The studies analysed in this article have revealed that the majority of the voting power in several protocols is concentrated among the top token holders, with evidence of increasing centralization over time. Moreover, DeFi governance has been found to face challenges the voting and governance process. In view of these challenges, researchers have proposed novel solutions such as a bond voting and a AI-enabled parameter selection solution to improve the current mechanisms. In conclusion, continued research and development in DeFi governance are crucial for ensuring its long-term sustainability and success.


<!-- ## References
```
{bibliography}
``` -->