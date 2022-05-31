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

depois disso, a API estará rodando em localhost:8000/search

# Limitações

índice de letras que também são números romanos não serão considerados como índice e serão considerados como números romanos.
Por exemplo, esta entrada lançará um erro:
```json
{
    "text":"CXXX"
}
```