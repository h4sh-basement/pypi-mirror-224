import argparse
import sys
import os
from metabolabpy.nmr import nmrDataSet  # pragma: no cover
from metabolabpy.nmr import nmrConfig
import inspect
import darkdetect
from qtmetabolabpy import *
from qtmetabolabpy import qtMetaboLabPy
import time
from time import sleep  # pragma: no cover
try:
    from PySide2.QtWidgets import *  # pragma: no cover
    from PySide2 import QtCore  # pragma: no cover
    from PySide2.QtGui import QIcon  # pragma: no cover
    import qtmodern.styles  # pragma: no cover
    from PySide2.QtGui import QPixmap
except:
    pass


def main():  # pragma: no cover
    sys.argv.append('None')
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--script", required=False, help="optional script argument")
    ap.add_argument("-ns", "--noSplash", required=False, help="turn splash screen off", action="store_true")
    ap.add_argument("-fs", "--FullScreen", required=False, help="open applicatin in full screen mode",
                    action="store_true")
    ap.add_argument("-k", "--KioskMode", required=False,
                    help="open application in full screen mode without windowed mode available",
                    action="store_true")
    ap.add_argument("fileName", metavar="fileName", type=str, help="load MetaboLabPy DataSet File")
    dd = ap.parse_known_args()
    # dd = ap.parse_known_intermixed_args()
    if len(dd[1]) > 0:
        sys.argv.pop()

    args = vars(ap.parse_args())
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    nmr_dir = os.path.split(inspect.getmodule(nmrDataSet).__file__)[0]
    base_dir = os.path.split(nmr_dir)[0]
    app = QApplication(['MetaboLabPy'])
    icon = QIcon()
    p_name = os.path.join(base_dir, "icon")
    icon.addFile(os.path.join(p_name, "icon-16.png"), QtCore.QSize(16, 16))
    icon.addFile(os.path.join(p_name, "icon-24.png"), QtCore.QSize(24, 24))
    icon.addFile(os.path.join(p_name, "icon-32.png"), QtCore.QSize(32, 32))
    icon.addFile(os.path.join(p_name, "icon-48.png"), QtCore.QSize(48, 48))
    icon.addFile(os.path.join(p_name, "icon-256.png"), QtCore.QSize(256, 256))
    app.setWindowIcon(icon)
    app.setApplicationDisplayName("MetaboLabPy")
    w = qtMetaboLabPy.QtMetaboLabPy()
    if args["FullScreen"] == True or args["KioskMode"] == True:
        w.w.showFullScreen()

    if args["KioskMode"] == True:
        w.w.actionToggle_FullScreen.triggered.disconnect()

    if args["noSplash"] == False:
        ##
        # Create and display the splash screen
        nmr_dir = os.path.split(inspect.getmodule(nmrDataSet).__file__)[0]
        base_dir = os.path.split(nmr_dir)[0]
        p_name = os.path.join(base_dir, "png")
        cf = nmrConfig.NmrConfig()
        cf.read_config()
        if cf.mode == 'dark' or (cf.mode == 'system' and darkdetect.isDark()):
            splash_pix = QPixmap(os.path.join(p_name, "metabolabpy_dark.png"))
        else:
            splash_pix = QPixmap(os.path.join(p_name, "metabolabpy.png"))

        splash = QSplashScreen(splash_pix)
        splash.setMask(splash_pix.mask())
        # adding progress bar
        splash.show()
        app.processEvents()
        max_time = 2
        max_range = 30
        time_inc = max_range
        for i in range(max_range):
            # Simulate something that takes time
            time.sleep(max_time / float(max_range))

        splash.close()
        ## End of splash screen

    if args["fileName"] != "None":
        try:
            w.load_file(args["fileName"])
        except:
            if (args["script"] != None):
                w.open_script(args["script"])
                w.script_editor()
                w.exec_script()

    else:
        if (args["script"] != None):
            w.open_script(args["script"])
            w.script_editor()
            w.exec_script()

    if cf.mode == 'system':
        if darkdetect.isDark():
            qtmodern.styles.dark(app)
        else:
            qtmodern.styles.light(app)
    elif cf.mode == 'light':
        qtmodern.styles.light(app)
    else:
        qtmodern.styles.dark(app)

    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()
    w_width = 1600 #w.w.size().width()
    w_height = w.w.size().height()
    ww = min(w_width, screen_width)
    wh = min(w_height, screen_height)
    w.show()
    if ww < 1300:
        w.w.showNormal()
        w.w.move(0, 0)

    app.processEvents()
    if w_width > screen_width:
        w.w.setMaximumWidth(screen_width)
        app.processEvents()

    if w_height > screen_height:
        w.w.setMaximumWidth(screen_height)
        app.processEvents()

    w.w.resize(ww, wh)
    app.processEvents()
    w.w.updateGeometry()
    app.processEvents()
    #print("update2")
    #print(dir(app))
    sys.exit(app.exec_())


if __name__ == "__main__":  # pragma: no cover
    main()
