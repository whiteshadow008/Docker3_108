FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
