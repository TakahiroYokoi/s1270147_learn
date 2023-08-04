import plotly.express as px
import pandas as pd

class heatMapItemsFrequencies:
    def show(itemsFrequenciesDictionary: dict):
        df = pd.DataFrame.from_dict(itemsFrequenciesDictionary)
        x = []
        y = []
        for p in df:
            p1 = p.split(' ')
            try:
                f_x = float(p1[0].replace("Point(",'').replace("['",''))
                f_y = float(p1[1].replace(')','').replace("']",''))
            except:
                f_y = 0
                f_x = 0
            x.append(f_x)
            y.append(f_y)


        df = df.T
        df = df.rename(columns={0: 'amount'})
        df['X'] = x
        df['Y'] = y
        df['name'] = df.iloc[:,0]

        fig = px.scatter_mapbox(
            data_frame = df,
            lat = "Y",
            lon = "X",
            color='amount',
            hover_name = "name",
            hover_data=["amount"],
            center = {'lat':34.686567, 'lon':135.52000},
            zoom = 4,
            height = 600,
            width = 800
        )
        fig.update_layout(mapbox_style='open-street-map')
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.update_layout(title_text="Population of each cities")
        fig.show()

