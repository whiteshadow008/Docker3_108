FROM python:3.8
ENV PYTHONUNBUFFERED 1
ADD . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python","-m" ,"flask","app.py"]
