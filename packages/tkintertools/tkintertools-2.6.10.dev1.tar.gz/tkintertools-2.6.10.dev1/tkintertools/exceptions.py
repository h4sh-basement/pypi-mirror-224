""" All exceptions """


class ScaleArgsValueError(ValueError):
    """ 缩放函数参数值错误 """

    def __init__(self, value):  # type: (float) -> None
        self.value = value

    def __str__(self):  # type: () -> None
        return f'The scaling factor should be a positive floating-point number, not {self.value}'


class ColorArgsValueError(ValueError):
    """ 颜色函数参数值错误 """

    def __init__(self, value):  # type: (float) -> None
        self.value = value

    def __str__(self):  # type: () -> None
        return f'The parameter proportion should be a floating-point number between 0~1, not {self.value}'


class WidgetStateModeError(ValueError):
    """ 控件状态模式错误 """

    def __init__(self, value):  # type: (str) -> None
        self.value = value

    def __str__(self):  # type: () -> None
        return f'The mode can only be "normal", "touch", "click" or "disabled", not "{self.value}"'
