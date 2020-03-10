FROM python:3.7-slim

RUN apt-get -y update

RUN pip3 install sklearn
RUN pip3 install yfinance
RUN pip3 install matplotlib  

RUN mkdir model
WORKDIR /model

RUN chmod 777 /model
COPY simulate_close_price.py /model

RUN cd /model

CMD python3 simulate_close_price.py
