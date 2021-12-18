import csv
import plotly.express as px
import numpy as np

#with open("Student Marks vs Days Present.csv") as f:
#df=csv.DictReader(f)
#fig=px.scatter(df, x="Days Present", y="Marks In Percentage")
#fig.show()

def getDataSource(data_path):
    ice_cream_sales=[]
    temperature=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            ice_cream_sales.append(float(row["Ice-cream Sales( ₹ )"]))
            temperature.append(float(row["Temperature"]))
    return {"x" : temperature, "y" : ice_cream_sales}


def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between temperature vs ice cream: ", correlation[0,1])

def setUp():
    data_path="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

setUp()


