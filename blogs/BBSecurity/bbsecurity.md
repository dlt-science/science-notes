# Blockchain Bridge Security

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic insight**</ins>

```{admonition} Key Insights
:class: tip
- To mitigate security risks, a cross-chain bridge leveraging zk-SNARK technology to provide a secure, trustless cross-chain bridge, marking the first implementation of Zero-Knowledge Proofs (ZKP) in a decentralised trustless bridge system, has been proposed.
- To facilitate secure cross-chain interoperability, a Hash time-lock scheme that does not rely on external trust ensuring transaction security is introduced.
- a high security and highly scalability option that supports the interoperability of multiple objects is sidechains/relay scheme.
- To mitigate token transfer risks, a series of protocols called "TrustBoost" using smart contracts to achieve a 'consensus on top of consensus' mechanism, bolstering trust across multiple blockchains and with promising prospects for future applications is proposed.
- To enhance interoperability, a novel framework mitigating security risks in cross-blockchain technology is proposed. It facilitates the identification of key assumptions and characteristics. It improves decision-making, minimises design errors, and aids in integrating various blockchain applications, thus promoting effective interoperability.
- Cryptographic techniques remain central to ensuring security on blockchain bridges. A balance between scalability and security is crucial for the future of blockchain bridges.
```

## Introduction

Blockchain technology has been lauded for its potential to disrupt various industries, given its unique properties such as decentralisation, transparency, and security. One recent advancement in this area is the development of blockchain bridges, which enable interoperability among different blockchains. Bridges facilitate communication between two blockchain ecosystems through the transfer of assets and information. However, as with any innovative technology, these bridges pose new security challenges. In this science note, we delve into the current academic landscape surrounding the security of blockchain bridges and summarise the recent research findings.

```{figure} images/bridge.drawio.png
---
width: 780px
height: 456px
name: bridge_security
---
Communication through a Blockchain Bridge.
```

## Interoperability and Security Challenges

 `````{margin} **Zero-Knowledge Proofs**
A zero-knowledge proof (ZKP) is a cryptographic technique that enables one party, the prover, to convince another party, the verifier, of the validity of a statement or the possession of a secret without revealing any additional information about the underlying secret or data.
`````
 `````{margin} **zk-SNARK**
  Zk-SNARK is an acronym that stands for “Zero-Knowledge Succinct Non-Interactive Argument of Knowledge.” A zk-SNARK is a cryptographic proof that allows one party to prove it possesses certain information without revealing that information.
`````
 Interoperability in blockchain environments brings forth a series of unique security challenges. Trustless, interoperable, cryptocurrency-backed assets can be subjected to various threats. In April 2022, attackers were able to obtain five of the nine validator keys, through which they stole 624 million USD by exploiting the Ronin bridge, making it the largest attack in the history of DeFi {cite}`kessler2022coindesk`. According to blockchain analytics firm Chainalysis, until August 2022 recurring attacks against bridges have cost users around 1.4 billion USD {cite}`browne2022cnbc`. In 2022 attacks on bridges accounted for 69% of total funds stolen {cite}`chainanalysis2022chainanalysis`. 
 
 This calls for novel security models and protocols that can protect against possible attack vectors introduced by cross-chain communication. This is particularly true for blockchain bridges that need to uphold the integrity and security of transactions across disparate networks. Most existing solutions rely on the trust assumptions of committees, which lowers security significantly.

Xie et al. {cite}`xie2022zkbridge` proposed a solution by introducing “zkBridge” an efficient cross-chain bridge that guarantees strong security without external trust assumptions. The main idea is to leverage zk-SNARK, which are succinct non-interactive proofs (arguments) of knowledge as a result security is ensured without relying on a committee. zkBridges uses the zk-SNARK protocol to achieve both reasonable proof generation times and on-chain verification costs. zkBridge is “trustless” as it does not require extra assumptions other than those of blockchains and underlying cryptographic protocols. It is the first to use Zero-Knowledge Proofs (ZKP) to enable a decentralised trustless bridge.

Pillai et al. {cite}`pillai2022cross` proposed a novel cross-blockchain integration framework designed to guide the integration of cross-blockchain technology. The framework aids in identifying crucial assumptions and characteristics, mitigating security risks, enhancing the decision-making process, and minimising design mistakes and performance issues. It recognises the integration system as the fundamental unit of cross-blockchain technology, providing comprehensive analysis and addressing security concerns. Moreover, the framework supports businesses in designing and integrating various blockchain applications, while enabling a more accurate evaluation of security assumptions. Thus, it paves the way for effective interoperability among multiple blockchains.

## The Role of Cryptography in Blockchain Bridge Security

`````{margin} **Sidechain**
  A sidechain is a blockchain that communicates with other blockchains via a two-way peg. It stems from the main blockchain and runs in parallel to it.
`````
`````{margin} **Cryptographic Protocol**
  A cryptographic protocol is an abstract or concrete protocol that performs a security-related function and applies cryptographic methods, often as sequences of cryptographic primitives. A protocol describes how the algorithms should be used and includes details about data structures and representations, at which point it can be used to implement multiple, interoperable versions of a programme.
`````
Securing blockchain bridges is greatly dependent on the strength of the cryptographic techniques deployed. The fundamental study by Kiayias et al. {cite}`kiayias2017ouroboros` on proof-of-stake blockchain protocols is of significant relevance. They outlined a novel cryptographic mechanism that provides transactional security while ensuring transparency.

To overcome the external trust assumption, Li et al. {cite}`li2023metaopera` in their paper proposed a Hash time-lock scheme, that utilises a hash function and time-lock features to achieve cross-chain interoperability. The security of the Hash time-lock scheme is based on cryptographic hardness assumptions. The asset receiver is forced to determine the collection and produce proof of collection to the payer within the cut-off time, or the asset will be returned via hash locks and blockchain “time” locks. The proof of receipt can be used by the payer to acquire assets of equal value on the recipient’s blockchain or trigger other events. However, this scheme only supports monetary exchange and thus has low scalability.

Li et al. {cite}`li2023metaopera`, identified a high security and highly scalability option is sidechains/relay scheme, which supports the interoperability of multiple objects such as assets and other data, thus having high scalability. In particular, the two-way peg is a mechanism that allows bidirectional communication between blockchains. An example of a two-way peg is simplified payment verification (SPV) in Bitcoin. Relays represent a mechanism that enables a blockchain network to authenticate data from other blockchain networks, eliminating the need for external third-party sources. Operating as a light client on a network, a relay system incorporates a smart contract and records block header information from different networks {cite}`frauenthaler2020leveraging`. A trade-off of the sidechain implementation is that the vulnerability might increase in the main chain or other sidechains if there is a compromised sidechain in the network {cite}`sztorc2015drivechain`.

Ding et al. {cite}`ding2018interchain`, proposed a framework for connecting multiple blockchain networks via an intermediary structure known as the InterChain. The InterChain possesses its own validation nodes, while SubChain networks are linked to this InterChain via gateway nodes.

Hardjono et al. {cite}`hardjono2019toward`, discussed blockchain interoperability by drawing parallels with the design principles of Internet architecture. Just as the internet uses routers to guide message packets across its network at a mechanical level, they propose the use of gateways to direct messages between different blockchain networks.

Such cryptographic protocols can serve as a guiding light for the development of security measures in the context of blockchain bridges.

## Scalability and Security

As important as security is for blockchain bridges, it should not compromise the scalability of the systems. Zamyatin et al. {cite}`zamyatin2019xclaim` discussed the scalability-security trade-off in their study on interoperable assets. There is a need for a balance that allows for scalability without jeopardising security. Future research in blockchain bridge security needs to address this delicate balance, ensuring the development of robust and efficient interoperable systems.

Zhang et al. {cite}`zhang2020research` introduced a method that facilitates asset exchange between inter-firm alliance chains and private chains. Users from both the sending and receiving chains authenticate their identities and secure a certificate by interacting with the alliance chain. When a cross-blockchain transfer request is initiated, the alliance chain validates the ownership of the users over the assets, then proceeds with the asset transfer through a cross-blockchain interaction process.

## Maintaining Sovereignty of blockchains

Existing solutions to boost the trust using a stronger blockchain, e.g., via checkpointing, require the weaker blockchain to give up sovereignty. Wang et al. {cite}`wang2022trustboost` in their paper present a series of protocols known as "TrustBoost" designed to bolster trust across multiple blockchains without compromising their sovereignty. These protocols function through smart contracts, achieving a "consensus on top of consensus" that avoids changes to the blockchains' consensus layers. TrustBoost operates by allowing cross-chain communication via bridges, facilitating the sharing of information across smart contracts on different blockchains. This system maintains its security as long as two-thirds of the participating blockchains are secure. Furthermore, TrustBoost shows potential in mitigating risks associated with cross-chain token transfers and exhibits promising prospects for future applications, especially as heterogeneous blockchain networks continue to mature.

## Conclusion

Blockchain bridges represent an important evolution in blockchain technology, facilitating crucial interoperability. However, the security aspects of these bridges are complex and multifaceted, requiring rigorous academic and industry attention. The body of research surrounding blockchain security provides critical insights that can help guide the development of secure and efficient blockchain bridges. As this field continues to evolve, a focus on understanding and mitigating security risks while maintaining scalability will be paramount.

<div style="text-align: right;font-weight: bold;">Ali Kathia</div>
<div style="text-align: right;font-style: italic;">May 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```