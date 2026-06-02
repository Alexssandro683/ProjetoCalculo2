import matplotlib.pyplot as plt

# =========================================
# GRÁFICOS
# =========================================

def gerar_graficos(t, v, s, a, p):

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    fig.patch.set_facecolor("#020617")

    for ax in axs.flat:
        ax.set_facecolor("#0f172a")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("#00D4FF")
        ax.grid(True, alpha=0.3)

    # =====================================
    # VELOCIDADE
    # =====================================

    axs[0,0].plot(t, v, linewidth=3)

    axs[0,0].set_title("Velocidade x Tempo")

    axs[0,0].set_xlabel("Tempo")

    axs[0,0].set_ylabel("Velocidade")

    # =====================================
    # POSIÇÃO
    # =====================================

    axs[0,1].plot(t, s, linewidth=3)

    axs[0,1].set_title("Posição x Tempo")

    axs[0,1].set_xlabel("Tempo")

    axs[0,1].set_ylabel("Posição")

    # =====================================
    # ACELERAÇÃO
    # =====================================

    axs[1,0].plot(t, a, linewidth=3)

    axs[1,0].set_title("Aceleração x Tempo")

    axs[1,0].set_xlabel("Tempo")

    axs[1,0].set_ylabel("Aceleração")

    # =====================================
    # POLUIÇÃO
    # =====================================

    axs[1,1].plot(t, p, linewidth=3)

    axs[1,1].set_title("Poluição x Tempo")

    axs[1,1].set_xlabel("Tempo")

    axs[1,1].set_ylabel("Poluição")

    plt.tight_layout()

    return fig