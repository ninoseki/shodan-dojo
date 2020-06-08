# SSL certificate

## Kata #1

Create a query to find a host which returns the same SSL certificate as `https://expired.badssl.com/`.

## Kata #2

Create a query to find a host which serves `https://calyxmeetbjcmzw5.onion/`.

## Kata #3

Create a query to find hosts serves `https://www.waseda.jp`.

### Notes

The website is protected by Cloudflare.

```bash
$ curl -v -s  https://www.waseda.jp > /dev/null
...
> GET / HTTP/2
> Host: www.waseda.jp
> User-Agent: curl/7.54.0
> Accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS updated)!
< HTTP/2 301
< date: Mon, 08 Jun 2020 02:30:14 GMT
< content-type: text/html; charset=iso-8859-1
< set-cookie: __cfduid=dbf9fd63de401692314adea745bcd3b891591583414; expires=Wed, 08-Jul-20 02:30:14 GMT; path=/; domain=.waseda.jp; HttpOnly; SameSite=Lax
< location: https://www.waseda.jp/top/
< cf-cache-status: DYNAMIC
< cf-request-id: 03335caf7c0000951bb206f200000001
< expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
< set-cookie: __cfruid=deb9cd340d6fd9e2cfd301a48c3551df86788f9c-1591583414; path=/; domain=.waseda.jp; HttpOnly; Secure; SameSite=None
< server: cloudflare
< cf-ray: 59ff30926e6f951b-NRT
...
```

So you cannot find the answer by using `dig` command.

```bash
$ dig www.waseda.jp
...
www.waseda.jp.		300	IN	CNAME	www.waseda.jp.cdn.cloudflare.net.
www.waseda.jp.cdn.cloudflare.net. 300 IN A	104.16.38.132
www.waseda.jp.cdn.cloudflare.net. 300 IN A	104.16.39.132
www.waseda.jp.cdn.cloudflare.net. 300 IN A	104.16.36.132
www.waseda.jp.cdn.cloudflare.net. 300 IN A	104.16.37.132
www.waseda.jp.cdn.cloudflare.net. 300 IN A	104.16.35.132
...
```

## Hints

- [Shodan: Keeping Up with SSL](https://blog.shodan.io/ssl-update/)
- [Shodan: Duplicate SSL Serial Numbers](https://blog.shodan.io/ssl-serial-number-weirdness/)

- You can use `ssl.cert.serial` and `ssl.cert.subject.cn` filters.
  - ssl.cert.serial:serial number (integer) or DER encoded value
    - e.g.
      - `ssl.cert.serial:21020869104500376438182461249190639870` (www.examle.org)
      - `ssl.cert.serial:0fd078dd48f1a2bd4d0f2ba96b6038fe` (www.example.org)
  - ssl.cert.cn: common name
    - e.g.
      - `ssl.cert.subject.cn:www.example.org` (www.example.com)

---

- [Answers](./answer.md)
