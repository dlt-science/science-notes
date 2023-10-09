# Evolutionary Approach for Concurrency Testing of Ripple Blockchain Consensus

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic Insight**</ins>

```{admonition} Key Insights
:class: tip
- The testing was exclusively conducted on the XRP algorithm, enabling a focused and in-depth analysis of its behavior and vulnerabilities without introducing complexity from other algorithms.
- Random testing may lack targeted coverage, efficiency, and reproducibility, making it ineffective for discovering specific types of bugs.
- The testbed is characterized by its relatively compact or constrained dimensions, indicating that it may encompass fewer resources, configurations, or components compared to larger-scale testing environments.
- Unlike previous blockchain systems such as Bitcoin and Ethereum, RCA is founded on the core principles of classical Byzantine fault tolerance consensus. Consequently, it may not be universally applicable.
- Every node in the Ripple network establishes its trust in a specific set of protocol participants, creating what is known as a Unique Node List (UNL). Therefore, the discussion does not revolve around the selection of trusted UNLs.

```

## Introduction

Blockchain systems are known to be vulnerable to concurrency bugs due to the inherent non-determinism in the delivery order of messages exchanged among distributed nodes. Detecting and addressing these bugs presents a significant challenge since they manifest only under specific conditions involving precise timing and the order of concurrent events during execution. The conventional systematic concurrency testing techniques, which endeavor to explore all possible message delivery sequences, are found to be impractical when applied to large-scale distributed systems such as blockchains. In contrast, random concurrency testing methods offer a pragmatic approach by seeking out bugs within randomly generated execution scenarios.

The research team {cite}`van2023ConAlgo` examined random concurrency testing in blockchain systems, focusing on the XRP Ledger of the Ripple blockchain. They emphasized the Ripple consensus algorithm, using an innovative evolutionary algorithm to enhance testing precision. The study demonstrates the effectiveness of random concurrency testing in uncovering blockchain concurrency bugs and the efficiency gains from the evolutionary algorithm. Their experiments not only confirmed known bugs but also discovered a previously unknown concurrency bug, highlighting the importance of rigorous testing for blockchain security and reliability.

## The RIPPLE Consensus Algorithm

 `````{margin} 
 **The execution of a consensus round consists of three phases:**
`````

`````{margin} **Open phase:**
 During this phase, nodes gather submitted transactions for inclusion in the next ledger and disseminate received transactions to other nodes in their Unique Node Lists (UNL).
`````

`````{margin} **Establish phase**
In this phase, nodes work to reach consensus on the set of transactions to be included in the next ledger. They exchange proposals for the next ledger in the form of proposal messages.
`````

`````{margin} **Validation Phase**
During this phase, nodes validate the ledger until 80% of nodes in their UNL agree on its hash. Once achieved, they execute ledger transactions, making them final and irreversible.
`````

The Ripple blockchain's XRP Ledger employs the Ripple Consensus Algorithm (RCA) to establish consensus on the global sequence of transaction blocks within the Ripple network. In contrast to earlier blockchain systems like Bitcoin and Ethereum, RCA builds upon the foundational principles of classical Byzantine fault tolerance (BFT) consensus and adheres to the fundamental design principles established by the seminal Practical Byzantine Fault Tolerance (PBFT) algorithm {cite}`cas1982byz`. Similar to PBFT, RCA exhibits Byzantine fault tolerance, meaning it can withstand certain malicious behaviors exhibited by network nodes, known as Byzantine behavior {cite}`lam1982byz`.
However, RCA diverges from PBFT in its approach. While PBFT assumes a known set of protocol participants, Ripple is tailored for the open membership ecosystem of the blockchain. Each node within the Ripple network defines the set of protocol participants it trusts, forming what is referred to as a Unique Node List (UNL). The protocol operates based on the votes from these nodes. RCA ensures correctness as long as at least 80% of the UNL nodes exhibit honest behavior, i.e., they are non-Byzantine in nature.

The Ripple consensus protocol operates through a series of synchronized consensus rounds, during which network nodes collectively agree on a set of transactions for execution. Importantly, Ripple nodes can receive transactions concurrently with the execution of these consensus rounds.
The design and implementation of the Ripple Consensus Algorithm (RCA) heavily rely on a shared concept of time and the synchronized execution of network nodes. Transitions between protocol steps are marked by predefined time intervals triggered by periodic timer messages. In Figure below, the protocol's execution illustrated using two client transactions submitted to nodes p1 and p2. For simplicity, message exchanges depicted solely between p1 and p2, with protocol messages represented as rectangles and internally created objects as diamonds.

```{figure} images/1.jpg
---
width: 750px
height: 260px
name: figure 3
---
Execution of the Ripple Consensus Algorithm (RCA).
```



**Correctness Specification: Safety and Liveness Properties**

The correctness of distributed consensus protocols is determined by the following safety and liveness properties {cite}`cach2011`:
  1. Agreement: No two nodes make different decisions.
  2. Validity: If a node makes a decision, it must be based on a proposal from another node.
  3. Integrity: No node makes a decision more than once.
  4. Termination: Every node eventually makes a decision.


In the context of blockchain consensus protocols, making a decision typically means reaching a consensus on which ledger to add to the blockchain. Agreement, validity, and integrity are safety properties designed to prevent negative outcomes during protocol execution. An example of a safety violation would be nodes disagreeing, potentially leading to network forks. Termination, on the other hand, is a liveness property ensuring that progress continues. A violation of termination could result in nodes failing to process client requests, rendering the system unresponsive.

## Random Testing

Random testing, also referred to as random search, stands as one of the most straightforward search algorithms to implement {cite}`arc2014hit` {cite}`bir2022sin`. It is frequently recommended as a foundational benchmark for assessing novel testing techniques {cite}`abd2020aut`. This approach involves a simple and unsophisticated sampling of the search space of schedules, with the aim of identifying potential concurrency bugs. Specifically, the algorithm generates N random schedules, executes them, and records those schedules that reveal one or more bugs. Two distinct variants of random testing are considered, distinguished by how they encode and execute the test cases.

### 1) Priority-based Random Testing
In priority-driven random testing, a message ordering extracted from the execution of a distributed system using the fundamental Partial Order Aware Concurrency Sampling (POS) algorithm {cite}`yuan2020effec` {cite}`yuan2018Par`. The approach involves randomly assigning a priority value to each message currently in transit and subsequently delivering these messages based on their assigned priorities. The allocation of varying priority values to these messages leads to diverse delivery sequences for the messages.

```{figure} images/2.jpg
---
width: 750px
height: 260px
name: figure 4
---
Execution of priority scheduling in a network with two nodes: p1 and p2.
```

### 2) Delay-based Random Testing:
Delay-driven random scheduling adapts early schedule perturbation techniques, typically used in the context of multithreaded concurrency {cite}`stol2002` {cite}`ede2002`, for application in distributed systems. Unlike introducing thread sleep statements to delay thread events, this approach postpones message execution by deferring their delivery. Each message is subjected to a random delay, and it is only dispatched after this designated timeout period has elapsed. This search algorithm employs a delay scheduling mechanism, where events are associated with specific time delays measured in milliseconds. By applying distinct delays to various events, it reshuffles their order, eliminating the need to collect messages in an inbox. Consequently, a test case is represented as a vector of integers, each denoting the time delay in milliseconds applied to a respective event. Figure below provides an illustrative example of an execution based on delay scheduling, utilizing the event mapping outlined in Figure 3b.

```{figure} images/3.jpg
---
width: 750px
height: 260px
name: figure 5
---
Execution of delay scheduling in a network with two nodes: p1 and p2.
```

### 3) Evolutionary Testing
The third search algorithm that was implemented and subjected to evaluation is the (µ + λ) evolutionary algorithm, as documented in reference {cite}`Weise2016`. This algorithm embarks on its journey with an initial population consisting of λ individuals. Within this population, a rigorous selection process ensues to identify the µ top-performing individuals, who are subsequently entrusted with the responsibility of producing λ offspring. These offspring emerge through the amalgamation of their parent solutions, an intricate process involving the utilization of crossover and mutation operators, thoughtfully outlined within the recombination function.     

As the algorithm progresses, it perpetuates this generational cycle by designating the best µ individuals from the preceding generation as parents for the subsequent one. This dynamic shift occurs within a cohort that encompasses both the µ parents and the λ offspring, fostering an ongoing refinement of the population. The algorithm dutifully continues iterating through these generations until it reaches one of two decisive endpoints: either the allocated search resources are entirely expended, or a potentially elusive bug is successfully detected amidst the evaluations.
Given the relatively time-intensive nature of evaluating a single schedule, a prudent choice has been made to employ conservative values for both µ and λ.

**Fitness Function:**
The effectiveness of evolutionary algorithms depends on the fitness function, especially in the context of this paper, where it assigns scores to schedules based on their proximity to detecting concurrency bugs. Assessing this proximity is challenging due to the complex nature of concurrency bugs. To address this, two fitness functions are defined:

  1) Time-based Fitness: This function measures the time taken for a test case to complete, rewarding longer validation processes that lead to more intricate executions.
  2) Proposal-based Fitness: This function assigns merit to schedules with higher maximum proposal sequences, guiding the algorithm toward more complex establishment phases and rounds of deliberation.

## Results and Analysis Summary

`````{margin} B1 (Proposal Message Bug)
Altered Ripple source code where nodes didn't verify sequence number monotonicity in proposal messages, potentially causing older proposals to override newer ones but compromising safety.
`````
`````{margin} B2 (Validation Threshold Bug)
Code modification requiring nodes to validate proposals with a 40% quorum threshold instead of the standard 80%, leading to potential ledger conflicts and safety issues.
`````
`````{margin} B3 (Original Source Code)
The unmodified, original Ripple source code.
`````

The testing process involved three versions of the Ripple source code, with two of them deliberately engineered to exhibit bugs that manifest only under specific message delivery orderings within the protocol messages: **Proposal Message Bug**, **Validation Threshold Bug**, and **Original Source Code**.    

They conducted tests on Ripple software version 1.7.2 within a private peer-to-peer network. This network comprised five Ripple server nodes running within Docker containers, with each node having all other nodes in its Unique Node List (UNLs).

For each Ripple source code version, the researchers conducted multiple executions of each search algorithm. They documented instances of specification violations and the time it took for these violations to occur. Employing multiple runs helped accommodate the inherent randomness in the behavior of the search algorithms.

1) **Effectiveness of random concurrency testing algorithms for detecting bugs in Ripple**    
In their evaluation, random concurrency testing utilizing RandomDelay outperformed RandomPriority in the detection of concurrency bugs. RandomPriority was able to identify the seeded bug in B1 within a single test run but did not uncover any bugs in the other benchmark scenarios. Conversely, RandomDelay detected the seeded bugs in both B1 and B2 across multiple test runs. Furthermore, it revealed a previously undisclosed bug that resulted in a violation of the termination property within Ripple's consensus algorithm.

2) **Effectiveness of guiding the test generation using the two fitness functions:**    
Their evaluation demonstrates the effectiveness of the evolutionary algorithm in skillfully steering test generation toward identifying flawed executions. This algorithm proved adept at detecting both the intentionally seeded bugs within benchmarks B1 and B2, as well as the newfound liveness issue in B3. The variance in bug detection rates between B1 and B2 can be attributed to the specific characteristics of the concurrency bugs introduced in these benchmarks. The bug present in B1 contravenes the agreement property (1) by causing consensus to be reached on two distinct transaction sets. In contrast, the bug in B2 infringes upon the agreement property (2) by validating two disparate ledgers. The validation of distinct ledgers should only occur when two nodes apply different transaction sets to their respective ledgers. This establishes B2 as a subset of B1, where breaking agreement (1) is made even more straightforward due to the additional bug insertion.


3) **Comparison of the two fitness functions:**    
The comparison between two distinct versions of the evolutionary algorithm, each employing different fitness functions, and independent random testing is centered around two primary evaluation metrics: bug detection success rate and bug detection time. The focus of the analysis primarily lies on bug detection in benchmarks B2 and B3, as benchmark B1 consistently detected the concurrency bug in all configurations.     
A notable observation is the contrasting bug detection success rates between B2 and B3. In the case of B2, evolutionary test case generation guided by fitness functions outperforms random search. However, this performance advantage does not hold true for B3, owing to the specific characteristics of the concurrency bug in this benchmark. During the tests, the B3 bug manifests when substantial delays are introduced to GetLedger and LedgerData messages, triggering it only when the cumulative delay for both message types exceeds 5250 ms. The number of generations required for an evolutionary algorithm to achieve these necessary delays depends largely on the characteristics of the initial population. If the majority of individuals in the initial population exhibit minimal delays for these message types, the evolutionary algorithm requires a higher number of generations to reach the required delay levels.

## Conclusion


This research paper uncovered an undisclosed concurrency bug in Ripple's production code while exploring concurrency behaviors in the Ripple XRP Ledger. It demonstrated the effectiveness of randomized concurrency testing methods in finding real-world concurrency bugs in complex systems. An evolutionary search-based concurrency testing algorithm was introduced, with two fitness functions designed to guide test generation towards extended execution durations or extended proposal sequences. The time-based fitness function proved more effective in bug detection.

This successful application of evolutionary search-based test generation suggests potential future research directions. Investigating different schedule representations can impact search performance, considering factors like locality, redundancy, and scalability. Evaluating the impact of variation operations on search performance, especially by exploring a wider range of operations, is important. Examining different fitness functions' influence on test execution is crucial, as they direct test cases toward specific system behaviors. Combining fitness functions with multi- and many-objective optimization algorithms can enable resource usage analysis in test case generation, particularly for regression testing.

Lastly, the proposed methodology's applicability extends beyond Ripple to testing consensus implementations in other distributed systems and blockchains using Byzantine fault-tolerant (BFT) consensus mechanisms. Future research can explore representations and fitness functions' performance when applied to different systems, broadening the method's scope and impact.

<div style="text-align: right;font-weight: bold;">Hamed Rostamzadeh</div>
<div style="text-align: right;font-style: italic;">October 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
