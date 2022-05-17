"""
15. rhombus

Dado o numero de linhas de um losango, retorne

Exemplo: 5
Irá retornar o seguinte losango:
  0
 010
01210
 010
  0

"""


def get_list_characters_line(central_number):
    return [*range(central_number), *range(central_number, -1, -1)]


def convert_list_in_string(list_line):
    return ''.join(str(i) for i in list_line)


def get_rhombus(max_number):

    largura = max_number * 2 + 1

    rhombus = ''
    for index in [*range(max_number), *range(max_number, -1, -1)]:
        string_line = convert_list_in_string(get_list_characters_line(index))
        rhombus += string_line.center(largura) + '\n'

    return rhombus


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':

    test(convert_list_in_string, [1, 2, 3, 4, 5], '12345')
    test(convert_list_in_string, [0, 1, 0], '010')

    test(get_list_characters_line, 2, [0, 1, 2, 1, 0])
    test(get_list_characters_line, 0, [0])

    test(get_rhombus, 1, " 0 " + '\n'
                         "010" + '\n'
                         " 0 " + '\n')

    test(get_rhombus, 2, "  0  " + '\n'
                         " 010 " + '\n'
                         "01210" + '\n'
                         " 010 " + '\n'
                         "  0  " + '\n')
