# Answers

## Kata #1

Shodan has several filters for SSL.

- ssl
- ssl.alpn
- ssl.cert.alg
- ssl.cert.expired
- ssl.cert.extension
- ssl.cert.fingerprint
- ssl.cert.issuer.cn
- ssl.cert.pubkey.bits
- ssl.cert.pubkey.type
- ssl.cert.serial
- ssl.cert.subject.cn
- ssl.chain_count
- ssl.cipher.bits
- ssl.cipher.name
- ssl.cipher.version
- ssl.version

You can use `ssl.cert.serial` filter for filtering results by a serial number of the SSL certificate.

```python
import ssl

from cryptography import x509
from cryptography.hazmat.backends import default_backend

pem_data = ssl.get_server_certificate(("expired.badssl.com", 443)).encode()
cert = x509.load_pem_x509_certificate(pem_data, default_backend())
print(cert.serial_number)
# 14824823351240255409
```

The answer is [ssl.cert.serial:14824823351240255409](https://www.shodan.io/search?query=ssl.cert.serial%3A14824823351240255409).

![](https://i.imgur.com/eQxUhth.png)

## Kata #2

`https://calyxmeetbjcmzw5.onion/` uses a self signed certificate.

![](https://i.imgur.com/GLhiDBv.png)

Its serial number is `00:F7:1A:27:58:7A:4C:C5:5E`.

So the answer is [ssl.cert.serial:00f71a27587a4cc55e](https://www.shodan.io/search?query=ssl.cert.serial%3A00f71a27587a4cc55e).

![](https://i.imgur.com/5mCCE2p.png)

## Kata #3

Apparently the certificate of `https://www.waseda.jp` uses `www.waseda.jp` common name.

![](https://i.imgur.com/U3pueYx.png)

You can use `ssl.cert.subject.cn` filter for filtering results by a common name of the SSL certificate.

So the answer is [ssl.cert.subject.cn:www.waseda.jp](https://www.shodan.io/search?query=ssl.cert.subject.cn%3Awww.waseda.jp).

![](https://i.imgur.com/aKu9TtO.png)

## Misc

The first answer uses integer value with `ssl.cert.serial` filter. The second answer uses [DER](https://wiki.openssl.org/index.php/DER) encoded value. You can use both values with the filter.
