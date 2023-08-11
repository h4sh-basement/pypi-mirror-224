# httpbin(1): HTTP Request & Response Service

This is a fork of the original httpbin project, which is located at https://github.com/postmanlabs/httpbin

Why fork?  we were unable to get ahold of the folks at postmanlabs to maintain the original project, and httpbin is used for other packages within the python ecosystem, such as [pytest-httpbin](https://pypi.org/project/pytest-httpbin/) which is in turn used by packages such as [requests](https://github.com/psf/requests/blob/main/requirements-dev.txt#L4) so we have forked this package.  That means that httpbin.org is not actually backed by this repo, but the [httpbin package](https://pypi.org/project/httpbin/) is.  Confusing right?  Know anyone at postmanlabs?  [get in touch](mailto:me@kevinmccarthy.org).

httpbin is a [Kenneth Reitz](http://kennethreitz.org/bitcoin) Project.
![ice cream](http://farm1.staticflickr.com/572/32514669683_4daf2ab7bc_k_d.jpg)

Run locally:
```sh
docker pull kennethreitz/httpbin
docker run -p 80:80 kennethreitz/httpbin
```

Some enviroments do not allow to bind to a privileged port. To run it on a
different port instead of port 80, set the environment variables as follows:

```sh
docker run -e HTTPIN_PORT=8000 -p 8000:8000 kennethreitz/httpbin
```

## Changelog
* 0.10.0:
  - Override docker image port with HTTPBIN_PORT
  - A number of fixes for code rot, thanks @mgorny and @tjni
* 0.9.2: ??? (never published as a package; seems to be internal to postman)
* 0.7.0: ???
* 0.6.2: ???
* 0.6.0: ???
* 0.5.0
  - Allow /redirect-to to work with multiple methods
  - Allow MD5 or SHA-256 to be chosen as algorithms for HTTP Digest Auth
  - Set a 10MB limit on /drip
* 0.4.1: Added floating-point support for /delay endpoint
* 0.4.0: New /image/svg endpoint, add deploy to heroku button, add 406 response to /image, and don’t always emit the transfer-encoding header for stream endpoint.
* 0.3.0 A number of new features, including a /range endpoint, lots of bugfixes, and a /encoding/utf8 endpoint
* 0.2.0: Added an XML endpoint.  Also fixes several bugs with unicode, CORS headers, digest auth, and more.
* 0.1.2: Fix a couple Python3 bugs with the random byte endpoints, fix a bug when uploading files without a Content-Type header set.
* 0.1.1: Added templates as data in setup.py
* 0.1.0: Added python3 support and (re)publish on PyPI

## Officially Deployed (but out of date) at:

- http://httpbin.org
- https://httpbin.org
- https://hub.docker.com/r/kennethreitz/httpbin/


## SEE ALSO

- http://requestb.in
- http://python-requests.org
- https://grpcb.in/

