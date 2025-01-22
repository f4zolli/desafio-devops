# DESAFIO-DEVOPS
Este projeto demonstra um ambiente básico para deploy automatizado de uma aplicação web simples, utilizando ferramentas essenciais de DevOps.

## Requisitos
- Docker instalado
- Docker Compose instalado

## Instruções de Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/f4zolli/desafio-devops.git

2. Entre no diretório do projeto:
   ```bash
   cd desafio-devops

3. Execute o script de deploy:
   ```bash
   ./deploy.sh

4. Acesse a aplicação em  [http://localhost](http://localhost)

## Observação
A aplicação por padrão utiliza um servidor web (nginx), caso opte por não utilizar o nginx, realize o clone da branch without_nginx:
   ```bash
   git clone --branch without_nginx https://github.com/f4zolli/desafio-devops.git
   ```
E caso opte por essa opção, a aplicação ficará disponível em [http://localhost:8080](http://localhost:8080)

## Tecnologias
**FLASK**: O framework Flask foi utilizado devido à sua simplicidade, flexibilidade e facilidade de configuração, visto que o objetivo era uma aplicação web simples.<br>
**NGINX**: Já a utilização do Nginx, foi atuar como proxy reverso, abordagem que é comum em aplicações dinâmicas, onde o mesmo funciona como intermediário entre o cliente (navegador) e o backend. Embora funcional, ainda se faz importante a utilização de servidores WSGI (Web Server Gateway Interface) em ambientes de produção, como o Gunicorn, garantindo melhor performance, escalabilidade e segurança.<br>
**Docker**: A conteinerização tanto do Flask, quanto do Nginx proporciona um ambiente isolado e consistente. Garantindo que o deploy seja automatizado e previsível em qualquer ambiente.<br>

Essas decisões foram tomadas para criar uma solução prática e funcional, de acordo com os requisitos do desafio, mas com espaço para evoluir em um cenário de produção real.
