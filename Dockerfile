FROM alexellis2/phototimer:0.1

RUN apt-get update && \
    apt-get install -qy \
      enfuse \
      python-pip --no-install-recommends && \
    pip install picamera

COPY app.py .
COPY config.py .
COPY pathMaker.py .

CMD ["python", "app.py"]
