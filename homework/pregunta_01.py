import glob
import os

import matplotlib.pyplot as plt
import pandas as pd

def pregunta_01():
  
  def graficar_datos(dataframe, ruta_grafico):
    def propiedades_series():
      return {
        "Television": ["dimgray", 1, 2],
        "Newspaper": ["grey", 1, 2],
        "Internet": ["tab:blue", 2, 3],
        "Radio": ["lightgrey", 1, 2],
      }
    
    def establecer_marcadores(dataframe, columna):
      for i in [0, -1]:
        plt.scatter(
          x=dataframe.index[i],
          y=dataframe[columna].iloc[i],
          color=propiedades_series()[columna][0],
        )
        
    def establecer_etiquetas(dataframe, columna):
        for i in [0, -1]:
          desplazamiento = 0.2 if i == 0 else -0.2
          alineacion_horizontal = "right" if i == 0 else "left"
          texto_valor = (
            f"{columna} {str(dataframe[columna][dataframe.index[i]])} %"
            if i == 0
            else f"{str(dataframe[columna][dataframe.index[i]])} %"
          )
          plt.text(
            dataframe.index[i] - desplazamiento,
            dataframe[columna][dataframe.index[i]],
            texto_valor,
            ha=alineacion_horizontal,
            va="center",
            color=propiedades_series()[columna][0],
          )
          
    def establecer_xticks(dataframe):
      plt.xticks(
        ticks=dataframe.index,
        labels=dataframe.index,
        ha="center",
      )

    def crear_grafico(dataframe):
      for columna in dataframe.columns:
        plt.plot(
          dataframe[columna],
          label=columna,
          color=propiedades_series()[columna][0],
          zorder=propiedades_series()[columna][1],
          linewidth=propiedades_series()[columna][2],
        )
        
        establecer_marcadores(dataframe, columna)
        
        establecer_etiquetas(dataframe, columna)
        
        establecer_xticks(dataframe)

    def embellecer_grafico():
      
      plt.title("Cómo las personas obtienen sus noticias", fontsize=16)
      plt.gca().spines["top"].set_visible(False)
      plt.gca().spines["left"].set_visible(False)
      plt.gca().spines["right"].set_visible(False)
      plt.gca().axes.get_yaxis().set_visible(False)
      plt.tight_layout()
      plt.annotate(
        " Fuentes",
        xy=(0.5, 1),
        xycoords="axes fraction",
        xytext=(0.5, 0.97),
        textcoords="axes fraction",
        horizontalalignment="center",
        fontsize=7,
      )

    def guardar_grafico(ruta_grafico):
      directorio_grafico = os.path.dirname(ruta_grafico)
      if os.path.exists(directorio_grafico):
        for archivo in glob.glob(f"{directorio_grafico}/*"):
          os.remove(archivo)
        os.rmdir(directorio_grafico)
      os.makedirs(directorio_grafico)
      plt.savefig(ruta_grafico)

    crear_grafico(dataframe)
    embellecer_grafico()
    guardar_grafico(ruta_grafico)

  datos = pd.read_csv("files/input/news.csv", index_col=0)
  graficar_datos(datos, "files/plots/news.png")

  return "Gráfico creado correctamente"


if __name__ == "__main__":
    print(pregunta_01())
