import pandas as pd
from bs4 import BeautifulSoup
import requests
import pickle


def convert_html_table(table): 
    ''' Function takes in a HTML table from a BeautifulSoup object
        Output is a pandas dataframe with appropriate rows and cols
    '''

    nrow = 0
    ncol = 0
    col_names = []
    
    #Find number of rows and columns and column names in the html table
    for row in table.find_all('tr'):
        #First find the number of rows and columns
        the_tds = row.find_all('td')
        if len(the_tds) > 0:
            nrow += 1
            if ncol == 0:
                # Set the number of columns for the table
                ncol = len(the_tds)       
        #Try to find column names in the table
        the_ths = row.find_all('th') 
        if len(the_ths) > 0 and len(col_names) == 0:
            for the_th in the_ths:
                col_names.append(the_th.get_text())
                
    #Define output dataframe
    cols = col_names if len(col_names) > 0 else range(0,ncol)
    df = pd.DataFrame(columns = cols, index= range(0,nrow))

    #Construct output dataframe, element-by-element
    i_row = 0
    for row in table.find_all('tr'):
        i_col = 0
        columns = row.find_all('th')
        for column in columns:
            df.iat[i_row,i_col] = column.get_text()
            i_col += 1
        columns = row.find_all('td')
        for column in columns:
            df.iat[i_row,i_col] = column.get_text()
            i_col += 1
        if len(columns) > 0:
            i_row += 1

   
    return df

def scrape_per_year(year):
    url = 'https://www.pro-football-reference.com/draft/%s-combine.htm' % year

    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    tab = soup.find_all('table')[0]
    table = convert_html_table(tab)

    table['Team'] = table['Drafted (tm/rnd/yr)'].str.split('/').str.get(0)
    table['Round'] = table['Drafted (tm/rnd/yr)'].str.split('/').str.get(1)
    table['Pick'] = table['Drafted (tm/rnd/yr)'].str.split('/').str.get(2)
    table['Year'] = table['Drafted (tm/rnd/yr)'].str.split('/').str.get(3)
    table['Round'] = table['Round'].str.extract('(\d+)',expand=False)
    table['Pick'] = table['Pick'].str.extract('(\d+)',expand=False)
    table.drop(['Drafted (tm/rnd/yr)', 'College'], axis=1, inplace=True)

    return table
    
#Loop through the relevant years
results = []
for y in range(2000,2016):
    df = scrape_per_year(y)
    df['Year'] = y
    results.append(df)
    
results = pd.concat(results).reset_index(drop=True)
results.to_pickle('data/sports-ref-scrape.pkl')

results


