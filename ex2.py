import pandas as pd
import matplotlib.pyplot as plt


def weno2():
    df = pd.read_csv("Leo_Llistat.csv", usecols=['NAME', 'ABSENCES', 'GROUP', 'MODULE'])
    daw = df[(df['GROUP'] == 'DAW2')]

    return weno2()
