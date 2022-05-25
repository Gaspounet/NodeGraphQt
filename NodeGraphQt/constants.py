#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from Qt import QtWidgets
from enum import Enum

from .pkg_info import __version__

__doc__ = """
| The ``NodeGraphQt.constants`` namespace contains variables used throughout 
 the whole NodeGraphQt library.
"""

# =================================== GLOBAL ===================================

#: current version.
VERSION = __version__
#: major version.
VERSION_MAJOR = int(VERSION.split('.')[0])
#: minor version.
VERSION_MINOR = int(VERSION.split('.')[1])
#: patch version.
VERSION_PATCH = int(VERSION.split('.')[2])

# ==================================== PIPE ====================================


class PIPE_STYLING(Enum):
    """
    Pipe styling layout:
    ``NodeGraphQt.constants.PIPE_STYLING``
    """
    #: default width.
    WIDTH = 1.2
    #: default color.
    COLOR = (175, 95, 30, 255)
    #: pipe color to a node when it's disabled.
    DISABLED_COLOR = (190, 20, 20, 255)
    #: pipe color when selected or mouse over.
    ACTIVE_COLOR = (70, 255, 220, 255)
    #: pipe color to a node when it's selected.
    HIGHLIGHT_COLOR = (232, 184, 13, 255)
    #: draw connection as a line.
    DRAW_TYPE_DEFAULT = 0
    #: draw connection as dashed lines.
    DRAW_TYPE_DASHED = 1
    #: draw connection as a dotted line.
    DRAW_TYPE_DOTTED = 2


class PIPE_SLICER_STYLING(Enum):
    """
    Slicer Pipe styling layout:
    ``NodeGraphQt.constants.PIPE_SLICER_STYLING``
    """
    #: default width.
    WIDTH = 1.5
    #: default color.
    COLOR = (255, 50, 75)


class PIPE_LAYOUT(Enum):
    """
    Pipe connection drawing layout:
    ``NodeGraphQt.constants.PIPE_LAYOUT``
    """
    #: draw straight lines for pipe connections.
    STRAIGHT = 0
    #: draw curved lines for pipe connections.
    CURVED = 1
    #: draw angled lines for pipe connections.
    ANGLE = 2

# ==================================== PORT ====================================


class PORT_STYLING(Enum):
    """
    Port styling layout:
    ``NodeGraphQt.constants.PORT_STYLING``
    """
    #: default port size.
    SIZE = 22.0
    #: default port color. (r, g, b, a)
    COLOR = (49, 115, 100, 255)
    #: default port border color.
    BORDER_COLOR = (29, 202, 151, 255)
    #: port color when selected.
    ACTIVE_COLOR = (14, 45, 59, 255)
    #: port border color when selected.
    ACTIVE_BORDER_COLOR = (107, 166, 193, 255)
    #: port color on mouse over.
    HOVER_COLOR = (17, 43, 82, 255)
    #: port border color on mouse over.
    HOVER_BORDER_COLOR = (136, 255, 35, 255)
    #: threshold for selecting a port.
    CLICK_FALLOFF = 15.0


class PORT_TYPE(Enum):
    """
    Port connection types:
    ``NodeGraphQt.constants.PORT_TYPE``
    """
    #: Connection type for input ports.
    IN = 'in'
    #: Connection type for output ports.
    OUT = 'out'


# ==================================== NODE ====================================

NODE_WIDTH = 160
NODE_HEIGHT = 60
NODE_ICON_SIZE = 18
NODE_SEL_COLOR = (255, 255, 255, 30)
NODE_SEL_BORDER_COLOR = (254, 207, 42, 255)

# === NODE PROPERTY ===

#: Property type will hidden in the properties bin (default).
NODE_PROP = 0
#: Property type represented with a QLabel widget in the properties bin.
NODE_PROP_QLABEL = 2
#: Property type represented with a QLineEdit widget in the properties bin.
NODE_PROP_QLINEEDIT = 3
#: Property type represented with a QTextEdit widget in the properties bin.
NODE_PROP_QTEXTEDIT = 4
#: Property type represented with a QComboBox widget in the properties bin.
NODE_PROP_QCOMBO = 5
#: Property type represented with a QCheckBox widget in the properties bin.
NODE_PROP_QCHECKBOX = 6
#: Property type represented with a QSpinBox widget in the properties bin.
NODE_PROP_QSPINBOX = 7
#: Property type represented with a ColorPicker widget in the properties bin.
NODE_PROP_COLORPICKER = 8
#: Property type represented with a Slider widget in the properties bin.
NODE_PROP_SLIDER = 9
#: Property type represented with a file selector widget in the properties bin.
NODE_PROP_FILE = 10
#: Property type represented with a file save widget in the properties bin.
NODE_PROP_FILE_SAVE = 11
#: Property type represented with a vector2 widget in the properties bin.
NODE_PROP_VECTOR2 = 12
#: Property type represented with vector3 widget in the properties bin.
NODE_PROP_VECTOR3 = 13
#: Property type represented with vector4 widget in the properties bin.
NODE_PROP_VECTOR4 = 14
#: Property type represented with float widget in the properties bin.
NODE_PROP_FLOAT = 15
#: Property type represented with int widget in the properties bin.
NODE_PROP_INT = 16
#: Property type represented with button widget in the properties bin.
NODE_PROP_BUTTON = 17

# === NODE VIEWER ===

#: Style to render the node graph background with nothing.
VIEWER_GRID_NONE = 0
#: Style to render the node graph background with dots.
VIEWER_GRID_DOTS = 1
#: Style to render the node graph background with grid lines.
VIEWER_GRID_LINES = 2

VIEWER_NAV_BG_COLOR = (25, 25, 25)
VIEWER_NAV_ITEM_COLOR = (35, 35, 35)
VIEWER_BG_COLOR = (35, 35, 35)
VIEWER_GRID_COLOR = (45, 45, 45)
VIEWER_GRID_SIZE = 50

# ================================== PRIVATE ===================================

URI_SCHEME = 'nodegraphqt://'
URN_SCHEME = 'nodegraphqt::'

# === PATHS ===

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_PATH, 'widgets', 'icons')
ICON_DOWN_ARROW = os.path.join(ICON_PATH, 'down_arrow.png')
ICON_NODE_BASE = os.path.join(ICON_PATH, 'node_base.png')

# === DRAW STACK ORDER ===

Z_VAL_PIPE = -1
Z_VAL_NODE = 1
Z_VAL_PORT = 2
Z_VAL_NODE_WIDGET = 3

# === ITEM CACHE MODE ===

# QGraphicsItem.NoCache
# QGraphicsItem.DeviceCoordinateCache
# QGraphicsItem.ItemCoordinateCache

ITEM_CACHE_MODE = QtWidgets.QGraphicsItem.DeviceCoordinateCache

# === NODE LAYOUT DIRECTION ===

#: Mode for vertical node layout.
NODE_LAYOUT_VERTICAL = 0
#: Mode for horizontal node layout.
NODE_LAYOUT_HORIZONTAL = 1
#: Variable for setting the node layout direction.
# NODE_LAYOUT_DIRECTION = NODE_LAYOUT_VERTICAL
NODE_LAYOUT_DIRECTION = NODE_LAYOUT_HORIZONTAL
