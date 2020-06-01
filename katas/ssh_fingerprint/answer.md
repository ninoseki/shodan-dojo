# Answer

Shodan records SSH publc keys and you can make a query against them.

![](https://i.imgur.com/3wb8hv7.png)

```python
from sshpubkeys import SSHKey

pub_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDS4ZCRAuR7Gr0SS2B3XR3IYLcwrCVTSu9nzEDIBHxkVYM+zwO4SBXxECJaOZMI14hgYGa1KMGMqoVAtd72Te+Uwmu4iwGNWW5mheAGUMsYJHhUzTpKxcHqhmXCJI9ngbrPO6KoBVSmYQ1QkYBMI/E8jYBPIy8cfMJIeX7/TL8irTrfA3RS04l84ngSCOFipLLsBq4fbDVc6qbMF6Y4hGcknpOY5PbqX/nG2PdNJ68acT9K1IwqXmi9ZukX1yvpH4a1J4EkwbMyrvrV+3f5RYyHOJr+HL9PhDUWu04zxg2RYl75mbLFOA+kZ92YxF8DRMh6k37GD+VvA56Q+33owZl1"
ssh = SSHKey(pub_key)
ssh.parse()
print(ssh.hash_md5())
# MD5:c9:91:4f:48:43:2f:83:66:cc:22:d3:57:b2:69:40:7a
```

The MD5 fingerprint of the SSH public key is `c9:91:4f:48:43:2f:83:66:cc:22:d3:57:b2:69:40:7a`.

You can use the fingerprint in the free-text search.

The answer is ["c9:91:4f:48:43:2f:83:66:cc:22:d3:57:b2:69:40:7a" port:22](https://www.shodan.io/search?query=%22c9%3A91%3A4f%3A48%3A43%3A2f%3A83%3A66%3Acc%3A22%3Ad3%3A57%3Ab2%3A69%3A40%3A7a%22+port%3A22+product%3A%22OpenSSH%22).

![](https://i.imgur.com/mXaQe2b.png)
