FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
	gcc \
	libmariadb-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]
