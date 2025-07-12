# 🛡️ Stride - MVP de Modelagem de Ameaças com IA

Este projeto é um MVP (Produto Mínimo Viável) que utiliza Inteligência Artificial para realizar **análise automática de segurança em diagramas de arquitetura de software**, com base na metodologia **STRIDE**. O sistema detecta componentes nos diagramas e gera um relatório com ameaças, vulnerabilidades e contramedidas associadas.

---

## 🚀 Objetivo

Automatizar a identificação de ameaças em diagramas de arquitetura através de uma interface web intuitiva que permite o upload de imagens, extração dos componentes e geração de relatórios de segurança com base na metodologia STRIDE.

---

## 🧰 Tecnologias Utilizadas

- **Streamlit**: Interface web para upload e exibição dos resultados.
- **YOLOv8 (Ultralytics)**: Detecção de componentes em diagramas via visão computacional.
- **Python**: Backend e lógica principal do projeto.
- **JSON**: Formato de saída dos relatórios.

---

## 📁 Estrutura do Projeto

```
├── dataset/
│   ├── images/                   # Imagens dos diagramas
│   └── labels/                   # Anotações YOLO para cada imagem
│   ├── classes.txt
│   ├── labels.cache
│   └── notes.json
│
├── runs/
│   └── detect/modelo-arquitetura/  # Resultados da detecção
│
├── src/
│   ├── app.py                    # Interface principal com Streamlit
│   ├── data.yaml                 # Configuração de classes do modelo YOLO
│   ├── utilities.py              # Funções de detecção e geração de relatório STRIDE
│   └── yolov8n.pt                # Pesos do modelo YOLO treinado
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt             # Dependências do projeto
```

---

## 🔄 Fluxo do MVP

1. O usuário faz upload de um diagrama de arquitetura (imagem) pela interface web.
2. A imagem é processada pelo modelo YOLOv8 para identificar os componentes presentes.
3. O sistema aplica a metodologia STRIDE para gerar um relatório de segurança com base nos componentes detectados.
4. O relatório com as ameaças e possíveis contramedidas é exibido na interface e pode ser baixado em formato JSON.

---

## 🐍 Como Rodar o Projeto

> Requisitos:
> - Python 3.8+
> - `pip` instalado
> - (opcional) Ambiente virtual

### 1. Clone o repositório

```bash
git clone https://github.com/MateusJensen/Stride.git
cd Stride
```

### 2. (Opcional) Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o aplicativo Streamlit

```bash
streamlit run src/app.py
```

---

## 📄 Exemplo de Uso

1. Acesse a interface web que será aberta automaticamente no navegador.
2. Faça upload de uma imagem `.png`, `.jpg` ou `.jpeg` de um diagrama de arquitetura.
3. Visualize os componentes detectados na imagem.
4. Consulte o relatório STRIDE com ameaças e vulnerabilidades.
5. Baixe o relatório completo em formato JSON.

---

## 🔐 Sobre a Metodologia STRIDE

A metodologia STRIDE identifica seis categorias de ameaças de segurança em sistemas de software:

- **S**poofing (Falsificação)
- **T**ampering (Violação de integridade)
- **R**epudiation (Repúdio)
- **I**nformation Disclosure (Divulgação de informação)
- **D**enial of Service (Negação de serviço)
- **E**levation of Privilege (Elevação de privilégio)

O sistema aplica automaticamente essas categorias aos componentes identificados com base em regras específicas e banco de dados de vulnerabilidades.

---

## 🧠 Funcionalidades do MVP

- Upload de diagramas de arquitetura.
- Detecção automática de componentes.
- Análise de ameaças baseada em STRIDE.
- Sugestão de vulnerabilidades e contramedidas.
- Relatório exportável em JSON.

---

## 📜 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
