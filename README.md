# pontos-api
Api para comunicação com banco de dados firebird

## Ambiente

### Python
- 3.8.2
- flask
- flak_cors

### Libs
```sudo apt install libfbclient2```

### criar arquivo db_config.json
```{ ```
    ```"host": "",```
    ```"user": "",```
    ```"password": "",```
    ```"database": ""```
```}```

### Configuração e execução
```python -m venv .venv```
```source .venv/bin/activate```
```pip install -r requirements.txt```
```flask run```

