
# Staking and Reward Mechanisms in PoS Protocols

<ins>**Innovation & Ideation**</ins>

```{admonition} Key Insights
:class: tip
- There are various applications of PoS-based System evovling using diverse rewar mechanism.
- Reward mechanism is a critical aspect, affecting both incentive structures and system decentralization.
- There is a trade-off: the more open the staking process is, the more inequality the reward distribution tends to be.
- The way of how PoS is implemented greatly matters its equality and decentralisation.
- We need to critically think about variouscPoS protocols. Not only know the high return rate, but also realise the centralisation and risks in different systems.
```

## Introduction

`````{margin} **Proof-of-Work (PoW)**
Proof-of-Work (PoW) is a consensus algorithm where participants, termed miners, solve complex computational problems to validate and record transactions. This mechanism, while secure, is often associated with significant energy consumption due to the required computational power. Generally, the more computing power one has, the more reward one could earn.
`````

`````{margin} **Proof-of-Stake (PoS)**
 Proof-of-Stake (PoS) is a consensus algorithm where participants, known as validators, demonstrate ownership of a certain amount of cryptocurrency to validate and create new blocks. Unlike PoW, PoS offers energy efficiency by not relying on extensive computational tasks and instead emphasizes asset collateralization for network security. Rather than relying on computational power, PoS protocols leverage the "stake" or amount of cryptocurrency a user holds.
`````
Blockchain's trustless foundation removes the necessity for inter-party trust, with its security and decentralization hinging on a fair consensus mechanisms while Proof-of-Work (PoW) and Proof-of-Stake (PoS) are currently the two most commonly used consensus protocols. Proof-of-Work (PoW) involves computating power competition and thus is critisized for its environmental footprint and potential inequities in mining. Conversely, Proof-of-Stake (PoS) operates on asset collateralization i.e., tokens and is getting popular due to its energy efficiency but faces risks of wealth concentration. This article summarizing Dr. Sheng-Nan Li's talk, which delves into the nuances and challenges of PoS protocols, especially focusing on staking and reward mechanisms.

We'll begin by dissecting the different reward mechanisms inherent to various proof-of-stake protocols. Understanding these mechanisms is foundational to grasping the incentives that drive user participation. Secondly, by measuring the decentralization of these proof-of-stake protocols, we can further understand the Reward Distribution Decentralization. Thirdly, we move to a general framework for modeling proof-of-stake protocols presnted by Dr.Li. This agent-based modeling approach allows us to evaluate decentralization from a more granular perspective. Lastly, we'll delve into a real-world application. Hedera serves as a prime example, helping elucidate the modeling framework and showcasing the practical implications of Dr. Li's findings.

## Overview of PoS Reward Mechanisms

To discuss the properties of staking and reward distribution in PoS, Ethereum 2.0, Cardano, and Polkadot are selected as examples.

### Ethereum 2.0

Ethereum 2.0, launched on September 15, 2022, signifies a major shift in the blockchain realm by adopting the Proof of Stake consensus protocol, specifically the Casper-FFG and LMD-GHOST versions. Central to this new protocol are validators as the main actors. The attestation process involves a minimum of 128 validators who propose attestations or votes as the attesting committee, from which 16 are chosen as Aggregators. Additionally, one validator is designated as the block proposer to propose one block per slot.

The reward with a sum_weight of 64 is structured based on various criteria as:
- A timely vote for the correct target earns a weight of 14.
- A timely vote for the correct source checkpoint earns a weight of 26.
- A timely vote for the correct head block earns a weight of 14.
- Participating in a sync committee earns a weight of 2.
- If a validator successfully proposes a block in the appropriate slot, they are rewarded with a weight of 8. This reward is approximately 7/8 of the attesting reward.

 Additionally, a key concept of the consensus and staking aspect is the validator effective balance, which is capped at 32 ETH and triggers ejection when it reaches 16 ETH. It takes 12 seconds for a slot and around 6.5 minutes for a Epoch (32 slots). Reward payout happens after two epochs following the finalization of a block. For the reward distribution, we have:

\[
    \text{base\_reward} = \frac{\text{Base\_Reward\_Factor (64)}}{\text{Base\_Reward\_Per\_Epoch(4)} \times \sqrt{\sum{\text{active\_balance}}}} \times \text{effective\_balance}
\]

A timely attester:

\[ \text{Inclusion speed reward} = \text{base\_reward} \times \frac{1}{\text{Inclusion\_distance}} \times \frac{7}{8} \]

 On the other hand, penalties are in place for cases such as not making timely voting on correct head, source or target but there is no penalty if a proposer misses a slot. The more severe panlty is slashing for proposers who propose two different blocks for the same slot and for attesters who makes 'surround voting' or 'doublel voting', resulting in a 36-day removal and the burning of a fraction of the staked ether.

### Cardano
Cardano, with its Shelley update introduced on July 29, 2020, employs the Ouroboros Praos consensus protocol (PoS). Central to its system are stake pools consisting of stake pool operators (SPOs), who act as slot leaders responsible for producing blocks. Additionally, there are delegators who can allocate their stakes to these pools. Cardano's system divides time into epochs, with each epoch containing 432,000 slots (1 second) that equate to five days. Rewards are dispensed at the end of each epoch. Cardano introduces a unique staking system with its "Pledging" or self-staking mechanism, allowing stake pool operators to commit their own ADA cryptocurrency, influencing the rewards they can potentially earn. To ensure the network remains decentralized and no single pool gains excessive control, Cardano has implemented a "Saturation Parameter." This parameter sets an optimal size for each pool, beyond which rewards begin to diminish, encouraging a balanced distribution of stakes across various pools. Additionally, the total rewards, sourced from a maximum supply, are influenced by factors like the pool's performance, and they are distributed proportionally based on produced blocks and the pool's total active stake. After deducting declared fees for pool operation, the remaining rewards are shared proportionally among all delegators, including the pool operator.

### Polkadot
Launched in May 2020, Polkadot operates using a Nominated Proof of Stake (NPoS) consensus mechanism. In this system, nominators can select up to 16 validator candidates, with the active validator set capped at 297. These validators, once elected, are responsible for producing blocks in the relay chain and also accept proofs from collators, who collect transaction data and proofs from the parachains. Time is organized into eras, each lasting 24 hours, during which validators produce blocks. Reward payout happens at the end of every era, with the total rewards following an inflationary model, estimated at approximately 10% yearly by total stake. Validators earn era points for their contributions, which influence their rewards but are separate from their stakes. Notably, the rewards are generally equal among all validators but can vary based on the era points they've accumulated. Validators can also claim a commission fee, while nominators share the rewards among the top 256 nominators, proportionally to their stake. However, there are slashing mechanisms in place including penalties of a fixed percentage of the stake of validator slot range from 0.1% to 100% and kicking out range from removing from the list of candiates in the next election to removing from all the nominators' lists of trusted candidates, depending on the severity of the violation.

Overall, PoS protocols of Ethereum 2.0, Cardano, and Ethereum 2.0 differ in the terminologies, the main actors and their roles, the incentive and reward distribution, and other technical details. This leads to the next question that whether the rewards are fairly distributed to the validators in real PoS-Platforms.

| Coin                  | Launch  | Roles                        | Reward period    | Slashing | Key Notes                              |
|-----------------------|---------|------------------------------|------------------|----------|----------------------------------------|
| Ethereum 2.0 (PoS)    | Sep-22  | Proposer/ Attesting committee| Epoch (~6.5mins) | YES      | capped at 32 ETH                       |
| Cardano (PoS)         | Jul-20  | Pool operator/ delegator     | Epoch (5 days)   | NO       | Pledge factor/ saturation              |
| Polkadot (NPoS)       | May-20  | Validator/ Nominator/ Collator| Era (24 hours)   | YES      | Era points/ equally distribute         |

## Decentralization of Reward Distribution

To evaluate the decentralization of reward distribution, particularly the distribution of wealth among participants, two primary metrics are employed:

### Gini index

The Gini index is the most frequently used inequality index of income or wealth distribution among a nation's population. It can theoretically range from 0 (complete equality) to 1 (complete inequality, where one participant possesses everything while others have nothing). In PoW-based systems, the Gini index measures the inequality of mining revenue distribution among miners. The Gini index is applied to the stakes and rewards of validators as:

\[
G = \frac{\sum_{i=1}^{N} \sum_{j=1}^{N} |x_i - x_j|}{2n \sum_{i=1}^{N} x_i}
\]

where \(x_i\) is the stake or reward of a validator \(i\), and there are \(N\) validators.

### Nakamoto Coefficient

The Nakamoto Coefficient quantifies decentralization by specifying the number of participants needed to compromise the system. In this setting, it is based on the stakes of validators. It specifies the minimum share of participants required to hold more than 50% of the staking power. A higher Nakamoto Coefficient indicates better decentralization of the protocol. It's expressed as:

\[
N_c = \frac{1}{n}\min \left( k \in [1,2,...,K] : S^{-1} \sum_{i=1}^{k} s_i > 0.5 \right)
\]

where \(s_i\) is the stake of validator \(i\) and there are \(N\) validators.

Diving deeper into the landscape, Polkadot and Cardano present contrasting approaches. Despite its limited set of validators, Polkadot has seen substantial growth in stake pools. On the other hand, with an unlimited validator set, Cardano recently noted that only around 40% of its pools receive rewards in each epoch. When analyzing the distribution patterns, Polkadot emerges as a leading player in both stake and reward distribution. Its design, which emphasizes equal reward distribution, has resulted in the lowest Gini Index and the most substantial Nakamoto Coefficient. In contrast, Cardano, despite its open validator set, exhibits a relatively high level of inequality.

In essence, how PoS is implemented plays a crucial role in determining both its equality and decentralization.

## General Framework of PoS Modeling

To clarify components that characterize the staking and reward of PoS protocols and develop an evaluation framework for better protocol design, an extensible framework of modeling (D)PoSs is introduced by Dr. Li. The framework process is split into three parts:


**1. Planning the Total Reward Before the Reward Period:**
- **Determining Total Reward:** At the outset, it's imperative to finalize the aggregate reward for each period. This will dictate the incentive structure and, in turn, the behaviors of participants.
  - **Inflation Model Considerations:** By determining the total reward, one can conceptualize the inflation model. This might be pertinent to the economic sustainability of the protocol.
  - **Supply Dynamics:** Different systems have varied supply constraints—some might have a fixed supply, while others might allow for unlimited total supply. Depending on this, the reward structure might differ.
  - **Yearly Return Rate:** Some systems might want to establish a fixed annual percentage yield (APY), ensuring consistent returns over time.

**2. Designing the Staking Behaviors and the Reward Distribution During the Reward Period:**
- **Validator and Nominator Interplay:** The behavior and interactions between validators and nominators are foundational. One needs to consider which validators nominators would opt for and which behaviors would maximize rewards.
  - **Behavior Incentives:** The protocol should incentivize behaviors that align with the system's goals, ensuring network security and efficiency.
  - **Reward Distribution Dynamics:** Decision-making around how rewards are split among validators is pivotal. Whether rewards should be equally distributed or be proportional to the total stake is a matter for consideration.

**3. Measurement After Prolonged Operation:**
- **Evaluating Protocol Performance:** After the system has been operational for a significant duration, it's crucial to assess its performance.
  - **Gini Index, Nike Model, and HHI Index:** These metrics will aid in gauging whether rewards have been disseminated equitably or fairly within the system. They provide insights into the distribution dynamics and potential disparities in reward allocation.

## Use-case: Staking Model in Hedera

Hedera Hashgraph, recognized for its unique hashgraph consensus algorithm, presents an intriguing case study for staking models. This consensus mechanism operates based on the principles of a Directed Acyclic Graph (DAG). Distinct from traditional blockchain systems, the hashgraph methodology propels transaction processing at speeds that significantly outpace conventional proof-of-work blockchains.

A negative value of its Degree Assortativity for weekly transaction networks suggests a disassortative nature, indicating that a significant portion of the participants likely transact through a select few dominant intermediaries. When examining wealth distribution within the network, it is observed that early users, those who joined during the initial month or year, tend to hold a substantial amount of tokens. However, a shift towards a more equitable distribution is evident post mid-2022.

The dynamics of account growth, the rate of Daily Active Accounts (DAA), and the volume of daily transaction fees are used in empirical data analytics.

Firstly, The upward trajectory in daily transaction fees was captured and predicted using a log-log function. This critical metric played a pivotal role in strategizing future reward planning. Operating under the assumption that rewards would be exclusively sourced from transaction fees, devoid of inflation, the annual total reward was organized in varied trends, such as increasing, steady, or decreasing.

Secondly, in terms of modeling the staking behaviors such as staking selection, stakers, in their decision-making, rely heavily on time-weighted values of a validator's historical performance. This takes into account factors like previous participation levels and reward rates. Delving into saturation dynamics, it was noted that the historical reward rate undergoes dilution when incoming stakes breach a set maximum cap, and drops to zero when they fall beneath a minimum threshold. Validator performance and staker preferences were also assessed. Two memory functions, which attribute weight to a node's engagement level and reward rate for each reward period, were combined to derive a comprehensive score for each node.

Thirdly, the daily total reward is distributed among nodes and stakers. While each node's daily reward is based on the node's latest participation level compared to the threshold and the share of node's receiving stakes, each staker's daily reward is based on the participation level of the node that the staker selected and the share of stake among the staker's selected node's total receiving staking.

Finally, the evaluation of decentralization using the Gini index suggests rewards are more equitably distributed among validators (nodes) than stakers. Moreover, the Nakamoto Coefficient indicates that a voting-weighted system is more decentralized than the "one stake one vote" approach.



## Conclusion

Modeling (D)PoSs offers insights into the long-term implications of protocol adjustments and enhances our understanding of the behavioral tendencies of validators or stakers. It also highlights their influence on system decentralization. As we delve deeper into various PoS protocols, it's crucial to recognize not just the attractive return rates but also the centralization and potential risks inherent in different systems.
