# A Comparative Analysis of Different Proof of Stake Consensus Mechanisms

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
- Platt et al.'s paper underscores the high energy consumption of Proof of Work (PoW) systems like Bitcoin and highlights the relative energy efficiency of Proof of Stake (PoS) systems.
- The energy usage of PoS blockchains is significantly influenced by the hardware used by validators, emphasizing the importance of hardware selection in these systems.
- There are notable variations in energy consumption among different PoS systems, influenced by various factors such as system design, implementation, and the number of validator nodes
- Hedera, a permissioned DLT system, showcased the lowest energy consumption per transaction in the study. This highlights Hedera's superior efficiency and positions it as a sustainable option in the blockchain sector.
- The authors developed a unique model to measure energy consumption on a per transaction basis in PoS blockchains, providing a nuanced understanding of energy usage
- The research advocates for a transition from energy-intensive PoW systems to more efficient PoS systems, suggesting that energy-saving hardware could drastically reduce energy consumption in PoS systems. 
```

## Introduction

Platt et al. {cite}`platt2021energy` in their academic paper, "The Energy Footprint of Blockchain Consensus Mechanisms Beyond Proof-of-Work", delves into the energy implications of different blockchain consensus mechanisms, primarily Proof of Work (PoW) and Proof of Stake (PoS). The authors highlight the extreme energy consumption of PoW systems, exemplified by Bitcoin, which has attracted criticism due to its environmental impact. As an alternative, PoS mechanisms aim to be more energy-efficient. However, the paper underscores that the energy consumption of PoS blockchains also depends greatly on the type of hardware used by validators.

The authors make a comparative analysis of different PoS systems, shedding light on their energy consumption patterns. They argue that the energy efficiency of consensus mechanisms is a vital factor determining their effectiveness and suitability for use in distributed ledger technology (DLT) systems. Their work underscores the need for more focused research and understanding of the energy implications of these mechanisms in the rapidly evolving world of blockchain technology. 

## The Energy Intensity of Blockchain Consensus Mechanisms and Bitcoin's Overwhelming Energy Footprint

 Proof-of-Work (PoW) systems like Bitcoin are criticized for their high energy requirements, comparable to those of industrialized nations, due to their correlation with market capitalization {cite}`sedlmeir2020energy`. Proof-of-Work (PoW) is a mechanism designed to resist Sybil attacks, and it has been implemented in many of the initial cryptocurrencies {cite}`nakamoto2008bitcoin`. This raises sustainability concerns. Proof-of-Stake (PoS) systems, which prioritize validators with higher stakes in the native currency, are shown by Platt et al. {cite}`platt2021energy` to significantly reduce energy consumption. Despite this, Bitcoin's energy use dwarfs that of all analyzed PoS systems by at least two orders of magnitude, emphasizing the potential of PoS as a more sustainable alternative {cite}`ismail2019review`.

## Variation in Energy Footprint and Consumption Patterns Among PoS Systems

There are marked variations in energy consumption among PoS systems. Factors such as system design, implementation, hardware used, number of validator nodes, and system throughput contribute to this variation. Permissionless systems, in particular, display larger energy footprints, indicating that these factors significantly affect their energy efficiency. Furthermore, hardware used by validators greatly impacts PoS blockchains' energy consumption, with a validator node's energy use found to be independent of system throughput in the analyzed permissionless systems. Especially, less active permissionless systems demonstrate a higher energy demand per transaction due to lower throughput and a large number of validators {cite}`carter2021much`.

## Methodology Overview

In their study {cite}`platt2021energy`, the authors developed a fundamental energy consumption model specific to PoS blockchains. This model primarily considered the energy consumption on a per transaction basis, rather than the overall system's consumption. The authors assumed that the validating nodes would run on comparable server hardware types, regardless of network load. Thus, the overall energy requirement of a protocol was attributed exclusively to the number and the specific hardware configuration of the validator nodes. Three different hardware configurations were considered to cover the potential hardware variation and expected hardware usage: a single-board computer, a rackmount server for midsize and large enterprises, and a high-performance server. This holistic approach allowed for a nuanced analysis of energy consumption across PoS blockchains.

## Examination of PoS DLT Systems

```{figure} images/ETH2.0.png
---
width: 801px
height: 611px
name: eth_diagram
---
Ethereum 2.0's Consensus Mechanism.
```

```{figure} images/Hedera.png
---
width: 541px
height: 492px
name: hedera_diagram
---
Hedera's Consensus Mechanism.
```

The study {cite}`platt2021energy` examined several high market capitalization DLT systems employing a PoS consensus algorithm, including Ethereum 2.0 with 183,753 validators, Algorand with 1,126 validators, Cardano with 2,958 validators, Polkadot with 297 validators, Tezos with 399 validators, and Hedera with 21 validators. These systems, despite their shared usage of PoS, vary in numerous aspects such as minimum thresholds for validation and delegation, the need to lock-up stakes, and rewards for validators. These findings provide a comprehensive view of the energy consumption landscape in PoS-based blockchains.

- **Bitcoin:** The energy consumption of Bitcoin, which uses a Proof-of-Work (PoW) consensus mechanism, exceeds the energy consumption of all Proof-of-Stake (PoS)-based systems analyzed by at least two orders of magnitude.

- **Ethereum 2.0:** Ethereum 2.0, which is transitioning to a PoS consensus mechanism, is expected to have significantly lower energy consumption than Bitcoin. However, the exact energy consumption varies depending on the throughput of the system.

- **Algorand:** Algorand, a PoS-based permissionless system, has lower energy consumption than Bitcoin and Ethereum 2.0. The energy consumption per transaction is relatively low due to its high throughput and small number of validators {cite}`gilad2017algorand`.

- **Cardano:** Cardano, another PoS-based system, also has lower energy consumption than Bitcoin. However, it consumes more energy than Algorand due to its lower throughput and higher number of validators.

- **Polkadot and Tezos:** These PoS-based systems have lower energy consumption than Bitcoin and Ethereum 2.0. However, their energy consumption is higher than that of Algorand and lower than that of Cardano.

- **Hedera:** Hedera, a permissioned system, has the lowest energy consumption per transaction among the systems analyzed. This is due to its high throughput and small number of validators. Transactions don't aggregate into blocks. Instead, they disseminate through a "gossip about gossip" protocol, where any new information acquired by a node is propagated exponentially quickly throughout the network {cite}`hedera2021gossip`.

## Results and Analysis Summary

The study {cite}`platt2021energy` conducted an in-depth analysis of various Distributed Ledger Technology (DLT) systems, focusing on their consensus mechanisms, number of validators, throughput, and energy consumption. The findings highlighted the necessity of transitioning from energy-intensive Proof of Work (PoW) systems, such as Bitcoin, to more energy-efficient Proof of Stake (PoS) systems.

Bitcoin's PoW system was found to be at least three orders of magnitude higher in energy consumption than the most energy-consuming PoS system. Most PoS systems were found to consume less energy than the VisaNet payment network. 

Significant differences in energy consumption were observed among the PoS systems studied. These differences were attributed to the number of validators, the systems' throughput, and the type of hardware used by validators. For instance, Hedera, a permissioned system with 21 validators, showed the least energy consumption per transaction. Conversely, systems with more validators and lower throughput had higher energy demands.

The study identified the assumption that the number of validators is an affine function of throughput as a limitation. Future studies were recommended to consider the network-wide energy consumption beyond validator nodes for a more comprehensive understanding of the energy usage in DLT systems.

## Conclusion

Platt et al. {cite}`platt2021energy` emphasized the urgent need for transitioning from energy-intensive PoW systems to more efficient PoS systems. Their analysis reveals that by opting for energy-saving hardware, PoS systems could drastically lower their energy consumption, potentially outperforming even traditional central payment systems in terms of energy usage. This research injects optimism into the discourse around blockchain technology's role in addressing climate change. Moreover, it serves as an important call-to-action for blockchain developers and practitioners, urging them to prioritize energy efficiency in their system designs. Utilizing benchmarking frameworks to quantify the real energy usage could be especially beneficial for permissioned systems that strive for high performance {cite}`sedlmeir2021dlps`. In the future, more nuanced models and factors influencing validator count, beyond network throughput, could be considered for a more comprehensive understanding. 

<div style="text-align: right;font-weight: bold;">Ali Kathia</div>
<div style="text-align: right;font-style: italic;">June 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
