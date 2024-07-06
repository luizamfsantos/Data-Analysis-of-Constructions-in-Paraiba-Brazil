# %%
# Import libraries

# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup

# %%
# Send an HTTP request and get the HTML content of the web page
url = 'http://159.203.110.236/obras/lista/?page=1&'
response = requests.get(url)
if response.status_code != 200:
    raise Exception("Failed to fetch the web page.")

# %%
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# %%
# Assuming the data is contained in a table with 'tr' and 'td' tags
table = soup.find('table')
data = []
for row in table.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

# %%
# Convert the extracted data into a pandas DataFrame
df = pd.DataFrame(data)

# %%


# Set column names if available
df.columns = ['Id', 'Descricao', 'Tipo','Governo','Extensao(km)','Estagio','Contrato','Valor','Valor Medido','% Financeiro','%Fisico','Empresa','Inicio','Conclusao','Fonte de Recursos','Ver']

# Display the DataFrame
print(df)

# %%
# Drop empty column 
df = df.drop(columns='Ver')

# %%
#Drop NA
df = df.drop(index=0)

# %%
# repeat steps for other pages
def scrape_page(page_number):
    base_url = 'http://159.203.110.236/obras/lista/?page='
    url = f'{base_url}{page_number}&'
    
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page {page_number}.")

    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the data is contained in a table with 'tr' and 'td' tags
    table = soup.find('table')
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

    return pd.DataFrame(data)

# Scrape pages 1, 2, 3, and 4 and concatenate the results into a single DataFrame
all_data_frames = [scrape_page(page_number) for page_number in range(1, 5)]
result_df = pd.concat(all_data_frames, ignore_index=True)

# Display the concatenated DataFrame
print(result_df)


# %%
# Set column names
result_df.columns = ['Id', 'Descricao', 'Tipo','Governo','Extensao(km)','Estagio','Contrato','Valor','Valor Medido','% Financeiro','%Fisico','Empresa','Inicio','Conclusao','Fonte de Recursos','Ver']

# %%
# # Drop empty column 
result_df = result_df.drop(columns='Ver')


# %%
# Drop useless column
result_df = result_df.drop(columns='Id')

# %%
 #Drop NA
result_df = result_df.dropna(subset=['Id'])

# %%
result_df

# %%
# Save as csv

# %%
result_df.to_csv('construcoes_pb.csv')


