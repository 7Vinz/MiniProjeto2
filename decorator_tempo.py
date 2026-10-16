"""Atividade 4 - Decorator que mede o tempo de execução e grava em log."""
import logging
import time
from functools import wraps

from config import ARQUIVO_LOG

logger = logging.getLogger("lgpd")
logger.setLevel(logging.INFO)

if not logger.handlers:
    _formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    _arquivo = logging.FileHandler(ARQUIVO_LOG, encoding="utf-8")
    _arquivo.setFormatter(_formato)
    logger.addHandler(_arquivo)

    _console = logging.StreamHandler()
    _console.setFormatter(_formato)
    logger.addHandler(_console)


def medir_tempo(func):
    """Mede o tempo de execução da função e registra no log."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duracao = time.perf_counter() - inicio
            logger.info("Função '%s' executada em %.6f segundos.",
                        func.__name__, duracao)
    return wrapper
