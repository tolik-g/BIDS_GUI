from PyQt5.QtWidgets import QFrame


class HLine(QFrame):
    """
    Horizontal line
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)


class VLine(QFrame):
    """
    Vertical line
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setLineWidth(1)
        self.setMidLineWidth(0)
