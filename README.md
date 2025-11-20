# TP2 - POS Tagging com BERT

Trabalho Prático 2 da disciplina de Processamento de Linguagem Natural.

## 📝 Descrição

Implementação e avaliação de um modelo de **POS Tagging** (Part-of-Speech Tagging) utilizando Transformers pré-treinados (BERT). O objetivo é classificar a classe gramatical de palavras em textos e analisar a performance do modelo em diferentes categorias gramaticais.

## 📊 Dataset

- **Fonte:** [batterydata/pos_tagging](https://huggingface.co/datasets/batterydata/pos_tagging)
- Disponível no Hugging Face Datasets

## 🚀 Tecnologias

- Python 3.12+
- PyTorch
- Transformers (Hugging Face)
- BERT (Bidirectional Encoder Representations from Transformers)
- Jupyter Notebook

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/caio-santt/tp2-nlp-pos-tagging.git
cd tp2-nlp-pos-tagging
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv tp2-env
source tp2-env/bin/activate  # Linux/Mac
# ou
tp2-env\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📓 Notebook

O notebook principal está em `TP2_POS_Tagging.ipynb` e contém:

1. **Configuração Inicial** - Imports e setup
2. **Exploração dos Dados** - Análise do dataset
3. **Preprocessamento** - Preparação dos dados
4. **Modelagem** - Fine-tuning do BERT
5. **Avaliação** - Métricas de performance
6. **Análise** - Discussão dos resultados por classe gramatical

## 🎯 Objetivos

- Implementar modelo de POS tagging usando BERT
- Avaliar precisão do modelo
- Analisar performance por classe gramatical
- Identificar classes com melhor e pior desempenho

## 📈 Resultados

[A ser completado após análise]

## 📚 Referências

- Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Dataset batterydata/pos_tagging](https://huggingface.co/datasets/batterydata/pos_tagging)

## 👤 Autor

Caio Sant

## 📄 Licença

Este projeto é para fins acadêmicos.
