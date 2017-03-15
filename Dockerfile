FROM alexellis2/phototimer:0.1
RUN apt-get update && apt-get install -qy enfuse --no-install-recommends

CMD ["python", "app.py"]
