# Self Sovereign Identity

## Introduction
According to World Bank estimates, nearly 850 million people lack an official identity {cite}`world_bank_2023`, and the proliferation of digital devices has made it increasingly essential to possess a verifiable digital identity. This has led to a rise in the number of digital transactions and the need for a secure and reliable identity management system. SSI is emerging as a decentralized alternative to traditional centralized identity management systems, in which identities are cryptographically verifiable. It allows individuals to control their own digital identities and share them with trusted parties.
```{glossary}
SSI
  Self-sovereign identity (SSI) is a decentralized digital identity management system which leverages blockchain technology as a data registry [{numref}`ssi-fig`], allowing individuals to create, control, and share their identities securely.
```
```{figure} images/SSI.drawio.png
---
width: 500px
name: ssi-fig
---
SSI entities and their relations
```

## Ongoing Research in the field of SSI

### SSI and Healthcare
Barros et al. {cite}`de2022leveraging` explore the concepts of self-sovereign identity, blockchain technology, and zero-knowledge proofs to propose a solution for presenting proof of vaccination without revealing users' identities. It allows collaboration between health organizations, governments, and other stakeholders such as the tourism or travel industries. Furthermore, it uses interoperable open-source tools across countries so that this system can be implemented globally at a minimal cost for each country's government.

### Land Registry using SSI
The land registry serves as a vital foundation for a country's economic development during nation-building. By documenting land-related information on a blockchain, this technology can enhance security and transparency within the land registry process. Shuaib et al. {cite}`shuaib2022self` suggest that a blockchain-based land registry system can be combined with a self-sovereign identity (SSI) solution to provide a secure and efficient identity management system for landowners. They evaluate three existing self-sovereign identity solutions for blockchain-based land registry systems: Everest, Evernym, and uPort {cite}`ssiplatforms`. These solutions are analyzed based on the self-sovereign identity principles {cite}`ssiprinciples` to determine their compliance and effectiveness in addressing identity problems in land registry systems. This can help to ensure that only authorized individuals can access and modify land registry records, thereby reducing the risk of fraud and errors.

### SSI and Voting
Estonia is one of the few countries in the world that have managed to make e-voting a reality {cite}`estonia2022estonia`. Sertkaya et al. {cite}`sertkaya2022estonian` proposed an EIV-AC scheme that integrates the Estonian Internet voting (EIV) scheme with anonymous credentials (AC) based on self-sovereign identity (SSI). The use of SSI-based anonymous credentials enables voters to prove their eligibility to vote without revealing their identity. The zero-knowledge proof of knowledge is used to prove that the voter has the right to vote without revealing any additional information. The EIV-AC scheme enhances the security and privacy of the EIV scheme, making it more compliant with privacy-enhancing and data minimization regulations.

### Conclusion
Self-sovereign identity has the potential to revolutionize various industries, including healthcare, voting systems and many more. As research and development in SSI continue to progress, it will be crucial to address challenges related to interoperability, scalability, and usability to fully realize the potential of SSI in a global context.

## References
```{bibliography}
```