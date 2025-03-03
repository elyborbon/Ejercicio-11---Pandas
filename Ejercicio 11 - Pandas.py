import pandas as pd 
datos = [["Colombia", "Peru", "Argentina"], ["Bolivia", "Uruguay"], ["Chile"]]
serie = pd.Series(datos)
print (serie)
serie = serie.apply(pd.Series).stack().reset_index(drop=True)
print (serie)