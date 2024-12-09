import http.client
import os
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError

import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = 2  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/6"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "12", "ERROR MULTIPLY"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/12/6"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "2.0", "ERROR DIVIDE"
        )

    def test_api_divide_zero(self):
        url = f"{BASE_URL}/calc/divide/5/0"
        try:
            response = urlopen(url, timeout=DEFAULT_TIMEOUT)
            # Si llegamos aquí, la respuesta fue exitosa, lo cual no debería pasar
            self.fail(f"Se esperaba un error 406 pero se recibió una respuesta exitosa de {url}")
        except HTTPError as e:
            # Verifica que el código de estado sea 406
            self.assertEqual(e.code, http.client.NOT_ACCEPTABLE, f"Error inesperado en {url}")
            # Verifica que el mensaje de la respuesta sea el esperado
            self.assertEqual(
                e.read().decode(), "Division by zero is not possible", "ERROR DIVIDE ZERO"
            )


    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )



if __name__ == "__main__":  # pragma: no cover
    unittest.main()
