"""Configurações gerais do projeto."""
import os

DB_URL = os.getenv(
    "LGPD_DB_URL",
    "postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2",
)
PASTA_SAIDA = "saida"
ARQUIVO_LOG = "tempo_execucao.log"
