FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLAG="csictf{c00k13s_4r3_n0t_s3cur3}"

EXPOSE 5000

CMD ["python", "app.py"]
