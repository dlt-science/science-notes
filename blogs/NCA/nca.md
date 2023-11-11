# Lorenz chaotic system cryptography

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic Insight**</ins>

```{admonition} Key Insights
:class: tip
- Bitcoin and Ethereum blockchains use cryptographic algorithms, such as ECDSA {cite}`johnson2001elliptic` and SHA-256, to secure transactions by relying on the computational difficulty of large prime number factorization. 
 - Quantum computers can efficiently break ECDSA through Shor's algorithm<!--{cite}`monz2016realization` -->, potentially compromising the cryptographic foundations of blockchains.
- The weakness of SHA-256 against quantum computers is attributed to Grover's algorithm<!--{cite}`long2001grover` -->, which efficiently searches through its finite 256-bit output space.
- When scalable quantum computers arrive, they could retrospectively decrypt and forge signatures{cite}`aggarwal2017quantum`, effectively compromising blockchain integrity and security. 
- This presents an emergent need to transition to quantum-resistant cryptography{cite}`jao2011towards` based on more extencive and infinite problems rather than factorization to primes.
```

## Introduction

In the ever-evolving landscape of cryptography, the quest for quantum-resistant algorithms has become paramount as quantum computing capabilities loom on the horizon. Traditional cryptographic systems face potential vulnerabilities to quantum attacks{cite}`kearney2021vulnerability`, prompting researchers to explore innovative solutions that harness the power of chaos. One proposal is the cryptographic algorithm based on the Lorenz chaotic system{cite}`al2019image`, a system renowned for its deterministic chaos{cite}`schuster2006deterministic` and the promise of an infinite output space. In this article, we delve into the foundations of the Lorenz chaotic system, discuss its potential application as a quantum-resistant cryptographic algorithm, and explore the implications of leveraging chaotic dynamics for securing our digital future.

## Finite Horizon: Vulnerability to Quantum Threats

 `````{margin} **ECDSA**
 Elliptic Curve Digital Signature Algorithm.
`````
 `````{margin} **SHA-256**
Secure Hash Algorithm 256-bit.
`````

The security of widely adopted cryptographic algorithms such as ECDSA and SHA-256 faces a vulnerability rooted in their finite outcome spaces. ECDSA relies on the computational complexity of discrete logarithm problems{cite}`odlyzko1984discrete`, and SHA-256 functions as a one-way hash algorithm{cite}`gueron2011sha`. However, the deterministic nature of these algorithms, resulting in a finite set of possible outputs, poses a challenge in the era of quantum computing. Quantum computers, with their formidable processing capabilities{cite}`preskill1998reliable`, could exploit algorithms like Shor's to efficiently solve discrete logarithm and hash inversion problems, potentially unraveling the security provided by ECDSA and SHA-256. The finite nature of these algorithms makes them susceptible to quantum attacks, highlighting the pressing need for quantum-resistant cryptographic solutions to fortify the integrity of digital signatures and secure hash functions in the face of evolving computational paradigms.

## Exploring Chaotic Cryptography: Quantum-Resistant Potential
Chaotic cryptographic algorithms{cite}`kocarev2001chaos`, particularly those based on systems like Lorenz{cite}`li2020image`, present an intriguing frontier in the quest for quantum-resistant security{cite}`zhang2021blockchain`. The inherent chaos in systems like Lorenz generates an infinite and highly sensitive outcome space, rendering them exceptionally resilient to conventional and quantum attacks. The sensitivity to initial conditions means that even slight variations in the secret key produce vastly different outputs{cite}`tsallis1997power`, making it virtually impossible for quantum computers to break the encryption without precise knowledge of the secret key with infinite precision. This unique characteristic positions chaotic cryptographies as promising candidates for safeguarding sensitive information in the face of evolving computational capabilities, offering a potential solution to the quantum threat looming over traditional cryptographic systems.

## The Challenge of Finding Negative Orbits
In chaotic systems, finding the negative orbit{cite}`alligood1998chaos` poses a formidable challenge due to the inherent sensitivity to initial conditions. Chaotic systems, by their nature, exhibit unpredictability and sensitivity to the smallest perturbations in the starting conditions. The search for a negative orbit involves tracing the trajectory of a system backward in time, which is hindered by the lack of precision in initial conditions and the exponential divergence of trajectories. This sensitivity makes the reverse calculation practically impossible in some systems called Nonreversible Chaotic Systems(NCS){cite}`chotorlishvili2008non`, as small errors in determining the initial state amplify rapidly, rendering precise backward prediction unattainable in these chaotic systems. The unpredictability and intricacy of chaotic dynamics thus contribute to the inherent difficulty in retracing orbits in reverse, further emphasizing the complexity of understanding negative orbits within chaotic systems.

## Propose New Chaotic Encryption Using Initial Conditions as Secret Keys

In proposing a novel approach to encryption, we leverage the chaotic dynamics of systems like Lorenz to enhance security through the utilization of initial conditions as secret keys{cite}`maurer1994strong2`. Instead of traditional methods , our proposal involves encrypting messages by identifying initial points near the secret key within the chaotic system. By transmitting only the locations of these points related to the secret point, the recipient, who possesses knowledge of the secret key, can decipher the message. This process capitalizes on the inherent sensitivity of chaotic systems to initial conditions, ensuring that any minor deviation in knowledge renders the precise decoding of the message practically impossible for unauthorized parties. Our approach harnesses the complexity of chaotic dynamics to create a robust encryption scheme, where the secret key becomes the linchpin for decrypting messages, ensuring heightened security and privacy.

## Example of Encryption
In this example, we aim to illustrate the workings of cryptography. Figure 3 contains our secret message, which we have encrypted in Figure 4. In Figure 5, it becomes evident how attempting to decrypt the message with an incorrect secret key renders the result entirely meaningless. You can watch the [full video at You Tube](https://www.youtube.com/watch?v=2V_CT5BFaig). Also, you can watch a [fullscrean video of decryption](https://www.youtube.com/watch?v=yl03frH3V6A)(including some fun).

```{figure} images/harry_me.jpg
---
width: 750px
height: 360px
name: gov_evolution
---
Message to Encrypt
```

```{figure} images/untitled33.png
---
width: 750px
height: 360px
name: gov_evolution
---
Encrypted Message
```

```{figure} images/main_frame_R.jpg
---
width: 750px
height: 360px
name: gov_evolution
---
Comparison the Right and Wrong Secret-keys
```

<!-- {cite}`shand1993fast2` {cite}`gaidimaro`-->

## Why It Might Be Quantum-Resistant?

In our proposed chaotic encryption scheme, the utilization of initial conditions as secret keys introduces a layer of security against potential quantum threats. Quantum computers, with their formidable computational capabilities{cite}`preskill1998reliable`, are known for their efficiency in certain mathematical tasks. However, the infinite space of outcomes generated by chaotic systems{cite}`benatti2012deterministic`, coupled with the need for truly infinite precision{cite}`ditto1995principles` in understanding the secret key, creates a significant barrier for quantum decryption. Unlike classical systems, where quantum algorithms might pose a threat, the sheer complexity and sensitivity of chaotic dynamics demand an unparalleled precision that challenges the capabilities of quantum computers. This presents an intriguing avenue for future research—to explore the quantum resilience of chaotic encryption{cite}`zhu2016best` and investigate the threshold where quantum decryption becomes practically implausible due to the infinite and intricate nature of chaotic outcomes{cite}`van2006quantum`. By delving into this uncharted territory, we aim to contribute to the ongoing discourse on quantum-resistant cryptographic methods and fortify the security of communication systems in the face of advancing technologies.


## Propose New Chaotic Hashing algorithm

Introducing a dynamic paradigm to hashing, our proposal involves encoding messages into points in three-dimensional space. The innovation lies in utilizing the 3D points as the initial conditions for a chaotic system, injecting an element of unpredictability and complexity into the hashing process. By dragging these points to a secret location and allowing the chaotic system to evolve for a defined duration, we generate a final set of points that serves as the hash value for the original message. This approach capitalizes on the sensitivity of chaotic systems to initial conditions, making even minor changes in the starting points lead to vastly different hash outcomes. The dynamic interplay between message encoding, spatial manipulation, and chaotic evolution introduces a unique layer of security to the hashing process. Future research could delve into the cryptographic resilience of this dynamic 3D chaotic hashing scheme and explore its potential as a quantum-resistant method, considering the intricate and expansive nature of chaotic outcomes in multidimensional spaces.





<!-- ```{figure} images/untitled33.png
---
width: 750px
height: 360px
name: gov_evolution
---
Message to Hash
``` -->



## Conclusion
In conclusion, the vulnerabilities of traditional cryptographic algorithms to quantum threats prompt a crucial shift towards quantum-resistant solutions. The proposal of chaotic cryptography, particularly leveraging the Lorenz chaotic system, emerges as a promising avenue for resilience. Its infinite and sensitive outcome space introduces a formidable barrier for quantum decryption, enhancing security against evolving computational capabilities. The proposed chaotic encryption scheme, utilizing initial conditions as secret keys, presents a paradigm shift in digital communication security, ensuring unauthorized decryption is practically impossible. The dynamic 3D chaotic hashing algorithm extends this innovation, introducing complexity and unpredictability. As quantum challenges evolve, these proposed methods invite further exploration into their quantum resilience, offering innovative layers of security for the digital era.







<div style="text-align: right;font-weight: bold;">Yimika Erinle</div>
<div style="text-align: right;font-style: italic;">April 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
