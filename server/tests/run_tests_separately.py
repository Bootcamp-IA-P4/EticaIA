import unittest
import sys
import os

# Asegúrate de que la carpeta raíz esté en el path para que se pueda importar el paquete "tests"
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

tests = ["tests.test_api", "tests.test_db_save", "tests.test_scraper"]

loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity=2)

for test in tests:
    print(f"\n🔹 Ejecutando: {test}")
    suite = loader.loadTestsFromName(test)
    runner.run(suite)
