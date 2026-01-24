from PySide6.QtWidgets import QGraphicsView, QLineEdit, QGraphicsPixmapItem
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter


class ControlGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # 以鼠标为中心缩放
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)

        self.setDragMode(QGraphicsView.NoDrag)

        self._dragging = False
        self._last_scene_pos: QPointF | None = None
        self._drag_item = None  # 当前拖动的 item

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(1.25, 1.25)
        else:
            self.scale(0.8, 0.8)
        event.accept()

    def _pick_pixmap_item(self, event):
        """优先取鼠标下的 pixmap item；否则取 scene 里第一个 pixmap item。"""
        item = self.itemAt(event.position().toPoint())
        if isinstance(item, QGraphicsPixmapItem):
            return item

        sc = self.scene()
        if sc is None:
            return None
        for it in sc.items():  # z-order 从上到下
            if isinstance(it, QGraphicsPixmapItem):
                return it
        return None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_item = self._pick_pixmap_item(event)
            if self._drag_item is not None:
                self._dragging = True
                self._last_scene_pos = self.mapToScene(event.position().toPoint())
                self.setCursor(Qt.ClosedHandCursor)
                event.accept()
                return
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._dragging and self._drag_item is not None and self._last_scene_pos is not None:
            cur = self.mapToScene(event.position().toPoint())
            delta = cur - self._last_scene_pos
            self._last_scene_pos = cur

            # 直接移动画布 pixmap（跟手、与缩放无关）
            self._drag_item.setPos(self._drag_item.pos() + delta)

            event.accept()
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._dragging:
            self._dragging = False
            self._last_scene_pos = None
            self._drag_item = None
            self.setCursor(Qt.ArrowCursor)
            event.accept()
            return
        super().mouseReleaseEvent(event)


class DragLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(DragLineEdit, self).__init__(parent)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            self.setText(event.mimeData().urls()[0].toLocalFile())
            event.accept()
        else:
            event.ignore()
