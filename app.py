import streamlit as st
import time
import base64
import streamlit.components.v1 as components

# =========================================
# IMPORTANDO CÁLCULOS
# =========================================

from calculos import (
    velocidade,
    distancia,
    poluicao,
    dados_simulacao
)

# =========================================
# IMPORTANDO GRÁFICOS
# =========================================

from graficos import gerar_graficos

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================

st.set_page_config(
    page_title="Simulador Futurista",
    page_icon="🚗",
    layout="wide"
)

# =========================================
# CSS GLOBAL
# =========================================

st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0b1020, #020617 70%);
    color: white;
    font-family: 'Segoe UI', sans-serif;
    overflow-x: hidden;
}

/* GRID FUTURISTA */

.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    top: 0;
    left: 0;

    background:
        linear-gradient(rgba(0,212,255,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,0.08) 1px, transparent 1px);

    background-size: 60px 60px;
    animation: gridMove 8s linear infinite;
    z-index: 0;
}

@keyframes gridMove {
    from { transform: translateY(0px); }
    to { transform: translateY(-60px); }
}

div[data-testid="stAppViewContainer"] {
    position: relative;
    z-index: 1;
}

/* TÍTULOS */

.main-title {
    font-size: 52px;
    font-weight: bold;
    text-align: center;
    color: #00D4FF;
    text-shadow: 0 0 20px #00D4FF;
}

.sub-title {
    text-align: center;
    color: #94A3B8;
    font-size: 18px;
    margin-bottom: 30px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid rgba(0,212,255,0.2);
}

/* CARDS */

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,212,255,0.25);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,212,255,0.15);
}

.card-title {
    color: #00D4FF;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
}

.card-value {
    font-size: 24px;
    font-weight: bold;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TÍTULO
# =========================================

st.markdown("""
<div class="main-title">
🚀 Simulador Futurista de Veículos
</div>

<div class="sub-title">
Sistema Inteligente de Modelagem Matemática e Simulação Computacional
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================
# SIDEBAR
# =========================================

st.sidebar.header("⚙️ Configurações")

velocidade_inicial = st.sidebar.slider(
    "Velocidade Inicial (km/h)",
    0,
    200,
    80
)

aceleracao = st.sidebar.slider(
    "Aceleração (m/s²)",
    -10,
    10,
    2
)

tempo = st.sidebar.slider(
    "Tempo de Simulação (s)",
    1,
    60,
    10
)

# =========================================
# ÁUDIO DO MOTOR
# =========================================

with open("assets/motor.mp3.mp3", "rb") as audio_file:
    audio_bytes = audio_file.read()

motor_audio_data = base64.b64encode(audio_bytes).decode("utf-8")

sound_volume = 0.2 + 0.8 * min(1.0, max(0.0, velocidade_inicial / 200))
playback_rate = 0.85 + 0.4 * min(1.0, max(0.0, (aceleracao + 10) / 20))

sound_volume = min(1.0, max(0.2, sound_volume))
playback_rate = min(1.4, max(0.85, playback_rate))


# =========================================
# RESULTADOS MATEMÁTICOS
# =========================================

velocidade_final = velocidade(
    velocidade_inicial,
    aceleracao,
    tempo
)

distancia_total = distancia(
    velocidade_inicial,
    aceleracao,
    tempo
)

poluicao_total = poluicao(
    velocidade_inicial,
    aceleracao,
    tempo
)
combustivel = 80 - (tempo * 0.5)

autonomia = combustivel * 5

# =========================================
# TELEMETRIA
# =========================================

st.markdown("""
<h1 style="
text-align:center;
color:#00D4FF;
text-shadow:0 0 20px #00D4FF;
">
 Telemetria do Veículo
</h1>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">🚗 Velocidade</div>
        <div class="card-value">{velocidade_inicial} km/h</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">⚙️ Aceleração</div>
        <div class="card-value">{aceleracao} m/s²</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">⛽ Combustível</div>
        <div class="card-value">{combustivel:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">📍 Autonomia</div>
        <div class="card-value">{autonomia:.0f} km</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =========================================
# CENTRAL MATEMÁTICA
# =========================================

st.markdown(f"""
<div style="
background: rgba(255,255,255,0.03);
border: 1px solid rgba(0,212,255,0.25);
padding: 20px;
border-radius: 20px;
box-shadow: 0 0 20px rgba(0,212,255,0.15);
">

<h1 style="
text-align:center;
color:#00D4FF;
font-size:28px;
margin-bottom:20px;
text-shadow:0 0 10px #00D4FF;
">
🧠 Central Matemática
</h1>

<hr style="border:1px solid rgba(0,212,255,0.2)">

<div style="
display:flex;
flex-direction:column;
gap:14px;
font-size:15px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
color:white;
">
<span>🏁 Velocidade Final</span>

<span style="
color:#38BDF8;
font-size:16px;
font-weight:bold;
">
{velocidade_final:.2f} km/h
</span>
</div>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
color:white;
">
<span>📏 Distância Percorrida</span>

<span style="
color:#38BDF8;
font-size:16px;
font-weight:bold;
">
{distancia_total:.2f} m
</span>
</div>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
color:white;
">
<span>🌫️ Poluição Gerada</span>

<span style="
color:#38BDF8;
font-size:16px;
font-weight:bold;
">
{poluicao_total:.2f}
</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================
# PAINEL DE SIMULAÇÃO
# =========================================

st.markdown("""
<h1 style="
text-align:center;
color:#00D4FF;
font-size:38px;
text-shadow:0 0 15px #00D4FF;
margin-bottom:25px;
">
 Painel de Simulação
</h1>
""", unsafe_allow_html=True)

vel_anim = max(0.7, 8 - velocidade_inicial / 20)

lane_speed = max(0.7, 4 - velocidade_inicial / 50)

car_swing = max(0.2, 0.35 - velocidade_inicial / 800)

colA, colB = st.columns([1, 2])

# =========================================
# CENTRAL VEICULAR
# =========================================

with colA:

    painel_html = f"""
    <!DOCTYPE html>
    <html>

    <head>

    <style>

    body {{

        margin:0;
        padding:0;
        background:transparent;
        overflow:hidden;
        font-family:'Segoe UI', sans-serif;

    }}

    .painel {{

        background: rgba(255,255,255,0.04);

        border: 1px solid rgba(0,212,255,0.25);

        border-radius: 20px;

        padding: 25px;

        height: 300px;

        box-shadow: 0 0 20px rgba(0,212,255,0.15);

        display:flex;

        flex-direction:column;

        justify-content:center;

        color:white;

    }}

    .titulo {{

        color:#00D4FF;

        text-align:center;

        font-size:22px;

        margin-bottom:30px;

        text-shadow:0 0 10px #00D4FF;

        font-weight:bold;

    }}

    .linha {{

        display:flex;

        justify-content:space-between;

        align-items:center;

        margin-bottom:18px;

        font-size:16px;

    }}

    .valor {{

        color:#00D4FF;

        font-weight:bold;

        text-shadow:0 0 8px #00D4FF;

    }}

    </style>

    </head>

    <body>

        <div class="painel">

            <div class="titulo">
                 Central Veicular
            </div>

            <div class="linha">

                <span>🚗 Velocidade</span>

                <span class="valor">
                    {velocidade_inicial} km/h
                </span>

            </div>

            <div class="linha">

                <span>⚙️ Aceleração</span>

                <span class="valor">
                    {aceleracao} m/s²
                </span>

            </div>

            <div class="linha">

                <span>📏 Distância</span>

                <span class="valor">
                    {distancia_total:.2f} m
                </span>

            </div>

            <div class="linha">

                <span>🌫️ Poluição</span>

                <span class="valor">
                    {poluicao_total:.2f}
                </span>

            </div>

        </div>

    </body>

    </html>
    """

    components.html(
        painel_html,
        height=320
    )

# =========================================
# SIMULAÇÃO VISUAL
# =========================================

with colB:

    simulador = f"""

   <style>

    .simulator {{

        position: relative;

        width: 100%;
        height: 260px;

        border-radius: 20px;

        overflow: hidden;

        background:
        linear-gradient(to bottom,
        #ff9966 0%,
        #ff5e62 35%,
        #1e3c72 70%,
        #0f172a 100%);

        border: 1px solid rgba(0,212,255,0.3);

        box-shadow: 0 0 20px rgba(0,212,255,0.2);

    }}

    /* SOL */

    .sun {{

        position:absolute;

        width:120px;
        height:120px;

        border-radius:50%;

        background: rgba(255,220,120,0.9);

        top:30px;
        right:120px;

        box-shadow:0 0 40px rgba(255,200,100,0.9);

    }}

    /* NUVENS */

    .cloud {{

        position:absolute;

        background:white;

        border-radius:100px;

        opacity:0.3;

        will-change: left;

    }}

    .cloud1 {{

        width:80px;
        height:40px;

        top:60px;
        left:-100px;

        animation:cloudMove 12s linear infinite;

    }}

    .cloud2 {{

        width:60px;
        height:30px;

        top:100px;
        left:-100px;

        animation:cloudMove 15s linear infinite;
        animation-delay:2s;

    }}

    .cloud3 {{

        width:70px;
        height:35px;

        top:80px;
        left:-100px;

        animation:cloudMove 18s linear infinite;
        animation-delay:4s;

    }}

    @keyframes cloudMove {{

        from {{
            left:-100px;
        }}

        to {{
            left:100%;
        }}

    }}

    /* MAR */

    .ocean {{

        position:absolute;

        bottom:118px;

        width:200%;
        height:55px;

        background:
        repeating-linear-gradient(
            90deg,
            #38BDF8,
            #0EA5E9 60px,
            #38BDF8 120px
        );

        animation:oceanMove 6s linear infinite;

        opacity:0.8;

    }}

    @keyframes oceanMove {{

        from {{
            transform: translateX(0px);
        }}

        to {{
            transform: translateX(-200px);
        }}

    }}

    /* AREIA */

    .sand {{

        position:absolute;

        bottom:90px;

        width:100%;
        height:28px;

        background:
        linear-gradient(to bottom,
        #f4d03f,
        #d4a017);

    }}

    /* PALMEIRAS */

    .tree {{

        position:absolute;

        bottom:92px;

        font-size:38px;

        animation:treeMove {vel_anim}s linear infinite;

        animation-timing-function: linear;

        will-change: left, transform;
    }}

    @keyframes treeMove {{

        from {{
            left:-120px;
        }}

        to {{
            left:100%;
        }}

    }}

    /* ESTRADA */

    .road {{

        position:absolute;

        bottom:0;

        width:100%;
        height:90px;

        background:
        linear-gradient(to bottom,
        #3f3f46,
        #18181b);

        overflow:hidden;

    }}

    /* FAIXAS */

    .lane {{

        position:absolute;

        top:42px;

        width:120px;
        height:6px;

        background:white;

        border-radius:10px;

        box-shadow:0 0 10px rgba(255,255,255,0.8);

        animation:laneMove {lane_speed}s linear infinite;
    }}

    @keyframes laneMove {{

        from {{
            left:-150px;
        }}

        to {{
            left:100%;
        }}

    }}

    /* CARRO */

    .car {{

        position:absolute;

        bottom:18px;

        right:70px;

        font-size:60px;

        animation:carMove {car_swing}s infinite alternate;

        animation-timing-function: ease-in-out;

        filter: drop-shadow(0 0 10px rgba(255,255,255,0.5));

        will-change: transform;

    }}

    @keyframes carMove {{

        from {{
            transform: translateY(0px);
        }}

        to {{
            transform: translateY(-3px);
        }}

    }}

    /* HUD */

    .hud {{

        position:absolute;

        top:15px;
        left:15px;

        color:white;

        font-family:monospace;

        font-size:14px;

        text-shadow:0 0 10px black;

    }}

    </style>

    <div class="simulator">

        <div class="sun"></div>
        <div class="cloud cloud1"></div>

        <div class="cloud cloud2"></div>

        <div class="cloud cloud3"></div>
        <div class="ocean"></div>

        <div class="sand"></div>

        <audio id="motorSound" loop preload="auto">
            <source src="data:audio/mpeg;base64,{motor_audio_data}" type="audio/mpeg" />
        </audio>

        <script>
            const motor = document.getElementById('motorSound');
            motor.volume = {sound_volume};
            motor.playbackRate = {playback_rate};
            motor.play().catch(() => {{ }});
        </script>

        <div class="hud">

            SPEED: {velocidade_inicial} km/h<br>
            ACC: {aceleracao} m/s²

        </div>

        <div class="tree" style="animation-delay:0s;">🌴</div>

        <div class="tree"
        style="
        animation-delay:2s;
        bottom:94px;
        ">
        🌴
        </div>

        <div class="tree" style="animation-delay:1.2s; font-size:32px;">🏖️</div>

        <div class="tree"
        style="
        animation-delay:3.2s;
        bottom:94px;
        font-size:32px;
        ">
        🏖️
        </div>

        <div class="road">

            <div class="lane" style="animation-delay:0s;"></div>

            <div class="lane"
            style="
            animation-delay:1s;
            ">
            </div>

            <div class="lane"
            style="
            animation-delay:2s;
            ">
            </div>

        </div>

        <div class="car">🛻</div>

    </div>

    """

    components.html(simulador, height=270)

st.divider()


# =========================================
# DADOS DOS GRÁFICOS
# =========================================

t, v, s, a_array, p = dados_simulacao(
    velocidade_inicial,
    aceleracao,
    tempo
)

# =========================================
# GERAR GRÁFICOS
# =========================================

fig = gerar_graficos(
    t,
    v,
    s,
    a_array,
    p
)

# =========================================
# MOSTRAR GRÁFICOS
# =========================================

st.markdown("""
<h1 style="
text-align:center;
color:#00D4FF;
text-shadow:0 0 15px #00D4FF;
">
📊 Análise Matemática
</h1>
""", unsafe_allow_html=True)

st.pyplot(fig)

# =========================================
# BOTÃO
# =========================================

if st.button("🚀 Iniciar Simulação"):

    components.html("""
    <audio autoplay>
        <source src="https://www.soundjay.com/transportation/car-start-01.mp3" type="audio/mp3">
    </audio>
    """, height=0)

    st.toast("Motor ligado 🔥")

    with st.spinner("Executando cálculos matemáticos..."):

        barra = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            barra.progress(i + 1)

    st.success("Simulação finalizada. Pronto para nova rodada.")

    st.info("A física foi aplicada e o som de aceleração reflete sua configuração.")