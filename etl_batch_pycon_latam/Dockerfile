FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN bash -c 'mkdir -pv /etl_batch_pycon_latam/tmp;

WORKDIR /etl_batch_pycon_latam

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "-u", "main.py"]