# Net Zero Banking Alliance: A Token-based Model

<ins>**Industry Perspective**</ins>

```{admonition} Key Insights
:class: tip
- A token-based model marks a significant evolution in sustainable finance, effectively integrating environmental goals with banking operations, particularly in managing financed emissions.
- Tokens quantify CO2 emissions, offering a precise and transparent method to track and manage emissions in banking activities, aligning financial practices with environmental targets.
- This system allows for nuanced emissions management, supporting intertemporal and cross-industry compensation, and enhancing efforts to achieve Net Zero goals.
- Utilising blockchain technology for CO2 tokens adds a layer of security and efficiency, fostering trust in the banking sector's environmental commitments.
- The model shifts focus from traditional metrics to the actual purpose of financing, ensuring more accurate impact in reducing banking portfolios' carbon footprint.
- Despite its potential, the model's implementation faces challenges such as stakeholder alignment, regulatory compliance, and balancing financial and environmental objectives, underscoring the need for ongoing adaptation in sustainable finance.
```

## Introduction

ESG, an acronym that stands for Environmental, Social, and Governance, represents a paradigm shift in how businesses and investors evaluate the impact of their activities. While the three pillars—environmental, social, and governance—reflect distinct dimensions, our spotlight falls distinctly on the environmental realm, echoing the growing urgency to address climate change and environmental sustainability.

Within the environmental spectrum, the concept of emissions is stratified into three critical scopes, each bearing a unique set of challenges and opportunities. 

**Scope 1** emissions encompass direct emissions from sources owned or controlled by the bank, which typically include internal combustion engines and on-site energy production. These emissions are directly measurable and quantifiable, forming the foundational layer of a bank’s carbon footprint.

**Scope 2** emissions, on the other hand, entail indirect emissions associated with the electricity, heating, and cooling consumed by a bank. While not originating directly from the bank, Scope 2 emissions are nevertheless a consequence of the bank's operations, highlighting the necessity to transition towards cleaner, renewable energy sources.

**Scope 3** emissions broaden the horizon, encompassing a web of indirect emissions that result from a bank's value chain. This includes emissions linked to the bank's customers, suppliers, and the lifecycle of products and services. Thus, a bank's Scope 3 emissions essentially comprise the Scope 1 and Scope 2 emissions of their customers. Consequently, it is common to refer to these as 'financed emissions' {cite}`nationalgrid2023what`.

`````{margin} **CO2 Equivalent (CO2e)**
  CO2 equivalent, often abbreviated as CO2e, is a crucial measurement that represents a unified metric encompassing various greenhouse gases' impact on global warming.
`````
Furthermore, one of the most important metric in ESG world is CO2 Equivalent (CO2e) {cite}`europa2023glossary`. It quantifies emissions in terms of the amount of CO2 that would exert an equivalent warming effect over a specified period. Understanding CO2e is vital for assessing and mitigating environmental impact.

In this article, we aim to explore the links between the banking system and its financed emissions. The Net Zero Banking Alliance {cite}`unepfi2023Net` stands at the forefront of this exploration. This collaborative coalition of banks and financial institutions is dedicated to mitigating climate change. Its primary goal is to address 'Scope 3' emissions, which constitute the largest portion of a bank’s emissions. Banks participating in this initiative commit to reducing their CO2e footprint, particularly by focusing on their Scope 3 emissions. From the customers' perspective, these are equivalent to Scope 1 and Scope 2 emissions, often termed 'financed emissions.' In addition to reducing emissions, these banks support sustainable initiatives. This alliance is crucial in reshaping the financial sector's role in environmental conservation. Its goals include a 55% reduction in financed emissions by 2030 and, by 2050, balancing any remaining financed emissions with activities that remove an equivalent amount of greenhouse gases from the atmosphere, such as afforestation, reforestation, and carbon capture technologies {cite}`unicredit2023our` {cite}`credit2022credit`.

For financial institutions, joining the Net Zero Banking Alliance is pivotal. It goes beyond just meeting regulatory requirements; it establishes credibility, fosters client trust, and attracts eco-conscious investors. Embracing sustainability, banks contribute to environmental protection and enhance their long-term viability and resilience against climate-related risks.

Additionally, being a pioneer in adopting the Net Zero approach in a proactive way can provide a competitive edge in the growing arena of green assets. Contrary to the common misconception of a trade-off between emissions and profits, it is possible to cut this trade-off by highlighting the potential for simultaneous environmental stewardship and financial growth.

The aim of this article is to argue that the current approach to the Net Zero methodology in banking is overly cautious and not as effective from an ESG optimisation perspective. In other words, it's not fully efficient in reducing the carbon footprint of current bank portfolios.


## Net Zero as-Is mechanics

Current strategies and methodologies in the banking industry involve several key steps to integrate Net Zero principles:

- **Identifying Industry Perimeter:** Industry perimeters (e.g., Oil & Gas, Power, Steel, etc.) are identified based on NACE codes {cite}`europa2010list` related to customers as present in Master Data information. This is one of the most significant pain points. The Net Zero methodology should be linked to the purpose of the financing, not the NACE code of the company. For example, general financing with no clear purpose should no longer be allowed. If a steel company has a loan for installing photovoltaic panels to generate renewable energy for its activities, this loan should not be included in the Net Zero baseline for the Steel industry. This represents a major data quality issue in banks. It's crucial to start an initiative to map the real purpose of historical loans (i.e., stock) to avoid withdrawing credit lines from companies that are paradoxically implementing ESG strategies, as in the steel company example. According to the standard and as-is Net Zero approach, general financing towards steel (typically mapped with steel NACEs) should be avoided due to the carbon intensity emissions of the steel industry. However, financing for renewable energy, mapped with specific NACEs related to the specific purpose of financing and not to the industry, will highlight an ESG benefit derived from this financing.

- **Maturity of Loans:** As best practice, loans with a residual maturity of under one year should not be included.

- **Credit Status of Loans:** If a loan is a Non-Performing Exposure, it should not be considered to avoid artificially increasing baselines and preventing greenwashing. That is, a baseline that is artificially too large can be easily reduced to meet Net Zero targets.

- **Common Metrics Towards Various Industries in Net Zero Baseline:** Establishing common metrics for various industries is essential in the Net Zero baseline.

`````{margin} **Enterprise Value Including Cash (EVIC)**
  Enterprise Value Including Cash (EVIC) is defined as the aggregate of the market capitalization of a company's ordinary and preferred shares at the end of the fiscal year, combined with the book values of its total debt and minority interests, without subtracting any cash or cash equivalents to preclude the occurrence of negative enterprise values.
`````

- **Calculating EVIC for Each Customer:** EVIC, or Enterprise Value Including Cash, is calculated as the sum of the ordinary shares' market capitalization at the fiscal year-end, the market capitalization of preferred shares at the fiscal year-end, and the book values of total debt and minority interests {cite}`openriskEnterprise`. The current calculation methodology involves determining the proportion of a company’s EVIC that is attributable to a specific bank.

```{figure} images/DATA1.png
---
width: 393px
height: 221px
name: data_1
---

```

For example, let's consider a steel company with a 1 billion € EVIC, financed by several banks. If Bank 1 has extended a loan of 100 million € to this company, it means Bank 1 holds 10% of the steel company’s EVIC. According to the Net Zero methodology, 10% of the steel company’s emissions (Scope 1 and Scope 2) are then attributable to Bank 1’s financed emissions (Scope 3), and this 10% contributes to Bank 1’s Net Zero emissions baseline.

However, this is another point of contention. For a bank joining the Net Zero Banking Alliance, it's more relevant to consider the proportion of the loan granted to the steel company in relation to the bank's balance sheet, rather than the other way around. This requires a paradigm shift in the calculation approach. The table below illustrates this concept.

```{figure} images/DATA2.png
---
width: 393px
height: 221px
name: data_2
---

```

As demonstrated in this example, and comparing the two tables, the accurate ratio to consider should be 20%, not 10%. This 20% represents the portion of the steel company’s emissions that should be attributable to Bank 1’s Net Zero baseline.

- **Setting Baseline Years and Targets:** Financial institutions establish baseline perimeters and specific emission reduction targets for high-emission industries such as cement, aviation, automotive, oil & gas, and power sectors. Each perimeter consists of a list of companies operating in one of these industries, serving as the starting point for evaluating environmental impact.

- **Monitoring at Company and Portfolio Levels:** Banks meticulously monitor emissions data at both the company and portfolio levels, with detailed expectations for emission reduction. Actual emission values are compared against expected detailed GHG values during the Net Zero time horizon (2030 and 2050), facilitating a comprehensive analysis of the environmental impact {cite}`credit2022our2050`.

- **Plethora of Metrics:** The metrics used within banks and industries, especially in the Oil & Gas sector, are not uniform. For example, Credit Agricole’s Net Zero Oil & Gas targets {cite}`credit2022credit` include 'Scope 1&2 of all counterparts and Scope 3 of upstream players, based on our on-balance sheet exposure.' In contrast, UniCredit’s Net Zero Oil & Gas targets {cite}`unicredit2022overview` consider only 'Scope 3, Category 11' {cite}`unicredit2022ourpath`. This example illustrates how targets vary depending on the metrics used. The Net Zero Banking Alliance should ensure a top-down approach that is equal for all market players.

- **Integration of Net Zero in Credit Origination Processes:** It is essential to integrate Net Zero principles into credit origination processes. Each potential counterpart is evaluated from a Net Zero perspective, including determining if the counterpart falls within the baseline perimeter. If it does, the next step is to assess whether the counterpart adheres to the expected reduction plan outlined in Net Zero documents. If the criteria are met, the credit process proceeds; if not, additional documentation and commitments are requested. In some cases, if the criteria are not met, the credit may not be approved, ensuring support only for environmentally responsible businesses.

This meticulous approach should ensure that banks not only adhere to their own sustainability goals but also contribute significantly to the global effort of reducing carbon emissions. By embedding Net Zero principles into their credit evaluation processes, financial institutions play a vital role in promoting environmentally conscious business practices and fostering a greener, more sustainable future.

## Net Zero proposed approach

As discussed in the previous section, the current Net Zero approach has several weaknesses, primarily related to the NACE-industry related approach, the plethora of metrics, and the EVIC approach. Additionally, a revised approach should consider the following aspects:

1. **The need for a more dynamic model:** The current model is predominantly mathematical and requires modification to account for the financial and economic dynamics of banks and their customers' transition plans. The current baselines might be overly penalising, particularly for customers with high transition risks, potentially depriving them of the opportunity to set up effective transition plans to reduce their emissions.

2. **Incorporating mechanisms for compensation:** The existing model links the granting of credit to a company's emissions but fails to include mechanisms for compensation:

- Between different companies.
- Within the same bank's portfolio.
- Across various industries that constitute the bank's exposure.

In our view, the challenge lies in **mismatched metrics and the unexploited CO2e potential**. For instance, when companies exceed their emission reduction targets, there remains an unutilised CO2e capacity. This presents an opportunity for financing other businesses, both in general financing and specialised financing domains.

By addressing these issues, the proposed approach aims to create a more balanced and effective strategy for implementing Net Zero principles in the banking sector. This would allow for a more nuanced assessment of companies’ emissions and better support the transition towards lower carbon outputs across different industries {cite}`intensa2023strategy`.

### Scenario 1

```{figure} images/Scenario1.png
---
width: 1141px
height: 183px
name: scenario_1
---

```
This scenario represents the best-case outcome: assuming a target for reducing emissions by 30%, all companies in our example successfully meet this target. Consequently, no CO2 equivalent compensation within the portfolio is necessary.

```{figure} images/scene1.png 
---
width: 1158px
height: 107px
name: scene_1
---

```

As demonstrated in the data, this portfolio achieves a total savings of 4,479,042 tons of CO2 equivalent. These savings can be transferred from this portfolio to other portfolios that are not generating savings but are accruing CO2 equivalent debits.

### Scenario 2

In this scenario, as illustrated in the data below, the portfolio generates a CO2 equivalent debit in years X+1 and X+2. Faced with this situation, the top managers of the Oil & Gas portfolio have a couple of options, according to the proposed model:

- Compensate for the debit by requesting an equivalent amount of CO2 equivalent savings from other portfolios. This approach relies on the inter-portfolio exchange of CO2 credits to balance emissions.

- If they have confidence in the credibility of their customers' transition plans, they can opt to wait for intertemporal compensation within their own Oil & Gas portfolio.

For instance, examining the table provided, it’s evident that all companies within the portfolio eventually reach the target reduction of 30%. The previous CO2 debits (related to years X+1 and X+2) are successfully compensated in subsequent years X+3, X+4, and X+5. 

```{figure} images/Scenario2.png
---
width: 1138px
height: 188px
name: scenario_2
---

```

```{figure} images/scene2.png
---
width: 970px
height: 152px
name: scene_2
---

```

### Scenario 3

In this scenario, as shown in the data below, the portfolio generates a CO2 equivalent debit in years X+1 and X+2. The top managers of the Oil & Gas portfolio, following the proposed model, have several options:

- They can compensate for the debit by requesting an equivalent amount of CO2 equivalent savings from other portfolios, effectively balancing emissions through inter-portfolio exchanges.

- If they trust the credibility of their customers' transition plans, they can opt for intertemporal compensation within their own Oil & Gas portfolio.

However, in contrast to Scenario 2, not all companies within this portfolio achieve the target reduction of 30%. Therefore, according to our model, the previous CO2 debits (related to years X+1 and X+2) are only partially compensated in years X+3, X+4, and X+5.

Additionally, for a company like Company C, which does not meet the target, the top managers face a strategic decision. If Company C is significant for the bank’s income statement and balance sheet, they might decide to retain it in the portfolio. Conversely, if Company C is not strategically important from an economic and financial perspective, a run-off strategy may be implemented, or a deeper analysis of the new transition plan could be considered.

This scenario highlights the challenges and strategic decisions involved in managing a portfolio with varying levels of emission reductions and underscores the importance of aligning environmental goals with financial and economic considerations.

```{figure} images/Scenario3.png
---
width: 1137px
height: 190px
name: scenario_3
---

```

```{figure} images/scene3.png 
---
width: 965px
height: 147px
name: scene_3
---

```

### Scenario 4 

In this scenario, none of the companies within our portfolio reach the final target of a 30% reduction in emissions, and all fail to meet the yearly targets from year X+2 onwards.

In such a case, a detailed analysis is required for each company to determine:

- Which companies should be put in run-off due to their inability to meet emission targets.

- Which companies should be retained in the portfolio. This could be because they are strategically important, or they could potentially be financed with green financing, among other reasons.

Moreover, it becomes necessary to compensate for these CO2 debits with emissions savings from another portfolio, such as the power portfolio. This analysis should be conducted annually as soon as the yearly data are available. The focus should be on cherry-picking companies that:

- Are on track to reach the Net Zero pathway.
- Are the most profitable for the bank.
- If they are not on track to reach the Net Zero pathway but are profitable and strategic for the bank's portfolio, they should be financed with green financing to help them align with the Net Zero pathway.

This scenario highlights the need for an ongoing, dynamic approach to portfolio management, balancing environmental targets with financial and strategic considerations. It underscores the importance of adaptive strategies in achieving Net Zero goals while maintaining profitability.

```{figure} images/Scenario4.png 
---
width: 1141px
height: 193px
name: scenario_4
---

```

```{figure} images/scene4.png
---
width: 1160px
height: 107px
name: scene_4
---

```

## Tokens for Net Zero Proposed Mechanics

The proposed model for Net Zero banking is founded on several key principles:

1. Compensation of CO2 equivalent within and across portfolios, including intertemporal compensation.
2. Compensation of CO2 equivalent among companies within the same portfolio.
3. The use of tokens and tokenomics as central enablers for the efficient management and allocation of CO2 equivalent units.

Building Blocks of the New Model:

- **Maximising Revenues and Emission Reduction:** This model aims to maximise revenues without exceeding CO2 equivalent targets, effectively eliminating the trade-off between emissions and profits.
- **Introduction of Tokens:** Tokens represent CO2 equivalent units, facilitating efficient and value-driven transactions. These digital tokens are transferable within the bank’s organisational structures (e.g., from one portfolio to another) using internal transfer rates.
- **Central Organisational Structure:** A centralised 'CO2 Treasury' manages the CO2 tokens, providing an effective system for reallocating savings from compliant companies to those that are not.

Tokens are digital representations of CO2 equivalent units and possess several characteristics:

- **Fungibility:** Tokens are interchangeable, each having equivalent value within the system.
- **Divisibility:** Tokens can be divided into smaller units, enhancing liquidity.
- **Intrinsic Value:** Tokens hold real value, making them valuable assets.


Tokenomics governs these tokens, ensuring sustainable supply, stability, and a robust carbon credit ecosystem. The value of these tokens may fluctuate based on various factors and can be transferred with specific penalties or weighting schemes to maximise effectiveness.

Central organisational structure 'CO2 Treasury' can play a crucial role in this model, managing the distribution and movement of CO2 equivalent tokens among portfolios and over time. This centralised system ensures efficient allocation and utilisation, avoiding moral hazards among Relationship Managers.

Utilising blockchain technology can significantly enhance the transparency, security, and efficiency of these transactions. Blockchain provides an immutable ledger that ensures the integrity of token movements, fostering trust among stakeholders. The 'CO2 Treasury' issues these tokens when baselines are established and is the sole official issuer of CO2 tokens within the bank. It is the only organisational structure authorised to move them among bank portfolios. The responsibility for intertemporal movements within the same portfolio lies with the Portfolio Manager.

## Conclusion

In summary, the proposed token-based Net Zero banking model represents a significant shift in the industry. By adopting tokens, banks can more effectively navigate the complexities of emissions reductions. This model's key components include maximising revenues, introducing tokens, implementing a central organisational structure, and integrating blockchain technology.

Key Findings:

1. **As-Is Net Zero Mechanics:** We have identified pain points in the current use of NACE codes and the EVIC model. It's crucial to consider the NACE of the loan (new business and stock) rather than the NACE related to the company. Additionally, the significance of loans in relation to a single company or economic group should be weighed against the bank’s balance sheet, rather than the other way around.
2. **Efficient Carbon Credit Management:** The token-based model facilitates the efficient management of CO2 equivalent units, ensuring that emissions reduction targets are met while maximising business opportunities.

3. **Blockchain Integration:** The integration of blockchain technology enhances the transparency and security of CO2 token transactions, fostering trust among stakeholders.

Future research on the token-based Net Zero banking model should focus on two key areas: the effectiveness of transferring CO2 equivalent tokens within the banking system, particularly considering penalties and valuation over time, and the impact of this model on banks' business models, risk management, and client relationships. This exploration is crucial for advancing a sustainable and financially viable approach in the banking sector.


<div style="text-align: right;font-weight: bold;">Alessio Pezzotta</div>
<div style="text-align: right;font-style: italic;">December 2023</div>

## References

```{bibliography}
:filter: docname in docnames
```
