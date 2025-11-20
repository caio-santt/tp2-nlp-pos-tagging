"""
Script para explorar o dataset batterydata/pos_tagging
"""
from datasets import load_dataset

print("Carregando dataset batterydata/pos_tagging...")
dataset = load_dataset("batterydata/pos_tagging")

print("\n=== ESTRUTURA DO DATASET ===")
print(dataset)

print("\n=== EXEMPLO DO TREINO ===")
print("Primeiro exemplo:")
exemplo = dataset['train'][0]
for key, value in exemplo.items():
    print(f"  {key}: {value}")

print("\n=== FEATURES ===")
print(dataset['train'].features)

print("\n=== ESTATÍSTICAS ===")
print(f"Exemplos de treino: {len(dataset['train'])}")
print(f"Exemplos de validação: {len(dataset['validation']) if 'validation' in dataset else 'N/A'}")
print(f"Exemplos de teste: {len(dataset['test']) if 'test' in dataset else 'N/A'}")

# Analisar tags
if 'pos_tags' in exemplo:
    print("\n=== POS TAGS ===")
    pos_tags_feature = dataset['train'].features['pos_tags']
    print(f"Tipo: {type(pos_tags_feature)}")
    print(f"Feature: {pos_tags_feature}")
    
    # Tentar extrair nomes das tags
    if hasattr(pos_tags_feature, 'feature') and hasattr(pos_tags_feature.feature, 'names'):
        tag_names = pos_tags_feature.feature.names
        print(f"\nTotal de classes: {len(tag_names)}")
        print(f"Classes POS: {tag_names}")
    
print("\n=== ANÁLISE DE ALGUNS EXEMPLOS ===")
for i in range(min(3, len(dataset['train']))):
    exemplo = dataset['train'][i]
    print(f"\nExemplo {i+1}:")
    if 'tokens' in exemplo:
        print(f"  Tokens: {exemplo['tokens'][:10]}...")  # primeiros 10
    if 'pos_tags' in exemplo:
        print(f"  POS Tags: {exemplo['pos_tags'][:10]}...")  # primeiros 10
