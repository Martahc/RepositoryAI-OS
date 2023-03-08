import unittest
import os



class TestProgram(unittest.TestCase):

    def test_wordClouds_exists(self):
        # Verificar si se han generado todas las nubes de palabras
        pdf_directory = os.listdir(os.path.join(os.getcwd(), "pdfs"))
        wc_directory = os.listdir(os.path.join(os.getcwd(), "wordClouds"))
        self.assertEqual(len(wc_directory), len(pdf_directory))

    def test_histogxram_exists(self):
        # Verificar si se ha generado el histograma con las figuras/articulo
        self.assertTrue(os.path.exists("histogram_num_figures.jpg"))

    def test_output_file_exists(self):
        # Verificar si el archivo de salida se ha generado
        self.assertTrue(os.path.exists("results.txt"))

    def test_output_file_not_empty(self):
        # Verificar si el archivo de salida no está vacío
        self.assertTrue(os.path.getsize("results.txt") > 0)



