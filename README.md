# Gerador de QR Code com Streamlit

Um aplicativo web simples e intuitivo para gerar QR codes a partir de URLs ou textos, desenvolvido com [Streamlit](https://streamlit.io/).

## 🎯 Funcionalidades

- 📱 Gera QR codes de alta qualidade
- 🔗 Suporta URLs e textos personalizados
- 💾 Download do QR code como arquivo PNG
- 🎨 Interface simples e responsiva
- ⚡ Execução em tempo real

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/betoschneider/qr-code-streamlit.git
cd qr-code-streamlit
```

2. Instale as dependências:
```bash
uv sync
```

### Executar a Aplicação

#### Localmente
```bash
streamlit run app.py
```

A aplicação será aberta no seu navegador padrão em `http://localhost:8501`.

#### Com Docker
Para rodar a aplicação usando Docker, utilize o comando:

```bash
docker-compose up --build -d
```

A aplicação estará disponível em `http://localhost:8515`.

## 📋 Dependências

- **streamlit**: Framework para criar aplicações web em Python
- **qrcode**: Biblioteca para gerar QR codes

## 📁 Estrutura do Projeto

```
.
├── app.py              # Aplicação principal do Streamlit
├── main.py             # Arquivo auxiliar
├── pyproject.toml      # Configuração do projeto
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## 💡 Como Funciona

1. O usuário insere uma URL ou texto na caixa de entrada
2. A aplicação gera um QR code automaticamente
3. O QR code é exibido na tela
4. O usuário pode fazer download da imagem em PNG

## 🔧 Personalização

Você pode modificar os parâmetros do QR code no arquivo `app.py`:

- `version`: Versão do QR code (controla o tamanho)
- `box_size`: Tamanho de cada "caixa" do QR code
- `border`: Tamanho da borda em torno do QR code

## 🌐 Acesso Online

Acesse a aplicação em: [https://betoschneider.com](https://betoschneider.com)

## 📄 Licença

Este projeto é de código aberto. Sinta-se livre para usar, modificar e distribuir.

## 👨‍💻 Autor

Desenvolvido por [betoschneider.com](https://betoschneider.com)

## 📝 Contribuições

Encontrou um bug ou tem sugestões de melhorias? Abra uma issue ou envie um pull request no [GitHub](https://github.com/betoschneider/qr-code-streamlit).

---

Feito com ❤️ usando Streamlit
