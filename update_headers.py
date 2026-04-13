import os
import glob

# Get all html files
html_files = glob.glob('*.html')
# We exclude the ones that are special or already updated fully
html_files = [f for f in html_files if f not in ['index.html']]


new_header = """    <!-- TOP HEADER -->
    <div class="top-bar">
        <div class="top-bar-inner">
            <div class="top-bar-left">
                <div class="icon-circle">📞</div>
                <p>(051) 496 6384<br>RPM: #976-765606 / RPC: 980-967317</p>
            </div>
            
            <div class="logo-center">
                <svg width="180" height="90" viewBox="0 0 180 90" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="90" cy="45" r="35" fill="none" stroke="#FDCB29" stroke-width="8" stroke-dasharray="10 5" />
                    <text x="90" y="52" font-family="Arial" font-weight="bold" font-size="28" fill="#5AA436" text-anchor="middle">Andina</text>
                    <text x="90" y="65" font-family="Arial" font-size="10" fill="#206229" text-anchor="middle">Corporation Of Consultants</text>
                </svg>
            </div>

            <div class="top-bar-right">
                <div class="icon-circle">📍</div>
                <p>Psj. Olaya 110 Ofc. 601<br>Plaza Mayor Cercado de Lima - Lima</p>
            </div>
        </div>
    </div>

    <!-- NAV BAR AMARILLA -->
    <nav class="nav-bar">
        <ul class="nav-menu">
            <li><a href="index.html">INICIO</a></li>
            <li><a href="nosotros.html">EMPRESA</a></li>
            <li><a href="servicios.html">SERVICIO ⌄</a></li>
            <li><a href="productos.html">PRODUCTOS</a></li>
            <li><a href="proyectos.html">PROYECTOS</a></li>
            <li><a href="contacto.html">CONTACTO</a></li>
            <li><a href="andinacorp-ecommerce.html">ECOMMERCE</a></li>
            <li><a href="#" style="padding: 15px 15px;">🔍</a></li>
        </ul>
    </nav>"""

new_footer = """    <!-- FOOTER GRIS OSCURO -->
    <footer>
        <div class="footer-inner">
            <div class="footer-logo">
                <svg width="40" height="40" viewBox="0 0 180 90" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="45" cy="45" r="35" fill="none" stroke="#FDCB29" stroke-width="12" />
                </svg>
                <h3 style="color:#5AA436; font-size: 22px;">Andina<br><span style="font-size: 10px; color:white; font-family: 'Open Sans', sans-serif;">Corporation Of Consultants</span></h3>
            </div>
            
            <div class="footer-copy">
                &copy; 2026 Todos los Derechos reservados.<br>Andina Corporation of Consultants SRL
            </div>
            
            <div class="footer-social">
                <a href="#" class="social-icon">f</a>
                <a href="#" class="social-icon">t</a>
                <a href="#" class="social-icon">g</a>
                <a href="#" class="social-icon">in</a>
                <!-- Botón scroll up -->
                <div class="btn-up" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">▲</div>
            </div>
        </div>
    </footer>"""


for filepath in html_files:
    print(f"Processing {filepath}")
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine Active tab in Nav
    active_nav = ""
    if "nosotros" in filepath: active_nav = '<li><a href="nosotros.html"'
    elif "servicios" in filepath: active_nav = '<li><a href="servicios.html"'
    elif "productos" in filepath: active_nav = '<li><a href="productos.html"'
    elif "proyectos" in filepath: active_nav = '<li><a href="proyectos.html"'
    elif "contacto" in filepath: active_nav = '<li><a href="contacto.html"'
    elif "ecommerce" in filepath: active_nav = '<li><a href="andinacorp-ecommerce.html"'

    dynamic_header = new_header
    if active_nav:
         dynamic_header = dynamic_header.replace(active_nav, active_nav.replace('<li>', '<li class="active">'))
    
    # Replace the old <header> block entirely
    import re
    # Match from <header> to </header>
    content = re.sub(r'<header.*?>.*?</header>', dynamic_header, content, flags=re.DOTALL)
    
    # Replace the old <footer> block entirely
    content = re.sub(r'<footer.*?>.*?</footer>', new_footer, content, flags=re.DOTALL)

    # Some pages had <header class="scrolled"> inside a container, others had <div class="container nav-content">...
    # The regex r'<header>.*?</header>' catches it if formatted standardly. 

    with open(filepath, 'w') as f:
        f.write(content)

print("Done updating headers and footers.")
