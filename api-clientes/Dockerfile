FROM openjdk:17-slim

WORKDIR /api-clientes

COPY target/api-clientes.jar .

EXPOSE 8080

CMD ["java", "-jar", "api-clientes.jar"]
