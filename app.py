import streamlit as st
import qrcode
# from PIL import Image
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
        qr = qrcode.QRCode(version=1, box_size=20, border=5)
        qr.add_data(valor)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Plotar imagem
        st.image(img.get_image())

        # Download
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        st.download_button("Baixar QR Code", buf.getvalue(), f"qrcode_{date}.png", "image/png", icon=":material/download:")

    st.markdown("---")
    st.markdown("Desenvolvido por [betoschneider.com](https://betoschneider.com)")
    st.markdown("Código-fonte disponível no [GitHub](https://github.com/betoschneider/qr-code-streamlit)")

if __name__ == "__main__":
    main()
    