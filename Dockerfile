FROM python:3.7

RUN pip install --upgrade virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3 
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]