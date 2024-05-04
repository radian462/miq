FROM python:3.11
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
ENV NAME World
CMD ["python", "./main.py"]
