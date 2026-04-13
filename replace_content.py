import re

def update_file(filename, new_body_content):
    with open(filename, 'r') as f:
        content = f.read()
    
    # We replace everything between </nav> and <!-- FOOTER GRIS OSCURO -->
    pattern = re.compile(r'(</nav>).*?(<!-- FOOTER GRIS OSCURO -->)', re.DOTALL)
    new_content = pattern.sub(f'\\1\n\n{new_body_content}\n\n\\2', content)
    
    with open(filename, 'w') as f:
        f.write(new_content)

# 1. SERVICIOS 
servicios_html = """
    <!-- TOP BANNER -->
    <div class="page-top-banner">
        <div class="banner-overlay"></div>
        <div class="banner-content">
            <h1>SERVICIOS</h1>
            <p>Inicio &rightarrow; Servicios</p>
        </div>
    </div>

    <!-- MAIN SIDBAR LAYOUT -->
    <div class="page-container" style="background-color: var(--bg-beige);">
        <div class="sidebar-layout">
            <div class="sidebar">
                <ul>
                    <li class="active"><a href="#">CONSTRUCCIÓN CIVIL</a></li>
                    <li><a href="#">ASESORAMIENTO</a></li>
                    <li><a href="#">CONSULTORÍA</a></li>
                    <li><a href="#">EXPORTACIÓN</a></li>
                    <li><a href="#">COMERCIALIZACION</a></li>
                    <li><a href="#">PROYECTOS</a></li>
                </ul>
            </div>
            
            <div class="content-area">
                <h2>CONSTRUCCIÓN CIVIL</h2>
                <div class="accent-line"></div>
                <p>Construcción civil, pavimentación, carreteras, remodelación en drywall (oficinas, departamentos, casas para vivienda, hoteles, discotecas, condominios, fábricas, industrias, etc).</p>
                <img src="https://images.unsplash.com/photo-1541888946425-d81bb19480c5?auto=format&fit=crop&q=80&w=800" alt="Construccion Civil" style="width:100%; max-width:600px;">
            </div>
        </div>
    </div>
"""

# 2. NOSOTROS (NUESTRA EMPRESA)
nosotros_html = """
    <!-- TOP BANNER -->
    <div class="page-top-banner">
        <div class="banner-overlay"></div>
        <div class="banner-content">
            <h1>NUESTRA EMPRESA</h1>
            <p>Inicio &rightarrow; Empresa</p>
        </div>
    </div>

    <div class="page-container" style="background-color: var(--bg-beige);">
        <div class="two-col-layout">
            <div class="col-left">
                <h2 class="title-with-line">ACERCA DE NOSOTROS</h2>
                <div class="title-line"></div>
                <p style="font-size:13px; margin-bottom:15px;">ANDINA CC SRL., es una empresa peruana, dedicada a la prestación de bienes, servicios, consultorías y ejecución de obras y proyectos para el sector público y privado del país.</p>
                <p style="font-size:13px; margin-bottom:15px;">Se funda el 18 de Enero del 2013, con el fin de hacer participar a la población del ámbito en cada uno de sus proyectos, como parte de nuestra responsabilidad social empresarial para generar riqueza y bienestar integral en el marco de mejores condiciones de vida.</p>
                
                <div class="vision-mision">
                    <div>
                        <h4>VISIÓN</h4>
                        <p>Ser una empresa líder en la prestación de servicios estratégicos y ejecución de proyectos rentables y empresarialmente sostenibles.</p>
                    </div>
                    <div>
                        <h4>MISIÓN</h4>
                        <p>Somos una empresa orientada a lograr la excelencia para la prestación de servicios de calidad, integridad y lealtad a nuestros clientes.</p>
                    </div>
                </div>

                <p style="font-size:13px; margin-bottom:20px;">Interesados en la protección medioambiental y la seguridad con estándares del más alto nivel para intervenir. ANDINA CC SRL tiene el único objetivo de promover e impulsar procesos de desarrollo integral.</p>
                
                <img src="https://images.unsplash.com/photo-1454165833767-027ffea9e77b?auto=format&fit=crop&q=80&w=800" alt="Collage Andina" style="max-width: 100%; margin-top:20px;">
            </div>
            
            <div class="col-right">
                <h2 class="title-with-line" style="font-size: 18px;">PERSONERÍA JURÍDICA</h2>
                <ul class="legal-list">
                    <li>
                        <h5>Segundo Alamiro Llamoctanta Espinoza</h5>
                        <p>Gerente General</p>
                    </li>
                    <li>
                        <h5>Partida Electrónica N° 11137550</h5>
                        <p>SUNARP</p>
                    </li>
                    <li>
                        <h5>20529667524</h5>
                        <p>RUC</p>
                    </li>
                    <li>
                        <h5>Inscripción</h5>
                        <p>REMYPE</p>
                    </li>
                    <li>
                        <h5 style="color:#007635;">Constancia de inscripción como: Participante, postor y contratista en bienes y servicios al Estado.</h5>
                        <p>RNP</p>
                    </li>
                    <li>
                        <h5>Consultor y Ejecutor</h5>
                        <p>OCSE</p>
                    </li>
                </ul>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 80px;">
            <h2 class="title-with-line" style="text-align:center;">ALIANZAS</h2>
            <div class="title-line" style="margin: 0 auto 30px;"></div>
            <div style="background-color: #333; color: white; display: inline-block; width: 250px; text-align: center;">
                <img src="https://via.placeholder.com/250x150.png?text=ASIDEP+LOGO" alt="ASIDEP" style="width: 100%;">
                <div style="padding: 15px;">
                    <h4 style="margin-bottom:5px;">ASIDEP</h4>
                    <p style="font-size:12px;">Ejecutor Calificado</p>
                </div>
                <div style="background-color: #007635; padding: 10px; cursor: pointer; font-size: 13px; margin: 15px; border-radius:30px;">CONTACTAR</div>
            </div>
        </div>
    </div>
"""

# 3. CONSULTORÍA (ASESORÍA)
consultoria_html = """
    <!-- TOP BANNER -->
    <div class="page-top-banner">
        <div class="banner-overlay"></div>
        <div class="banner-content">
            <h1>ASESORÍA</h1>
            <p>Inicio &rightarrow; Asesoría</p>
        </div>
    </div>

    <div style="background-color: var(--bg-beige);">
        <div class="alternating-row">
            <div class="alt-text">
                <h3>A. RECURSOS NATURALES Y MEDIO AMBIENTE</h3>
                <div class="alt-line"></div>
                <p>Medidas de protección y conservación de recursos hídricos, bosques naturales, lugares turísticos, arqueológicos, redes de servicios de transporte, hotelería, gastronomía, artesanía, productores y organizaciones sociales potencialmente interesados en la transformación y en generar valor agregado a la producción con calidad para sus mercados.</p>
            </div>
            <div class="alt-image">
                <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&q=80&w=800" alt="Recursos Naturales">
            </div>
        </div>

        <div class="alternating-row reverse">
            <div class="alt-text">
                <h3>D. COMPRA - VENTA, ALQUILER, REPARACIÓN Y MANTENIMIENTO</h3>
                <div class="alt-line"></div>
                <p>Bienes muebles, inmuebles, maquinaria, equipos, software, hardware, vehículos, metales, materiales, insumos, herramientas, agregados, ropa industrial, accesorios, ferretería entre otros para la industria de la construcción, producción y comercialización en general.</p>
            </div>
            <div class="alt-image">
                <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&q=80&w=800" alt="Compra Venta">
            </div>
        </div>
    </div>
"""

# 4. CONTACTO
contacto_html = """
    <!-- TOP BANNER -->
    <div class="page-top-banner">
        <div class="banner-overlay"></div>
        <div class="banner-content">
            <h1>CONTACTO</h1>
            <p>Inicio &rightarrow; Contacto</p>
        </div>
    </div>

    <div class="page-container" style="background-color: var(--bg-beige);">
        <div class="contact-layout">
            <div class="contact-form">
                <h2 class="title-with-line" style="font-size: 28px;">CONTACTO</h2>
                <div class="title-line"></div>
                <p style="font-size:13px; margin-bottom:30px;">ANDINA puede apoyar con la gestión de recursos para financiamiento de proyectos de entidades nacionales e internacionales en las siguientes líneas de financiamiento: Estudios de pre inversión (perfiles y expedientes de proyectos).</p>
                
                <form>
                    <div class="form-row">
                        <div class="form-group">
                            <label>Nombres</label>
                            <input type="text">
                        </div>
                        <div class="form-group">
                            <label>Apellidos</label>
                            <input type="text">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label>E-mail</label>
                            <input type="email">
                        </div>
                        <div class="form-group">
                            <label>Telefono</label>
                            <input type="text">
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label>Mensaje</label>
                            <textarea rows="6"></textarea>
                        </div>
                    </div>
                    <button type="button" class="btn-submit">ENVIAR</button>
                </form>
            </div>

            <div class="contact-info">
                <div class="info-block">
                    <h4>REDES SOCIALES</h4>
                    <div style="display:flex; gap:10px;">
                        <div style="width:30px; height:30px; background:#1E5B2B; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center;">f</div>
                        <div style="width:30px; height:30px; background:#1E5B2B; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center;">t</div>
                        <div style="width:30px; height:30px; background:#1E5B2B; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center;">g</div>
                        <div style="width:30px; height:30px; background:#1E5B2B; color:white; border-radius:50%; display:flex; align-items:center; justify-content:center;">in</div>
                    </div>
                </div>

                <div class="info-block">
                    <h4>DIRECCIÓN</h4>
                    <p><span>📍</span> Jr. San Pablo 590 Ofc. 101. Urb. Casurco - Barr. San Sebastián - Cajamarca PERU</p>
                </div>

                <div class="info-block">
                    <h4>HORARIO DE ATENCIÓN</h4>
                    <p><span>🕒</span> Lunes - Viernes: 8:00am - 6:00pm<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sabado: 9:00am - 3:00pm<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Domingo: 10:00am - 2:00pm</p>
                </div>

                <div class="info-block">
                    <h4>TELEFONOS:</h4>
                    <p><span>📞</span> 076 280 361<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;RPM: #976765606 / RPC: 980-967317</p>
                </div>

                <div class="info-block">
                    <h4>E-MAIL:</h4>
                    <p><span>✉</span> info@andinacc.com</p>
                </div>
            </div>
        </div>
    </div>
"""

update_file('servicios.html', servicios_html)
update_file('nosotros.html', nosotros_html)
update_file('consultoria.html', consultoria_html)
update_file('contacto.html', contacto_html)

