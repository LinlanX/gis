def heading(s_x, s_y, e_x, e_y):
    """输入两点坐标返回两点连线的方向角（与正北方向的夹角）"""
    return float((90 - math.degrees(math.atan2(e_y - s_y, e_x - s_x))) % 360.0)
