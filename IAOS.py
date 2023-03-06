from grobid_client.grobid_client import GrobidClient
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import pathlib
import sys
import os


# Creamos el cliente
grobid_client = GrobidClient("http://localhost:8070")


# Obtener la ruta donde estan los pdfs
ruta = sys.argv[1]

# Creamos una lista para los numeros de figuras por articulo
num_figuras = []

# Creamos un nuevo directorio donde guardaremos las nubes de palabras
if (os.path.exists("wordClouds") == False):
    os.mkdir("wordClouds")

# Crear y abrir el fichero de salida  en modo de escritura
archivo = open(os.path.join(os.getcwd(), "results.txt"), "w")

# Obtenemos el directorio con los articulos
directorio = pathlib.Path(ruta)

# Recorremos el directorio
for fichero in directorio.iterdir():

    archivo.write(fichero.name + "\n")

    response = grobid_client.process_pdf("processFulltextDocument", str(fichero), generateIDs=False,
                                     consolidate_header=False, consolidate_citations=False,
                                     include_raw_citations=False, include_raw_affiliations=False,
                                     tei_coordinates=False, segment_sentences=False)
    texto = str(response)

    # Verificar si la respuesta es correcta
    if response[1]==200:

        print("Codigo HTTP ",response[1])

        # Contamos cuantas figuras contiene el documento y lo introducimos en la lista
        num_figuras.append(texto.count("</figure>"))

        # Obtener informacion abstracta

        abstract = texto[texto.find("<abstract>") + len("<abstract>"): texto.find("</abstract>")]

        # Crear la nube de palabras
        wordcloud = WordCloud(width=400, height=400,
                              min_font_size=8).generate(abstract)

        # Dibujar la nube de palabras
        plt.figure(figsize=(8, 8))
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.show()
        nombre_imagen = "wordClouds/" + fichero.name + "_WordCloud.png"
        wordcloud.to_file(nombre_imagen)

        # Lista de Links por cada articulo
        patron = r'<ptr target="(https?://[^\s]+)"'
        lista_URLs = re.findall(patron, texto)
        if len(lista_URLs) == 0:
            archivo.write("No existen links en el articulo\n")
        else:
            archivo.write("Los Links encontrados son:\n")
            for link in lista_URLs:
                archivo.write(link + "\n")

        archivo.write("\n")

    else:
        print("Codigo HTTP ", response[1])

if response[1]==200:
    articulos = ["Art1", "Art2", "Art3", "Art4", "Art5", "Art6", "Art7", "Art8", "Art9", "Art10"]
    plt.bar(articulos, num_figuras)
    plt.title("Numero de figuras por articulo")
    plt.xlabel('Articulos')
    plt.ylabel('Numero de figuras')
    plt.savefig("histogram_num_figures.jpg")
