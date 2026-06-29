# Modelagem e Análise de Arranjos de Sensores

Trabalho Extra da disciplina **Processamento de Sinais I**.

## Integrantes

* Fabio Daniel dos Santos Lacerda
* 
* Luís Felipe Chaves de Oliveira
* 

**Professor:** Rafael S. Chaves
**Instituição:** Centro Federal de Educação Tecnológica Celso Suckow da Fonseca - CEFET/RJ
**Semestre:** 2026.1
---

# Descrição do Projeto

Este projeto tem como objetivo implementar e analisar técnicas de **processamento espacial de sinais** por meio de diferentes geometrias de arranjos de sensores, conforme proposto na disciplina de Processamento de Sinais I.

Foram implementadas rotinas para:

* Geração de arranjos de sensores:

  * Uniform Linear Array (ULA);
  * Uniform Circular Array (UCA);
  * Uniform Planar Array (UPA);
  * Uniform Cylindrical Array (UCYA);
* Cálculo do **Steering Vector**;
* Cálculo do **Array Factor**;
* Geração do **Beampattern**;
* Implementação de um **Delay-and-Sum Beamformer**;
* Simulações de transmissão direcional e análise da potência recebida.

Todos os gráficos apresentados no relatório são gerados automaticamente pelos notebooks do projeto.

---

# Instruções de Execução

O projeto foi desenvolvido em **Python**, utilizando o **Google Colaboratory (Google Colab)**.

### 1. Clone o repositório

```bash
git clone https://github.com/masterAristocats/Proc-Sin-Trabalho-Extra.git
cd Proc-Sin-Trabalho-Extra
```

### 2. Abra os notebooks

Abra os arquivos `.ipynb` diretamente no **Google Colab** ou em um ambiente Jupyter Notebook.

No Google Colab:

* Faça upload do projeto ou conecte o Colab ao GitHub;
* Abra o notebook correspondente;
* Execute todas as células em sequência.

### 3. Reprodução dos Resultados

Cada notebook realiza automaticamente os experimentos correspondentes e gera:

* Visualizações tridimensionais dos arranjos;
* Diagramas de radiação (*Beam Patterns*);
* Mapas de calor;
* Gráficos de potência recebida;
* Resultados dos experimentos de beamforming.

---

# Estrutura do Projeto

```text
Proc-Sin-Trabalho-Extra/
│
├── article/             # Artigo técnico
| |-- paper.pdf
| |-- paper.tex
│
├── src/                 # Funções auxiliares utilizadas nos notebooks
| |-- generate_ula.py
| |-- generate_uca.py
| |-- generate_upa.py
| |-- generate_ucya.py
| |-- steering_vector.py
| |-- beampattern.py
| |-- beamformer.py
│
├── figures/             # Figuras geradas automaticamente
│
├── data/                # Notebooks desenvolvidos no Google Colab
| |-- directional_transmission.ipynb
| |-- multiple_sources.ipynb
│
├── examples/                # Notebooks desenvolvidos no Google Colab
| |-- generate_ula.ipynb
| |-- generate_uca.ipynb
| |-- generate_upa.ipynb
| |-- generate_ucya.ipynb
| |-- steering_vector.ipynb
| |-- beampattern.ipynb
| |-- beamformer.ipynb
│
└── README.md
```

# Dependências

O projeto foi desenvolvido utilizando **Python 3**.

As principais bibliotecas utilizadas são:

* NumPy
* SciPy
* Matplotlib

Caso execute localmente, instale as dependências com:

```bash
pip install numpy scipy matplotlib
```

No **Google Colab**, essas bibliotecas já estão disponíveis por padrão, não sendo necessária instalação adicional.

---

# Resultados

Os notebooks reproduzem automaticamente todos os resultados apresentados no artigo técnico, incluindo:

* Geração das diferentes geometrias de arranjos;
* Visualização tridimensional dos sensores;
* Cálculo do Steering Vector;
* Geração dos Beam Patterns;
* Simulações de Beamforming;
* Experimentos de transmissão direcional;
* Análises da potência recebida e ganho espacial.

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina **Processamento de Sinais I**.
