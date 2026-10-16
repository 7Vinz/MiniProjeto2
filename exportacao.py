"""Atividades 2 e 3 - Geração dos arquivos CSV."""
import csv
import os
from collections import defaultdict

from sqlalchemy import select

from anonimizacao import CABECALHO, LGPD
from banco import engine as engine_padrao, usuarios
from config import PASTA_SAIDA
from decorator_tempo import logger, medir_tempo


def _abrir_csv(caminho):
    # utf-8-sig para o Excel abrir os acentos corretamente
    return open(caminho, "w", newline="", encoding="utf-8-sig")


@medir_tempo
def gerar_arquivos_por_ano(pasta=PASTA_SAIDA, engine=engine_padrao):
    """Atividade 2: um CSV (anonimizado) para cada ano de nascimento."""
    os.makedirs(pasta, exist_ok=True)
    por_ano = defaultdict(list)

    with engine.connect() as conn:
        for row in conn.execute(select(usuarios).order_by(usuarios.c.id)):
            anonimizado = LGPD(row)
            por_ano[anonimizado[5].year].append(anonimizado)

    for ano, registros in sorted(por_ano.items()):
        with _abrir_csv(os.path.join(pasta, f"{ano}.csv")) as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(CABECALHO)
            writer.writerows(registros)

    total = sum(len(r) for r in por_ano.values())
    logger.info("%d registros gravados em %d arquivos (um por ano).",
                total, len(por_ano))


@medir_tempo
def gerar_arquivo_todos(pasta=PASTA_SAIDA, engine=engine_padrao):
    """Atividade 3: todos.csv com nome e CPF, sem anonimização."""
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "todos.csv")
    total = 0

    with engine.connect() as conn, _abrir_csv(caminho) as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["nome", "cpf"])
        consulta = select(usuarios.c.nome, usuarios.c.cpf).order_by(usuarios.c.id)
        for nome, cpf in conn.execute(consulta):
            writer.writerow([nome, cpf])
            total += 1

    logger.info("%d registros gravados em '%s'.", total, caminho)
