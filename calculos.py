import numpy as np

# =========================================
# VELOCIDADE
# v(t) = v0 + a.t
# =========================================

def velocidade(v0, a, t):
    return v0 + a * t

# =========================================
# POSIÇÃO
# s(t) = v0.t + (a.t²)/2
# =========================================

def posicao(v0, a, t):
    return v0 * t + (a * t**2) / 2

# =========================================
# DISTÂNCIA VIA INTEGRAL
# =========================================

def distancia(v0, a, t):

    t_array = np.linspace(0, t, 200)

    v = velocidade(v0, a, t_array)

    return np.trapezoid(v, t_array)

# =========================================
# POLUIÇÃO
# =========================================

def poluicao(v0, a, t, k=0.05):

    t_array = np.linspace(0, t, 200)

    v = velocidade(v0, a, t_array)

    p = k * v**2

    return np.trapezoid(p, t_array)

# =========================================
# DADOS COMPLETOS DOS GRÁFICOS
# =========================================

def dados_simulacao(v0, a, tempo):

    t = np.linspace(0, tempo, 200)

    v = velocidade(v0, a, t)

    s = posicao(v0, a, t)

    acel = np.full_like(t, a)

    p = 0.05 * v**2

    return t, v, s, acel, p