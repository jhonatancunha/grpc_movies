### Como gerar proto?

```bash
yarn build:proto
```

### Como usar cada função gRPC?

Veja o arquivo `Insomnia_2023-05-13.json`

### createMovie

Construa o objeto de `Request` da seguinte forma:

```ts
{
    movie: {
        // ... DADOS DO FILME A SER CRIADO
    },
}
```

### getMoviesById

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "id_aqui",
}
```

### updateMovie

Construa o objeto de `Request` da seguinte forma:

```ts
{
     movie: {
        // ... NOVOS DADOS DO FILME
    },
    data: "id_do_filme_a_ser_atualizado",
}
```

### deleteMovie

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "id_do_filme_a_ser_deletado",
}
```

### getMoviesByActor

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "nome_do_ator",
}
```

### getMoviesByGenre

Construa o objeto de `Request` da seguinte forma:

```ts
{
    data: "nome_do_genero",
}
```
