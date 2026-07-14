# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import Optional
from datetime import date

PROJECT_STATUS = ["Montagem","Garantia"]

@dataclass
class NonConformity():

    title: str
    problem_description: str
    creator_id:int
    creation_date:date
    project_id: str
    project_status: str    
    components: list = field(default_factory=list)
    nonconformity_id: Optional[int] = None

    def __post_init__(self):
        self._normalize()
        self._validate()
        
    def _normalize(self):
        self.title = self.title.strip()
        self.problem_description = self.problem_description.strip()
        self.project_id = self.project_id.strip()
        self.project_status = self.project_status.strip().title()

    def _validate(self):
        if not self.title:
            raise ValueError("Titulo da RNC nao pode ser vazio")
        if not self.problem_description:
            raise ValueError("Descricao do problema nao pode ser vazia")        
        if not self.project_id:
            raise ValueError("Projeto nao pode ser vazio")
        if not self.project_status:
            raise ValueError("Status do projeto nao pode ser vazio")
        if self.project_status not in PROJECT_STATUS:
            raise ValueError("Status invalido")

    