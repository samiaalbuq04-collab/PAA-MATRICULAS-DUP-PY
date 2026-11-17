from trabalho_base import mergesort


def duplicada_esperta(v):
    ordenada, comps_ord = mergesort(v)
    comps_var = 0
    for i in range(len(ordenada) - 1):
        comps_var += 1
        if ordenada[i] == ordenada[i + 1]:
            return ordenada[i], comps_ord + comps_var
    return -1, comps_ord + comps_var
