FROM python:3.7-slim
WORKDIR /usr/src/app
COPY . .
ENV GOOGLE_APPLICATION_CREDENTIALS "fintech-totalpay-dev.json"
RUN echo "printenv grep | GOOGLE_APPLICATION_CREDENTIALS"
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD ["python","__main__.py"]