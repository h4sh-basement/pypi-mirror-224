""" 3D support """

import math  # 数学支持
import statistics  # 数据统计
from tkinter import Event  # 类型提示
from typing import Iterable, overload  # 类型提示

from .__main__ import Canvas, Tk, Toplevel  # 继承和类型提示
from .constants import *  # 常量


class Canvas_3D(Canvas):
    """ 3D 画布基类 """

    def __init__(
        self,
        master,  # type: Tk | Toplevel
        width,  # type: int
        height,  # type: int
        x=None,  # type: int | None
        y=None,  # type: int | None
        *,
        lock=True,  # type: bool
        expand=True,  # type: bool
        keep=True,  # type: bool
        camera_distance=CAMERA_DISTANCE,  # type: float
        **kw
    ):  # type: (...) -> None
        """
        `master`: 父控件 \ 
        `width`: 画布宽度 \ 
        `height`: 画布高度 \ 
        `x`: 画布左上角的横坐标 \ 
        `y`: 画布左上角的纵坐标 \ 
        `lock`: 画布内控件的功能锁，为 False 时功能暂时失效 \ 
        `expand`: 画布内控件是否能缩放 \ 
        `keep`: 画布比例是否保持不变 \ 
        `camera_distance`: 相机位置与原点间的距离，默认值为 1000 \ 
        `**kw`: 与 tkinter.Canvas 类的参数相同
        """
        Canvas.__init__(
            self, master, width, height, x, y, lock=lock, expand=expand, keep=keep, **kw)
        self.distance = camera_distance
        self._items_3d = []  # type: list[Point | Line | Side]
        self._geos = []  # type: list[Geometry]
        self._zoom()  # 更新画布视野

    def _zoom(self, rate_x=None, rate_y=None):  # type: (float | None, float | None) -> None
        # override: 保持画布视野居中
        Canvas._zoom(self, rate_x, rate_y)
        half_width, half_height = self.width[1] / 2, self.height[1] / 2
        self.configure(
            scrollregion=(-half_width, -half_height, half_width, half_height))

    def items_3d(self):  # type: () -> tuple[Point | Line | Side]
        """ 返回 `Canvas_3d` 类全部的基本 3D 对象 """
        return tuple(self._items_3d)

    def geos(self):  # type: () -> tuple[Geometry]
        """ 返回 `Canvas_3d` 类全部的几何体对象 """
        return tuple(self._geos)

    def space_sort(self):  # type: () -> None
        """ 空间位置排序 """  # BUG: 在距离比较近的两个对象时，仍会显示不正确
        self._items_3d.sort(key=lambda item: item._camera_distance())
        for item in self._items_3d:
            self.lower(item.item)


class Space(Canvas_3D):
    """ 三维空间 """

    def __init__(
        self,
        master,  # type: Tk | Toplevel
        width,  # type: int
        height,  # type: int
        x=None,  # type: int | None
        y=None,  # type: int | None
        *,
        lock=True,  # type: bool
        expand=True,  # type: bool
        keep=True,  # type: bool
        camera_distance=CAMERA_DISTANCE,  # type: float
        origin_size=ORIGIN_SIZE,  # type: float
        origin_width=ORIGIN_WIDTH,  # type: float
        origin_fill=ORIGIN_FILL,  # type: str
        origin_outline=ORIGIN_OUTLINE,  # type: str
        **kw
    ):  # type: (...) -> None
        """
        `master`: 父控件 \ 
        `width`: 画布宽度 \ 
        `height`: 画布高度 \ 
        `x`: 画布左上角的横坐标 \ 
        `y`: 画布左上角的纵坐标 \ 
        `lock`: 画布内控件的功能锁，为 False 时功能暂时失效 \ 
        `expand`: 画布内控件是否能缩放 \ 
        `keep`: 画布比例是否保持不变 \ 
        `camera_distance`: 相机位置与原点间的距离，默认值为 1000 \ 
        `origin_size`: 原点大小，默认值为 1 \ 
        `origin_width`: 原点轮廓宽度，默认值为 1 \ 
        `origin_fill`: 原点填充颜色，默认为无色 \ 
        `origin_outline`: 原点轮廓颜色，默认为无色 \ 
        `**kw`: 与 tkinter.Canvas 类的参数相同
        """
        Canvas_3D.__init__(
            self, master, width, height, x, y, lock=lock, expand=expand, keep=keep, camera_distance=camera_distance, **kw)
        self._origin = Point(
            self, ORIGIN_COORDINATE, size=origin_size, width=origin_width, fill=origin_fill, outline=origin_outline)
        self._items_3d.clear()
        self.bind('<B3-Motion>', self._translate)
        self.bind('<Button-3>', lambda _: self._translate(_, True))
        self.bind('<ButtonRelease-3>', lambda _: self._translate(_, False))
        self.bind('<B1-Motion>', self._rotate)
        self.bind('<Button-1>', lambda _: self._rotate(_, True))
        self.bind('<ButtonRelease-1>', lambda _: self._rotate(_, False))
        if SYSTEM == 'Linux':  # 兼容 Linux 系统
            self.bind('<Button-4>', lambda _: self._scale(_, True))
            self.bind('<Button-5>', lambda _: self._scale(_, False))
        else:
            self.bind('<MouseWheel>', self._scale)

    def _translate(self, event, flag=None, _cache=[]):
        # type: (Event, bool | None, list[float]) -> None
        """ 平移事件 """
        if flag is True:  # 按下
            _cache[:] = [event.x, event.y]
            return self.configure(cursor='fleur')
        elif flag is False:  # 松开
            return self.configure(cursor='arrow')
        dx, dy = event.x-_cache[0], event.y-_cache[1]
        _cache[:] = [event.x, event.y]
        for item in self._items_3d+[self._origin]:
            item.translate(
                0, dx*self.width[0]/self.width[1], dy*self.height[0]/self.height[1])
            item.update()
        self.space_sort()

    def _rotate(self, event, flag=None, _cache=[]):
        # type: (Event, bool | None, list[float]) -> None
        """ 旋转事件 """
        if flag is True:
            _cache[:] = [event.x, event.y]
            return self.configure(cursor='fleur')
        elif flag is False:
            return self.configure(cursor='arrow')
        dx, dy = event.x-_cache[0], event.y-_cache[1]
        _cache[:] = [event.x, event.y]
        for item in self._items_3d:
            item.rotate(0, -2*dy/self.width[1]*math.tau, 2*dx /
                        self.height[1]*math.tau, center=self._origin.coordinates[0])
            item.update()
        self.space_sort()

    def _scale(self, event, flag=None):  # type: (Event, bool | None) -> None
        """ 缩放事件 """
        if flag is not None:
            event.delta = flag
        k = 1.1 if event.delta > 0 else 0.9
        for item in self._items_3d:
            item.scale(k, k, k, center=self._origin.coordinates[0])
            item.update()
        self.space_sort()


def translate(coordinate, dx=0, dy=0, dz=0):
    # type: (list[float], float, float, float) -> None
    """
    ### 平移
    将一个三维空间中的点进行平移 \n
    ---
    `coordinate`: 点的空间坐标 \ 
    `dx`: x 方向位移长度 \ 
    `dy`: y 方向位移长度 \ 
    `dz`: z 方向位移长度
    """
    for i, delta in enumerate((dx, dy, dz)):
        coordinate[i] += delta


@overload
def rotate(coordinate, dx=0, dy=0, dz=0, *, center):
    # type: (list[float], float, float, float, ..., Iterable[float]) -> None
    ...


@overload
def rotate(coordinate, dx=0, *, axis):
    # type: (list[float], float,  ..., Iterable[Iterable[float]]) -> None
    ...


def rotate(coordinate, dx=0, dy=0, dz=0, *, center, axis=None):
    # type: (list[float], float, float, float, ..., Iterable[float], Iterable[Iterable[float]] | None) -> None
    """
    ### 旋转
    将一个三维空间中的点以一个点或线为参照进行旋转 \n
    ---
    `coordinate`: 点的空间坐标 \ 
    `dx`: x 方向旋转弧度，或者绕旋转轴线的旋转弧度 \ 
    `dy`: y 方向旋转弧度 \ 
    `dz`: z 方向旋转弧度 \ 
    `center`: 旋转中心的空间坐标 \ 
    `axis`: 旋转轴线的空间坐标
    """
    if axis is not None:  # 参照为线（定轴转动）
        center = _Line(*axis).center()  # 旋转轴中点
        n = list(axis[0])
        for i in range(3):
            n[i] -= axis[1][i]
            coordinate[i] -= center[i]
        n_m = math.hypot(*n)
        for i in range(3):
            n[i] /= n_m
        x_2, y_2, z_2 = map(lambda _: _**2, n)
        zx, xy, yz = [n[i-1]*v for i, v in enumerate(n)]
        s_θ, c_θ = math.sin(dx), math.cos(dx)
        _c_θ = 1 - c_θ

        matrix = [[x_2*_c_θ + c_θ, xy*_c_θ + n[2]*s_θ, zx*_c_θ - n[1]*s_θ],
                  [xy*_c_θ - n[2]*s_θ, y_2*_c_θ + c_θ, yz*_c_θ + n[0]*s_θ],
                  [zx*_c_θ + n[1]*s_θ, yz*_c_θ - n[0]*s_θ, z_2*_c_θ + c_θ]]

        for i, δ in enumerate(center):
            matrix[i] = δ + sum(matrix[i][j]*coordinate[j] for j in range(3))

    else:  # 参照为点（定点转动）
        sx, sy, sz = math.sin(dx), math.sin(dy), math.sin(dz)
        cx, cy, cz = math.cos(dx), math.cos(dy), math.cos(dz)

        matrix = [[cz * cy, cz * sy * sx - sz * cx, cz * sy * cx + sz * sx],
                  [sz * cy, sz * sy * sx + cz * cx, sz * sy * cx - cz * sx],
                  [-sy,     cy * sx,                cy * cx]]

        for i, δ in enumerate(center):
            matrix[i] = δ + sum(
                matrix[i][j] * (coordinate[j] - center[j]) for j in range(3))

    coordinate[:] = matrix


def scale(coordinate, kx=1, ky=1, kz=1, *, center):
    # type: (list[float], float, float, float, ..., Iterable[float]) -> None
    """
    ### 缩放
    将一个三维空间中的点以另一个点为缩放中心进行缩放 \n
    ---
    `coordinate`: 点的空间坐标 \ 
    `kx`: x 方向缩放比例 \ 
    `ky`: y 方向缩放比例 \ 
    `kz`: z 方向缩放比例 \ 
    `center`: 缩放中心的空间坐标
    """
    if kx <= 0 or ky <= 0 or kz <= 0:  # 限制缩放比例的范围
        raise ValueError('invalid scaling factor')
    for i, k in enumerate((kx, ky, kz)):
        coordinate[i] += (coordinate[i] - center[i]) * (k - 1)


class _3D_Object:
    """ 3D 对象基类 """

    def __init__(self, *coordinates):  # type: (list[float]) -> None
        self.coordinates = list(coordinates)  # 所有点的坐标

    def translate(self, dx=0, dy=0, dz=0):  # type: (float, float, float) -> None
        """
        ### 平移
        `dx`: x 方向位移长度 \ 
        `dy`: y 方向位移长度 \ 
        `dz`: z 方向位移长度
        """
        for coordinate in self.coordinates:
            translate(coordinate, dx, dy, dz)

    @overload
    def rotate(self, dx=0, dy=0, dz=0, *, center=ROTATE_CENTER):
        # type: (float, float, float, ..., Iterable[float]) -> None
        ...

    @overload
    def rotate(self, dx=0, *, axis):
        # type: (float, ..., Iterable[Iterable[float]]) -> None
        ...

    def rotate(self, dx=0, dy=0, dz=0, *, center=ROTATE_CENTER, axis=None):
        # type: (float, float, float, ..., Iterable[float], Iterable[Iterable[float]] | None) -> None
        """
        ### 旋转
        `dx`: x 方向旋转弧度，或者绕旋转轴线的旋转弧度 \ 
        `dy`: y 方向旋转弧度 \ 
        `dz`: z 方向旋转弧度 \ 
        `center`: 旋转中心，默认为原点 \ 
        `axis`: 旋转轴线，无默认值
        """
        for coordinate in self.coordinates:
            rotate(coordinate, dx, dy, dz, center=center, axis=axis)

    def scale(self, kx=1, ky=1, kz=1, *, center=None):
        # type: (float, float, float, ..., Iterable[float] | None) -> None
        """
        ### 缩放
        `kx`: x 方向缩放比例 \ 
        `ky`: y 方向缩放比例 \ 
        `kz`: z 方向缩放比例 \ 
        `center`: 缩放中心，默认为几何中心
        """
        if center is None:
            center = self.center()
        for coordinate in self.coordinates:
            scale(coordinate, kx, ky, kz, center=center)

    def center(self):  # type: () -> tuple[float, float, float]
        """ 几何中心 """
        return tuple(statistics.mean(xyz) for xyz in zip(*self.coordinates))

    def _project(self, distance):
        """
        ### 投影
        `distance`: 对象与观察者的距离
        """
        # NOTE: 这里可能需要一些优化


class _Point(_3D_Object):
    """ 点（基类） """

    def __init__(self, coordinate):  # type: (list[float]) -> None
        _3D_Object.__init__(self, coordinate)

    def _project(self, distance):  # type: (float) -> list[float]
        # override: 具体的实现
        relative_dis = distance - self.coordinates[0][0]
        if relative_dis <= 1e-16:
            return [float('inf')]*2  # BUG: 目前超出范围只能让其消失
        k = distance/relative_dis
        return [self.coordinates[0][1]*k, self.coordinates[0][2]*k]


class _Line(_3D_Object):
    """ 线（基类） """

    def __init__(
        self,
        start,  # type: list[float]
        end,  # type: list[float]
    ):  # type: (...) -> None
        _3D_Object.__init__(self, start, end)
        self.points = [_Point(start), _Point(end)]

    def _project(self, distance):  # type: (float) -> list[list[float]]
        # override: 具体的实现
        return [point._project(distance) for point in self.points]


class _Side(_3D_Object):
    """ 面（基类） """

    def __init__(self, *coordinates):  # type: (list[float]) -> None
        _3D_Object.__init__(self, *coordinates)
        self.lines = [_Line(coordinates[index-1], coordinate)
                      for index, coordinate in enumerate(coordinates)]

    def _project(self, distance):  # type: (float) -> list[list[list[float]]]
        # override: 具体的实现
        return [line._project(distance) for line in self.lines]


class Point(_Point):
    """ 点 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        coords,  # type: Iterable[float]
        *,
        size=POINT_SIZE,  # type: float
        width=POINT_WIDTH,  # type: float
        fill=COLOR_POINT_FILL,  # type: str
        outline=COLOR_POINT_OUTLINE,  # type: str
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `coords`: 点的空间坐标 \ 
        `size`: 点的大小 \ 
        `width`: 点轮廓的宽度 \ 
        `fill`: 点内部的填充颜色 \ 
        `outline`: 点轮廓的颜色
        """
        _Point.__init__(self, list(coords))
        canvas._items_3d.append(self)
        self.canvas = canvas
        self.size = size
        self.width = width
        self.fill = fill
        self.item = canvas.create_oval(
            -1, -1, -1, -1, fill=fill, outline=outline, width=width)
        self.update()

    def update(self):  # type: () -> None
        """ 更新对象的显示 """
        x, y = self._project(self.canvas.distance)
        self.canvas.coords(self.item, (x-self.size)*self.canvas.rx, (y-self.size) *
                           self.canvas.ry, (x+self.size)*self.canvas.rx, (y+self.size)*self.canvas.ry)

    def _camera_distance(self):  # type: () -> float
        """ 与相机距离 """
        sign = math.copysign(1, self.canvas.distance - self.coordinates[0][0])
        return sign*math.dist([self.canvas.distance, 0, 0], self.coordinates[0])


class Line(_Line):
    """ 线 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        point_start,  # type: Iterable[float]
        point_end,  # type: Iterable[float]
        *,
        width=LINE_WDITH,  # type: float
        fill=COLOR_LINE_FILL,  # type: str
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `point_start`: 起点坐标 \ 
        `point_end`: 终点坐标 \ 
        `width`: 线的宽度 \ 
        `fill`: 线的颜色
        """
        _Line.__init__(self, list(point_start), list(point_end))
        canvas._items_3d.append(self)
        self.canvas = canvas
        self.width = width
        self.fill = fill
        self.item = canvas.create_line(-1, -1, -1, -1, width=width, fill=fill)
        self.update()

    def update(self):  # type: () -> None
        """ 更新对象的显示 """
        self.canvas.coords(self.item, *[coord*(self.canvas.ry if i else self.canvas.rx)
                           for point in self._project(self.canvas.distance) for i, coord in enumerate(point)])

    def _camera_distance(self):  # type: () -> float
        """ 与相机距离 """
        center = self.center()
        sign = math.copysign(1, self.canvas.distance - center[0])
        return sign*math.dist([self.canvas.distance, 0, 0], center)


class Side(_Side):
    """ 面 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        *points,  # type: Iterable[float]
        width=SIDE_WIDTH,  # type: float
        fill=COLOR_SIDE_FILL,  # type: str
        outline=COLOR_SIDE_OUTLINE,  # type: str
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `points`: 各点的空间坐标 \ 
        `width`: 面轮廓的宽度 \ 
        `fill`: 面内部的填充颜色 \ 
        `outline`: 面轮廓的颜色
        """
        _Side.__init__(self, *[list(point) for point in points])
        canvas._items_3d.append(self)
        self.canvas = canvas
        self.width = width
        self.fill = fill
        self.outline = outline
        self.item = canvas.create_polygon(
            -1, -1, -1, -1, width=width, fill=fill, outline=outline)
        self.update()

    def update(self):  # type: () -> None
        """ 更新对象的显示 """
        self.canvas.coords(self.item, *[coord*(self.canvas.ry if i else self.canvas.rx)
                           for line in self._project(self.canvas.distance) for point in line for i, coord in enumerate(point)])

    def _camera_distance(self):  # type: () -> float
        """ 与相机距离 """
        center = self.center()
        sign = math.copysign(1, self.canvas.distance - center[0])
        return sign*math.dist([self.canvas.distance, 0, 0], center)


class Geometry:
    """ 几何体 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        *sides,  # type: Side
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `sides`: 组成几何体的面
        """
        canvas._geos.append(self)
        self.canvas = canvas
        self.sides = list(sides)

    def translate(self, dx=0, dy=0, dz=0):  # type: (float, float, float) -> None
        """
        ### 平移
        `dx`: x 方向位移长度 \ 
        `dy`: y 方向位移长度 \ 
        `dz`: z 方向位移长度
        """
        for side in self.sides:
            side.translate(dx, dy, dz)

    @overload
    def rotate(self, dx=0, dy=0, dz=0, *, center=ROTATE_CENTER):
        # type: (float, float, float, ..., Iterable[float]) -> None
        ...

    @overload
    def rotate(self, dx=0, *, axis):
        # type: (float, ..., Iterable[Iterable[float]]) -> None
        ...

    def rotate(self, dx=0, dy=0, dz=0, *, center=ROTATE_CENTER, axis=None):
        # type: (float, float, float, ..., Iterable[float], Iterable[Iterable[float]] | None) -> None
        """
        ### 旋转
        `dx`: x 方向旋转弧度，或者绕旋转轴线的旋转弧度 \ 
        `dy`: y 方向旋转弧度 \ 
        `dz`: z 方向旋转弧度 \ 
        `center`: 旋转中心，默认为原点 \ 
        `axis`: 旋转轴线，无默认值
        """
        for side in self.sides:
            side.rotate(dx, dy, dz, center=center, axis=axis)

    def scale(self, kx=1, ky=1, kz=1, *, center=None):
        # type: (float, float, float, ..., Iterable[float] | None) -> None
        """
        ### 缩放
        `kx`: x 方向缩放比例 \ 
        `ky`: y 方向缩放比例 \ 
        `kz`: z 方向缩放比例 \ 
        `center`: 缩放中心，默认为几何中心
        """
        if center is None:
            center = self.center()
        for side in self.sides:
            side.scale(kx, ky, kz, center=center)

    def center(self):  # type: () -> tuple[float, float, float]
        """ 几何中心 """
        return tuple(statistics.mean(axis) for axis in zip(*set(tuple(coord) for side in self.sides for coord in side.coordinates)))

    def update(self):  # type: () -> None
        """ 更新几何体 """
        for side in self.sides:
            side.update()

    def append(self, *sides):  # type: (Side) -> None
        """
        ### 添加面
        `sides`: `Side` 类
        """
        for side in sides:
            self.sides.append(side)


class Cuboid(Geometry):
    """ 长方体 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        x,  # type: float
        y,  # type: float
        z,  # type: float
        length,  # type: float
        width,  # type: float
        height,  # type: float
        *,
        color_up='',  # type: str
        color_down='',  # type: str
        color_left='',  # type: str
        color_right='',  # type: str
        color_front='',  # type: str
        color_back='',  # type: str
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `x`: 左上角 x 坐标 \ 
        `y`: 左上角 y 坐标 \ 
        `z`: 左上角 z 坐标 \ 
        `length`: 长度 \ 
        `width`: 宽度 \ 
        `height`: 高度 \ 
        `color_up`: 上表面颜色 \ 
        `color_down`: 下表面颜色 \ 
        `color_left`: 左侧面颜色 \ 
        `color_right`: 右侧面颜色 \ 
        `color_front`: 正面颜色 \ 
        `color_back`: 后面颜色
        """
        canvas._geos.append(self)
        self.canvas = canvas
        coords = [[x+l, y+w, z+h]
                  for l in (0, length)
                  for w in (0, width)
                  for h in (0, height)]
        self.sides = [
            Side(canvas, coords[0], coords[1],
                 coords[3], coords[2], fill=color_back),
            Side(canvas, coords[0], coords[1],
                 coords[5], coords[4], fill=color_left),
            Side(canvas, coords[0], coords[2],
                 coords[6], coords[4], fill=color_up),
            Side(canvas, coords[1], coords[3],
                 coords[7], coords[5], fill=color_down),
            Side(canvas, coords[2], coords[3],
                 coords[7], coords[6], fill=color_right),
            Side(canvas, coords[4], coords[5],
                 coords[7], coords[6], fill=color_front),
        ]


class Tetrahedron(Geometry):
    """ 四面体 """

    def __init__(
        self,
        canvas,  # type: Canvas_3D | Space
        point_1,  # type: Iterable[float]
        point_2,  # type: Iterable[float]
        point_3,  # type: Iterable[float]
        point_4,  # type: Iterable[float]
        *,
        colors=('',)*4  # type: Iterable[str]
    ):  # type: (...) -> None
        """
        `canvas`: 父画布 \ 
        `point_1`: 第一个顶点 \ 
        `point_2`: 第二个顶点 \ 
        `point_3`: 第三个顶点 \ 
        `point_4`: 第四个顶点 \ 
        `colors`: 颜色序列
        """
        canvas._geos.append(self)
        self.canvas = canvas
        self.sides = [
            Side(canvas, point_1, point_2, point_3, fill=colors[0]),
            Side(canvas, point_1, point_2, point_4, fill=colors[1]),
            Side(canvas, point_1, point_3, point_4, fill=colors[2]),
            Side(canvas, point_2, point_3, point_4, fill=colors[3]),
        ]


__all__ = list(filter(lambda name: '__' not in name, globals()))
