# Simple tornado web service

This is a simple web service with tornado.
 * return status handling
 * ws parameters
 * output

## Some help
 * [Offical doc](http://www.tornadoweb.org/en/stable/guide/structure.html)
 * [Some examples](http://www.drdobbs.com/open-source/building-restful-apis-with-tornado/240160382)
 * [Return status](https://solidgeargroup.com/best-practices-rest-api)

## How to run

```python server.py```

## With Docker

build the image:
```docker build -t tornado_img .```

run the container:
```docker run --rm -p 8888:8888 -ti tornado_img python server.py```
