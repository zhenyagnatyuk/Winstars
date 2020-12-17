FROM python:3.8
WORKDIR /model
VOLUME /input 
COPY model.py .
RUN pip install pandas
ENTRYPOINT ["python", "model.py"]
CMD  ["data.csv"]