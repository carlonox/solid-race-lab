# SOLID Race Lab

Taller práctico de los principios SOLID — Ingeniería de Software II,
Universidad Nacional de Colombia.

En vez de discutir los principios SOLID solo en teoría, aquí los aplicas
completando código real de una carrera de vehículos que se anima en la
consola. Cada ejercicio corresponde a un principio SOLID; cuando lo
completas correctamente, la carrera de ese ejercicio corre sin errores y
puedes **verla** moverse en tu terminal.

## Instalación

Requiere Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Estructura

```
engine/            Motor de animación en consola (completo, no lo modifiques)
  track.py

exercises/          Los 5 ejercicios — aquí es donde trabajas
  ex1_srp.py         Single Responsibility Principle
  ex2_ocp.py          Open/Closed Principle
  ex3_lsp.py           Liskov Substitution Principle
  ex4_isp.py            Interface Segregation Principle
  ex5_dip.py             Dependency Inversion Principle

tests/              Pruebas automáticas que validan cada ejercicio
```

## Cómo trabajar cada ejercicio

Cada archivo en `exercises/` tiene, en su docstring inicial, el problema
a resolver y una lista de tareas puntuales (`TODO(SRP)`, `TODO(OCP)`,
etc. marcan exactamente dónde completar código).

1. Lee el docstring del ejercicio (p. ej. `exercises/ex1_srp.py`).
2. Completa los `TODO`.
3. Corre la demo visual para verla en la consola:

   ```bash
   python -m exercises.ex1_srp
   python -m exercises.ex2_ocp
   python -m exercises.ex3_lsp
   python -m exercises.ex4_isp
   python -m exercises.ex5_dip
   ```

4. Corre las pruebas de ese ejercicio para confirmar que quedó bien:

   ```bash
   pytest tests/test_ex1_srp.py -v
   ```

   O todas a la vez:

   ```bash
   pytest -v
   ```

Un ejercicio está resuelto cuando sus pruebas pasan en verde **y** la
demo corre sin errores (sin excepciones, sin comportamiento raro).

## Los 5 ejercicios

| # | Principio | Qué debes hacer |
|---|-----------|------------------|
| 1 | SRP — Single Responsibility | Separar la lógica de movimiento (`Car`) del registro de resultados (`RaceLogger`) |
| 2 | OCP — Open/Closed | Agregar `Motorcycle` y `Bicycle` **sin** tocar `Vehicle`, `Car`, `Truck` ni `Track` |
| 3 | LSP — Liskov Substitution | Rediseñar `UnreliableCar` para que nunca rompa el contrato de `Vehicle` (nunca retrocede, nunca lanza excepción) |
| 4 | ISP — Interface Segregation | Partir una interfaz gorda (`VehicleActions`) en interfaces pequeñas y agregar `Drone` |
| 5 | DIP — Dependency Inversion | Hacer que `Race` reciba sus vehículos desde afuera en vez de construirlos él mismo |

## Material de apoyo

En `docs/` encuentras:

- **Taller-SOLID-Enunciado.pdf** — la guía del taller para usar en clase.
- **Material-Estudio-SOLID.pdf** — teoría de cada principio con ejemplos
  tomados de este mismo proyecto, para repasar antes o después del taller.

## Para el profesor

Este repositorio tiene dos ramas:

- `main` — la versión que reciben los estudiantes (con los `TODO`).
- `solution` — la solución de referencia completa, usada para validar
  que las pruebas realmente miden lo correcto. **No la compartas con los
  estudiantes** (o bórrala/oculta antes de repartir el repositorio).

```bash
git checkout solution   # ver / correr la solución completa
git checkout main       # volver a la versión de los estudiantes
```
