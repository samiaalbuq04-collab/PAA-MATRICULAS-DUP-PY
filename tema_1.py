from trabalho_base import mergesort, aleatorio


def duplicada_esperta_fases(v):
    ordenada, comps_ord = mergesort(v)
    comps_var = 0
    for i in range(len(ordenada) - 1):
        comps_var += 1
        if ordenada[i] == ordenada[i + 1]:
            return ordenada[i], comps_ord, comps_var
    return -1, comps_ord, comps_var


def duplicada_esperta(v):
    r, c_ord, c_var = duplicada_esperta_fases(v)
    return r, c_ord + c_var


def duplicada_ingenua(v):
    comps = 0
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            comps += 1
            if v[i] == v[j]:
                return v[i], comps
    return -1, comps


def testar_correcao():
    casos = [[], [7], [4, 4, 4], [1, 2, 3]]
    for k in range(1000):
        casos.append(aleatorio(30, 0, 60, semente=k))
    for v in casos:
        r1, _ = duplicada_ingenua(v)
        r2, _ = duplicada_esperta(v)
        tem = len(set(v)) < len(v)  # oráculo, só no teste
        assert (r1 != -1) == tem
        assert (r2 != -1) == tem
        assert r1 == -1 or v.count(r1) >= 2
        assert r2 == -1 or v.count(r2) >= 2
    print("correção ok em", len(casos), "entradas")


if __name__ == "__main__":
    testar_correcao()
