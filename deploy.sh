#!/bin/bash

echo "Inicializando o ambiente..."

# Atualizando pacotes
sudo apt update
sudo apt install docker.io docker-compose -y

echo "Construindo e subindo o container..."
sudo docker-compose up --build -d

echo "Aplicação disponível em: http://localhost:8080"
