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


from datetime import date, datetime

#curr_time = input("TIME: hh:mm AM/PM ")
hi_laoag = input("Laoag HI: ")
hi_batac = input("Batac HI: ")
hi_sinait = input("Sinait HI: ")


now = datetime.now()

curr_time = now.strftime("%I:%M %p") 

# Create a QgsTextFormat object
text_format = QgsTextFormat()

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

laoag_hi.setText(hi_laoag + "ºC")
batac_hi.setText(hi_batac + "ºC")
sinait_hi.setText(hi_sinait + "ºC")


def format_text(val, loc, desc=0):
    #TODO
    text_format.setFont(font)
    if 26 < val < 33:
        text_format.setColor(QColor(250, 214, 76))  # yellow color
        if loc == "sinait":
            sinait_desc.setText("CAUTION")
        elif loc == "batac":
            batac_desc.setText("CAUTION")
        else:
            laoag_desc.setText("CAUTION")
    elif 32 < val < 42:
        text_format.setColor(QColor(255, 186, 63))  # orange color
        if loc == "sinait":
            sinait_desc.setText("EXTREME CAUTION")
        elif loc == "batac":
            batac_desc.setText("EXTREME CAUTION")
        else:
            laoag_desc.setText("EXTREME CAUTION")
    elif 41 < val < 52:
        text_format.setColor(QColor(255, 138, 56))  # very orange color
        if loc == "sinait":
            sinait_desc.setText("DANGER")
        elif loc == "batac":
            batac_desc.setText("DANGER")
        else:
            laoag_desc.setText("DANGER")
    elif val > 51:
        text_format.setColor(QColor(255, 68, 79))  # Red color
        if loc == "sinait":
            sinait_desc.setText("EXTREME DANGER")
        elif loc == "batac":
            batac_desc.setText("EXTREME DANGER")
        else:
            laoag_desc.setText("EXTREME DANGER")
    else:
        text_format.setColor(QColor(250, 214, 76))  # yellow color
        if loc == "sinait":
            sinait_desc.setText("CAUTION")
        elif loc == "batac":
            batac_desc.setText("CAUTION")
        else:
            laoag_desc.setText("CAUTION")
    if desc == 0:    
        if loc == "laoag":
            text_format.setSize(38)
        else:
            text_format.setSize(10)
    else:
        if loc == "laoag":
            text_format.setSize(9.5)
        else:
            text_format.setSize(3.5)       
    
 
format_text(int(hi_laoag), "laoag")
laoag_hi.setTextFormat(text_format)
format_text(int(hi_laoag), "laoag", 1)
laoag_desc.setTextFormat(text_format)

format_text(int(hi_batac), "batac")
batac_hi.setTextFormat(text_format)
format_text(int(hi_batac), "batac", 1)
batac_desc.setTextFormat(text_format)

format_text(int(hi_sinait), "sinait")
sinait_hi.setTextFormat(text_format)
format_text(int(hi_sinait), "sinait", 1)
sinait_desc.setTextFormat(text_format)


time.setText(curr_time[0:3] + "00" + " " + curr_time[-2:]  + " -")

#base_path = os.path.join()
png_path = os.path.join("/Users/kaizerjohnmacni/Downloads/hi/png", str(today) + " " + curr_time[0:2] +  " " + curr_time[-2:] + ".png")

exporter = QgsLayoutExporter(layout)
exporter.exportToImage(png_path, QgsLayoutExporter.ImageExportSettings())
print("done")

