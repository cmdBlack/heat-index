"""
Description: A script to automate generation of Heat Index Infographics
            
AUTHOR: KAIZER MACNI

"""


import os

from qgis.core import *
from PyQt5.QtWidgets import QApplication
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from qgis.PyQt.QtGui import (
    QPolygonF,
    QColor,
)

from qgis.PyQt.QtCore import (
    QPointF,
    QRectF,
    QSize,
)

from PyQt5.QtGui import QFont

from qgis.PyQt.QtXml import QDomDocument


from datetime import date
from datetime import datetime


#curr_time = input("TIME: hh:mm AM/PM ")
hi_laoag = input("Laoag HI: ")
hi_batac = input("Batac HI: ")
hi_sinait = input("Sinait HI: ")

now = datetime.now()

curr_time = now.strftime("%H:%M %p")




# Create a QgsTextFormat object
text_format1 = QgsTextFormat()
text_format2 = QgsTextFormat()
text_format3 = QgsTextFormat()
text_format4 = QgsTextFormat()
text_format5 = QgsTextFormat()
text_format6 = QgsTextFormat()
text_format7 = QgsTextFormat()
text_format8 = QgsTextFormat()


# Create a QFont object
font = QFont()
font.setFamily("Arial Black")  # Or any other font family you prefer
font.setBold(True)        # Set font to bold (optional)





###########################################################


app = QApplication([])
qgs = QgsApplication([], False)
#qgs.setPrefixPath("C:\\OSGeo4W\\apps\\qgis-ltr", True)
qgs.setPrefixPath("/Applications/QGIS-LTR.app/Contents/MacOS/bin", True) 



qgs.initQgis()

canvas = QgsMapCanvas()

project = QgsProject.instance()
bridge = QgsLayerTreeMapCanvasBridge(project.layerTreeRoot(), canvas)
project.read("/Users/kaizerjohnmacni/Downloads/hi/HI.qgz")




today = date.today()


#today = "2024-10-03"


project = QgsProject.instance()
            
manager = project.layoutManager()
layouts_list = manager.printLayouts()




layout = QgsPrintLayout(project)
layout.initializeDefaults()

        
document = QDomDocument()

# read template content
template_file = open("/Users/kaizerjohnmacni/Downloads/hi/HI-LAYOUT.qpt")


template_content = template_file.read()
template_file.close()
document.setContent(template_content)


# load layout from template and add to Layout Manager
layout.loadFromTemplate(document, QgsReadWriteContext()) 
project.layoutManager().addLayout(layout)

layout = QgsProject.instance().layoutManager().layoutByName("HI")

laoag_hi = layout.itemById("LAOAG_TEMP")
batac_hi = layout.itemById("BATAC_TEMP")
sinait_hi = layout.itemById("SINAIT_TEMP")
laoag_desc = layout.itemById("LAOAG_DESC")
batac_desc = layout.itemById("BATAC_DESC")
sinait_desc = layout.itemById("SINAIT_DESC")
time = layout.itemById("TIME")

laoag_hi.setText(str(hi_laoag) + "ºC")
batac_hi.setText(str(hi_batac) + "ºC")
sinait_hi.setText(str(hi_sinait) + "ºC")

#LAOAG
# Set the font color (e.g., caution)
text_format1.setColor(QColor(250, 214, 76))  # yellow color
text_format1.setSize(38)
text_format1.setFont(font)

# Set the font color (e.g., extreme caution)
text_format2.setColor(QColor(255, 186, 63))  # orange color
text_format2.setSize(38)
text_format2.setFont(font)

# Set the font color (e.g., danger)
text_format3.setColor(QColor(255, 138, 56))  # very orange color
text_format3.setSize(38)
text_format3.setFont(font)

# Set the font color (e.g., extreme danger)
text_format4.setColor(QColor(255, 68, 79))  # Red color
text_format4.setSize(38)
text_format4.setFont(font)

#BATAC-SINAIT
# Set the font color (e.g., caution)
text_format5.setColor(QColor(250, 214, 76))  # yellow color
text_format5.setSize(10)
text_format5.setFont(font)

# Set the font color (e.g., extreme caution)
text_format6.setColor(QColor(255, 186, 63))  # orange color
text_format6.setSize(10)
text_format6.setFont(font)

# Set the font color (e.g., danger)
text_format7.setColor(QColor(255, 138, 56))  # very orange color
text_format7.setSize(10)
text_format7.setFont(font)

# Set the font color (e.g., extreme danger)
text_format8.setColor(QColor(255, 68, 79))  # Red color
text_format8.setSize(10)
text_format8.setFont(font)

# Set the text format of the label item 1-4
if 26 < int(hi_laoag) < 33:
    laoag_hi.setTextFormat(text_format1)
    laoag_desc.setText("CAUTION")
    laoag_desc.setFontColor(QColor(250, 214, 76))
elif 32 < int(hi_laoag) < 42:
    laoag_hi.setTextFormat(text_format2)
    laoag_desc.setText("EXTREME CAUTION")
    laoag_desc.setFontColor(QColor(255, 186, 63))
elif 41 < int(hi_laoag) < 52:
    laoag_hi.setTextFormat(text_format3)
    laoag_desc.setText("DANGER")
    laoag_desc.setFontColor(QColor(255, 138, 56))
elif int(hi_laoag) > 51:
    laoag_hi.setTextFormat(text_format4)
    laoag_desc.setText("EXTREME DANGER")
    laoag_desc.setFontColor(QColor(255, 68, 79))
else:
    laoag_hi.setTextFormat(text_format1)
    laoag_desc.setText("CAUTION")
    laoag_desc.setFontColor(QColor(250, 214, 76))


# Set the text format of the label item 5-8
if 26 < int(hi_batac) < 33:
    batac_hi.setTextFormat(text_format5)
    batac_desc.setText("CAUTION")
    batac_desc.setFontColor(QColor(250, 214, 76))
elif 32 < int(hi_batac) < 42:
    batac_hi.setTextFormat(text_format6)
    batac_desc.setText("EXTREME CAUTION")
    batac_desc.setFontColor(QColor(255, 186, 63))
elif 41 < int(hi_batac) < 52:
    batac_hi.setTextFormat(text_format7)
    batac_desc.setText("DANGER")
    batac_desc.setFontColor(QColor(255, 138, 56))
elif int(hi_batac) > 51:
    batac_hi.setTextFormat(text_format8)
    batac_desc.setText("EXTREME DANGER")
    batac_desc.setFontColor(QColor(255, 68, 79))
else:
    batac_hi.setTextFormat(text_format5)
    batac_desc.setText("CAUTION")
    batac_desc.setFontColor(QColor(250, 214, 76))
    
if 26 < int(hi_sinait) < 33:
    sinait_hi.setTextFormat(text_format5)
    sinait_desc.setText("CAUTION")
    sinait_desc.setFontColor(QColor(250, 214, 76))
elif 32 < int(hi_sinait) < 42:
    sinait_hi.setTextFormat(text_format6)
    sinait_desc.setText("EXTREME CAUTION")
    sinait_desc.setFontColor(QColor(255, 186, 63))
elif 41 < int(hi_sinait) < 52:
    sinait_hi.setTextFormat(text_format7)
    sinait_desc.setText("DANGER")
    sinait_desc.setFontColor(QColor(255, 138, 56))
elif int(hi_sinait) > 51:
    sinait_hi.setTextFormat(text_format8)
    sinait_desc.setText("EXTREME DANGER")
    sinait_desc.setFontColor(QColor(255, 68, 79))
else:
    sinait_hi.setTextFormat(text_format5)
    sinait_desc.setText("CAUTION")
    sinait_desc.setFontColor(QColor(250, 214, 76))


#laoag_hi.setFontColor(QColor(255, 255, 0))

time.setText(str(curr_time[0:3]) + "00" + " " + str(curr_time[-2:])  + " -")

#base_path = os.path.join()
png_path = os.path.join("/Users/kaizerjohnmacni/Downloads/hi/png", str(today) + " " +   curr_time + ".png")



exporter = QgsLayoutExporter(layout)
exporter.exportToImage(png_path, QgsLayoutExporter.ImageExportSettings())
print("done")


"""
Caution
fad64c 27-32

if(rr_lagayan == "*"):     
    lagayan_rain = n_rains    
elif rr_lagayan == 0:
    lagayan_rain = n_rains
elif rr_lagayan < 61:
    lagayan_rain = l_rains
elif 26 < rr_lagayan < 33:
    lagayan_rain = m_rains
elif rr_lagayan > 180:
    lagayan_rain = h_rains

Extreme caution
#ffba3f 33-41

Danger
ff8a38 42-51

Extreme danger
#ff444f > 52
"""










