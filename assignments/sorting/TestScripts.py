# O objetivo do trabalho é fazer uma análise experimental para comparar alguns algoritmos de ordenação.
#
#     Implemente os algoritmos estudados em aula (seleção, inserção, mergesort, quicksort, heapsort). Escreva o programa mais simples possível para testar cada algoritmo. Compare o esforço necessário para a implementação correta de cada algortimo.
#     Compare o desempenho dos algoritmos em sequências de números inteiros geradas aleatoriamente. Use sequências de 100 até 100000 números. (E mais se for possível.) Meça e compare os tempos de cada algoritmo.
#     Repita os testes com sequências especiais: ordenadas em ordem crescente, ordenadas em ordem descrescente, com muitas repetições, com poucas repetições.
#     No caso de mergesort e quicksort, interrompa a recursão quando o subproblema for pequeno e execute ordenação por inserção em cada subproblema. No caso de quicksort, faça o mesmo executando ordenação por inserção uma única vez, ao final do processo. Vale a pena fazer essas modificações? A partir de quando? Para qual definição de pequeno?
#     Adapte os seus programas para ordenar palavras. Teste o desempenho de cada algoritmo no arquivo BR4.txt contendo 10000 palavras e no arquivo BR5.txt contendo 100000 palavras. Houve mudança do desempenho relativo dos algoritmos agora que comparar valores é mais complicado?

import random

#32 bits based
lowest_int =  −2147483648
highest_int =  2147483647

def random_integer()->int:
    return ramdom.randint(lowest_int, highest_int)

def generate_list_random_numbers(list_length:int)->list:
    return [random_integer()  for i in range(list_length)]

def generate_list_ordered(list_length:int)->list:
    k = random.randint(lowest_int, highest_int-list_length)
    return [ i for i in range(k, k+list_length)]

def generate_list_reverse_ordered(list_length:int)->list:
    k = random.randint(lowest_int+list_length, highest_int)
    return [i for i in range(k, k-list_length)]

def generate_list_unique(list_length:int)->list:
    return random.sample(range(lowest_int, highest_int), list_length)

def generate_list_many_repetitions(list_length:int, rep_percentage:int)->list:
    rep_size = int(rep_percentage*list_length/100)
    rep_num = random_integer();

    mylist = [random_integer for i in range(list_length-rep_size)]
    mylist.append([rep_num for i in range(rep_size)])
    random.shuffle(mylist)

    return mylist
