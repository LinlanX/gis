def heading(s_x, s_y, e_x, e_y):
    """输入两点坐标返回两点连线的方向角（与正北方向的夹角）"""
    return float((90 - math.degrees(math.atan2(e_y - s_y, e_x - s_x))) % 360.0)


def headingf(line_feat):
    """返回线要素最后两个点的方向角，驶出此线的角度"""
    line_geom = line_feat.GetGeometryRef()
    point_count = line_geom.GetPointCount()
    s_x = line_geom.GetX(point_count - 2)
    s_y = line_geom.GetY(point_count - 2)
    e_x = line_geom.GetX(point_count - 1)
    e_y = line_geom.GetY(point_count - 1)
    return float((90 - math.degrees(math.atan2(e_y - s_y, e_x - s_x))) % 360.0)


def headingt(line_feat):
    """返回线要素前两个点的方向角，进入此线的角度"""
    line_geom = line_feat.GetGeometryRef()
    s_x = line_geom.GetX(0)
    s_y = line_geom.GetY(0)
    e_x = line_geom.GetX(1)
    e_y = line_geom.GetY(1)
    return float((90 - math.degrees(math.atan2(e_y - s_y, e_x - s_x))) % 360.0)
