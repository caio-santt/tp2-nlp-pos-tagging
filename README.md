# TP2 - POS Tagging com BERT

Trabalho Prático 2 da disciplina de Processamento de Linguagem Natural.  
**Aluno**: Caio Santana Trigueiro | **Matrícula**: 2022043310

## 📝 Descrição

Implementação e avaliação de um modelo de **POS Tagging** (Part-of-Speech Tagging) utilizando BERT. O objetivo é classificar a classe gramatical de palavras em textos e **analisar a precisão do modelo em cada uma das 48 classes gramaticais** do Penn Treebank.

## 📊 Dataset

- **Fonte:** [batterydata/pos_tagging](https://huggingface.co/datasets/batterydata/pos_tagging)
- **Penn Treebank format**
- **48 classes gramaticais** (POS tags)
- **Train:** 13,054 sentenças (321,815 tokens)
- **Test:** 1,451 sentenças (37,965 tokens)
- **Validation:** 10% do train (criado automaticamente)

## 🚀 Tecnologias

- Python 3.12+
- PyTorch 2.9+
- Transformers 4.57+ (Hugging Face)
- BERT (bert-base-uncased)
- Datasets (Hugging Face)
- Evaluate (seqeval)
- Scikit-learn, Pandas, Matplotlib, Seaborn
- Jupyter Notebook

## 📦 Como Usar

### Opção 1: Google Colab (Recomendado) ⭐

1. Acesse [Google Colab](https://colab.research.google.com/)
2. Faça upload do notebook `TP2_POS_Tagging_Colab.ipynb`
3. Execute célula por célula ou "Runtime > Run all"
4. Aguarde ~8-10 minutos (execução automática com GPU)

### Opção 2: Instalação Local

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

4. Inicie o Jupyter:
```bash
jupyter notebook
```

## 📓 Notebook

### ☁️ Recomendação: Use o Google Colab!

O notebook foi desenvolvido para execução no **Google Colab** (GPU gratuita):
- Upload do arquivo `.ipynb` no Colab
- Execução automática em ~8-10 minutos
- Todas as dependências instaladas automaticamente
- Sem necessidade de configuração local

**Link do Colab:** [Open in Colab](https://colab.research.google.com/)

### 📝 Conteúdo do Notebook

O notebook principal `TP2_POS_Tagging_Colab.ipynb` está **completo** e contém:

1. **Configuração Inicial** - Imports e setup
2. **Exploração dos Dados** - Análise do dataset e 48 classes
3. **Preprocessamento** - Tokenização BERT com alinhamento de labels
4. **Modelagem** - Fine-tuning do BERT (3 épocas)
5. **Avaliação** - Métricas no conjunto de teste
6. **Análise Detalhada por Classe** ⭐ (Requisito Principal)
   - Precision, Recall, F1 para cada uma das 48 classes
   - Top 10 e Bottom 10 classes
   - Gráfico de F1 por classe
   - Matriz de confusão (top 15)
   - Classification report completo
7. **Exemplos** - Predições em sentenças reais
8. **Conclusões** - Análise de pontos fortes, fracos e melhorias

## 🎯 Objetivos

✅ Implementar modelo de POS tagging usando BERT  
✅ Tokenização com alinhamento de subword tokens  
✅ Avaliar métricas globais (accuracy, F1, precision, recall)  
✅ **Analisar precisão por classe gramatical** (48 classes)  
✅ Identificar classes com melhor e pior desempenho  
✅ Visualizar resultados (gráficos + matriz de confusão)  
✅ Salvar modelo treinado e resultados em CSV  

## 📈 Resultados Esperados

O modelo deve alcançar:
- **Accuracy > 95%**
- **F1 Score médio > 95%**
- **Alta precisão** em classes frequentes: NN, IN, DT, NNP, JJ
- **Desafios** em classes raras: SYM, LS, UH (baixo support)

## ⏱️ Tempo de Execução

- **Google Colab (GPU T4)**: ~8-10 minutos ⚡
- **GPU local (CUDA)**: ~15-20 minutos
- **CPU local**: ~2-3 horas 🐢

## 📁 Arquivos Gerados

Após execução do notebook:
- `pos_tagging_results_by_class.csv` - Métricas detalhadas por classe
- `modelo_bert_pos_tagging/` - Modelo BERT treinado
- `results/` - Checkpoints de treinamento
- `logs/` - Logs do TensorBoard

## 📚 Referências

- Devlin, J., et al. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers)
- [Dataset batterydata/pos_tagging](https://huggingface.co/datasets/batterydata/pos_tagging)

## 👤 Autor

**Caio Santana Trigueiro**  
Matrícula: 2022043310  
Curso: Ciência da Computação  
Disciplina: Processamento de Linguagem Natural

## 📄 Licença

Este projeto é para fins acadêmicos.
