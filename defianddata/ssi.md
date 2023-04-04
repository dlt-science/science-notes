---
title: "SSI"
date: 2023-04-04 07:00:00
author: "Parshant Singh"
---

# Exploring the Technical Foundations of Self-Sovereign Identity: Real World Applications and Innovations

## Introduction
According to World Bank estimates, nearly 850 million people lack an official identity {cite}`world_bank_2023`, and the proliferation of digital devices has made it increasingly essential to possess a verifiable digital identity. This has led to a rise in the number of digital transactions and the need for a secure and reliable identity management system. SSI is emerging as a decentralized alternative to traditional centralized identity management systems, in which identities are cryptographically verifiable. It allows individuals to control their own digital identities and share them with trusted parties. Each entity in the SSI system is identified by a unique DID (Decentralised Identifier) $(\ref{eq1})$ which can be resolved to reveal information such as the entity's public key and other metadata.

$$
{\tt \underbrace{DID}_{Scheme}: \overbrace{example}^{DID \, Method}:\underbrace{BzCbsNYhMrjHiqZDTUASHg}_{Method \, Specific \, Identifier}} \label{eq1}
$$
<p align="center"><em>DID breakdown</em></p>

```{seealso}
Find out more about some of the most commonly used DID methods:
- [DID:INDY](https://hyperledger.github.io/indy-did-method/)
- [DID:UPORT](https://developer.uport.me/ethr-did/docs/index)
- [DID:SOV](https://sovrin.org/)
```

While centralized identities and federated identities offer convenience, control remains with the identity provider {cite}`laurent2015digital`. User-centric identities such as OpenID {cite}`recordon2006openid` and OAuth {cite}`fett2016comprehensive` improve portability but do not give full control to the users. SSI is designed to provide users with full control over their digital identities, and involves guiding principles around security, controllability, and portability. In addition to providing full control, Bernabe et al. {cite}`bernabe2019privacy` presented a classification of techniques for maintaining privacy in SSI, which included Secure Multiparty Computation and Zero-Knowledge Proofs, among others.


The three main parties involved in SSI systems are issuer, holder and verifier as shown in [{numref}`ssi-fig`]. The issuer issues a cryptographically signed credential to the holder, and the verifier is the entity that that confirm the authenticity of the credential using a decentralised data registry such as blockchain. Holders store their credentials in secure digital wallets and can share them with other parties as needed. The holder can also create a presentation request and share it with the verifier.

`````{margin} **What is SSI ?**
  Self-Sovereign Identity (SSI) is a decentralized digital identity management system which leverages blockchain technology as a data registry, allowing individuals to create, control, and share their identities securely.
`````

`````{margin} **What is a Verifiable Credential (VC) ?**
  A verifiable credential is a digital artifact that provides a tamper-evident, cryptographically verifiable proof of an individual's personal information or attributes.
`````

```{figure} images/SSI.drawio.png
---
width: 550px
height: 300px
name: ssi-fig
---
SSI entities and their relations
```
<!-- <details><summary><b>Click here to see how a verifiable credential actually looks like</b></summary> -->
```{dropdown} Click here to see how a verifiable credential actually looks like
This is a credential issued using the javascript library <code>didkit-wasm</code>
```json
{
      "@context":[
         "https://www.w3.org/2018/credentials/v1",
         {
            "alias":"https://schema.org/name",
            "logo":"https://schema.org/logo",
            "website":"https://schema.org/url",
            "description":"https://schema.org/description",
            "BasicProfile":"https://tzprofiles.com/BasicProfile"
         }
      ],
      "id":"urn:uuid:7041d211-72c9-49fe-b6d1-d8b6b94abfe3",
      "type":[
         "VerifiableCredential",
         "BasicProfile"
      ],
      "credentialSubject":{
         "id":"did:pkh:tz:tz1N699qJqMVbMDan2r6R3QYFw42J5ydReh6",
         "alias":"TU Munich",
         "website":"Germany",
         "description":"My name",
         "logo":"Helene-Mayer-Ring 7B"
      },
      "issuer":"did:pkh:tz:tz1QRuc9BkvsBfeSGr6kJ5GCzBsrDjMedvA7",
      "issuanceDate":"2023-01-13T12:24:52.630Z",
      "proof":{
         "@context":{
            "TezosMethod2021":"https://w3id.org/security#TezosMethod2021",
            "TezosSignature2021":{
               "@context":{
                  "@protected":true,
                  "@version":1.1,
                  "challenge":"https://w3id.org/security#challenge",
                  "created":{
                     "@id":"http://purl.org/dc/terms/created",
                     "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                  },
                  "domain":"https://w3id.org/security#domain",
                  "expires":{
                     "@id":"https://w3id.org/security#expiration",
                     "@type":"http://www.w3.org/2001/XMLSchema#dateTime"
                  },
                  "id":"@id",
                  "nonce":"https://w3id.org/security#nonce",
                  "proofPurpose":{
                     "@context":{
                        "@protected":true,
                        "@version":1.1,
                        "assertionMethod":{
                           "@container":"@set",
                           "@id":"https://w3id.org/security#assertionMethod",
                           "@type":"@id"
                        },
                        "authentication":{
                           "@container":"@set",
                           "@id":"https://w3id.org/security#authenticationMethod",
                           "@type":"@id"
                        },
                        "id":"@id",
                        "type":"@type"
                     },
                     "@id":"https://w3id.org/security#proofPurpose",
                     "@type":"@vocab"
                  },
                  "proofValue":"https://w3id.org/security#proofValue",
                  "publicKeyJwk":{
                     "@id":"https://w3id.org/security#publicKeyJwk",
                     "@type":"@json"
                  },
                  "type":"@type",
                  "verificationMethod":{
                     "@id":"https://w3id.org/security#verificationMethod",
                     "@type":"@id"
                  }
               },
               "@id":"https://w3id.org/security#TezosSignature2021"
            }
         },
         "type":"TezosSignature2021",
         "proofPurpose":"assertionMethod",
         "proofValue":"edsigtaEZjPNqyWT6ZfZDTPUds7vK9RrUSFbJEpy67mAfPFYviUiWrpvhvPx2xZXRDVsPoJ3UMWjC8x1oJgY6ZziWufc87kamV8",
         "verificationMethod":"did:pkh:tz:tz1QRuc9BkvsBfeSGr6kJ5GCzBsrDjMedvA7#TezosMethod2021",
         "created":"2023-01-13T12:24:52.638Z",
         "publicKeyJwk":{
            "alg":"EdBlake2b",
            "crv":"Ed25519",
            "kty":"OKP",
            "x":"WlWqCerXoqMAMKfDWD0m2cIpvysFFqiU7L8L_I7zbfI"
         }
      }
   }
```





```{admonition} Key Insights!
:class: tip
- SSI solutions are designed to be blockchain-agnostic and adhere to [W3C's specifications](https://www.w3.org/TR/did-core/).
- The identity wallets (eg - uPort, Trinsic, Connect.Me) are different from the digital wallets (eg - Coinbase, Ledger, Trezor) that store cryptocurrencies in the sense that they store and manage DIDs and VCs instead of cryptocurrencies.
- To protect privacy, SSI solutions (eg - [Hyperledger Indy](https://medium.com/stm-blockchain/how-zero-knowledge-proofs-work-on-indy-network-241d6da112bc) and Aries) are increasingly using Zero-Knowledge Proofs (ZKPs) to prove the authenticity of credentials without revealing the actual data.
- To facilitate a secure communication between different SSI components (issuer-holder-verifier), [DIDComm](https://medium.com/decentralized-identity/understanding-didcomm-14da547ca36b) and [CHAPI](https://iiw.idcommons.net/101_Session:_Verifiable_Credential_Handler_(CHAPI)_and_DIDComm) protocols have been developed and heavily used.
```

## Applications of SSI

Schlatt et al. {cite}`schlatt2022designing` demonstrates how a customer can leverage a Zero-knowledge Proof concept called 'blinded link secret' to make selective disclosure of information.
Similarly, Barros et al. {cite}`de2022leveraging` implemented a prototype of an application for presenting proof of vaccination without revealing users' identities. It allows collaboration between health organizations, governments, and other stakeholders such as the tourism or travel industries. Furthermore, it uses interoperable open-source tools across countries so that this system can be implemented globally at a minimal cost for each country's government. The NHS Digital Staff Passport solution {cite}`lacity2022implementing` employs the Sovrin Network as a public key infrastructure (PKI) to manage verifiable credentials for staff onboarding. Hospitals register on the network and use their private keys to sign credentials, while staff members utilize Evernym's [Connect.Me](https://www.connect.me/) SSI digital wallet app to store and share credentials.

Shuaib et al. {cite}`shuaib2022self` suggest that a blockchain-based land registry system can be combined with a self-sovereign identity (SSI) solution to provide a secure and efficient identity management system for landowners. The evaluation of three existing self-sovereign identity solutions: Everest, Evernym, and uPort {cite}`ssiplatforms` based on the self-sovereign identity principles {cite}`ssiprinciples` to determine their compliance and effectiveness in addressing identity problems in land registry systems. The everest platform turned out to be most compliant with the SSI principles and Evernym and uPort had some limitations in terms of interoperability and user control.

Estonia is one of the few countries in the world that have managed to make e-voting a reality {cite}`estonia2022estonia`. Sertkaya et al. {cite}`sertkaya2022estonian` proposed an EIV-AC scheme that integrates the Estonian Internet voting (EIV) scheme with anonymous credentials (AC) based on self-sovereign identity (SSI). The use of SSI-based anonymous credentials enables voters to prove their eligibility to vote without revealing their identity. The zero-knowledge proof of knowledge is used to prove that the voter has the right to vote without revealing any additional information. The EIV-AC scheme enhances the security and privacy of the EIV scheme, making it more compliant with privacy-enhancing and data minimization regulations.

## Can SSI work without Blockchain?
Blockchain is not the only option when it comes to implementing Self-sovereign Identity system. Alternatives like IPFS, Public-key cryptography and even traditional Certificate Authorities can be used to implement SSI {cite}`doyouneedblockchain`. However, the main advantage of using blockchain is that it provides a decentralized and immutable ledger that can be used to store and verify credentials.

### Conclusion
Self-sovereign identity has the potential to revolutionize various industries, including healthcare, voting systems and many more. As research and development in SSI continue to progress, it will be crucial to address challenges related to interoperability, scalability, and usability to fully realize the potential of SSI in a global context.


```{bibliography}
```