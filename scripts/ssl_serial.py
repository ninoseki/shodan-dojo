import ssl

from cryptography import x509
from cryptography.hazmat.backends import default_backend

pem_data = ssl.get_server_certificate(("expired.badssl.com", 443)).encode()
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
print(cert.serial_number)
# 14824823351240255409
