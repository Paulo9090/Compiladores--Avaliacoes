


def lexer(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:\'",.<>/?\\|'
    math_operators = '+-*/'
    math_symbols = '()[]{}@#!0123456789'
    output_str = ''
    tokens = input_str.split()
    for token in tokens:
    
     print('10 primeiros tokens lidos:')
    for i, token in enumerate(tokens):
        print('{}: {}'.format(i+1, token))
        if len(tokens) > 10:
          tokens = tokens[:10]  # Limita a leitura aos 10 primeiros tokens

        if any(c in 'xyztw' for c in token):
            if any(c in math_operators + math_symbols for c in token):
                # token contém caracteres permitidos e operadores matemáticos
                output_str += token + ' '
            else:
                print('Token {} contém um caractere não permitido.'.format(token))
                return
        else:
            # token não contém caracteres x, y, z, t, ou w
            if token[0].isdigit():
                print('Token {} começa com um número e é uma palavra reservada do sistema.'.format(token))
                return
            for char in token:
                if char not in allowed_chars:
                    print('Token {} contém um caractere não permitido.'.format(token))
                    return
            output_str += token + ' '
    if any(c in 'xyztw' for c in output_str) and any(c in math_operators + math_symbols for c in output_str):
        print('Cadeia aceita: {} (expressão matemática)'.format(output_str))
    else:
        print('Cadeia aceita: {}'.format(output_str))



# Exemplo de uso:
input_str = input('Digite uma cadeia de caracteres: ')
lexer(input_str)
