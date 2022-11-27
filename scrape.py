def

wikiurl = "https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6ssten_Unternehmen_in_der_Schweiz"


table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)


soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())