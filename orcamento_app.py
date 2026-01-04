import streamlit as st
from PIL import Image
import urllib

st.set_page_config(page_title="Solicitação de Orçamento", page_icon="🔐", layout="centered")
st.set_page_config(page_title="Área do Cliente - VIMAK", layout="centered")
st.title("🔐 Área do Cliente - VIMAK |Solicitação de Orçamento|")
st.markdown("---")

#st.title("🔐 Seja bem vindo!! VIMAK PLANEJADOS")
st.write(" Obrigatório preencha os dados abaixo. Em poucos minutos retornaremos seu contato pelo WhatsApp.")

# ------------------------------
# DADOS DO CLIENTE
# ------------------------------
st.subheader("📌 Dados do Cliente")

nome = st.text_input("Nome completo")
telefone = st.text_input("Telefone (WhatsApp)")
email = st.text_input("E-mail (opcional)")
endereco = st.text_input("Endereço completo")
cidade = st.text_input("Cidade")

st.markdown("---")

# ------------------------------
# DADOS DO AMBIENTE
# ------------------------------
st.subheader("📍 Preciso De Orçamento Para Ambiente")

ambiente = st.selectbox(
    "Opção de Ambiente",
    ["Casa", "Apartamento", "Comercial", "Reforma", "Outro"]
)

# Medidas
tem_medidas = st.checkbox("Tenho as medidas do ambiente!")

if tem_medidas:
    col1, col2, col3 = st.columns(3)
    largura = col1.text_input("Largura (cm)")
    altura = col2.text_input("Altura (cm)")
    profundidade = col3.text_input("Profundidade (cm)")
else:
    largura = altura = profundidade = ""

st.markdown("---")

# ------------------------------
# COMPONENTE: ITEM COM IMAGEM
# ------------------------------
def item_checkbox(nome, imagem_path, col_ratio=[1,5], largura_img=80):
    col1, col2 = st.columns(col_ratio)
    with col1:
        img = Image.open(imagem_path)
        st.image(img, width=largura_img)
    with col2:
        return st.checkbox(nome)

# ------------------------------
# ACABAMENTOS
# ------------------------------
st.subheader("🎨 Escolha os Acabamentos que deseja! ")

acab_branco = item_checkbox("Branco Texturizado", "branco_tx.jpg")
acab_madeirado = item_checkbox("Madeirado", "madeirado.jpg")
acab_colorido_liso = item_checkbox("Colorido Liso", "colorido.jpg")
acab_colorido_text = item_checkbox("Colorido Texturizado", "colorido.jpg")
acab_laca = item_checkbox("Laca / Alto Brilho", "alto_brilho.jpg")

st.markdown("---")

# ------------------------------
# ILUMINAÇÃO
# ------------------------------
st.subheader("💡 Deseja ter Iluminação? ")

iluminacao_com = item_checkbox("Com Iluminação", "iluminacao.png", col_ratio=[1,3])
iluminacao_sem = item_checkbox("Sem Iluminação", "iluminacao.png", col_ratio=[1,3])

st.markdown("---")

#------------------------------
# FERRAGENS
# ------------------------------
st.subheader(" Escolha as suas ferragens!")

corredica_oculta = item_checkbox("Corrediças Ocultas", "corredica_oculta.jpg", col_ratio=[1,3])
corredica_telescópica = item_checkbox("Corrediças Telescópicas", "corredica_telescopica.png", col_ratio=[1,3])
dobradica_com_amortecedor = item_checkbox("Dobradiças com Amortecedor", "dobradicas.jpg", col_ratio=[1,3])
dobradicas_sem_amortecedor = item_checkbox("Dobradiças sem amortecedor", "dobradicas.jpg", col_ratio=[1,3])
articulador = item_checkbox("Articulador", "articulador.jpg", col_ratio=[1,3])
pistao_gas = item_checkbox("Pistão a gás", "pistao_gas.jpg", col_ratio=[1,3])

st.markdown("---")

# ------------------------------
# PUXADORES
# ------------------------------
st.subheader("🔩 Escolha o Puxadores que mais gosta!")

pux_perfil = item_checkbox("Perfil Alumínio", "perfil_m0218.jpg", col_ratio=[1,3])
pux_ponto = item_checkbox("Ponto / Alça", "alca.jpg", col_ratio=[1,3])
pux_cava = item_checkbox("Cava", "perfil_cava.jpg", col_ratio=[1,3])
pux_passante = item_checkbox("Passante", "porta_passante.jpg", col_ratio=[1,3])
pux_toque = item_checkbox("Abertura no Toque (Push-open)", "abertura_toque.jpg", col_ratio=[1,3])

st.markdown("---")

# ------------------------------
# BOTÃO DE ENVIO
# ------------------------------
if st.button("📤 Enviar solicitação"):

    if nome == "" or telefone == "":
        st.warning("⚠️ Nome e telefone são obrigatórios!")
        st.stop()

    st.success("Solicitação enviada com sucesso! Entraremos em contato pelo WhatsApp.")

    # ------------------------------
    # Função auxiliar
    # ------------------------------
    def marcar(nome, selecionado):
        return f"- {nome}\n" if selecionado else ""

    # ------------------------------
    # ACABAMENTOS
    # ------------------------------
    acabamentos_texto = ""
    acabamentos_texto += marcar("Branco Texturizado", acab_branco)
    acabamentos_texto += marcar("Madeirado", acab_madeirado)
    acabamentos_texto += marcar("Colorido Liso", acab_colorido_liso)
    acabamentos_texto += marcar("Colorido Texturizado", acab_colorido_text)
    acabamentos_texto += marcar("Laca / Alto Brilho", acab_laca)

    if acabamentos_texto == "":
        acabamentos_texto = "Nenhum selecionado."

    # ------------------------------
    # ILUMINAÇÃO
    # ------------------------------
    iluminacao_texto = ""
    iluminacao_texto += marcar("Com iluminação", iluminacao_com)
    iluminacao_texto += marcar("Sem iluminação", iluminacao_sem)

    if iluminacao_texto == "":
        iluminacao_texto = "Nenhuma opção selecionada."

    # ------------------------------
    # FERRAGENS
    # ------------------------------
    ferragens_texto = ""
    ferragens_texto += marcar("Corrediças Ocultas", corredica_oculta)
    ferragens_texto += marcar("Corrediças Telescópicas", corredica_telescópica)
    ferragens_texto += marcar("Dobradiças com Amortecedor", dobradica_com_amortecedor)
    ferragens_texto += marcar("Dobradiças sem Amortecedor", dobradicas_sem_amortecedor)
    ferragens_texto += marcar("Articulador", articulador)
    ferragens_texto += marcar("Pistão de Gas", pistao_gas)

    if ferragens_texto == "":
        ferragens_texto = "Nenhuma opção selecionada."

    # ------------------------------
    # PUXADORES
    # ------------------------------
    puxadores_texto = ""
    puxadores_texto += marcar("Perfil Alumínio", pux_perfil)
    puxadores_texto += marcar("Ponto / Alça", pux_ponto)
    puxadores_texto += marcar("Cava", pux_cava)
    puxadores_texto += marcar("Passante", pux_passante)
    puxadores_texto += marcar("Push-open", pux_toque)

    if puxadores_texto == "":
        puxadores_texto = "Nenhum puxador selecionado."

    # ------------------------------
    # MENSAGEM FINAL
    # ------------------------------
    mensagem = f"""
Olá! Meu nome é {nome}.

Gostaria de solicitar um orçamento para: **{ambiente}**.

---

**📏 Medidas:**  
Largura: {largura} cm  
Altura: {altura} cm  
Profundidade: {profundidade} cm  

---

**🎨 Acabamentos desejados:**  
{acabamentos_texto}

**💡 Iluminação:**  
{iluminacao_texto}

**🛠️ Ferragens selecionadas:**  
{ferragens_texto}

**🚪 Puxadores selecionados:**  
{puxadores_texto}

---

**📍 Endereço:** {endereco}  
**Cidade:** {cidade}  
**Contato:** {telefone}
"""

    st.markdown("### 💬 Mensagem gerada:")
    st.markdown(mensagem)

    # Envio pelo WhatsApp
    mensagem_whatsapp = urllib.parse.quote(mensagem)
    link = f"https://wa.me/55{telefone}?text={mensagem_whatsapp}"
    st.markdown(f"[📩 Enviar pelo WhatsApp]({link})")
