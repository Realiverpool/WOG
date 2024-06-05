FROM python:alpine
WORKDIR /app
RUN pip install --no-cache-dir Flask
EXPOSE 5000
COPY main_score.py /app/
COPY templates/ /app/templates/
COPY utils.py /app/
COPY Scores/ /app/Scores/
CMD python main_score.py

