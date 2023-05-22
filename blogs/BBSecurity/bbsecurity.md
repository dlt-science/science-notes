# Blockchain Bridge Security

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
- Interoperability in blockchains introduces unique security challenges.
- Cryptographic techniques remain central to ensuring security in blockchain bridges.
- Standardized protocols for blockchain bridge security are a subject of active research.
- A balance between scalability and security is crucial for the future of blockchain bridges.
```

## Introduction

Blockchain technology has been lauded for its potential to disrupt various industries, given its unique properties such as decentralization, transparency, and security. One recent advancement in this area is the development of blockchain bridges, which enable interoperability among different blockchains. Bridges facilitate communication between two blockchain ecosystems through the transfer of assets and information. However, as with any innovative technology, these bridges pose new security challenges. In this science note, we delve into the current academic landscape surrounding the security of blockchain bridges and summarize the recent research findings.

## Interoperability and Security Challenges

 Interoperability in blockchain environments brings forth a series of unique security challenges. Trustless, interoperable, cryptocurrency-backed assets can be subjected to various threats. Most existing solutions rely on trust assumptions of committees, this lowers the security significantly. In April 2022, attackers were able to obtain five of the nine validator keys, through which they stole 624 million USD by exploiting Ronin bridge, making it the largest attack in the history of DeFi.  

Xie et al. proposed a solution by introducing “zkBridge” an efficient cross-chain bridge that guarantees strong security without external trust assumptions. The main idea is to leverage zk-SNARK, which are succinct non-interactive proofs (arguments) of knowledge as a result security is ensured without relying on a committee. zkBridges uses zk-SNARK protocol to achieve both reasonable proof generation time and on-chain verification cost. zkBridge is “trustless” as it does not require extra assumptions other than those of blockchains and underlying cryptographic protocols. It is the first to use ZKP to enable a decentralized trustless bridge.

According to several reports, recurring attacks against bridges have cost users more than 1.5 billion USD.  This calls for novel security models and protocols that can protect against possible attack vectors introduced by cross-chain communication. This is particularly true for blockchain bridges that need to uphold the integrity and security of transactions across disparate networks.

## The Role of Cryptography in Blockchain Bridge Security

Securing blockchain bridges is greatly dependent on the strength of the cryptographic techniques deployed. The fundamental study by Kiayias et al. on proof-of-stake blockchain protocols is of significant relevance. They outlined a novel cryptographic mechanism that provides transactional security while ensuring transparency.

To overcome the external trust assumption, Li et al. in their paper proposed a Hash time-lock scheme, which utilizes a hash function and time-lock features to achieve cross-chain interoperability. The security of the Hash time-lock scheme is based on cryptographic hardness assumptions. The asset receiver is forced to determine the collection and produce proof of collection to the payer within the cut-off time, or the asset will be returned via hash locks and blockchain “time” locks. The proof of receipt can be used by the payer to acquire assets of equal value on the recipient’s blockchain or trigger other events. However, this scheme only supports monetary exchange and thus has low scalability.

Li et al. identified a high security and highly scalability option is sidechains/relay scheme which supports the interoperability of multiple objects such as assets and other data, thus having high scalability. Sidechain is a blockchain that communicates with other blockchains via a two-way peg. In particular, the two-way peg is a mechanism that allows bidirectional communication between blockchains. An example of a two-way peg is simplified payment verification (SPV) in Bitcoin. 

Such cryptographic protocols can serve as a guiding light for the development of security measures in the context of blockchain bridges.

```{figure} images/BBS.drawio.png
---
width: 750px
height: 260px
name: bridge_security
---
Security and Scalability of Cross-Chain Technologies.
```

## Scalability and Security

As important as security is for blockchain bridges, it should not compromise the scalability of the systems. Zamyatin et al. discussed the scalability-security trade-off in their study on interoperable assets. There is need for a balance that allows for scalability without jeopardizing security. Future research in blockchain bridge security needs to address this delicate balance, ensuring the development of robust and efficient interoperable systems.

## Maintaining Sovereignty of blockchains

Existing solutions to boost the trust using a stronger blockchain, e.g., via checkpointing, requires the weaker blockchain to give up sovereignty. Wang et al. in their paper present a series of protocols known as "TrustBoost" designed to bolster trust across multiple blockchains without compromising their sovereignty. These protocols function through smart contracts, achieving a "consensus on top of consensus" that avoids changes to the blockchains' consensus layers. TrustBoost operates by allowing cross-chain communication via bridges, facilitating the sharing of information across smart contracts on different blockchains. This system maintains its security as long as two-thirds of the participating blockchains are secure. Furthermore, TrustBoost shows potential in mitigating risks associated with cross-chain token transfers and exhibits promising prospects for future applications, especially as heterogeneous blockchain networks continue to mature.

## Conclusion

Blockchain bridges represent an important evolution in blockchain technology, facilitating crucial interoperability. However, the security aspects of these bridges are complex and multifaceted, requiring rigorous academic and industry attention. The body of research surrounding blockchain security provides critical insights that can help guide the development of secure and efficient blockchain bridges. As this field continues to evolve, a focus on understanding and mitigating security risks while maintaining scalability will be paramount.

<div style="text-align: right;font-weight: bold;">Ali Kathia</div>
<div style="text-align: right;font-style: italic;">May 2023</div>

## References

Kiayias, A. et al. (2017) ‘Ouroboros: A provably secure proof-of-stake Blockchain Protocol’, Advances in Cryptology – CRYPTO 2017, pp. 357–388. doi:10.1007/978-3-319-63688-7_12. 

Li, T. et al. (2023) Metaopera: A cross-metaverse interoperability protocol, arXiv.org. Available at: https://arxiv.org/abs/2302.01600 (Accessed: 18 May 2023). 

Wang, X. et al. (2022) TrustBoost: Boosting Trust among interoperable blockchains, arXiv.org. Available at: https://arxiv.org/abs/2210.11571 (Accessed: 18 May 2023). 

Xie, T. et al. (2022) ‘ZkBridge’, Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security [Preprint]. doi:10.1145/3548606.3560652. 

Zamyatin, A. et al. (2019) ‘Xclaim: Trustless, interoperable, cryptocurrency-backed assets’, 2019 IEEE Symposium on Security and Privacy (SP) [Preprint]. doi:10.1109/sp.2019.00085. 

```{bibliography}
:filter: docname in docnames
```