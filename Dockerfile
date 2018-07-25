FROM python:3
COPY app.py /
COPY req.txt /
COPY utils.py /
RUN pip install -r req.txt
RUN pip install --upgrade pip
CMD python app.py
