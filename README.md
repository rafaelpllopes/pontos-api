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

