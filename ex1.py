import pandas as pd
import matplotlib.pyplot as plt


def weno():
    df = pd.read_csv("Leo_Llistat.csv", usecols=['NAME', 'NOTES', 'YEAR'])
    exe = df.groupby(by='NAME').mean()
    clase = df['NAME']

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    alumnos = clase
    media = exe
    ax.bar(alumnos, media)
    plt.show()

    return plt.show()
