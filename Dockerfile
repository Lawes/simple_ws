FROM alpine:3.6

EXPOSE 8888

RUN apk update && \
	apk add --no-cache python2 py-tornado

COPY server.py .