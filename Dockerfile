FROM python:3
COPY app.py /src
COPY req.txt /src
COPY utils.py /src
RUN pip install -r req.txt
CMD python /src/app.py
