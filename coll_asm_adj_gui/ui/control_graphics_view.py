from PySide2.QtWidgets import QGraphicsView, QGraphicsScene
from PySide2.QtCore import Qt, QPoint


class ControlGraphicsView(QGraphicsView):

    def __init__(self, parent=None):
        super(ControlGraphicsView, self).__init__()
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setAcceptDrops(True)
        self.__zoom = 5

    def wheelEvent(self, event):
        if event.delta() > 0 and self.__zoom >= 10:
            return
        elif event.delta() < 0 and self.__zoom <= 0:
            return
        else:
            cur_point = event.position()
            scene_pos = self.mapToScene(QPoint(cur_point.x(), cur_point.y()))

            view_width = self.viewport().width()
            view_height = self.viewport().height()

            h_scale = cur_point.x() / view_width
            v_scale = cur_point.y() / view_height

            if event.delta() > 0:
                self.scale(1.25, 1.25)
                self.__zoom += 1
            else:
                self.scale(0.8, 0.8)
                self.__zoom -= 1
            view_point = self.transform().map(scene_pos)
            self.horizontalScrollBar().setValue(int(view_point.x() - view_width * h_scale))
            self.verticalScrollBar().setValue(int(view_point.y() - view_height * v_scale))

            self.update()


class ControlGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(ControlGraphicsScene, self).__init__()

        self.__left_click = False
        self.__point = QPoint(0, 0)
        self.__start_pos = None
        self.__end_pos = None

    def mouseMoveEvent(self, e):
        if self.__left_click:
            self.__end_pos = e.pos() - self.__start_pos
            self.__point = self.__point + self.__end_pos
            self.__start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__left_click = True
            self.__start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.__left_click = False
