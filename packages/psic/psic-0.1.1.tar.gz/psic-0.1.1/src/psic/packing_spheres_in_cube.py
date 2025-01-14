# -*- coding: utf-8 -*-
"""
2D：矩形区域填充圆形
3D：六面体区域填充球体
>4D: 超立方体区域填充超球
"""
import json
import os

import numpy as np
from numpy import ndarray, array, arange, sum, sqrt, empty, diag_indices_from, transpose, unique, delete, concatenate
from scipy.spatial.distance import cdist  # type: ignore

from psic.calc_fraction import calc_area_fraction, calc_volume_fraction
from psic.plot_model import plot_circle, plot_distribution, plot_sphere
from psic.wrappers import show_running_time

DTYPE = 'float64'


def rayleigh_set(scale: float, size: int) -> ndarray:
    dataset = np.random.rayleigh(scale=scale, size=size)
    return array(dataset)


def crash_time(center_1: ndarray, center_2: ndarray, velocity_1: ndarray, velocity_2: ndarray, r_1: ndarray,
               r_2: ndarray, dt: float) -> float:
    """
    已知两圆/球体在dt时间后发生重叠，计算两圆/球体碰撞时刻。
    ----------
    center_1 : ndarray
        1号圆/球心坐标
    center_2 : ndarray
        2号圆/球心坐标
    velocity_1 : ndarray
        1号圆/球速度
    velocity_2 : ndarray
        2号圆/球速度
    r_1 : ndarray
        1号圆/球半径
    r_2 : ndarray
        2号圆/球半径
    dt : float
        两圆/球体碰撞时间位于区间[0, dt]内

    Returns
    -------
    tc : float
        两圆/球体发生碰撞的时间
    """
    a = sum((velocity_2 - velocity_1) ** 2)
    b = 2 * sum((velocity_2 - velocity_1) * (center_2 - center_1))
    c = sum((center_2 - center_1) ** 2) - (r_1[0] + r_2[0]) ** 2
    delta = sqrt(b ** 2 - 4 * a * c)
    t1 = (-b - delta) / (2 * a)
    t2 = (-b + delta) / (2 * a)
    tc = min(t1, t2, dt)

    return tc


def update_crash_velocity(center_1: ndarray, center_2: ndarray) -> tuple[ndarray, ndarray]:
    """
    更新两圆/球碰撞后各自的速度矢量
    两球碰撞后的速度为沿着两球心连线方向互相远离对方的单位矢量
    """
    v1 = center_2 - center_1
    v2 = center_1 - center_2
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)
    return v1, v2


def dist_square(X: ndarray = empty(0), Y: ndarray = empty(0)) -> ndarray:
    """
    求点集合X到Y中任意两点之间的距离平方

    Parameters
    ----------
    X : ndarray
        点集合的坐标矩阵，n*维度
    Y : ndarray
        点集合的坐标矩阵，m*维度

    Returns
    -------
    dist_square : ndarray
        返回n*m的矩阵，i行j列代表X[i]和Y[j]之间的距离的平方
    """
    if Y.size == 0:
        dist_square = cdist(X, X) ** 2
    else:
        dist_square = cdist(X, Y) ** 2
    return dist_square


def r_square(X: ndarray = empty(0), Y: ndarray = empty(0)) -> ndarray:
    """
    求两个半径集合和的平方

    Parameters
    ----------
    X : ndarray
        半径数组，n*1
    Y : ndarray
        半径数组，m*1

    Returns
    -------
    r_square : ndarray
        返回n*m的矩阵，i行j列代表半径X[i]和Y[j]和的平方
    """
    if Y.size == 0:
        r_square = (X + X.T) ** 2
    else:
        r_square = (X + Y.T) ** 2
    return r_square


def is_crash_index(C0: ndarray = empty(0), R0: ndarray = empty(0), C1: ndarray = empty(0),
                   R1: ndarray = empty(0)) -> ndarray:
    """
    判断圆/球集合C0和C1是否存在重叠的元素，得到发生重叠的圆/球在C1中的索引

    Parameters
    ----------
    C0 : ndarray
        圆心坐标数组，n*维度
    R0 : ndarray
        半径数组，n*1
    C1 : ndarray
        圆心坐标数组，n*维度
    R1 : ndarray
        半径数组，n*1

    Returns
    -------
    is_crash_index : ndarray
        得到不重复的发生碰撞的圆的索引
    """
    if C1.size == 0:
        left = dist_square(C0)
        right = r_square(R0)
        is_crash = left < right
        row, col = diag_indices_from(is_crash)
        is_crash[row, col] = False
        is_crash_index = transpose(is_crash.nonzero())
        is_crash_index = unique(is_crash_index[:, 1])
    else:
        left = dist_square(C0, C1)
        right = r_square(R0, R1)
        is_crash = left < right
        is_crash_index = transpose(is_crash.nonzero())
        is_crash_index = unique(is_crash_index[:, 1])
    return is_crash_index


def update_reflect_velocity(centers: ndarray, velocities: ndarray, size: list) -> ndarray:
    """
    圆/球心超出区域边界后发生反射，更新反射后的速度

    Parameters
    ----------
    centers : ndarray
        圆心坐标数组，n*维度
    velocities : ndarray
        半径数组，n*1
    size : list
        区域取值范围

    Returns
    -------
    v : ndarray
        更新之后的速度
    """
    a = centers < size[0][0]
    b = centers > size[0][1]
    c = (a + b).astype(int)
    c[c == 1] = -1.0
    c[c == 0] = 1.0
    v = velocities * c

    return v


def create_centers(ncircle: int, size: list) -> ndarray:
    """
    建立ncircle个取值范围在size区域内随机分布的圆/球心坐标数组

    Parameters
    ----------
    ncircle : int
        建立的圆/球心坐标数量
    size : list
        区域取值范围

    Returns
    -------
    centers : ndarray
        建立的圆心坐标数组，ncircle*维度
    """
    centers = np.random.rand(ncircle, len(size))
    for i, _ in enumerate(size):
        centers[:, i] = centers[:, i] * (size[i][1] - size[i][0]) + size[i][0]
    return centers.astype(DTYPE)


def create_velocities(ncircle: int, size: list) -> ndarray:
    """
    建立ncircle个随机分布的速度矢量数组

    Parameters
    ----------
    ncircle : int
        建立的圆/球心坐标数量
    size : list
        区域取值范围

    Returns
    -------
    velocities : ndarray
        建立的速度矢量数组，ncircle*维度
    """
    velocities = np.random.rand(ncircle, len(size)) * 2 - 1.0
    return velocities.astype(DTYPE)


def create_radiuses(ncircle: int, radius_sets: ndarray) -> ndarray:
    """
    建立ncircle个符合radiuse_sets分布的半径数组

    Parameters
    ----------
    ncircle : int
        建立的半径数量
    radius_sets: ndarray
        已知的半径分布集合

    Returns
    -------
    radiuses : ndarray
        建立的半径数组，ncircle*1
    """
    radiuses = radius_sets[range(min(ncircle, len(radius_sets)))]
    return radiuses.reshape(ncircle, -1)


def update_radius_sets(radius_sets: ndarray, radiuses: ndarray) -> ndarray:
    """
    从radius_sets中删除与radiuses中相同的所有元素
    """
    for r in radiuses:
        radius_sets = delete(radius_sets, np.where(radius_sets == r))
    return radius_sets


@show_running_time
def packing_spheres_in_cube(ncircle: int, radius_sets: ndarray, size: list, gap: float, num_add: int, max_iter: int,
                            dt0: float, dt_interval: int, status: dict) -> tuple[ndarray, ndarray]:
    """
    向区域内填充圆/球
    
    packing_spheres_in_cube(ncircle, radius_sets, size, gap, num_add, max_iter, dt0, dt_interval, status)

    Parameters
    ----------
    ncircle : int
        单次向矩形区域内增加圆的数量
    radius_sets : ndarray
        填充粒子的半径分布集合
    size : list
        区域取值范围
    gap : float
        圆/球之间的间隔
    num_add : int
        循环添加圆形次数
    max_iter : int
        时间回溯的最大迭代次数
    dt0 : float
        初始时间步长
    dt_interval : int
        向矩形内部添加dt_interval次圆后，运动一次
    status : dict
        运行状态字典
        
    Returns
    -------
    centers_1 : ndarray
        留在区域内的圆心坐标
    radiuses_1 : ndarray
        与centers_1对应的半径
    """
    # 初始化
    centers_2 = create_centers(1, size)
    velocities_2 = create_velocities(1, size)
    radiuses_2 = create_radiuses(1, radius_sets)

    # 当前圆形计数-1
    n = 0

    # 更新半径集合
    radius_sets_0 = radius_sets
    radius_sets = update_radius_sets(radius_sets, radius_sets_0[0:1])

    # 循环添加圆形
    for i in range(num_add):

        centers_0 = centers_2
        velocities_0 = velocities_2
        radiuses_0 = radiuses_2

        centers_new = create_centers(ncircle, size)
        velocities_new = create_velocities(ncircle, size)
        radiuses_new = create_radiuses(ncircle, radius_sets)

        is_crash_old = is_crash_index(centers_0, radiuses_0, centers_new, radiuses_new)
        is_crash_self = is_crash_index(centers_new, radiuses_new)
        is_crash = concatenate((is_crash_old, is_crash_self), axis=0)
        is_crash = unique(is_crash)
        is_not_crash = delete(arange(len(centers_new)), is_crash)

        radius_sets = update_radius_sets(radius_sets, radiuses_new[is_not_crash])

        centers_new = delete(centers_new, is_crash, 0)
        velocities_new = delete(velocities_new, is_crash, 0)
        radiuses_new = delete(radiuses_new, is_crash, 0)

        centers_1 = concatenate((centers_0, centers_new), axis=0)
        velocities_1 = concatenate((velocities_0, velocities_new), axis=0)
        radiuses_1 = concatenate((radiuses_0, radiuses_new), axis=0)

        n = len(radiuses_1) - 1

        centers_2 = centers_1
        velocities_2 = velocities_1
        radiuses_2 = radiuses_1

        dt = dt0

        if i % dt_interval == 0:  # 开始运动
            velocities_2 = update_reflect_velocity(centers_2, velocities_2, size)
            count = 0
            while count < max_iter:
                count += 1

                centers_2 = centers_1 + velocities_1 * dt
                is_crash = is_crash_index(centers_2, radiuses_1)

                if len(is_crash) < 2:
                    break
                elif len(is_crash) == 2:  # 找到有且仅有两个圆/球碰撞的情况，回溯得到两圆/球碰撞时间，更新两圆/球碰撞之后的速度
                    center_1 = centers_1[is_crash[0]]
                    center_2 = centers_1[is_crash[1]]
                    velocity_1 = velocities_1[is_crash[0]]
                    velocity_2 = velocities_1[is_crash[1]]
                    r_1 = radiuses_1[is_crash[0]]
                    r_2 = radiuses_1[is_crash[1]]

                    tc = crash_time(center_1, center_2, velocity_1, velocity_2, r_1, r_2, dt)

                    centers_2 = centers_1 + velocities_1 * tc
                    center_1 = centers_2[is_crash[0]]
                    center_2 = centers_2[is_crash[1]]

                    v1, v2 = update_crash_velocity(center_1, center_2)
                    velocities_2[is_crash[0]] = v2
                    velocities_2[is_crash[1]] = v1
                    break
                else:
                    dt *= 0.5

            if count >= max_iter:
                print('The number of iterations is out of range.')

        try:
            if i % int(num_add / 10) == 0:
                if len(size) == 2:
                    fraction = calc_area_fraction(centers_1, radiuses_1 - gap, size)
                    print(i, n, fraction)
                    status['log'] += '%s, %s, %s\n' % (i, n, fraction)

                if len(size) == 3:
                    fraction = calc_volume_fraction(centers_1, radiuses_1 - gap, size)
                    status['log'] += '%s, %s, %s\n' % (i, n, fraction)

        except ZeroDivisionError:
            print(ZeroDivisionError)

        if len(radius_sets_0) <= n + ncircle + 1:
            break

        status['progress'] = int(i / num_add * 100)

    return centers_1, radiuses_1


@show_running_time
def create_model(ncircle: int, size: list, gap: float, num_add: int, max_iter: int, dt0: float, dt_interval: int,
                 rayleigh_para: float, num_ball: int, rad_min: float, rad_max: float, model_path: str,
                 status: dict) -> int:
    """
    根据参数列表生成填充模型
    
    create_model(ncircle, size, gap, num_add, max_iter, dt0, dt_interval, rayleigh_para, num_ball, rad_min, rad_max, model_path, status)
    
    Parameters
    ----------
    ncircle : int
        单次向矩形区域内增加圆的数量
    size : list
        区域取值范围
    gap : float
        圆/球之间的间隔
    num_add : int
        循环添加圆形次数
    max_iter : int
        时间回溯的最大迭代次数
    dt0 : float
        初始时间步长
    dt_interval : int
        向矩形内部添加dt_interval次圆后，运动一次
    rayleigh_para : float
        瑞利分布参数
    num_ball : int
        生成集合内球体数量
    rad_min : int
        去掉集合内半径小于rad_min的球
    rad_max : int
        去掉集合内半径大于rad_max的球
    model_path : str
        生成模型文件的存储路径
    status : dict
        运行状态字典
    
    Process
    -------
    生成模型文件：model.npy
    生成参数文件：args.json
    生成日志文件：model.log
    生成信息文件：model.msg
    生成模型图片：model.png
    生成分布图片：density.png
    
    Returns
    -------
    0
    """

    args = ncircle, size, gap, num_add, max_iter, dt0, dt_interval, rayleigh_para, num_ball, rad_min, rad_max, model_path, status

    # 生成需要填充的半径集合
    radius_sets = rayleigh_set(rayleigh_para, num_ball)
    radius_sets = radius_sets.astype(DTYPE)
    radius_sets = abs(np.sort(-radius_sets))
    radius_sets = radius_sets[radius_sets > rad_min]
    radius_sets = radius_sets[radius_sets < rad_max]

    # 转换为半径，毫米
    radius_sets *= 0.001 / 2.0

    status['status'] = 'Running'

    centers, radiuses = packing_spheres_in_cube(ncircle, radius_sets, size, gap, num_add, max_iter, dt0, dt_interval,
                                                status)

    data = concatenate((centers, radiuses), axis=1)

    geo_dimension = len(size)

    filename = os.path.join(model_path, 'model.npy')
    np.save(filename, data)
    status['log'] += 'Save %s\n' % filename

    filename = os.path.join(model_path, 'model.png')
    if geo_dimension == 2:
        plot_circle(centers, radiuses - gap, size, filename, 150)
    elif geo_dimension >= 3:
        plot_sphere(centers, radiuses - gap, size, filename, (500, 500))
    else:
        raise NotImplementedError(f'the geometry dimension {geo_dimension} is not supported')
    status['log'] += 'Save %s\n' % filename

    filename = os.path.join(model_path, 'density.png')
    plot_distribution(radiuses - gap, filename, 150)
    status['log'] += 'Save %s\n' % filename

    status['progress'] = 100
    status['status'] = 'Done'

    filename = os.path.join(model_path, 'model.msg')
    if geo_dimension == 2:
        fraction = calc_area_fraction(centers, radiuses - gap, size)
    elif geo_dimension >= 3:
        fraction = calc_volume_fraction(centers, radiuses - gap, size)
    else:
        raise NotImplementedError(f'the geometry dimension {geo_dimension} is not supported')
    message = {
        'fraction': fraction,
        'num_ball': len(radiuses),
        'size': size,
        'gap': gap
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(message, f, ensure_ascii=False)
    status['log'] += 'Save %s\n' % filename

    filename = os.path.join(model_path, 'args.json')
    status['log'] += 'Save %s\n' % filename
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(args[:-1], f, ensure_ascii=False)

    filename = os.path.join(model_path, 'model.log')
    status['log'] += 'Save %s\n' % filename
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(status['log'])

    return 0


if __name__ == "__main__":
    ncircle = 8
    size = [[0, 1], [0, 1]]
    # size = [[0, 1], [0, 1], [0, 1]]
    gap = 0.0
    num_add = 10000
    max_iter = 100
    dt0 = 0.01
    dt_interval = 10000
    rayleigh_para = 20
    num_ball = 1200
    rad_min = 10
    rad_max = 100
    model_path = ''
    thread_id = 1
    status = {'status': 'Submit', 'log': '', 'progress': 0}
    args = (ncircle, size, gap, num_add, max_iter, dt0, dt_interval, rayleigh_para, num_ball, rad_min, rad_max,
            model_path, status)
    print(status)
    create_model(*args)
    print(status)
