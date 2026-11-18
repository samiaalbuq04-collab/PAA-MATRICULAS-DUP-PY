from trabalho_base import mergesort, aleatorio, teste_do_dobro, salvar_csv, distintos


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


# ---------- Parte da Yara: medições ----------

def melhor_caso(n):
    # repetida nas duas primeiras posições
    return [5, 5] + list(range(100, 100 + n - 2))


def media_caso(n, versao, reps=30):
    # 30 entradas aleatórias com semente fixa; valores em 0..n//2 garantem repetidas
    total = 0
    for s in range(reps):
        total += versao(aleatorio(n, 0, n // 2, semente=s))[1]
    return total / reps


if __name__ == "__main__":
    testar_correcao()

    dados = []
    tam = (100, 200, 400, 800, 1600)
    grande = (12500, 25000, 50000, 100000)

    # Ingênua: só até 1600, porque cresce com n²
    teste_do_dobro("Ingênua, pior caso", lambda n: duplicada_ingenua(distintos(n))[1],
                   tamanhos=tam, versao="ingenua_pior", dados=dados)
    teste_do_dobro("Ingênua, melhor caso", lambda n: duplicada_ingenua(melhor_caso(n))[1],
                   tamanhos=tam, versao="ingenua_melhor", dados=dados)
    teste_do_dobro("Ingênua, caso médio", lambda n: media_caso(n, duplicada_ingenua),
                   tamanhos=tam, versao="ingenua_medio", dados=dados)

    # Esperta: também a série grande
    teste_do_dobro("Esperta, pior caso", lambda n: duplicada_esperta(distintos(n))[1],
                   tamanhos=tam + grande, versao="esperta_pior", dados=dados)
    teste_do_dobro("Esperta, melhor caso", lambda n: duplicada_esperta(melhor_caso(n))[1],
                   tamanhos=tam + grande, versao="esperta_melhor", dados=dados)
    teste_do_dobro("Esperta, caso médio", lambda n: media_caso(n, duplicada_esperta),
                   tamanhos=tam, versao="esperta_medio", dados=dados)

    # Peso de cada fase da esperta (pior caso)
    teste_do_dobro("Esperta, fase ordenação (pior caso)",
                   lambda n: duplicada_esperta_fases(distintos(n))[1],
                   tamanhos=tam + grande, versao="esperta_fase_ordenacao", dados=dados)
    teste_do_dobro("Esperta, fase varredura (pior caso)",
                   lambda n: duplicada_esperta_fases(distintos(n))[2],
                   tamanhos=tam + grande, versao="esperta_fase_varredura", dados=dados)

    salvar_csv(dados, "medicoes.csv")
