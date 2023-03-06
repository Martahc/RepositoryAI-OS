FROM python:3.9

WORKDIR /app

COPY IAOS.py .


RUN pip install requests
RUN pip install wordcloud
RUN pip install grobid_client_python

ENTRYPOINT ["python", "IAOS.py"]

CMD ["--ruta", "/default/path/to/pdfs"]