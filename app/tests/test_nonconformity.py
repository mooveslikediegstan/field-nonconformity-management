# -*- coding: utf-8 -*-
from datetime import date
from typing import Optional
import pytest
from backend.models.nonconformity import NonConformity

@pytest.fixture
def valid_nonconformity():
    return NonConformity(
        title="Acoplamento de baixa rotação divergente da especificação",
        problem_description="Acoplamento de baixa rotação divergente da especificação de Engenharia",
        creator_id=1,
        creation_date=date(2026, 7, 15),
        project_id="20250622",
        project_status="Montagem"
    )

def make_analyst(valid_nonconformity, **overrides):
    return NonConformity(**{**valid_nonconformity.__dict__, **overrides})

# --- criacao basica ---

def test_analyst_created_with_valid_fields(valid_nonconformity):
    assert valid_nonconformity.title == "Acoplamento de baixa rotação divergente da especificação"
    assert valid_nonconformity.problem_description == "Acoplamento de baixa rotação divergente da especificação de Engenharia"
    assert valid_nonconformity.creator_id==1
    assert valid_nonconformity.creation_date==date(2026, 7, 15)
    assert valid_nonconformity.project_id=="20250622"
    assert valid_nonconformity.project_status=="Montagem"

# --- campos obrigatórios

def test_empty_title_should_fail(valid_nonconformity):
    with pytest.raises(ValueError, match="Titulo da RNC nao pode ser vazio"):
        make_analyst(valid_nonconformity, title="")

def test_empty_title_should_fail(valid_nonconformity):
    with pytest.raises(ValueError, match="Descricao do problema nao pode ser vazia"):
        make_analyst(valid_nonconformity, problem_description="")

def test_empty_title_should_fail(valid_nonconformity):
    with pytest.raises(ValueError, match="Projeto nao pode ser vazio"):
        make_analyst(valid_nonconformity, project_id="")

def test_empty_title_should_fail(valid_nonconformity):
    with pytest.raises(ValueError, match="Status do projeto nao pode ser vazio"):
        make_analyst(valid_nonconformity, project_status="")

# --- status ---

def test_invalid_status_should_fail(valid_nonconformity):
    with pytest.raises(ValueError, match="Status invalido"):
        make_analyst(valid_nonconformity, status="Recebimento de Carga")

def test_all_valid_statuses_are_accepted(valid_analyst):
    for status in ["Montagem","Garantia"]:
        a = make_analyst(valid_analyst, status=status)
        assert a.status == status

