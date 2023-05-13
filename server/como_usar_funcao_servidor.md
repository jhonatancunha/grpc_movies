Veja o arquivo `Insomnia_2023-05-13.json`

### CREATE

Construa o objeto de `Request` da seguinte forma:

```ts
{
    movie: {
        // ... DADOS DO FILME A SER CRIADO
    },
}
```

### FIND BY ID

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "id_aqui",
}
```

### UPDATE

Construa o objeto de `Request` da seguinte forma:

```ts
{
     movie: {
        // ... NOVOS DADOS DO FILME
    },
    data: "id_do_filme_a_ser_atualizado",
}
```

### DELETE

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "id_do_filme_a_ser_deletado",
}
```

### FIND BY ACTOR

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "nome_do_ator",
}
```

### FIND BY CATEGORY

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "nome_da_categoria",
}
```
