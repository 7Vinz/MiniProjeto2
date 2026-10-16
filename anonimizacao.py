"""Atividade 1 - Funções de anonimização de dados pessoais."""
import re

CABECALHO = ["id", "nome", "cpf", "email", "telefone",
             "data_nascimento", "created_on", "updated_on"]


def anonimizar_nome(nome):
    """'Olivia Araújo' -> 'O***** Araújo' (mascara só o primeiro nome)."""
    partes = nome.split(" ")
    primeiro = partes[0]
    if primeiro:
        partes[0] = primeiro[0] + "*" * (len(primeiro) - 1)
    return " ".join(partes)


def anonimizar_cpf(cpf):
    """'237.615.809-59' -> '237.***.***-**'."""
    return cpf[:4] + re.sub(r"\d", "*", cpf[4:])


def anonimizar_email(email):
    """'nuneserick@example.com' -> 'n*********@example.com'."""
    usuario, arroba, dominio = email.partition("@")
    if not usuario:
        return email
    return usuario[0] + "*" * (len(usuario) - 1) + arroba + dominio


def anonimizar_telefone(telefone):
    """'+55 (011) 9483-6810' -> '6810'."""
    return telefone[-4:]


def LGPD(row):
    """Recebe uma linha do banco e devolve a tupla anonimizada."""
    id_, nome, cpf, email, telefone, nascimento, created, updated = tuple(row)
    return (
        id_,
        anonimizar_nome(nome),
        anonimizar_cpf(cpf),
        anonimizar_email(email),
        anonimizar_telefone(telefone),
        nascimento,
        created,
        updated,
    )
