FROM maven:3.6.0-jdk-10-slim

RUN apt-get update && apt-get install -y python3 python3-pip git nano sudo

COPY . /app

WORKDIR /app/web-runner
RUN mvn clean install -DskipTests

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install -r gossip/requirements.txt

WORKDIR /app/web-runner
CMD (java -jar target/simulator.main-0.1.0.jar &) && cd .. && (python3 ./main.py &) && (python3 gossip/main.py)
