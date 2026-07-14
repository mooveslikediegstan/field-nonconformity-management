# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional
from datetime import date


@dataclass
class Component:

    component_id: str
    description: str
    component_problem:str
    quantity:int = 1
    is_missing_part: bool
    component_key: Optional[int] = None

    def __post_init__(self):
        self._normalize()
        self._validate()
        
    def _normalize(self):
        self.component_id = self.component_id.strip()
        self.description = self.description.strip()
        self.component_problem = self.component_problem.strip()


    def _validate(self):
        if not self.component_id:
            raise ValueError("Codigo do componente nao pode ser vazio")
        if not self.description:
            raise ValueError("Descricao do componente nao pode ser vazio")        
        if not self.component_problem:
            raise ValueError("Problema do componente nao pode ser vazio")
        if self.quantity < 1:
            raise ValueError("Quantidade nao pode ser menor ou igual a zero")
        if not self.is_missing_part:
            raise ValueError("Flag de peça faltante nao pode ser vazio")


        
        
