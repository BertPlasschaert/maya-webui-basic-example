from PySide2 import QtCore, QtWidgets, QtWebEngineWidgets, QtWebChannel
import json
import os
from pathlib import Path
from typing import List

from maya import cmds
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance

SOURCE_FOLDER = Path(r"\Users\bertp\Desktop\maya-webui-basic-example")


class Backend(QtCore.QObject):
    @QtCore.Slot(int)
    def openAsset(self, asset_id: int) -> None:
        print(f"open Asset id: {asset_id}")

        sg_asset = get_asset_from_id(asset_id)
        cmds.file(
            sg_asset.get("latestVersionPath"),
            open=True,
        )

    @QtCore.Slot(int)
    def importAsset(self, asset_id: int) -> None:
        print(f"import Asset id: {asset_id}")

        sg_asset = get_asset_from_id(asset_id)
        cmds.file(
            sg_asset.get("latestVersionPath"),
            i=True,
        )

    @QtCore.Slot(int)
    def referenceAsset(self, asset_id: int) -> None:
        print(f"reference Asset id: {asset_id}")

        sg_asset = get_asset_from_id(asset_id)
        cmds.file(
            sg_asset.get("latestVersionPath"),
            reference=True,
        )

    @QtCore.Slot(result=str)
    def getAssetList(self) -> str:
        asset_list = get_all_assets()
        return json.dumps(asset_list)


class MayaBrowser(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MayaBrowser, self).__init__(parent)

        # NOTE: backend and channel MUST be a class or global variables
        self.backend = Backend()
        self.channel = QtWebChannel.QWebChannel()
        self.channel.registerObject("backend", self.backend)

        view = QtWebEngineWidgets.QWebEngineView()
        view.page().setWebChannel(self.channel)
        filepath = Path.joinpath(SOURCE_FOLDER, "static/index.html")
        url = QtCore.QUrl.fromLocalFile(str(filepath))
        view.load(url)
        self.setCentralWidget(view)

        # NOTE: this fully stops the instance from running after the window is closed
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


def get_asset_from_id(asset_id: int) -> dict:
    # your shotgrid api connection here
    return dict(
        id=1,
        name="asset01",
        thumbnailPath=r"images\thumbnail.png",
        latestVersionPath=Path.joinpath(SOURCE_FOLDER, "assets/example_asset.ma"),
        latestVersionNumber=1,
        lastEditedDate="08-03-1999",
        status="apr",
    )


def get_all_assets() -> List[dict]:
    # your shotgrid api connection here
    return [
        dict(
            id=1,
            name="asset01",
            thumbnailPath=r"images\thumbnail.png",
            latestVersionPath=os.path.join(SOURCE_FOLDER, "assets/example_asset.ma"),
            latestVersionNumber=1,
            lastEditedDate="14-03-2019",
            status="apr",
        ),
        dict(
            id=2,
            name="asset02",
            thumbnailPath=r"images\thumbnail.png",
            latestVersionPath=os.path.join(SOURCE_FOLDER, "assets/example_asset.ma"),
            latestVersionNumber=1,
            lastEditedDate="14-03-2019",
            status="ip",
        ),
        dict(
            id=3,
            name="asset03",
            thumbnailPath=r"images\thumbnail.png",
            latestVersionPath=os.path.join(SOURCE_FOLDER, "assets/example_asset.ma"),
            latestVersionNumber=1,
            lastEditedDate="14-03-2019",
            status="ip",
        ),
        dict(
            id=4,
            name="asset04",
            thumbnailPath=r"images\thumbnail.png",
            latestVersionPath=os.path.join(SOURCE_FOLDER, "assets/example_asset.ma"),
            latestVersionNumber=1,
            lastEditedDate="14-03-2019",
            status="ip",
        ),
        dict(
            id=5,
            name="asset05",
            thumbnailPath=r"images\thumbnail.png",
            latestVersionPath=os.path.join(SOURCE_FOLDER, "assets/example_asset.ma"),
            latestVersionNumber=1,
            lastEditedDate="14-03-2019",
            status="ip",
        ),
    ]


def get_maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)


if __name__ == "__main__":
    app = get_maya_main_window()
    browser = MayaBrowser(parent=app)
    browser.show()
