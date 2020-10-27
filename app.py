import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px
import numpy 

        ### DONNEES DASHBOARD ###
#dataframe avec taux de pauvreté par etat et par ville
df_poverty=pd.read_csv("PercentagePeopleBelowPovertyLevel.csv",na_values='-',encoding = "ISO-8859-1")
#dataframe ou le taux de pauvrete de l'etat est une moyenne des taux de pauvrete de ces villes
df_poverty=df_poverty.groupby('Geographic Area')['poverty_rate'].mean().reset_index()
#dataframe qui represente le taux de personne diplomées pour chaque ville de chaque etat 
df_graduate=pd.read_csv("PercentOver25CompletedHighSchool.csv",na_values='-',encoding="ISO-8859-1")
df_graduate['percent_completed_hs']=df_graduate['percent_completed_hs'].astype(float)

#dataframe qui representera le taux de personnes diplomées par etat grace a la moyenne du taux de toutes ces villes
df_graduate=df_graduate.groupby('Geographic Area')['percent_completed_hs'].mean().reset_index()


#dataframe qui contient la population totale par etat en 2016 
#elle va permet de faire des maps de taux 
df_census=pd.read_csv("US_census.csv",na_values='00000',encoding = "ISO-8859-1")
df_census=df_census.loc[:,['NAME','STNAME','POPESTIMATE2016']]
df_census=df_census.groupby('STNAME')['POPESTIMATE2016'].sum().reset_index()
df_census=df_census.replace(to_replace='Alabama',value='AL')
df_census=df_census.replace(to_replace="Alaska",value="AK")
df_census=df_census.replace(to_replace="Arizona",value="AZ")
df_census=df_census.replace(to_replace="Arkansas",value="AR")
df_census=df_census.replace(to_replace="California",value="CA")
df_census=df_census.replace(to_replace="Colorado",value="CO")
df_census=df_census.replace(to_replace="Connecticut",value="CT")
df_census=df_census.replace(to_replace="Delaware",value="DE")
df_census=df_census.replace(to_replace="District of Columbia",value="DC")
df_census=df_census.replace(to_replace="Georgia",value="GA")
df_census=df_census.replace(to_replace="Hawaii",value="HI")
df_census=df_census.replace(to_replace="Idaho",value="ID")
df_census=df_census.replace(to_replace="Illinois",value="IL")
df_census=df_census.replace(to_replace="Indiana",value="IN")
df_census=df_census.replace(to_replace="Iowa",value="IA")
df_census=df_census.replace(to_replace="Kansas",value="KS")
df_census=df_census.replace(to_replace="Maine",value="ME")
df_census=df_census.replace(to_replace="Maryland",value="MD")
df_census=df_census.replace(to_replace="Massachussetts",value="MA")
df_census=df_census.replace(to_replace="Mississippi",value="MS")
df_census=df_census.replace(to_replace="Missouri",value="MO")
df_census=df_census.replace(to_replace="Montana",value="MT")
df_census=df_census.replace(to_replace="Michigan",value="MI")
df_census=df_census.replace(to_replace="Minnesota",value="MN")
df_census=df_census.replace(to_replace="Nebraska",value="NE")
df_census=df_census.replace(to_replace="Nevada",value="NV")
df_census=df_census.replace(to_replace="New Mexico",value="NM")
df_census=df_census.replace(to_replace="New Hampshire",value="NH")
df_census=df_census.replace(to_replace="North Carolina",value="NC")
df_census=df_census.replace(to_replace="North Dakota",value="ND")
df_census=df_census.replace(to_replace="New Jersey",value="NJ")
df_census=df_census.replace(to_replace="New York",value="NY")
df_census=df_census.replace(to_replace="Ohio",value="OH")
df_census=df_census.replace(to_replace="Oklahoma",value="OK")
df_census=df_census.replace(to_replace="Oregon",value="OR")
df_census=df_census.replace(to_replace="Pennsylvania",value="PA")
df_census=df_census.replace(to_replace="Rhode Island",value="RI")
df_census=df_census.replace(to_replace="South Carolina",value="SC")
df_census=df_census.replace(to_replace="South Dakota",value="SD")
df_census=df_census.replace(to_replace="Tennessee",value="TN")
df_census=df_census.replace(to_replace="Texas",value="TX")
df_census=df_census.replace(to_replace="Utah",value="UT")
df_census=df_census.replace(to_replace="Virginia",value="VA")
df_census=df_census.replace(to_replace="Vermont",value="VT")
df_census=df_census.replace(to_replace="Washington",value="WA")
df_census=df_census.replace(to_replace="West Virginia",value="WV")
df_census=df_census.replace(to_replace="Wisconsin",value="WI")
df_census=df_census.replace(to_replace="Wyoming",value="WY")
#creer dataframe de tous les crimes repertoriés  en 2016 a partir du fichier csv
df=pd.read_csv('new_data.csv',na_values=['99999','99998'])
#enlever toutes les lignes ou les mineurs ne sont pas impliqués
df=df.dropna(how='all',subset=["F0_9","F10_12","F13_14","F15","F16","F17","JA","JB","JH","JI","JN","JW","M0_9","M10_12","M13_14","M15","M16","M17"])
#remplacer les na par des 0
df=df.fillna(0)
#remplacer par les vrais abbreviation des etats pour etre compatible avec la map 
df=df.replace(to_replace='ALA',value='AL')
df=df.replace(to_replace="ALASKA",value="AK")
df=df.replace(to_replace="ARIZ",value="AZ")
df=df.replace(to_replace="ARK",value="AR")
df=df.replace(to_replace="CALIF",value="CA")
df=df.replace(to_replace="COLO",value="CO")
df=df.replace(to_replace="CONN",value="CT")
df=df.replace(to_replace="DEL",value="DE")
df=df.replace(to_replace="D C",value="DC")
df=df.replace(to_replace="HAWAII",value="HI")
df=df.replace(to_replace="IDAHO",value="ID")
df=df.replace(to_replace="ILL",value="IL")
df=df.replace(to_replace="IND",value="IN")
df=df.replace(to_replace="IOWA",value="IA")
df=df.replace(to_replace="KANS",value="KS")
df=df.replace(to_replace="MAINE",value="ME")
df=df.replace(to_replace="MD",value="MD")
df=df.replace(to_replace="MASS",value="MA")
df=df.replace(to_replace="MISS",value="MS")
df=df.replace(to_replace="MO",value="MO")
df=df.replace(to_replace="MONT",value="MT")
df=df.replace(to_replace="MICH",value="MI")
df=df.replace(to_replace="MINN",value="MN")
df=df.replace(to_replace="NEBR",value="NE")
df=df.replace(to_replace="NEV",value="NV")
df=df.replace(to_replace="N MEX",value="NM")
df=df.replace(to_replace="N H",value="NH")
df=df.replace(to_replace="N C",value="NC")
df=df.replace(to_replace="N DAK",value="ND")
df=df.replace(to_replace="N J",value="NJ")
df=df.replace(to_replace="N Y",value="NY")
df=df.replace(to_replace="OHIO",value="OH")
df=df.replace(to_replace="OKLA",value="OK")
df=df.replace(to_replace="OREG",value="OR")
df=df.replace(to_replace="R I",value="RI")
df=df.replace(to_replace="S C",value="SC")
df=df.replace(to_replace="S DAK",value="SD")
df=df.replace(to_replace="TENN",value="TN")
df=df.replace(to_replace="TEXAS",value="TX")
df=df.replace(to_replace="UTAH",value="UT")
df=df.replace(to_replace="WASH",value="WA")
df=df.replace(to_replace="W VA",value="WV")
df=df.replace(to_replace="WIS",value="WI")
df=df.replace(to_replace="WYO",value="WY")

#df2 correspondra a un tableau qui compte le nombre de mineurs arretés par etat 
#la fonction melt() permet de faire un pivot sur les differentes categories mise dans value_vars
df2=df.melt(id_vars=['STNAME','OFFENSE'],value_vars=["F0_9","F10_12","F13_14","F15","F16","F17","JA","JB","JH","JI","JN","JW","M0_9","M10_12","M13_14","M15","M16","M17"],value_name='arrestation',var_name='categories')

#tableau qui compte le nombre de mineurs arretés par categorie et par etat
df_categories=df2.groupby(['STNAME','categories'])['arrestation'].sum().reset_index()
df_categories=df_categories.pivot(index='STNAME',columns='categories',values='arrestation')

#cette ligne permet de supprimer les categories de race pour ne pas les compter 2 fois 
df2=df2[df2['categories'].isin(["F0_9","F10_12","F13_14","F15","F16","F17","M0_9","M10_12","M13_14","M15","M16","M17"])].reset_index()

#cette ligne va creer une nouvelle dataframe avec dedans une colonne correspondant aux etats et l'autre aux nombres de mineurs arretés
df2=df2.groupby('STNAME')['arrestation'].sum().reset_index()

#dataframe ou l'on joint la dataframe avec le nombre de personnes arretées par etat et la population totale par etat
#pour creer une colonne rate qui correspond au taux de personne arrete sur la pop totale 
df2=pd.merge(df2,df_census,on='STNAME',how='left')

#dataframe ou l'on joint la dataframe avec les taux de personnes arretées par etat et le nombre de personne arretées
# par categories pour ensuite effectuer les taux sur chaque categories 
df2=pd.merge(df2,df_categories,on='STNAME',how='left')

#creation et ajout du taux d'arrestation totales par etat
df2['rate_tot']=df2['arrestation']/df2['POPESTIMATE2016']

#creation et ajout du taux d'arrestation par sexe par etat
df2['rate_feminin']=(df2['F0_9']+df2['F10_12']+df2['F13_14']+df2['F15']+df2['F16']+df2['F17'])/df2['POPESTIMATE2016']
df2['rate_masculin']=(df2['M0_9']+df2['M10_12']+df2['M13_14']+df2['M15']+df2['M16']+df2['M17'])/df2['POPESTIMATE2016']

#creation et ajout du taux d'arrestation par age  par etat
df2['0_9']=(df2['F0_9']+df2['M0_9'])/df2['POPESTIMATE2016']
df2['10_12']=(df2['F10_12']+df2['M10_12'])/df2['POPESTIMATE2016']
df2['13_14']=(df2['F13_14']+df2['M13_14'])/df2['POPESTIMATE2016']
df2['15']=(df2['F15']+df2['M15'])/df2['POPESTIMATE2016']
df2['16']=(df2['F16']+df2['M16'])/df2['POPESTIMATE2016']
df2['17']=(df2['F17']+df2['M17'])/df2['POPESTIMATE2016']



#creation d'une dataframe avec moyenne de taux d'arrestation par tranche d'age
df_age = pd.DataFrame({'age': ['0_9','10_12','13_14','15','16','17'], 'arrestation_rate':[df2['0_9'].mean(),df2['10_12'].mean(),df2['13_14'].mean(),df2['15'].mean(),df2['16'].mean(),df2['17'].mean()] }, columns = ['age', 'arrestation_rate'])


#ligne qui marche pas : ne convertit pas en str
df_age['age']=df_age['age'].astype(str) 

##ajout du taux d'arrestation par categories par etat
df2['F0_9']=df2['F0_9']/df2['POPESTIMATE2016']
df2['F10_12']=df2['F10_12']/df2['POPESTIMATE2016']
df2['F13_14']=df2['F13_14']/df2['POPESTIMATE2016']
df2['F15']=df2['F15']/df2['POPESTIMATE2016']
df2['F16']=df2['F16']/df2['POPESTIMATE2016']
df2['F17']=df2['F17']/df2['POPESTIMATE2016']
df2['M10_12']=df2['M10_12']/df2['POPESTIMATE2016']
df2['M0_9']=df2['M0_9']/df2['POPESTIMATE2016']
df2['M13_14']=df2['M13_14']/df2['POPESTIMATE2016']
df2['M15']=df2['M15']/df2['POPESTIMATE2016']
df2['M16']=df2['M16']/df2['POPESTIMATE2016']
df2['M17']=df2['M17']/df2['POPESTIMATE2016']
df2['JA']=df2['JA']/df2['POPESTIMATE2016']
df2['JW']=df2['JW']/df2['POPESTIMATE2016']
df2['JB']=df2['JB']/df2['POPESTIMATE2016']
df2['JH']=df2['JH']/df2['POPESTIMATE2016']
df2['JI']=df2['JI']/df2['POPESTIMATE2016']
df2['JN']=df2['JN']/df2['POPESTIMATE2016']



### MISE EN PLACE DASHBOARD ###

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {

    'background': '#000000',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        children='Implication de mineurs dans des crimes aux Etats-Unis'),
    dcc.Markdown('''### Codebook: 
                    Abbreviations des états:
            Alabama:AL      Louisiana:LA        Maine:ME                Alaska:AK\t         
            Maryland:MD     Arizona:AZ          Massachusetts:MA        Arkansas:AR\t        
            Michigan:MI     California:CA       Minnesota:MN            Colorado:CO\t
            Mississippi:MS  Connecticut:CT      Missouri:MO             Delaware:DE\t
            Montana:MT      District of Columbia:DC     Nebraska:NE     Florida:FL\t
            Nevada:NV       Georgia:GA          New Hampshire:NH        Idaho:ID\t
            New Jersey:NJ   Illinois:IL         New Mexico:NM           Indiana:IN\t
            New York:NY     Hawaii:HI           North Carolina:NC       Iowa:IA\t
            North Dakota:ND Kansas:KS           Ohio:OH                 Kentucky:KY\t
            Oklahoma:OK     Washington:WA       Oregon:OR               West Virginia:WV\t
            Pennsylvania:PA Wisconsin:WI        Rhode Island:RI         Wyoming:WY\t
            South Carolina:SC  South Dakota:SD  Tennessee:TN            Texas:TX\t
            Utah:UT         Vermont:VT          Virginia:VA\n
            '''),

    html.H4(children='''
        PARTIE SUR LE TAUX DE PAUVRETE.\n
    '''),
    dcc.Graph(
        id='graph_poverty',
        figure={
            'data':[
                {'x':df_poverty['Geographic Area'],'y':df_poverty['poverty_rate'],'type':'bar','name':'Taux de pauvreté par etat'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'title':'Taux de pauvreté par état'
            }
        }
    ),
    dcc.Graph(
        id='map_us',
        figure={
           "data":[go.Choropleth(
                    locations=df_poverty['Geographic Area'], # Spatial coordinates
                    z = df_poverty['poverty_rate'].astype(float), # Data to be color-coded
                    locationmode = 'USA-states', # set of locations match entries in `locations`
                    colorscale = 'Reds',
                    colorbar_title = "Taux de pauvreté",
                )],
            "layout":go.Layout(title = go.layout.Title(
                    text = 'Map du taux de pauvreté aux USA en 2016'
                    ),
                    geo = {
                    'scope' : 'usa',
                    'projection':{'type':'albers usa'},
                    'showlakes': True,
                    'lakecolor':'rgb(255, 255, 255)'}
            )
        }
    ),
    html.H4(children='''
        PARTIE SUR LE TAUX DE PERSONNES DIPLOMEES .\n
    '''),
    dcc.Graph(
        id='graph_graduate',
        figure={
            'data':[
                {'x':df_graduate['Geographic Area'],'y':df_graduate['percent_completed_hs'],'type':'bar','name':'Taux de diplomés par etat'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'title':'Taux de pauvreté par état'
            }
        }
    ),
    dcc.Graph(
        id='map_us_graduate',
        figure={
           "data":[go.Choropleth(
                    locations=df_graduate['Geographic Area'], # Spatial coordinates
                    z = df_graduate['percent_completed_hs'].astype(float), # Data to be color-coded
                    locationmode = 'USA-states', # set of locations match entries in `locations`
                    colorscale = 'dense',
                    colorbar_title = "Taux de diplomés",
                )],
            "layout":go.Layout(title = go.layout.Title(
                    text = 'Map du taux de diplomés aux USA en 2016'
                    ),
                    geo = {
                    'scope' : 'usa',
                    'projection':{'type':'albers usa'},
                    'showlakes': True,
                    'lakecolor':'rgb(255, 255, 255)'}
            )
        }
    ),

    html.H4(children='PARTIE SUR LES ARRESTATIONS DE MINEURS POUR CHAQUE ETAT'),
    generate_table(df2),
    # Ce graphe ne fonctionne pas a cause de la conversion de type, nous voulions réaliser un graphe representant le taux de crime 
    # réalisé par tranche d'age par rapport aux nombre de crimes totales 

    # dcc.Graph(
    #     id='graph_age',
    #     figure={
    #         'data':[    #ce graphe ne marche pas a cause du pb de conversion 
    #             {'x':df_age['age'],'y':df_age['arrestation_rate'],'type':'bar','name':'Taux darrestation par age'}
    #         ],
    #         'layout': {
    #             'plot_bgcolor': colors['background'],
    #             'paper_bgcolor': colors['background'],
    #             'title':'Taux darrestation par age'
    #         }
    #     }
    # ),
    html.Div([html.Div([html.H1("Map interactive des USA representant les taux d'arrestations de mineurs")],
                                style={'textAlign': "center", "padding-bottom": "30"}),
                       html.Div([dcc.Dropdown(id="value-selected", value='rate_tot',
                                              options=[{'label': "taux d'arrestations totales", 'value': 'rate_tot'},
                                                        {'label': "taux d'arrestations de filles", 'value': 'rate_feminin'},
                                                        {'label': "taux d'arrestations de garcons", 'value': 'rate_masculin'},
                                                       {'label': "Taux d'arrestations de jeunes noirs", 'value': 'JB'},
                                                       {'label': "Taux d'arrestations de jeunes blancs ", 'value': 'JW'},
                                                       {'label': "taux d'arrestations de jeunes asiatiques", 'value': 'JA'},
                                                       {'label': "taux d'arrestations de jeunes indiens", 'value': 'JI'}],
                                              style={"display": "block", "margin-left": "auto", "margin-right": "auto",
                                                     "width": "70%"},
                                              className="six columns")], className="row"),
                       ], className="container"),
    dcc.Graph(
         id='map_us_nb_arrestation',
         figure={
            "data":[go.Choropleth(
                     locations=df2['STNAME'], # Spatial coordinates
                     z = df2['rate_tot'].astype(float), # Data to be color-coded
                     locationmode = 'USA-states', # set of locations match entries in `locations`
                     colorscale = 'Reds',
                     colorbar_title = "Taux de mineurs arrêtés",
                 )],
             "layout":go.Layout(title = go.layout.Title(
                     text = 'Map du taux de mineurs arretés aux USA en 2016'
                     ),
                     geo = {
                     'scope' : 'usa',
                     'projection':{'type':'albers usa'},
                     'showlakes': True,
                     'lakecolor':'rgb(255, 255, 255)'}
             )
         }
     ),
])
@app.callback(
    dash.dependencies.Output("map_us_nb_arrestation", "figure"),
    [dash.dependencies.Input("value-selected", "value")])
def update_figure(selected):
    def title(text):
        if text == "rate_tot":
            return "Taux d'arrestations totales par état "
        elif text == "JB":
            return "Taux d'arrestations de jeunes noirs par état"
        elif text == "JW":
            return "Taux d'arrestations de jeunes blancs par état"
        elif text == "JA":
            return "Taux d'arrestations de jeunes asiatiques par état"
        else:
            return "Taux d'arrestations de jeunes indiens par état"
    trace = go.Choropleth(locations=df2['STNAME'],z=df2[selected],locationmode='USA-states',text=df2['STNAME'],autocolorscale=False,
                          colorscale="YlGnBu",colorbar={"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                    'title': {"text": title(selected), "side": "bottom"}})
    return {"data": [trace],
            "layout": go.Layout(title=title(selected),height=800,geo={'scope':'usa','showlakes':True,'lakecolor':'rgb(255, 255, 255)',
                                                                      'projection': {'type': "albers usa"}})}

if __name__ == '__main__':
    app.run_server(debug=True)
    
    



# **Nombre d'arrestations par état**
# Les Etats où le nombre de mineurs arrêtés est le plus important sont la Californie, le Texas, le Wisconsin et la Pennsylvanie. La Californie et le Texas sont les deux états les plus peuplés des Etats-Unis et la Pennsylvanie est le 6e. Cela peut expliquer ces chiffres. 
# 
# 
# 
# 
# **Taux de filles impliquées dans des crimes**
# On remarque ici que les filles sont plus impliquées que les garçons dans deux types de crimes seulements : la prostitution et le vice commercial d'une part, et le délit de fuite d'autre part. Ce sont les deux crimes dans lesquelles les filles sont le plus impliquées. 
# 
# 
# 
# 
# **Taux de garçons impliqués dans des crimes**
# Là où le taux de garçons impliqués dans des affaires judiciaires est le plus élevé se trouve être le bookmaking : les paris d'argent. Le deuxième crime majoritairement commis par des garçons se trouve être le viol. On remarque plus globalement que les affaires judiciaires concernent plus majoritairement les garçons que les filles.
# 
# 
# 
# 
# **Nombres de crimes effectués en fonction de la race**
# L'étude des données révèle que les mineurs blancs sont le plus impliqués dans des affaires judiciaires à hauteur de 60.000 environ puis que ce seraient les mineurs noirs à hauteur de 30.000 environ. Les autres ethnies sont beaucoup moins impliquées dans les affaires. Cela s'explique par la densité de population des différentes ethnies: la population blanche représentant la plus grande partie de la population américaine et la population noire représentant une autre grande partie toutefois moins importante.
# 
# 
# 
# 
# **Taux de crimes par état**
# Les états dont le taux de crime est le plus important sont le Wyoming, le Montana et l'Idaho. Ce sont des états peu peuplés du Nord-Ouest des Etats-Unis. On remarque que les états les plus peuplés ne font pas partie des états dont le taux de crimes est le plus important.
# 
# 
# 
# 
# **Conclusion**
# Ce projet nous a permit de développer notre maîtrise du langage: python. 