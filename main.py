"""Ponto de entrada: executa as atividades 2 e 3 (com log de tempo)."""
from banco import engine, metadata
from decorator_tempo import logger
from exportacao import gerar_arquivo_todos, gerar_arquivos_por_ano


def main():
    # Cria a tabela caso não exista (ignora se não houver permissão)
    try:
        metadata.create_all(engine)
    except Exception as e:
        logger.warning("create_all ignorado: %s", e)

    gerar_arquivos_por_ano()
    gerar_arquivo_todos()


if __name__ == "__main__":
    main()
