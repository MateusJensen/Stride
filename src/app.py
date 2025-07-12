import json
import tempfile
import streamlit as st
from utilities import *

st.set_page_config(page_title="Gerador STRIDE com IA", layout="wide")
st.title("🔐 Análise de Segurança com IA + STRIDE")

uploaded_file = st.file_uploader("📤 Envie um diagrama de arquitetura (imagem)", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(uploaded_file.getvalue())
        image_path = tmp.name

    st.image(uploaded_file, caption="📌 Diagrama recebido", use_column_width=True)

    with st.spinner("🔍 Detectando componentes e gerando relatório..."):
        components = detect_components(image_path)
        stride_results = generate_stride_report(components)

        # Gera relatório completo com vulnerabilidades
        full_report = {}
        for comp, threats in stride_results.items():
            vuln_details = get_vulnerabilities(comp, threats)
            full_report[comp] = vuln_details

    st.success("✅ Relatório gerado com sucesso!")

    st.subheader("📦 Componentes detectados")
    st.write(components)

    st.subheader("🛡️ Relatório STRIDE com vulnerabilidades")
    st.json(full_report)

    # Botão para baixar JSON
    json_str = json.dumps(full_report, indent=4, ensure_ascii=False)
    st.download_button("⬇️ Baixar relatório em JSON", data=json_str, file_name="security_report.json", mime="application/json")
