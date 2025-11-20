"""
Script para analisar distribuição de POS tags no dataset
"""
from datasets import load_dataset
from collections import Counter
import pandas as pd

print("Carregando dataset...")
dataset = load_dataset("batterydata/pos_tagging")

# Coletar todas as tags
all_tags_train = []
all_tags_test = []

print("\nColetando tags do conjunto de treino...")
for exemplo in dataset['train']:
    all_tags_train.extend(exemplo['labels'])

print("Coletando tags do conjunto de teste...")
for exemplo in dataset['test']:
    all_tags_test.extend(exemplo['labels'])

# Contar ocorrências
counter_train = Counter(all_tags_train)
counter_test = Counter(all_tags_test)

print(f"\n=== ESTATÍSTICAS GERAIS ===")
print(f"Total de tokens no treino: {len(all_tags_train):,}")
print(f"Total de tokens no teste: {len(all_tags_test):,}")
print(f"Classes únicas no treino: {len(counter_train)}")
print(f"Classes únicas no teste: {len(counter_test)}")

# Todas as classes únicas
all_unique_tags = sorted(set(all_tags_train + all_tags_test))
print(f"\nTotal de classes POS: {len(all_unique_tags)}")
print(f"\nClasses POS: {all_unique_tags}")

# Criar DataFrame com distribuição
print("\n=== DISTRIBUIÇÃO DE CLASSES (TREINO) ===")
df_train = pd.DataFrame(counter_train.most_common(), columns=['POS Tag', 'Count'])
df_train['Percentage'] = (df_train['Count'] / df_train['Count'].sum() * 100).round(2)
print(df_train.to_string(index=False))

print("\n=== TOP 10 CLASSES MAIS FREQUENTES ===")
print(df_train.head(10).to_string(index=False))

print("\n=== TOP 10 CLASSES MENOS FREQUENTES ===")
print(df_train.tail(10).to_string(index=False))

# Salvar para análise posterior
df_train.to_csv('pos_tags_distribution_train.csv', index=False)
print("\n✓ Distribuição salva em 'pos_tags_distribution_train.csv'")
