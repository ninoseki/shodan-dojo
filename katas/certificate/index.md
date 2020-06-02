# SSL certificate

## Kata #1

Create a query to find a host which returns the same SSL certificate as `https://expired.badssl.com/`.

## Kata #2

Create a query to find a host which serves `https://calyxmeetbjcmzw5.onion/`.

## Hints

- [Shodan: Keeping Up with SSL](https://blog.shodan.io/ssl-update/)
- [Shodan: Duplicate SSL Serial Numbers](https://blog.shodan.io/ssl-serial-number-weirdness/)

- You can use `ssl.cert.serial` filter.
  - ssl.cert.serial:serial number (integer) or DER encoded value
  - e.g.
    - `ssl.cert.serial:21020869104500376438182461249190639870` (www.examle.org)
    - `ssl.cert.serial:0fd078dd48f1a2bd4d0f2ba96b6038fe` (www.example.org)

---

- [Answer](./answer.md)
