def transform_to_fng(grammar):
    fng_grammar = {}
    new_nonterminal = 'S0'  # Novo símbolo inicial
    
    # Passo 1: Adicionar a regra S0 -> S ao início da gramática
    fng_grammar[new_nonterminal] = [grammar['S']]
    
    # Passo 2: Remover regra S da gramática
    del grammar['S']
    
    # Passo 3: Substituir recursões à esquerda
    for nonterminal in grammar:
        productions = grammar[nonterminal]
        new_productions = []
        
        for production in productions:
            if production[0] == nonterminal:  # Verifica recursão à esquerda
                new_variable = nonterminal + "'"  # Novo símbolo não terminal
                new_productions.append(production[1:] + (new_variable,))
                new_productions.append(production[1:] + (new_variable, new_variable))
            else:
                new_productions.append(production)
        
        fng_grammar[nonterminal] = new_productions
    
    # Passo 4: Adicionar regras S -> λ e S0 -> λ, se necessário
    if 'S' not in fng_grammar:
        fng_grammar['S'] = [('λ',)]
    if new_nonterminal not in fng_grammar:
        fng_grammar[new_nonterminal] = [('λ',)]
    
    return fng_grammar

# Exemplo de uso
grammar = {
    'S': ['A', 'B', 'ABS'],
    'A': ['aA', 'λ'],
    'B': ['aBAB', 'λ']
}

fng_grammar = transform_to_fng(grammar)
print("Forma Normal de Greibach:")
for nonterminal in fng_grammar:
    productions = fng_grammar[nonterminal]
    for production in productions:
        print(nonterminal, '->', ' '.join(production))
