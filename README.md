# Analyzing Road Constructions Data in the state of Pairaba, Brazil

Welcome to the data analysis project focused on road constructions in the state of Pairaba, Brazil. In this analysis, I present an in-depth examination of data obtained from the SIDA-DER/PB website [using Jupyter Notebooks and Python for web scraping](https://github.com/luizamfsantos/Data-Analysis-of-Constructions-in-Paraiba-Brazil/blob/main/Construcoes%20Paraiba%20WebScraper.ipynb). The primary objective of this project is to gain insights into the pricing strategies of construction companies and identify instances of potential overcharging after the initial project approval.

To initiate the analysis, I utilized Python and Jupyter Notebooks to gather data from the SIDA-DER/PB website, which serves as a reliable repository of road construction-related information in Paraiba, Brazil. The web scraping process enabled me to gather valuable data about various road construction projects undertaken by different companies across the state.

In the upcoming phases of this project, I will leverage Python's powerful data visualization libraries to create informative and visually appealing representations of the collected data. By presenting the findings through interactive graphs and charts, we aim to offer a clear understanding of the pricing patterns and detect any discrepancies in charges among construction companies.

The main focus of this analysis revolves around two key aspects:
1. **Cost per Kilometer:** We will delve into the data to determine the varying rates at which different construction companies charge per kilometer for their projects. This analysis will provide valuable insights into the pricing competitiveness of each company.

2. **Overcharging After Approval:** An essential aspect of this analysis involves investigating the cost discrepancies that may occur after the initial project approval. By comparing the approved project budgets with the actual charges incurred during construction, we aim to identify potential cases of overcharging.

Throughout the analysis, I will be adhering to ethical standards and ensuring data privacy and security. This project intends to contribute to a transparent and accountable road construction ecosystem in Pairaba, Brazil.

Stay tuned for the forthcoming updates, where I will present the detailed findings and visualizations derived from the collected data. Your feedback and contributions are always welcome as we work together to enhance the understanding of road constructions in Paraiba, Brazil.

Thank you for your interest in this project, and let's embark on this insightful data analysis journey together!

### Data
The data was scrapped from a government website. This is a brief summary of the main variables from the data. 
|Variable|Type|Example|What does it represent?|
|---------|----|--------------------------------|--------------------------------|
|Descricao|Char|PB-028: Fábrica Elizabeth/PB-008|Name of the road being worked on|
|Tipo|Char|Pavimentação|Type of construction being done|
|Governo|Char|João Azevedo|Government in charge during the construction|
|Extensao(km)|Float|2.9|Length of the construction|
|Estagio|Char|Concluida|Stage of the construction|
|Contrato|Char|PJ-035/2021|Contract number|
|Valor (R$)|Float|3079159.50|Real cost|
|Valor Medido (R$)|Float|1703029.29|Initial projected cost|
|% Financeiro|Float|100.00|   |
|% Fisico|Float|37.12|   |
|Empresa|Char|MAC - Mesquita Andrade Construções LTDA.|Company responsible for the construction|
|Inicio|Date|"2020-10-01"|Starting date|
|Conclusao|Date|"2021-06-01"|Conclusion date|
|Fonte de Recursos|Char|100 TESOURO DO ESTADO|Source of resources|

The provided date information initially only included the month and year for both the start and end dates. To enable date manipulation and calculate time differences, we assumed the first day of the month for both dates. Consequently, the time variation could span from -31 to 31 days, with negative variation occurring when the start date fell at the end of a month and the end date fell at the beginning of a month. For instance, if the actual dates were 2021-06-30 and 2022-07-01 for the start and end dates, respectively, the accurate time difference would be 1 year. However, my model would calculate using 2021-06-01 and 2022-07-01, resulting in 1 year and 1 month.

On the other hand, the highest positive variation would occur when the start date was at the beginning of a month, and the end date was at the end of a month. For example, if the actual start date was 2021-06-01, and the end date was 2022-07-31, the true difference would be 1 year and 2 months, while my model would calculate it as 1 year and 1 month.
