FROM python:3.9-alpine
WORKDIR /DockerFolder
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install nltk
CMD ["python","python.py"] 