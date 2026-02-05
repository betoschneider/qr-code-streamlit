import streamlit as st
import qrcode
import io
from datetime import datetime

def main():
    st.set_page_config(
        page_title="Gerador de QR Code", 
        page_icon=":qrcode:", 
        layout="centered"
    )

    st.title("Gerador de QR Code com Streamlit")

    # Input do usuário
    valor = st.text_input("Insira URL ou texto", "https://google.com")

    if valor:
        # Gerar QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(valor)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Criar colunas para centralizar
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            # Plotar imagem
            st.image(img.get_image(), width="stretch")

            # Download
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            st.download_button(
                "Baixar QR Code", 
                buf.getvalue(), 
                f"qrcode_{date}.png", 
                "image/png", 
                icon=":material/download:",
                width="stretch"
            )

    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center;'>
            Desenvolvido por <a href='https://betoschneider.com' target='_blank'>betoschneider.com</a> | 
            Disponível no <a href='https://github.com/betoschneider/qr-code-streamlit' target='_blank'>GitHub</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
    