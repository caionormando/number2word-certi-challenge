FROM python:3.7

WORKDIR /usr/src/docker-number2word

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","__main__.py"]