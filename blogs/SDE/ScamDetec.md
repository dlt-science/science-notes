# The Detection of Scams on the Ethereum Blockchain

<!-- ![Academic Insight](images/AI.svg) -->
<ins>**Academic Insight**</ins>

<!-- ```{admonition} Key Insights
:class: tip
- Scams constitute the most significant portion of criminal activities on Ethereum, including phishing, Ponzi schemes, pump-and-dumps, and so on.
- Scam detection on Ethereum faces various challenges, such as systematically analyzing scams, extracting features for accurate detection, and achieving timely detection.
- To combat phishing scams, a network embedding algorithm called trans2vec, which considers transaction amount and timestamp, is proposed.
- To enhance model interpretability, a semantic-aware detection approach called SADPonzi extracting semantic information from contract bytecode and matching it with ponzi semantic patterns is introduced.
- To detect honeypot contracts early in their creation, a LightGBM model incorporating N-gram features of contract bytecode is put forward.
- To predict future rug pull scams, an automated rug pull detection using features of the pool’s state and the token distribution among the users is proposed.
- To predict the coin being pumped before the actual pump event, a random forest model and a generalized linear model using the information of market movements are present.
``` -->

```{admonition} Key Insights
:class: tip
- Ethereum harbours an array of scams, spanning phishing, Ponzi schemes, and pump-and-dumps.
- Identifying and countering these scams pose intricate challenges, encompassing systematic analysis, accurate feature extraction, and prompt detection.
- Novel strategies emerge: trans2vec leveraging transaction to tackle phishing, SADPonzi deciphering bytecode for Ponzi schemes, and LightGBM incorporating N-gram features to foresee early-stage honeypots.
- Predicting rug pulls involves assessing the pool state, token distribution of users, and forecasting the coin being pumped relies on sophisticated market movement information.
```

## Introduction
Ethereum is famous as the largest blockchain platform that supports smart contracts, which has become increasingly prosperous and has attracted investors from all over the world. However, due to its anonymity, Ethereum has become a hotbed for various kinds of fraudulent activities, such as phishing scams, Ponzi schemes, honeypot schemes, rug pull scams, pump-and-dump schemes, and so on, which pose a serious threat to trading security on Ethereum. From Chainalysis 2022 Crypto Crime Report {cite}`Chainalysis2022`, scams have been the largest form of cryptocurrency-based crime since 2017, leading to significant losses, which is shown in [{numref}`crypto_value`]. Therefore, it is imperative to protect investors from scams and create a secure trading ecosystem on Ethereum. In this science note, we delve into the current academic landscape surrounding scam detection on Ethereum and summarise detection techniques of five kinds of common scams.

```{figure} images/crypto_value.png
---
name: crypto_value
---
Total cryptocurrency value received by illicit address from 2017 to 2021.
```

## Challenges in Scam Detection on Ethereum

There are three main challenges to be addressed in scam detection on Ethereum :
- **How to systematically analyze scams:** Different types of scams may employ different methods and strategies, targeting different victims. Therefore, researchers need to collect and analyze a large amount of fraud case data to gain a deeper understanding of the characteristics and patterns of fraudulent behaviour.

- **How to extract effective features:** The performance of scam detection is closely related to the choice of extracted features. Since fraudulent behaviour may exhibit subtle differences from normal behaviour, it is necessary to select discriminative features to distinguish between the two.

- **How to timely detect scams:** Detecting scams timely is crucial to minimize losses and prevent more ordinary investors from falling victim to fraud. When scams are identified or predicted early, authorities and exchanges can take appropriate actions to freeze suspicious accounts and block fraudulent transactions.

## Phishing Scam Detection
`````{margin} **Phishing Scam**
  Phishing scam is a common kind of scam where phishers attempt to obtain sensitive information and money from accounts by disguising as a trustworthy entity.
`````
Wu et al. {cite}`wu2022who` conducted the first investigation on phishing identification on Ethereum. Transaction information is very critical but cannot be captured by general random walk-based network embedding methods. Therefore, they proposed a novel network embedding algorithm called trans2vec to extract the features for subsequent phishing identification by taking the transaction amount and timestamp into consideration. They also assumed that a larger amount of value of the transaction implies a closer relationship between accounts and the later the transaction is, the greater the impact on the current relationship of the accounts.

New means of Non-Fungible Tokens (NFTs) phishing scams have emerged in the Ethereum ecosystem with the popularity of NFTs. Previous research lacks a systematic review and retrospective analysis of NFT phishing scams. Yang et al. {cite}`yang2023NFT` collected 469 NFT phishing accounts and transactions and systematically summarized different patterns of NFT phishing scams, measuring the economic impacts and preferences of scammers. Interestingly, NFT phishers chose to transfer 57.5% of NFTs to their accomplices for further operations, accompanied by signs of gang theft. Detecting NFT phishing gangs and exploring withdrawal methods could be a potential research direction in the future.

## Ponzi Scheme Detection
`````{margin} **Ponzi Scheme**
  The Ponzi scheme is an investment fraud in which so-called returns are paid to existing investors through funds provided by new investors.
`````
Existing methods to identify Ponzi smart contracts can be classified into two categories: transaction behaviour-based detection {cite}`Jung2019Data` and opcodes-based detection {cite}`chen2018ponzi`. The former requires a considerable number of transactions to learn the behaviours, and the latter lacks interpretability. Chen et al. {cite}`chen2021sadponzi` proposed SADPonzi, a semantic-aware detection approach, which utilizes the symbolic execution technique to extract semantic information from contract bytecode and match it with four semantic patterns of Ponzi contracts, ultimately identifying Ponzi contracts. Experimental results indicate that SADPonzi outperforms all the existing techniques in terms of accuracy and robustness. However, the symbolic execution technique has a limitation in handling evasion methods which can lead to serious path explosion.

## Honeypot Scheme Detection
`````{margin} **Honeypot Scam**
  Honeypot Scheme is a smart contract intentionally designed with a flaw to attract victim attackers, who attempt to exploit it by sending funds. However, the contracts fail to operate as expected, resulting in the loss of the investment.
`````
To detect honeypot contracts early in their creation, Chen et al. {cite}`chen2020honey` put forward a machine learning model for honeypot contracts detection based on N-gram features and LightGBM. They construct a series of N-Gram-based features and use a feature selection method to drop out those useless features. The model performs well in different imbalances of the data set. In the future, it is a potential way to combine the behaviour of contracts' creators and features of contracts to get a more accurate classification model for detecting honeypot contracts. 

## Rug Pull Scam Detection
`````{margin} **Rug Pull Scam**
  Rug Pull Scam is a scam where developers abandon a project and take their investors’ money when enough investors rush into the project and exchange it for worthless tokens.
`````
Xia et al. {cite}`Xia2021Trade` are the first ones to propose an accurate approach for flagging rug pull scams and the scam tokens on Uniswap based on a guilt-by-association heuristic and a machine-learning powered technique. The guilt-by-association heuristic technique helps to identify and expand 
obvious scam tokens and scammers. Machine learning-based detection helps to identify more scammers and scam tokens based on transactions on Uniswap. Interestingly, they found thousands of collusion addresses to help carry out the scams in league with the scam token/pool creators. Four kinds of collusion addresses can be seen in [{numref}`collusion_address`].

However, the method proposed by Xia et al. {cite}`Xia2021Trade` is only effective for detecting scams accurately after they have been executed. Mazorra et al. {cite}`Mazorra2022Rug` designed an accurate automated rug pull detection to predict future rug pulls and scams using relevant features of the pool’s state and the token distribution among the users. They use the Herfindahl–Hirschman Index and clustering transaction coefficient as heuristics to measure the distribution of the token among the investors. Additionally, they feed these features to train XGBoost and FT-Transformer models, respectively, and predict tokens before the malicious manoeuvre.

```{figure} images/collusion_address.png
---
name: collusion_address
---
Four kinds of collusion addresses categorized based on their Uniswap transaction behaviours.
```

## Pump-and-Dump Scheme Detection
`````{margin} **Pump-and-Dump Scheme**
  Pump-and-Dump Scheme is a form of price manipulation that involves artificially inflating an asset’s price before selling the cheaply purchased asset at a higher price. Once the assets are dumped, the price falls and investors lose money. 
`````
Telegram, with its relative anonymity, has fostered the organization of pump-and-dump activities by many people in channels. Xu et al. {cite}`Xu2019Anatomy` analyzed features of pumped coins and market movements of coins before, during, and after pump and dump. They also built a predictive random forest model and a generalized linear model able to predict the coin being pumped before the actual pump event by Telegram channels using the information of market movements. In addition, they proposed a simple but effective trading strategy that can be used in combination with the prediction models, leading to fewer people falling victim to market manipulation and more people trading strategically. Different from the work in {cite}`Xu2019Anatomy`, La et al. {cite}`La2023Dog` built a machine learning model able to detect pump-and-dump schemes using the information of rush orders within 25 seconds from the moment it starts, instead of predicting it before it happens.

## Conclusion
The popularity of Ethereum has attracted a surge of fraudulent activities, posing serious risks to users. Detecting and preventing scams on Ethereum presents several challenges, ongoing research and innovative approaches are making significant progress in scam detection. In this science note, we delve into the current academic landscape surrounding scam detection on Ethereum and summarise detection techniques of five common types of scams. Scam detection on Ethereum remains a worthwhile and pressing challenge in the field. Through ongoing exploration and innovation, we can collectively strive to build a more secure and trustworthy cryptocurrency trading ecosystem.

<div style="text-align: right;font-weight: bold;">Qishuang Fu</div>
<div style="text-align: right;font-style: italic;">August 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
