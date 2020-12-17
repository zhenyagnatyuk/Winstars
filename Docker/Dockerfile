FROM python:3.8
WORKDIR /model
COPY model.py .
RUN pip install pandas
ENTRYPOINT ["python", "model.py"]
CMD  ["data.csv"]
