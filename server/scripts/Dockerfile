FROM python:alpine
RUN apk add --no-cache socat
WORKDIR /app
COPY . .
CMD ["socat", "TCP-LISTEN:2029,reuseaddr,fork", "EXEC:'python ./main.py'"]