from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.core import (
    QgsApplication,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingMultiStepFeedback,
    QgsProcessingParameterCrs,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterFeatureSink,
    QgsProcessingProvider
)
from qgis import processing
import os


# =========================
# 🔹 YOUR ORIGINAL LOGIC
# =========================
class CenterCentroidOfALineString(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterCrs(
            'CRSforcalculationandexport',
            'CRS for calculation and export',
            defaultValue='EPSG:3035'
        ))

        self.addParameter(QgsProcessingParameterFeatureSource(
            'Linestring',
            'Linestring',
            types=[QgsProcessing.TypeVectorLine]
        ))

        self.addParameter(QgsProcessingParameterFeatureSink(
            'R_centroidForLinestring',
            'R_Centroid for linestring'
        ))

    def processAlgorithm(self, parameters, context, model_feedback):
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Fix geometries
        outputs['FixGeometries'] = processing.run(
            'native:fixgeometries',
            {
                'INPUT': parameters['Linestring'],
                'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True
        )

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Reproject layer
        outputs['ReprojectLayer'] = processing.run(
            'native:reprojectlayer',
            {
                'INPUT': outputs['FixGeometries']['OUTPUT'],
                'TARGET_CRS': parameters['CRSforcalculationandexport'],
                'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True
        )

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Geometry by expression
        outputs['GeometryByExpression'] = processing.run(
            'native:geometrybyexpression',
            {
                'EXPRESSION': 'centroid(line_substring($geometry,$length/2,0))',
                'INPUT': outputs['ReprojectLayer']['OUTPUT'],
                'OUTPUT_GEOMETRY': 2,
                'OUTPUT': parameters['R_centroidForLinestring']
            },
            context=context,
            feedback=feedback,
            is_child_algorithm=True
        )

        results['R_centroidForLinestring'] = outputs['GeometryByExpression']['OUTPUT']
        return results

    def name(self):
        return 'center_point_on_line'

    def displayName(self):
        return 'Center Point on Line'

    def group(self):
        return 'Center Point Tools'

    def groupId(self):
        return 'center_point_tools'

    def createInstance(self):
        return CenterCentroidOfALineString()


# =========================
# 🔹 PROCESSING PROVIDER
# =========================
class CenterPointProvider(QgsProcessingProvider):

    def loadAlgorithms(self):
        self.addAlgorithm(CenterCentroidOfALineString())

    def id(self):
        return "center_point_provider"

    def name(self):
        return "Center Point Tools"

    def longName(self):
        return self.name()


# =========================
# 🔹 PLUGIN CLASS
# =========================
class CenterPointOnLinePlugin:

    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.provider = None

    def initGui(self):
        # Prevent duplicate menu/icon
        self.unload()

        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')

        self.action = QAction(
            QIcon(icon_path),
            "Center Point on Line",
            self.iface.mainWindow()
        )
        self.action.triggered.connect(self.run)

        self.iface.addPluginToMenu("&Center Point on Line", self.action)
        self.iface.addToolBarIcon(self.action)

        # Register provider
        self.provider = CenterPointProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def unload(self):
        # Remove menu & toolbar safely
        if self.action:
            try:
                self.iface.removePluginMenu("&Center Point on Line", self.action)
                self.iface.removeToolBarIcon(self.action)
            except:
                pass

        # Remove provider safely
        if self.provider:
            try:
                QgsApplication.processingRegistry().removeProvider(self.provider)
            except:
                pass

    def run(self):
        # Open processing tool directly
        processing.execAlgorithmDialog("center_point_provider:center_point_on_line")