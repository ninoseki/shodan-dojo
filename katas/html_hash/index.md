# Hash of the website HTML

Create a query to find hosts which returns the same HTTP response body (HTML) as `http://example.com`.

```bash
$ curl example.com
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```

## Hints

- Shodan uses MuarmurHash3 as a hashing function.
- You can use `http.html_hash` filter.
  - http.html_hash: MuarmurHash3 hash value
  - e.g.
    - `http.html_hash:809425345` ("sinkehole\n")
- MuarmurHash3 libraries:
  - Go https://github.com/DataDog/mmh3
  - JS: https://www.npmjs.com/package/murmurhash3js
  - Python: https://pypi.org/project/mmh3/
  - Ruby: https://rubygems.org/gems/mmh3/
  - etc.

---

- [Answer](./answer.md)
