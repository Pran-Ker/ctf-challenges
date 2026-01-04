FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLAG="csictf{h34d3rs_c4n_b3_sp00f3d}"

EXPOSE 5000

CMD ["python", "app.py"]
