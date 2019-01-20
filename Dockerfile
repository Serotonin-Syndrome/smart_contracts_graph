FROM maven:3.6.0-jdk-10-slim

RUN apt-get update && apt-get install -y python3 pip3 git nano sudo

COPY . /app
EXPOSE 8096
EXPOSE 8080

WORKDIR /app/web-runner
RUN mvn clean install -DskipTests

WORKDIR /app
RUN pip3 install -r requirements.txt

WORKDIR /app/web-runner
CMD java -jar target/simulator.main-0.1.0.jar
