# Exploring the Technical Foundations of Self-Sovereign Identity: A Deep Dive into Real-World Applications and Innovations

## Introduction
According to World Bank estimates, nearly 850 million people lack an official identity {cite}`world_bank_2023`, and the proliferation of digital devices has made it increasingly essential to possess a verifiable digital identity. This has led to a rise in the number of digital transactions and the need for a secure and reliable identity management system. SSI is emerging as a decentralized alternative to traditional centralized identity management systems, in which identities are cryptographically verifiable. It allows individuals to control their own digital identities and share them with trusted parties. Each entity in the SSI system is identified by a unique DID (Decentralised Identifier) which can be resolved to reveal information such as the entity's public key and other metadata.

`````{margin} **What is SSI ?**
  Self-Sovereign Identity (SSI) is a decentralized digital identity management system which leverages blockchain technology as a data registry [{numref}`ssi-fig`], allowing individuals to create, control, and share their identities securely.
`````

$$
{\tt \underbrace{DID}_{Scheme}: \overbrace{example}^{DID \, Method}:\underbrace{BzCbsNYhMrjHiqZDTUASHg}_{Method \, Specific \, Identifier}}
$$
<p align="center"><em>DID breakdown</em></p>

```{seealso}
Find out more about some of the most commonly used DID methods:
- [DID:INDY](https://hyperledger.github.io/indy-did-method/)
- [DID:UPORT](https://developer.uport.me/ethr-did/docs/index)
- [DID:SOV](https://sovrin.org/)
```

```{figure} images/SSI.drawio.png
---
width: 550px
height: 300px
name: ssi-fig
---
SSI entities and their relations
```
<details><summary><b>Click here to see how a verifiable credential actually looks like</b></summary>

This is a credential issued using the javascript library didkit-wasm.
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
</details>

:::{note}
Verifiable Credentials (VC) are different from Verifiable Presentations (VP). Credentials are issued by trusted authorities and contain claims, while verifiable presentations are created by holders to share selected credentials with verifiers in specific contexts. Verifiable credentials are stored in a wallet, while verifiable presentations are created on the fly.
:::


## Applications of SSI

### SSI and Healthcare
Barros et al. {cite}`de2022leveraging` explore the concepts of self-sovereign identity, blockchain technology, and zero-knowledge proofs to propose a solution for presenting proof of vaccination without revealing users' identities. It allows collaboration between health organizations, governments, and other stakeholders such as the tourism or travel industries. Furthermore, it uses interoperable open-source tools across countries so that this system can be implemented globally at a minimal cost for each country's government.
The NHS Digital Staff Passport solution {cite}`lacity2022implementing` employs the Sovrin Network as a public key infrastructure (PKI) to manage verifiable credentials for staff onboarding. Hospitals register on the network and use their private keys to sign credentials, while staff members utilize Evernym's [Connect.Me](https://www.connect.me/) SSI digital wallet app to store and share credentials. .

### Land Registry using SSI
The land registry serves as a vital foundation for a country's economic development during nation-building. By documenting land-related information on a blockchain, this technology can enhance security and transparency within the land registry process. Shuaib et al. {cite}`shuaib2022self` suggest that a blockchain-based land registry system can be combined with a self-sovereign identity (SSI) solution to provide a secure and efficient identity management system for landowners. They evaluate three existing self-sovereign identity solutions for blockchain-based land registry systems: Everest, Evernym, and uPort {cite}`ssiplatforms`. These solutions are analyzed based on the self-sovereign identity principles {cite}`ssiprinciples` to determine their compliance and effectiveness in addressing identity problems in land registry systems. This can help to ensure that only authorized individuals can access and modify land registry records, thereby reducing the risk of fraud and errors.

### SSI and Voting
Estonia is one of the few countries in the world that have managed to make e-voting a reality {cite}`estonia2022estonia`. Sertkaya et al. {cite}`sertkaya2022estonian` proposed an EIV-AC scheme that integrates the Estonian Internet voting (EIV) scheme with anonymous credentials (AC) based on self-sovereign identity (SSI). The use of SSI-based anonymous credentials enables voters to prove their eligibility to vote without revealing their identity. The zero-knowledge proof of knowledge is used to prove that the voter has the right to vote without revealing any additional information. The EIV-AC scheme enhances the security and privacy of the EIV scheme, making it more compliant with privacy-enhancing and data minimization regulations.

### Conclusion
Self-sovereign identity has the potential to revolutionize various industries, including healthcare, voting systems and many more. As research and development in SSI continue to progress, it will be crucial to address challenges related to interoperability, scalability, and usability to fully realize the potential of SSI in a global context.