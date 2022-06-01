Este exercicio foi feito usando [fastAPI](https://fastapi.tiangolo.com), o código da solução está em [app/main.py](./app/main.py) e seus testes estão em [app/test_main.py](./app/test_main.py) usando testes paremetrizados com [pytest](https://docs.pytest.org/en/7.1.x/)
# Dependencias

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

# Começando

Este projeto usa o docker para construir as dependências e isolá-las em um container, então docker e docker-compose presisarão estar instalados.

Na primeira execução deste projeto execute o comando de build:
```
docker-compose build
```

A seguir, você pode executar o projeto executando:
```
docker-compose up
```

depois disso, a API estará rodando em localhost:8000/search um endpoint do tipo POST

você pode conhecer melhor os endpoints em
http://localhost:8000/docs

# Limitações

índice de letras que também são números romanos não serão considerados como índice e serão considerados como números romanos.
Por exemplo, esta entrada lançará um erro:
```json
{
    "text":"CXXX"
}
```