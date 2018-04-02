FROM python:3.6.5-alpine3.6
MAINTAINER brettbushnell95@gmail.com

ADD gos gos
RUN pip install -r gos/requirements.txt
RUN cd ..

EXPOSE 5000
CMD python3 -m gos.main

