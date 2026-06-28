# Rocketseat Python — Desafio 4: Calculadora

API REST em Flask que expõe quatro calculadoras com regras de negócio distintas. O projeto faz parte do **Módulo 6** do curso de Python da Rocketseat e aplica conceitos de arquitetura limpa, injeção de dependência e tratamento centralizado de erros.

## Funcionalidades

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/calculator/1` | `POST` | Recebe um número e aplica fórmulas matemáticas customizadas |
| `/calculator/2` | `POST` | Calcula o inverso do desvio padrão de uma lista de números |
| `/calculator/3` | `POST` | Calcula a variância de uma lista, com validação de regra de negócio |
| `/calculator/4` | `POST` | Calcula a média aritmética de uma lista de números |

## Tecnologias

- **Python 3**
- **Flask** — servidor HTTP e rotas
- **NumPy** — operações estatísticas (média, variância, desvio padrão)
- **pytest** — testes unitários

## Estrutura do projeto

```
modulo_6/
├── run.py                          # Ponto de entrada da aplicação
├── src/
│   ├── calculators/                # Regras de negócio de cada calculadora
│   ├── drivers/                    # Implementações de drivers (ex: NumPy)
│   │   └── interfaces/             # Contratos dos drivers
│   ├── errors/                     # Exceções HTTP e controller de erros
│   └── main/
│       ├── factories/              # Factories para injeção de dependência
│       ├── routes/                 # Blueprints Flask com as rotas
│       └── server/                 # Configuração do app Flask
```

## Como executar

### 1. Criar e ativar um ambiente virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 2. Instalar dependências

```bash
pip install flask numpy pytest
```

### 3. Subir o servidor

```bash
python run.py
```

A API ficará disponível em `http://localhost:3000`.

## Exemplos de requisição

### Calculadora 1

```bash
curl -X POST http://localhost:3000/calculator/1 \
  -H "Content-Type: application/json" \
  -d '{"number": 15}'
```

**Resposta (200):**

```json
{
  "data": {
    "calculator": 1,
    "result": 42.35
  }
}
```

### Calculadora 2

```bash
curl -X POST http://localhost:3000/calculator/2 \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4, 5]}'
```

### Calculadora 3

```bash
curl -X POST http://localhost:3000/calculator/3 \
  -H "Content-Type: application/json" \
  -d '{"numbers": [2, 3, 4]}'
```

Retorna a variância quando ela é maior ou igual à multiplicação dos números. Caso contrário, retorna erro `400`.

### Calculadora 4

```bash
curl -X POST http://localhost:3000/calculator/4 \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4, 5]}'
```

**Resposta (200):**

```json
{
  "data": {
    "calculator": 4,
    "result": 3.0
  }
}
```

## Tratamento de erros

Erros são padronizados pelo `error_controller` e retornados no formato:

```json
{
  "errors": [
    {
      "title": "UnprocessableEntity",
      "detail": "Body mal formatado!"
    }
  ]
}
```

| Status | Situação |
|--------|----------|
| `400` | Regra de negócio violada (ex: variância menor que multiplicação na calculadora 3) |
| `422` | Body da requisição inválido ou campos ausentes |
| `500` | Erro interno não tratado |

## Testes

Execute os testes com pytest a partir da raiz do projeto:

```bash
pytest
```

Ou um arquivo específico:

```bash
pytest src/calculators/calculator_4_test.py
```

## Arquitetura

O projeto segue uma separação em camadas:

- **Routes** — recebem requisições HTTP e delegam para as factories
- **Factories** — montam as instâncias das calculadoras com suas dependências
- **Calculators** — contêm a lógica de negócio e validação de entrada
- **Drivers** — abstraem bibliotecas externas (NumPy) via interface (`DriverHandlerInterface`)

Essa estrutura facilita testes com mocks e a troca de implementações sem alterar a regra de negócio.

## Autor

**Dian Cabral** — [dian.cabral@gmail.com](mailto:dian.cabral@gmail.com)
