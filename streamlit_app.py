import streamlit as st
from streamlit.components.v1 import html

def main():
    # Seitenkonfiguration
    st.set_page_config(
        page_title="Lions Club Mainspitze",
        page_icon="🦁",
        layout="wide"
    )

    # Header
    st.title("Lions Club Mainspitze")
    st.subheader("Wir dienen - We serve")
    
    # Hauptinhalt
    st.markdown("""
    ### Willkommen beim Lions Club Bischofsheim (Mainspitze)
    
    Wir sind eine engagierte Gemeinschaft von Menschen aus der Region, die sich mit Freude für 
    wohltätige Zwecke einsetzen. Unsere Mitglieder kommen hauptsächlich aus Bischofsheim, 
    Ginsheim und Gustavsburg.
    """)

    # Veranstaltungen und Aktivitäten
    st.header("Unsere Aktivitäten")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Jährliche Veranstaltungen")
        st.markdown("""
        - **Kaffeehaus**: Frühlingsereignis mit Kuchenbuffet
        - **Entenrennen**: Teil des Ginsheimer Altrheinfests
        - **Bischofsheimer Kerb**: Lokale Kirchweih
        - **Christmas Fire Truck Tour**: Weihnachtliche Feuerwehrauto-Tour
        """)
    
    with col2:
        st.subheader("Förderprojekte")
        st.markdown("""
        - Unterstützung lokaler Initiativen
        - Ukraine-Hilfe
        - Ahrtal-Wiederaufbau
        - Umweltschutzinitiativen
        """)

    # Mitmachen
    st.header("Mitmachen & Kontakt")
    st.markdown("""
    Möchtest du dich sozial engagieren und Teil unserer Gemeinschaft werden? 
    Sprich mit unserem Chat-Assistenten - er hilft dir gerne weiter!
    """)

    # Chat-Integration
    chat_html = '''
    <div id="lions-chat-container" style="height: 600px;">
    <script type="module" src="https://unpkg.com/feazy-plugin/dist/feazy-chat-component.es.js"></script>
    <chat-component 
        theme="light-theme"
        promptId="d7caaec4-0587-4dd4-89c6-a6880e63e832"
        chatTitle="Lions Website Assistent"
        showDataProtection="true"
        isDialogVisible="true"
        baseUrl="https://api.feazy.ai"
        id="lions-chat">
    </chat-component>
    
    <style>
        chat-component {
            --primary-color: #00338D;
            --secondary-color: #f8f9fa;
            --text-color: #333333;
            --border-color: #dee2e6;
            --bot-message-bg: #f1f3f5;
            --user-message-bg: #e9ecef;
            --header-bg: #00338D;
            --header-text: #ffffff;
            --chat-button-bg: #00338D;
            --chat-button-color: #ffffff;
            --send-button-bg: #00338D;
            --send-button-color: #ffffff;
        }
    </style>
    </div>
    '''
    
    html(chat_html, height=700)

    # Prompt Documentation
    st.header("Chat-Assistent Dokumentation")
    with st.expander("Über den Chat-Assistenten"):
        st.markdown("""
        Der Lions Website Assistent ist darauf spezialisiert, Besuchern alle wichtigen Informationen 
        über den Club zu vermitteln und bei Interesse den Kontakt herzustellen.
        
        **Hauptaufgaben:**
        1. Informieren über den Club und seine Aktivitäten
        2. Interesse für ehrenamtliches Engagement wecken
        3. Einfachen Erstkontakt ermöglichen
        4. Fragen zu Veranstaltungen und Projekten beantworten
        """)

    with st.expander("Kernwissen des Assistenten"):
        st.markdown("""
        #### Veranstaltungen
        - **Kaffeehaus**: Jährliches Frühlingsereignis mit Kuchenbuffet
        - **Entenrennen**: Teil des Ginsheimer Altrheinfests (1.000 Plastikenten)
        - **Bischofsheimer Kerb**: Teilnahme mit verschiedenen Aktivitäten
        - **Christmas Fire Truck Tour**: Weihnachtliches Catering bei der Feuerwehr-Tour

        #### Förderprojekte
        - Lokale Projekte in der Region
        - Umweltschutzinitiativen
        - Katastrophenhilfe (Ukraine, Ahrtal)
        """)

    with st.expander("Kontaktprozess"):
        st.markdown("""
        Bei Interesse an einer Mitgliedschaft oder weiterem Kontakt kann der Assistent:
        1. Die E-Mail-Adresse des Interessenten erfragen
        2. Einen E-Mail-Draft zur Bestätigung zeigen
        3. Nach Bestätigung die E-Mail versenden (Interessent wird in CC gesetzt)

        **E-Mail-Template:**
        ```
        Betreff: "Interessent:in Lions Club Mainspitze - [Name]"

        Text:
        Hallo,

        [Name] hat über den Website-Assistenten Interesse am Lions Club Mainspitze bekundet.

        Kontaktdaten:
        E-Mail: [E-Mail-Adresse]

        Interessensgebiet/Fragen:
        [Kurze Zusammenfassung des Gesprächs/der Interessen]

        Beste Grüße
        Lions Website Assistent
        ```
        """)

    # Footer
    st.markdown("---")
    st.markdown("© 2025 Lions Club Mainspitze")

if __name__ == "__main__":
    main()