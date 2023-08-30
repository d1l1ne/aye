FROM python:3

EXPOSE 5000

COPY . ./aye

RUN pip install --upgrade pip
RUN pip install flask_restful openai

CMD ["python", "./aye/main.py"]