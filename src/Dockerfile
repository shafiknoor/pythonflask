FROM python:3.6.5-alpine
WORKDIR /code
ADD . /code
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
