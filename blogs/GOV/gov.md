# Governance In DeFi

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
- The voting power in DeFi protocols becomes increasingly concentrated among a percentage of token holders over time in decentralised exchanges, lending protocols and yield aggregators.
- The paramount wallet addresses ranking within the top 5, 100, and 1000, exercise predominant influence over the voting power in the Balancer, Compound, Uniswap, and Yearn Finance protocols, with Compound displaying the least evidence of decentralisation.
- The most significant governance challenges identified by DeFi users are voter collusion, low participation rates, and voter apathy.
- To address vulnerabilities in DeFi governance, a novel voting mechanism resistant to sybil attacks called bond voting has been proposed.
- To enhance the manual parameter section, an AI-enabled adjustment solution has been demonstrated to automate governance mechanisms.
```

## Introduction

Decentralised finance (DeFi) has emerged as a potential substitute for traditional financial institutions, offering peer-to-peer transactions and a diverse range of services that democratise finance by enabling users to participate in protocol governance. However, several studies have suggested that the current governance mechanisms require improvements. This article provides an overview of findings associated with DeFi governance.

## Centralisation of Governance in DeFi Protocols

 `````{margin} **Lending Protocols**
  Lending Protocols are DeFi applications built on top of blockchain technology that allow users to lend and borrow cryptocurrency assets without the need for intermediaries such as banks or traditional financial institutions.
`````
`````{margin} **Decentralized Exchanges**
  Decentralized Exchanges (DeXs) are peer-to-peer trading platforms built on top of a blockchain that enable the direct exchange of cryptocurrency assets without the need for a central authority or intermediary.
`````
`````{margin} **Yield Aggregator**
  Yield Aggregator are DeFi applications that automate the process of seeking out the best yield opportunities for cryptocurrency assets, and provide users with a way to optimize their returns on investment.
`````

 Centralisation in DeFi has become a growing concern among researchers with several studies identifying a significant level of centrality in the governance mechanisms of DeFi protocol. Barbereau et al., {cite}`barbereau2022defi` found that the decentralisation of voting is significantly low with a majority of the voting power concentrated among a percentage of governance token holders. As evidenced by their findings, there was a significant degree of centrality, in lending protocols, decentralisd exchanges and yield aggregators. This research work employed case studies to comprehend the governance mechanisms of these protocols.

Similarly, result by Jensen et al. {cite}`jensen2021decentralized` demonstrate centrality in voting power with the protocols top 5, top 100, and top 1000 wallet addresses controlling majority of the voting power in Balancer, Compound, Uniswap and Yearn Finance protocols. In this study, the token holdings and users' wallets of protocols were analysed; Compound displayed the most evidence of centrality and Uniswap the least with the top 5 wallet addresses accounting for 42.1% and 12.05%, respectively.

Barbereau et al. {cite}`barbereau2022decentralised` ascertained that DeFi protocols become more centralised over time. In this longitudinal study, voting patterns demonstrated changes in the power dynamics as time progressed. The tendency for this centralisation of DeFi protocols is shown in [{numref}`gov_evolution`]. Furthermore, in analysing the governance structures of DeFi protocols, Stroponiati et al. {cite}`stroponiati5decentralized` ascribed reward-based economic incentives as the significant cause behind the development of centralised structures.

```{figure} images/Govern.drawio.png
---
width: 750px
height: 260px
name: gov_evolution
---
The Tendency for Centralisation in DeFi Governance.
```

## Challenges & Vulnerability In DeFi Governance

`````{margin} **Voter Collusion**
  Voter Collusion refers to a situation where a group of voters collude together to manipulate the outcome of a voting process in their favor, typically by coordinating their votes to create a super majority.
`````

`````{margin} **Voter Apathy**
  Voter Apathy refers to a situation where token holders or members of the organisation do not actively participate in the voting process due to a lack of interest
`````

`````{margin} **Sybil Attack**
  Sybil attacks occur when an attacker generates multiple false identities to gain significant network control, thereby allocating more votes than expected.
`````

In investigating governance challenges, Ekal et al., {cite}`ekal2022defi` identified voter collusion, low participation rates, and voter apathy as the most significant challenges. This empirical investigation utilised an interview survey approach to collect data from protocol users. Furthermore, to address voter concentration vulnerabilities, Mohan et al. {cite}`mohan2022voting` proposed a novel voting mechanism called bond voting which is resistant to sybil attacks. The bond voting mechanism issues 'voting bonds' to voters, which essentially requires a commitment to stake an amount of tokens, for a time period to gain voting power. Therefore, by combining this time commitment with weighed voting with a time commitment, sybil attacks are more difficult. Quadratic voting, another solution to voting concentration, allows participants to convey both their preferences and the intensity of those preferences, however, the drawback of this mechanism is its vulnerability to sybil attacks, voter collusion and voter fraud {cite}`kiayias2022sok`.

## AI-enabled On-chain Governance

To enhance and automate governance mechanisms, Xu et al., {cite}`xu2023auto` demonstrated an AI-enabled parameter adjustment solution which is more efficient than current implementations. Specifically, the study employed Deep Q-network (DQN) reinforcement learning to investigate for automated parameter selection in a DeFi environment. Although a lending protocol was employed in the study, the model's application can extend to other categories of DeFi protocols as well. In investigating DAOs, Nabben {cite}`nabben2023governance` observes that GitcoinDAO also employs algorithmic governance in various organisational components such as monitoring the compliance with rules of the organisation.

## Conclusion

The vision of DeFi is to foster a democratic process of governance and sustain high levels of decentralisation. However, recent studies have highlighted significant centrality in DeFi governance mechanisms, indicating the need for improvements in the existing governance models. The studies analysed in this article have revealed that the majority of the voting power in several protocols is concentrated among the top token holders, with evidence of increasing centralisation over time. Moreover, DeFi has been found to face challenges in the voting and governance process. In view of some of these challenges, researchers have proposed novel solutions such as a bond voting and an AI-enabled parameter-selection solution to improve the current mechanisms. Given the importance of decentralisation in the underlying philosophy of DeFi, proposing more solutions to governance challenges is crucial for creating a more inclusive and democratic financial ecosystem. Therefore, continued research and development will certainly be required.

<div style="text-align: right;font-weight: bold;">Yimika Erinle</div>
<div style="text-align: right;font-style: italic;">April 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```