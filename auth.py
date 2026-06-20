import streamlit as st

def check_password():
    """
    Verifica contraseña antes de acceder a la aplicación.
    Retorna True si el usuario está autenticado, False si no.
    """
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        # Mostrar página de login
        st.set_page_config(
            page_title="MoneyPrinterTurbo - Login",
            page_icon="🎬"
        )
        
        st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 40px;
            border-radius: 10px;
            background-color: #1e1e1e;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.title("🔐 MoneyPrinterTurbo")
        st.subheader("Acceso Restringido")
        st.write("Ingresa tu contraseña para continuar")
        
        password = st.text_input(
            "Contraseña:", 
            type="password",
            placeholder="••••••••"
        )
        
        if st.button("Iniciar Sesión", use_container_width=True):
            # Obtén la contraseña de los Secrets
            correct_password = st.secrets.get("APP_PASSWORD", "admin123")
            
            if password == correct_password:
                st.session_state.password_correct = True
                st.success("✅ Bienvenido!")
                st.rerun()
            else:
                st.error("❌ Contraseña incorrecta. Intenta de nuevo.")
        
        return False
    
    return True
