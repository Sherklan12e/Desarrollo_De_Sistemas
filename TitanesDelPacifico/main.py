from typing import List

class Categoria:
    def __init__(self, nivel: int, descripcion: str):
        self.nivel = nivel
        self.descripcion = descripcion

class Habilidad:
    def __init__(self, nombre: str, danio: int):
        self.nombre = nombre
        self.danio = danio

class Kaiju:
    def __init__(
        self,
        nombre: str,
        peso: float,
        dureza: int,
        energia: int,
        vida: int,
        tamano: float,
        inmune_al_fuego: bool,
        puede_volar: bool,
        categoria: Categoria,
        habilidades: List[Habilidad]
    ):
        self.nombre = nombre
        self.peso = peso
        self.dureza = dureza
        self.energia = energia
        self.vida = vida
        self.tamano = tamano
        self.inmune_al_fuego = inmune_al_fuego
        self.puede_volar = puede_volar
        self.categoria = categoria
        self.habilidades = habilidades

    def calcular_poder_pelea(self) -> float:
        suma_danio = sum(habilidad.danio for habilidad in self.habilidades)
        return self.energia * suma_danio * self.categoria.nivel
