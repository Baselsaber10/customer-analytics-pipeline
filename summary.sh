#!/bin/bash

mkdir -p results

docker cp customer_analytics_container:/app/pipeline/data_raw.csv results/
docker cp customer_analytics_container:/app/pipeline/data_preprocessed.csv results/
docker cp customer_analytics_container:/app/pipeline/insight1.txt results/
docker cp customer_analytics_container:/app/pipeline/insight2.txt results/
docker cp customer_analytics_container:/app/pipeline/insight3.txt results/
docker cp customer_analytics_container:/app/pipeline/summary_plot.png results/
docker cp customer_analytics_container:/app/pipeline/clusters.txt results/

docker stop customer_analytics_container
docker rm customer_analytics_container