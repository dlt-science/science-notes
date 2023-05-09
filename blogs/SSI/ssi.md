# Self-Sovereign Identity: Technical Foundations and Applications

<ins>**Innovation & Ideation**</ins>

```{admonition} Key Insights
:class: tip
- SSI systems leverage Decentralised Identifiers (DIDs) and Verifiable Credentials (VCs) to enable secure and trustworthy data sharing between issuers, holders, and verifiers, without relying on a centralised authority.
- Privacy-preserving techniques, such as zero-knowledge proofs and selective disclosure, allow SSI users to maintain control over their digital identities and securely share credentials without exposing unnecessary information.
- The implementation of SSI in various industries, including healthcare, land registration, and e-voting, demonstrates the potential for SSI to revolutionise identity management and enhance security, privacy, and trust in these systems.
- While blockchain is not mandatory for SSI systems, its use as a decentralised data registry ensures secure, tamper-evident, and verifiable storage of credentials, contributing to the trustworthiness and reliability of identity management processes.
```

## Introduction
According to World Bank estimates, nearly 850 million people lack an official identity {cite}`world_bank_2023`, and the proliferation of digital devices has made it increasingly essential to possess a verifiable digital identity. This has led to a rise in digital transactions and the need for a secure and reliable identity management system. SSI is emerging as a decentralised alternative to traditional centralised identity management systems, in which identities are cryptographically verifiable. It allows individuals to control their digital identities and share them with trusted parties. Each entity in the SSI system is identified by a unique DID (Decentralised Identifier) as shown below, which can be resolved to reveal information such as the entity's public key and other metadata.

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

While centralised identities and federated identities offer convenience, control remains with the identity provider {cite}`laurent2015digital`. User-centric identities such as OpenID {cite}`recordon2006openid` and OAuth {cite}`fett2016comprehensive` improve portability but do not give complete control to the users. SSI is designed to give users full control over their digital identities, and involves guiding principles around security, controllability, and portability. In addition to providing total control, Bernabe et al. {cite}`bernabe2019privacy` presented a classification of techniques for maintaining privacy in SSI, which included Secure Multiparty Computation and Zero-Knowledge Proofs, among others.


The three main parties involved in SSI systems are the issuer, holder and verifier, as shown in [{numref}`ssi-fig`]. The issuer issues a cryptographically signed credential to the holder, and the verifier is the entity that confirms the credential's authenticity using a decentralised data registry such as a Blockchain. Holders store their credentials in secure digital wallets and can share them with other parties as needed. The holder can also create a presentation and share it with the verifier on request.

`````{margin} **SSI**
  Self-Sovereign Identity (SSI) is a decentralised digital identity management system which leverages blockchain technology as a data registry, allowing individuals to create, control, and share their identities securely.
`````

`````{margin} **Verifiable Credential**
  A verifiable credential is a digital artefact that provides tamper-evident, cryptographically verifiable proof of an individual's personal information or attributes.
`````

```{figure} images/SSI.drawio.png
---
width: 550px
height: 300px
name: ssi-fig
---
SSI entities and their relations
```

```{seealso}
This is a verifiable credential issued using the javascript didkit-wasm library.
\
[Click here for full credential](https://gist.github.com/singhparshant/d2157ad4b48555c155d0f807d37ec3f1)
```javascript
{
....
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
....
}
```

```{admonition} Nitty Gritty of SSI
:class: info
- SSI solutions are designed to be blockchain-agnostic and adhere to [W3C's specifications](https://www.w3.org/TR/did-core/).
- The identity wallets (e.g., uPort, Trinsic, Connect.Me) are different from the digital wallets (e.g., Coinbase, Ledger, Trezor) that store cryptocurrencies in the sense that they store and manage DIDs and VCs instead of cryptocurrencies.
- To protect privacy, SSI solutions (e.g. - [Hyperledger Indy](https://medium.com/stm-blockchain/how-zero-knowledge-proofs-work-on-indy-network-241d6da112bc) and Aries) are increasingly using Zero-Knowledge Proofs (ZKPs) to prove the authenticity of credentials without revealing the actual data.
- To facilitate secure communication between different SSI components (issuer-holder-verifier), [DIDComm](https://medium.com/decentralized-identity/understanding-didcomm-14da547ca36b) and [CHAPI](https://iiw.idcommons.net/101_Session:_Verifiable_Credential_Handler_(CHAPI)_and_DIDComm) protocols have been developed and are heavily used.
```

## Applications for SSI

`````{margin} **Zero-Knowledge Proofs**
A zero-knowledge proof (ZKP) is a cryptographic technique that enables one party, the prover, to convince another party, the verifier, of the validity of a statement or the possession of a secret without revealing any additional information about the underlying secret or data.
`````

### SSI in healthcare
Recent studies have demonstrated the feasibility of using zero-knowledge proofs to disclose information selectively, such as proof of vaccination status, without revealing users' identities. These studies have employed interoperable open-source tools to implement these systems globally at a minimal cost. Schlatt et al. {cite}`schlatt2022designing` illustrates how a customer can leverage a Zero-knowledge Proof concept called 'blinded link secret' to disclose information selectively. Similarly, Barros et al. {cite}`de2022leveraging` implemented a prototype of an application for presenting proof of vaccination without revealing users' identities. Furthermore, it uses interoperable open-source tools across countries to implement this system globally at a minimal cost for each country's government. The NHS Digital Staff Passport solution {cite}`lacity2022implementing` employs the Sovrin Network as a public key infrastructure (PKI) to manage verifiable credentials for staff onboarding. Hospitals register on the network and use their private keys to sign credentials, while staff members utilise Evernym's [Connect.Me](https://www.connect.me/) SSI digital wallet app to store and share credentials.

### SSI in land registration
Shuaib et al. {cite}`shuaib2022self` suggest that a blockchain-based land registry system can be combined with a self-sovereign identity (SSI) solution to provide a secure and efficient identity management system for landowners. Three existing SSI solutions, Everest, Evernym, and uPort {cite}`ssiplatforms`, were evaluated based on SSI principles {cite}`ssiprinciples` to determine their compliance and effectiveness in addressing identity problems in land registry systems. The Everest platform was found to be the most compliant with the SSI principles, whereas Evernym and uPort had some limitations in terms of interoperability and user control.

### SSI in e-voting
Estonia is one of the few countries in the world that have managed to make e-voting a reality {cite}`estonia2022estonia`. Sertkaya et al. {cite}`sertkaya2022estonian` proposed an EIV-AC scheme that integrates the Estonian Internet voting (EIV) scheme with anonymous credentials (AC) based on self-sovereign identity (SSI). The use of SSI-based anonymous credentials enables voters to prove their eligibility to vote without revealing their identity. The zero-knowledge proof of identity is used to prove that the voter has the right to vote without revealing any additional information. The EIV-AC scheme enhances the security and privacy of the EIV scheme, making it more compliant with privacy-enhancing and data minimisation regulations.

### SSI in finance and identity management
Innovative proposals surrounding digital identity management systems, such as [Kiva's architecture](http://www.kiva.org/protocol/), suggest the development of an insurance marketplace for consequential damages related to identity claims. This marketplace could offer a market mechanism for evaluating the accuracy, trustworthiness, and usefulness of various identity claims, subsequently allowing lenders to confidently underwrite loans, even to individuals lacking formal credit history. Furthermore, by leveraging blockchain technology in a semi-decentralised identity management system, banks and microfinance lenders could underwrite the risk associated with issuing identity credentials, facilitating de-risking for subsequent lenders.

Ferdous et al. {cite}`ferdous2023ssi4web` introduce a <em>SSI4Web</em> framework and demonstrate how an SSI-based framework can be designed for web services and offer a secure and passwordless user authentication mechanism, which eliminates the need for users to remember passwords and reduces the risk of password breaches.

## Can SSI work without Blockchain?
Blockchain is one of many options when implementing a Self-sovereign Identity system. Alternatives like IPFS, Public-key cryptography and even traditional Certificate Authorities can be used to implement SSI. However, the main advantage of using Blockchain is that it provides a decentralised and immutable ledger that can be used to store and verify credentials.

## Conclusion
Self-sovereign identity can potentially revolutionise various industries, including healthcare, voting systems and many more. However, as research and development in SSI progress, it will be
 crucial to address interoperability, scalability, and usability challenges to realise SSI's potential in a global context fully.

<div style="text-align: right;font-weight: bold;">Parshant Singh</div>
<div style="text-align: right;font-style: italic;">April 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
