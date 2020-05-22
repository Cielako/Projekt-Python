from fpdf import FPDF
from Modules.is_online import is_online
from Modules.iplook import iplook
from Modules.portscanner import portscanner
from Modules.geolocation import geolocation
from Modules.domain_info import domain_info
import os

def pdfcreate(target):
    if os.path.exists("temp.pdf"):
        os.remove("temp.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu',fname='Fonts\DejaVuSansCondensed.ttf',uni= True)
    pdf.add_font('DejaVuB',fname='Fonts\DejaVuSans-Bold.ttf',uni= True)
    
    pdf.set_font("DejaVuB",size=14)
    pdf.cell(200,10, txt="Osiągalność witryny",ln=2,align="C")
    pdf.set_font("DejaVu",size=12)
    pdf.cell(200,10, txt=is_online(target),ln=2,align="C")# Moduł is_online
    
    pdf.set_font("DejaVuB",size=14)
    pdf.cell(200,10, txt="Trasa do adresu docelowego:",ln=2,align="C")
    pdf.set_font("DejaVu", size=12)
    ip = iplook(target) # Moduł iplook
    for r in range(len(ip)):
        pdf.cell(200, 10, txt=str(f"{r+1}: " + ip[r]), ln=2, align="C")
        
    pdf.set_font("DejaVuB",size=14)
    pdf.cell(200,10, txt="Odblokowane porty:",ln=2,align="C")
    pdf.set_font("DejaVu", size=12)
    if len(portscanner(target)) == 0: # Jeśli żaden port nie jest otwarty zwróć komunikat
         pdf.cell(200,10, txt="Brak otwartych portów :(",ln=2,align="C")# Moduł portscanner
    else:
        for x in portscanner(target):
            pdf.cell(200,10, txt=x,ln=2,align="C")
            
    pdf.set_font("DejaVuB",size=14)
    pdf.cell(200,10, txt="Informacje geolokalizacyjne o witrynie:",ln=2,align="C")
    pdf.set_font("DejaVu", size=12)
    for x,y in zip(geolocation(target).keys(),geolocation(target).values()):# Moduł geolocation
        pdf.cell(200,10, txt=str(f"{x} : {y}"),ln=2,align="C")
        
    pdf.set_font("DejaVuB",size=14)
    pdf.cell(200,10, txt="Informacje o domenie :",ln=2,align="C")
    pdf.set_font("DejaVu", size=12)
    for x,y in zip(domain_info(target).keys(),domain_info(target).values()):# Moduł domain_info
        pdf.cell(200,10, txt=str(f"{x} : {y}"),ln=2,align="C")
    pdf.output("temp.pdf")
    pdf.close()