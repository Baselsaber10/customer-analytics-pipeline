FROM python:3.11-slim

WORKDIR /app/pipeline/

COPY . /app/pipeline/

RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

CMD ["bash"]