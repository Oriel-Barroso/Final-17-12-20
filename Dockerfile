FROM python:3
RUN git clone https://github.com/Oriel-Barroso/Final-17-12-20.git
RUN pip install pip
RUN pip install parameterized
WORKDIR /Final-17-12-20
CMD ["python3","-m","unittest"]