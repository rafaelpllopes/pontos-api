# Pontos API
API para comunicação com banco de dados firebird

## Ambiente

### Python
- 3.8.2
- flask
- flak_cors

### Libs
```sudo apt install libfbclient2```

### Criar arquivo db_config.json
```{ ```
    ```"host": "",```
    ```"user": "",```
    ```"password": "",```
    ```"database": ""```
```}```

### Configuração e execução
1. ```python -m venv .venv```
2. ```source .venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```flask run```

### Habilitar https
1. ```sudo apt update```
2. ```sudo apt install software-properties-common```
3. ```sudo add-apt-repository universe```
4. ```sudo add-apt-repository ppa:certbot/certbot```
5. ```sudo apt update```
6. ```sudo apt install python-certbot-nginx```

#### Configurar nginx
```sudo nano /etc/nginx/sites-enabled/flaskapi``` editar ```server_name```, se necessario. 
1. ```sudo certbot --nginx```, para configurar e-mail e demais opções, configurar para redirecionar tudo para https;
2. ```sudo nginx -t```, para testar as configurações;
3. ```sudo ufw allow https```, para permitir acesso via porta https;
4. ```sudo systemctl restart nginx```, para reiniciar o nginx
5. ```sudo certbot renew --dry-run```, para renovar o certificado
6. configuar crontab ```30 4 1 * * sudo certbot renew --quiet```

