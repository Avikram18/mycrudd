FROM python:latest

ADD main.py .

RUN pip install flask

CMD ["python","./main.py"]