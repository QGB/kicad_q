# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'C:\\Users\\Administrator\\Documents\\KiCad\\9.0\\scripting\\plugins\\Q.py'
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2026-05-12 07:16:57 UTC (1778570217)

import sys
py = sys.modules['qgb.py']
from kicad import *
import kicad
def jk_BD6A24_2512(W=100, zip=0):
    # ***<module>.jk_BD6A24_2512: Failure: Different bytecode
    kicad_mod = new_kicad_mod(w=W, h=W)
    def add_2512_pad(x, y, angle=0):
        pad_w, pad_h, center_dist = (1.9, 2, 4.0)
        rad = math.radians(angle)
        cos_a, sin_a = (math.cos(rad), math.sin(rad))
        def rot(p):
            return (p[0] * cos_a - p[1] * sin_a, p[0] * sin_a + p[1] * cos_a)
        left_rel = (-center_dist / 2, 0)
        right_rel = (center_dist / 2, 0)
        left_abs = (x + rot(left_rel)[0], y + rot(left_rel)[1])
        right_abs = (x + rot(right_rel)[0], y + rot(right_rel)[1])
        pad1 = Pad(number='1', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=left_abs, size=[pad_w, pad_h], rotation=angle, layers=['F.Cu', 'F.Mask', 'F.Paste'])
        pad2 = Pad(number='2', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=right_abs, size=[pad_w, pad_h], rotation=angle, layers=['F.Cu', 'F.Mask', 'F.Paste'])
        kicad_mod.append(pad1)
        kicad_mod.append(pad2)
    rectline_center(kicad_mod, W / 2, W / 2, w=W, h=W, crosshair=1)
    def add_pad_pair(kmod, x, y, size, pin_num, drill_screw, smt_dy=(-0.6)):
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_THT, shape=Pad.SHAPE_RECT, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x, y + smt_dy], size=[size[0], 1.5], drill=0, layers=['F.Cu']))
    def p15_11(x0=W / 2 - 26.0, y0=11, smt_dy=(-0.6)):
        rxy = []
        size = [1, 1]
        drill_screw = 0.9
        groups = [(x0, 15, 0), (x0 + 28.0 + 4, 11, 15)]
        dln = {}
        for start_x, pin_count, start_num in groups:
            for i in range(pin_count):
                n = start_num + i
                x = start_x + 2.0 * i
                add_pad_pair(kicad_mod, x, y0, size, f'{n}', drill_screw=drill_screw, smt_dy=smt_dy)
                rxy.append((x, y0))
        return rxy
    yb = 30
    for i in centered_range(26, center=50, pitch=3.7):
        add_pad_pair(kicad_mod, i, yb, [1, 1], f'{i + 1}', drill_screw=1)
    r11 = p15_11(x0=W / 2 - 26.0, y0=yb + 10, smt_dy=(-0.6))
    xs = centered_range(24, center=50, pitch=4)
    x24 = centered_range(14, center=29, pitch=2.4) + centered_range(10, center=65, pitch=2.4)
    x3 = centered_range(14, center=29, pitch=3) + centered_range(10, center=65, pitch=3)
    y9 = 14
    for i in range(24):
        y = yb + 10 + y9
        add_2512_pad(xs[i], y, angle=90)
    r29 = p15_11(x0=W / 2 - 26.0, y0=yb + 10 + y9 + y9, smt_dy=0.6)
    return write_kicad_mod(kicad_mod, zip=zip)
def naoh(w=100, pitch=1.15, margin=1, D=92, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w, p=pitch, m=margin)
    xz, yz = (w / 2, w / 2)
    n = 0
    x = margin
    while x <= w - margin:
        y = margin
        while y <= w - margin:
            dist = ((x - xz) ** 2 + (y - yz) ** 2) ** 0.5
            if dist < D / 2:
                non_plated_hole(kicad_mod, x, y, 0.4)
                n += 1
            y += pitch
        x += pitch
    kicad_mod.name += f'n={n}'
    text(kicad_mod, f'n={n}', at=[(-10), 50], size=[3, 2.5], layers='F.Cmts.User')
    if D > 100:
        return write_kicad_mod(kicad_mod, zip=zip)
    else:
        circle_filled(kicad_mod, xz, yz, D + 2, layers=['F.Cu', 'F.Mask'])
        return write_kicad_mod(kicad_mod, zip=zip)
def laser_array(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    dx, pin_pitch = (14, 2.54)
    nx, ny_pins = (int(w // dx), 40)
    y_start = (w - (ny_pins - 1) * pin_pitch) / 2
    for i in range(nx):
        xi = w / 2 + (i - (nx - 1) / 2) * dx
        y_end = y_start + (ny_pins - 1) * pin_pitch
        for j in range(ny_pins):
            yi = y_start + j * pin_pitch
            plated_hole(kicad_mod, xi + 2.54, yi, 0.9)
            plated_hole(kicad_mod, xi - 2.54, yi, 0.9)
            if j % 3 == 0:
                plated_hole(kicad_mod, xi, yi, 1)
                rectline_center(kicad_mod, xi, yi + 2, w=14, h=7, crosshair=1)
        multi_dot_line(kicad_mod, [(xi + 2.54, y_start), (xi + 2.54, y_end)], width=1.2, layers='F.Cu', segments=10)
        multi_dot_line(kicad_mod, [(xi - 2.54, y_start), (xi - 2.54, y_end)], width=1.2, layers='B.Cu', segments=10)
    return write_kicad_mod(kicad_mod, zip=zip)
def circle8(d=0, w=100, itop=0, zip=0):
    if not d:
        d = -w / 2 * ((-1) + math.sqrt(5 - 2 * math.sqrt(6)))
    kicad_mod = new_kicad_mod(w=w, h=w, d=d)
    round_rect(kicad_mod, w, w, a=4)
    r = d / 2
    t = r + math.sqrt((2 * r) ** 2 - (w / 2 - r) ** 2)
    coords = [(r, r), (w - r, r), (r, w - r), (w - r, w - r), (t, w / 2), (w - t, w / 2), (w / 2, t), (w / 2, w - t)]
    if itop == 0:
        L = 'B'
        dy_4p = w - 1
    else:
        L = 'F'
        dy_4p = 1
    mask_layer = [L + '.Cu']
    for x, y in coords:
        circle(kicad_mod, x=x, y=y, d=d)
        circle(kicad_mod, x=x, y=y, d=33.0)
        m4_4j(kicad_mod, x, y, angle=35, D=14.6, thickness=1.5, one_smt=mask_layer)
    center = w / 2
    g = (t + w / 2 + r) / 3
    def d_hole(kicad_mod, x, y, ad, cd=0):
        non_plated_hole(kicad_mod, x, y, ad)
        if not cd:
            cd = 7
        circle(kicad_mod, x, y, cd)
    hole_rect_center(kicad_mod, center, center, side_len_x=w - g * 2, angle=0, d=3, cd=6, func=d_hole)
    hole_rect_center_x2(kicad_mod, center, center, w=28, h=w - 10, angle=0, d=6, func=d_hole, cd=10)
    hole_rect_center(kicad_mod, center, center, w=95, angle=0, d=1, func=d_hole, cd=7)
    d_hole(kicad_mod, center, center, 10, cd=14)
    return write_kicad_mod(kicad_mod, zip=zip)
def hole_rect_center_x2(kicad_mod, x, y, w, h, **ka):
    hole_rect_center(kicad_mod, x, y, w=w, h=h, **ka)
    hole_rect_center(kicad_mod, x, y, w=h, h=w, **ka)
def circle50(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    t = 1.6
    t = 0.1
    def cir(kicad_mod, x, y, d, **ka):
        circle(kicad_mod, x=x, y=y, d=d, crosshair=0, layers=glayers_edge_pure, width=t)
        non_plated_hole(kicad_mod, x, y, 9.8)
    cir(kicad_mod, x=25, y=25, d=50, crosshair=0, layers=glayers_edge_pure, width=t)
    cir(kicad_mod, x=75, y=25, d=50, crosshair=0, layers=glayers_edge_pure, width=t)
    d = 56.2
    cir(kicad_mod, x=50, y=75 - (d - 50) / 2, d=d, crosshair=0, layers=glayers_edge_pure, width=t)
    return write_kicad_mod(kicad_mod, zip=zip)
def hgr20_a(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    x = y = w / 2
    hole_rect_center(kicad_mod, x, y, side_len_x=w - 10, angle=0, d=3, func=non_plated_hole)
    hgr20_section(kicad_mod, x, y, angle=0)
    two_hole(kicad_mod, x, y - 30, 70, 5.9, angle=0, holes=[0, 1], hole_func=non_plated_hole)
    two_hole(kicad_mod, x, y - 30, 72, 5.9, angle=0, holes=[0, 1], hole_func=non_plated_hole)
    two_hole(kicad_mod, x, y + 30, 70, 5.9, angle=0, holes=[0, 1], hole_func=non_plated_hole)
    hgr20_flange_block(kicad_mod, x, y, angle=90)
    hgr20_block(kicad_mod, x, y, hole=4.9, angle=90)
    def hgr20b(x, y, holes, hole=4.9):
        hgr20_block(kicad_mod, x, y, hole=hole, holes=holes, angle=90)
        hgr20_block(kicad_mod, x, y, hole=4.9, angle=90)
    hgr20b(x - 35, y + 20, holes=[1, 2])
    hgr20b(x + 35, y + 20, holes=[0, 3])
    mgn12c_block(kicad_mod=kicad_mod, x=x - 20, y=13.5, up_rail=0.0)
    mgn12c_block(kicad_mod=kicad_mod, x=x + 20, y=13.5)
    non_plated_hole(kicad_mod, x + 20, 13.5, 7.95)
    return write_kicad_mod(kicad_mod, zip=zip)
def hgr20_section(kicad_mod, x, y, angle=0):
    z = ([0, 0], [0, 4.4], [3.5, 7.4], [3.5, 10.2], [0, 13.3], [0, 17.5])
    symmetric_x(kicad_mod, z, xm=20, x0=x - 10, y0=y - 8.75, angle=angle, layers=glayers_edge, width=0.01)
    rectline_center(kicad_mod, x, y, w=20, h=17.5, angle=angle, crosshair=1)
    return kicad_mod
def b3x2(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    x = w / 2
    y = w / 2
    round_rect(kicad_mod, w, w, a=4)
    circle(kicad_mod, x, y, 138)
    m = 3
    d = 34.5
    for i in range(m):
        xi = w / 2 + (i - (m - 1) / 2) * d
        for j in range(m):
            yi = w / 2 + (j - (m - 1) / 2) * d
            m4_4j(kicad_mod, xi, yi, angle=35)
            if i == 2 and j == 2:
                circle_filled(kicad_mod, xi, yi, 8, layers=glayers_FB_Mask)
            else:
                circle_filled(kicad_mod, xi, yi, 6, layers=glayers_FB_Mask)
        rectangle_full(kicad_mod, xi, w / 3, w=15, h=50, layers=glayers_FB_Cu)
    rectangle_full(kicad_mod, w / 3, w / 2 + d, w=50, h=15, layers=glayers_FB_Cu)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, angle=0, d=6, func=non_plated_hole)
    d3 = d * 3 - 8
    hole_rect_center(kicad_mod, x, y, side_len_x=d3, h=d, angle=0, d=4, func=non_plated_hole)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, h=d3, angle=0, d=4, func=non_plated_hole)
    for u in [(-1), 1]:
        x2 = w / 2 + u * d / 2
        dx = 5.5
        y = 1
        for xi in [x2 + dx, x2 - dx]:
            kicad_mod.append(Pad(number=f'{U.ct(kicad_mod) + 1}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[xi, y], size=[1, 2], layers=['F.Cu', 'F.Paste', 'F.Mask']))
            rectangle_full(kicad_mod, xi, y, w=2.5, layers=['F.Cu'])
            plated_hole(kicad_mod, xi, y, 0.95, size=1)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3x3_cover(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    x = w / 2
    y = w / 2
    d = 34.5
    round_rect(kicad_mod, w, w, a=4)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, angle=0, d=6, func=non_plated_hole)
    d3 = d * 3 - 8 + 2
    hole_rect_center(kicad_mod, x, y, side_len_x=d3, h=d, angle=0, d=4, func=non_plated_hole)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, h=d3, angle=0, d=4, func=non_plated_hole)
    def rect(kicad_mod, x, y, d):
        rectangle_full(kicad_mod, x, y, w=10, h=50, layers=glayers_F_Cu)
        circle_filled(kicad_mod, xi, yi, 8, layers=glayers_FB_Cu)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, h=d, angle=0, d=10, func=circle_filled, layers=glayers_FB_Cu)
    m = 3
    for i in range(m):
        xi = w / 2 + (i - (m - 1) / 2) * d
        for j in range(m):
            yi = w / 2 + (j - (m - 1) / 2) * d
            circle(kicad_mod, xi, yi, [15, 32, 34.5])
    non_plated_hole(kicad_mod, 50 + d, 50 + d, 4)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3x3(w=100, zip=0, itop=0):
    kicad_mod = new_kicad_mod(w=w, h=w, itop=itop, t=U.stime()[12:20])
    x = w / 2
    y = w / 2
    round_rect(kicad_mod, w, w, a=4)
    circle(kicad_mod, x, y, 138)
    m = 3
    d = 34.5
    if itop == 0:
        L = 'B'
        dy_4p = w - 1
    else:
        L = 'F'
        dy_4p = 1
    mask_layer = [L + '.Cu']
    for i in range(m):
        xi = w / 2 + (i - (m - 1) / 2) * d
        for j in range(m):
            yi = w / 2 + (j - (m - 1) / 2) * d
            m4_4j(kicad_mod, xi, yi, angle=35, one_smt=False)
            kicad_mod.append(Pad(number=f'{i},{j}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_CIRCLE, at=[xi, yi], size=[9, 9], layers=mask_layer))
            circle(kicad_mod, x=xi, y=yi, d=1, crosshair=0, layers=glayers_FB_Cu, width=8)
            if i == 2 and j == 2:
                circle_filled(kicad_mod, xi, yi, 8, layers=glayers_FB_Mask)
            else:
                circle_filled(kicad_mod, xi, yi, 6, layers=glayers_FB_Mask)
        rectangle_full(kicad_mod, xi, w / 3, w=15, h=50, layers=glayers_FB_Cu)
    rectangle_full(kicad_mod, w / 3, w / 2 + d, w=50, h=15, layers=glayers_FB_Cu)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, angle=0, d=6, func=non_plated_hole)
    d3 = d * 3 - 8 + 2
    hole_rect_center(kicad_mod, x, y, side_len_x=d3, h=d, angle=0, d=4, func=non_plated_hole)
    hole_rect_center(kicad_mod, x, y, side_len_x=d, h=d3, angle=0, d=4, func=non_plated_hole)
    xis = [w / 2]
    for u in [(-1), 1]:
        x2 = w / 2 + u * d
        dx = 5.5
        y = dy_4p
        for xi in [x2 + dx, x2 - dx]:
            xis.append(xi)
    for xi in xis:
        kicad_mod.append(Pad(number=f'{U.ct(kicad_mod) + 1}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[xi, y], size=[1, 2], layers=[L + i for i in ['.Cu', '.Paste', '.Mask']]))
        rectangle_full(kicad_mod, xi, y, w=2.5, layers=[L + '.Cu'])
        plated_hole(kicad_mod, xi, y, 0.95, size=1)
    return write_kicad_mod(kicad_mod, zip=zip)
def m12_4m10(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    x = w / 2
    y = w / 2
    hole_rect_center(kicad_mod, x, y, side_len_x=80, angle=0, d=10, func=non_plated_hole)
    non_plated_hole(kicad_mod, x, y, 12)
    hole_rect_center(kicad_mod, x, y, side_len_x=34.5, angle=0, d=1.18, func=m4_4j, one_smt=1)
    rectline_center(kicad_mod, x, y, w=34.5, crosshair=1)
    rectline_center(kicad_mod, x, y, w=69.0, crosshair=0)
    def d_hole(kicad_mod, x, y, ad):
        non_plated_hole(kicad_mod, x, y, ad)
        circle(kicad_mod, x, y, 10)
    hole_rect_center(kicad_mod, x, y, side_len_x=44, angle=45, d=4, func=d_hole)
    hole_rect_center(kicad_mod, x, y, side_len_x=64, angle=0, d=3, func=d_hole)
    rectangle_full(kicad_mod, x - 17.25, y, w=15, h=50, layers=glayers_FB_Cu)
    return write_kicad_mod(kicad_mod, zip=zip)
def m4_4j(kicad_mod=None, x=0, y=0, d=1.2, thickness=1.6, j_long=1, D=15, hole=5.8, inner_delta=0, hole_func=plated_hole, add_text=False, size=6.5, angle=0, one_smt=True, **ka):
    """\n    修正版：将所有组件作为一个整体绕 (x,y) 旋转 angle 度\n    """
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    circle(kicad_mod, x=x, y=y, d=D, crosshair=1, layers='F.Cu', width=0.1)
    circle(kicad_mod, x=x, y=y, d=11, crosshair=0, layers='F.Cu', width=0.1)
    if one_smt:
        kicad_mod.append(Pad(number=f'{x},{y}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_CIRCLE, at=[x, y], size=[9, 9], layers=one_smt))
    circle(kicad_mod, x=x, y=y, d=1, crosshair=0, layers=glayers_FB_Cu, width=7.3)
    circle(kicad_mod, x=x, y=y, d=34.5, crosshair=0, layers=glayers_silk, width=0.1)
    hole_func(kicad_mod, x=x, y=y, diameter=hole, size=size)
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    def rot(dx, dy):
        """核心：计算相对于 (x,y) 偏移 (dx,dy) 的点旋转 angle 后的新绝对坐标"""
        nx = x + (dx * cos_a - dy * sin_a)
        ny = y + (dx * sin_a + dy * cos_a)
        return (nx, ny)
    r_end = D / 2 - thickness / 2
    r_start = r_end - j_long
    mid_r = (r_start + r_end) / 2 - inner_delta
    j_long_total = thickness + j_long
    p1x, p1y = rot(d, -mid_r)
    kicad_mod.append(Pad(number='1', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, layers=Pad.LAYERS_THT, at=[p1x, p1y], size=[thickness, j_long_total], drill=[thickness, j_long_total], rotation=-angle))
    p2x, p2y = rot(-d, mid_r)
    kicad_mod.append(Pad(number='2', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, layers=Pad.LAYERS_THT, at=[p2x, p2y], size=[thickness, j_long_total], drill=[thickness, j_long_total], rotation=-angle))
    p3x, p3y = rot(-mid_r, -d)
    kicad_mod.append(Pad(number='3', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, layers=Pad.LAYERS_THT, at=[p3x, p3y], size=[j_long_total, thickness], drill=[j_long_total, thickness], rotation=-angle))
    p4x, p4y = rot(mid_r, d)
    kicad_mod.append(Pad(number='4', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, layers=Pad.LAYERS_THT, at=[p4x, p4y], size=[j_long_total, thickness], drill=[j_long_total, thickness], rotation=-angle))
    d0 = 1.1
    h1x, h1y = rot(d0, -r_start)
    hole_func(kicad_mod, x=h1x, y=h1y, diameter=thickness)
    h2x, h2y = rot(-d0, r_start)
    hole_func(kicad_mod, x=h2x, y=h2y, diameter=thickness)
    h3x, h3y = rot(-r_start, -d0)
    hole_func(kicad_mod, x=h3x, y=h3y, diameter=thickness)
    h4x, h4y = rot(r_start, d0)
    hole_func(kicad_mod, x=h4x, y=h4y, diameter=thickness)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=1)
    else:
        return kicad_mod
def single_m4_4j(d=33.9, hole=33.9, d_screw=4, margin=4, zip=0):
    """绘制单个圆模块（居中显示）"""
    # ***<module>.single_m4_4j: Failure: Different bytecode
    kicad_mod = new_kicad_mod()
    center = 15
    rectangle_full(kicad_mod, center, center, w=30, h=15, layers=glayers_FB_Cu)
    w, h = (30, 15)
    cut = 5
    oct_pts = [[w / 2, h / 2 - cut], [w / 2 - cut, h / 2], [-w / 2 + cut, h / 2], [-w / 2, -h / 2 - cut], [-w / 2 + cut, -h / 2], [w / 2, -h / 2 + cut]]
    polygon_full(kicad_mod, center, center + 20, oct_pts, layers=glayers_FB_Cu, angle=0)
    return write_kicad_mod(kicad_mod, zip=zip)
def pb230(h=204, z=0):
    kicad_mod = new_kicad_mod(w=230, h=h, edge_layers=glayers_silk)
    for n, (i, d) in enumerate({2: 0.8, 2.54: 0.8, 5: 1, 10: 2}.items()):
        y = n * (h / 4)
        for xi in range(4):
            x = xi * 57.5
            di = d + xi * d / 16
            perfboard(kicad_mod, w=50, h=48, x=2.5 + x, y=y, interval=i, d=di, size=di * 1.2)
    return write_kicad_mod(kicad_mod, zip=z)
def perfboard(kicad_mod=None, w=100, h=100, x=0, y=0, interval=2.54, d=1, size=1.2, zip=0):
    """\n    创建多孔板(洞洞板)封装（左上角原点）\n    \n    参数:\n    kicad_mod: 现有的KiCad模块对象（可选）\n    w: 板子宽度(mm)\n    h: 板子高度(mm)\n    x, y: 左上角原点坐标(默认0,0)\n    interval: 孔间距(默认2.54mm)\n    d: 孔径(默认1mm)\n    size: 焊盘大小(直径, 默认1.2mm)\n    zip: 是否压缩输出(默认0)\n    \n    返回: KicadMod对象\n    """
    cols = math.floor(w / interval) + 1
    rows = math.floor(h / interval) + 1
    write_kicad = False
    if kicad_mod is None:
        kicad_mod = new_kicad_mod(text_at=[x + w / 2, y - 2], w=w, h=h, i=interval, d=d)
        write_kicad = True
    for col in range(cols):
        for row in range(rows):
            pad_x = x + col * interval
            pad_y = y + row * interval
            kicad_mod.append(Pad(number='', type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, at=[pad_x, pad_y], size=[size, size], drill=d, layers=Pad.LAYERS_THT))
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=zip)
    else:
        return kicad_mod
def draw_trapezoid(kicad_mod, x, y, long_side, short_side, h, angle, layers, width=1.6, sides=[0, 1, 2, 3], **ka):
    """\n    在指定位置绘制旋转梯形\n    \n    参数:\n    kicad_mod: KiCad模块对象\n    x, y: 长边中点坐标\n    long_side: 长边长度\n    short_side: 短边长度\n    h: 梯形高度\n    angle: 旋转角度(度)\n    layers: 绘图层\n    width: 线宽(默认1.6)\n    sides: 需要绘制的边列表 [0,1,2,3] 分别对应:\n        0: 长边（底边）\n        1: 右侧斜边\n        2: 短边（顶边）\n        3: 左侧斜边\n        默认绘制所有四条边\n    segments: 曲线分段数(默认10)\n    """
    angle_rad = math.radians(angle)
    long_left = (x - long_side / 2, y)
    long_right = (x + long_side / 2, y)
    short_left = (x - short_side / 2, y + h)
    short_right = (x + short_side / 2, y + h)
    points = [long_left, long_right, short_right, short_left]
    rotated_points = []
    for point in points:
        dx = point[0] - x
        dy = point[1] - y
        new_x = x + dx * math.cos(angle_rad) - dy * math.sin(angle_rad)
        new_y = y + dx * math.sin(angle_rad) + dy * math.cos(angle_rad)
        rotated_points.append((new_x, new_y))
    edges = [(rotated_points[0], rotated_points[1]), (rotated_points[1], rotated_points[2]), (rotated_points[2], rotated_points[3]), (rotated_points[3], rotated_points[0])]
    for edge_idx in sides:
        if 0 <= edge_idx < 4:
                start, end = edges[edge_idx]
                multi_dot_line(kicad_mod, dots=[start, end], layers=layers, width=width, **ka)
def b4x6(rows=4, itop=0, m6=6, zip=0, margin=1.5, cuw=15, cud=9):
    """创建4行6列紧密排列的圆形阵列，直径34.5mm"""
    # ***<module>.b4x6: Failure: Different bytecode
    d = 34.5
    cols = 6
    spacing = d
    total_width = cols * spacing + 2 * margin
    total_height = rows * spacing + 2 * margin
    start_x = margin + spacing / 2
    start_y = margin + spacing / 2
    kicad_mod = new_kicad_mod(w=total_width, h=total_height, itop=itop, time=U.stime()[12:20])
    round_rect(kicad_mod, total_width, total_height, a=5, sides=[1, 2])
    cx = total_width / 2
    cy = total_height / 2
    rectline_center(kicad_mod, cx, cy, cols * spacing, rows * spacing)
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y + row * spacing
            circle(kicad_mod, x, y, diameter=d, layers=glayers_silk)
            circle(kicad_mod, x, y, diameter=20, layers=glayers_silk)
            if col == 0:
                circle_filled(kicad_mod, x, y + 0.25, cuw - 1, layer=glayers_FB_Cu, lceda=1)
            kicad_mod.append(Pad(number=f'{row}-{col}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_CIRCLE, at=[x, y], size=[cud, cud], layers=glayers_F_Cu))
            m4_4j(kicad_mod, x, y, d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5, angle=35)
    for row in range(rows - 1):
        for col in range(cols - 1):
            x_hole = start_x + (col + 0.5) * spacing
            y_hole = start_y + (row + 0.5) * spacing
            non_plated_hole(kicad_mod, x_hole, y_hole, m6)
    de = 3 + margin
    for y in [de, total_height - de]:
        for x in [start_x + (col + 0.5) * spacing for col in range(cols - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for x in [de, total_width - de]:
        for y in [start_y + (row + 0.5) * spacing for row in range(rows - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for n, (x, y) in enumerate(edge_distance_turn(total_width, total_height, [de - 0.3, de - 0.3])):
        non_plated_hole(kicad_mod, x, y, 4)
    n12 = [[2, 4, 6, 12, 10, 8, 14, 16, 18, 24, 22, 20], [3, 5, 11, 9, 15, 17, 23, 21]]
    for row_group in range(rows):
        for col_group in range(0, cols - itop * 2, 2):
            x_center = (col_group + itop + 0.5) * spacing + start_x
            y_center = start_y + (row_group + 0.5) * spacing - spacing / 2
            dr = spacing / 2 - 1
            w = spacing + cuw + 2
            h = cuw
            rectangle_full(kicad_mod, x_center, y_center, w=w, h=h, layers=glayers_FB_Cu)
            text(kicad_mod, f'{n12[itop][U.ct(kicad_mod)]}', at=[x_center - 5, y_center], size=[8, 4], layers=glayers_silk)
    if itop == 1:
        ph = 4.9
        dx = (-4)
        dy = 18
        plated_hole(kicad_mod, dx, dy, ph, size=ph + 2)
        plated_hole(kicad_mod, dx, total_height - dy, ph, size=ph + 2)
        cx = margin + spacing * 0.5 - 1
        cy = margin + spacing * 0.5 - 3
        multi_dot_line(kicad_mod, [(dx, dy), (cx, dy)], width=8, layers=glayers_FB_Cu, segments=0)
        multi_dot_line(kicad_mod, [(dx, total_height - dy), (cx, total_height - dy)], width=8, layers=glayers_FB_Cu, segments=0)
        w = cuw
        h = spacing + cuw + 2
        we = cuw + 4
        rectangle_full(kicad_mod, cx, cy, w=we, h=we, layers=glayers_FB_Cu)
        rectangle_full(kicad_mod, cx, total_height - cy, w=we, h=we, layers=glayers_FB_Cu)
        cx = margin + spacing * 0.5
        rectangle_full(kicad_mod, total_width - cx, start_y + spacing * 0.5, w=w, h=h, layers=glayers_FB_Cu)
        rectangle_full(kicad_mod, total_width - cx, start_y + spacing * 2.5, w=w, h=h, layers=glayers_FB_Cu)
        h = spacing + cuw + 2 - 4
        cut = 5
        oct_pts = [[w / 2, h / 2 - cut], [w / 2 - cut, h / 2], [-w / 2 + cut, h / 2], [-w / 2, -h / 2 - cut], [-w / 2 + cut, -h / 2], [w / 2, -h / 2 + cut]]
        polygon_full(kicad_mod, cx, start_y + spacing * 1.5, oct_pts, layers=glayers_FB_Cu, angle=0)
    t = 20
    draw_trapezoid(kicad_mod=kicad_mod, x=0, y=total_height / 2, long_side=total_height, short_side=77, h=t, angle=90, layers=glayers_edge_pure, width=0.254, sides=[1, 2, 3])
    two_hole(kicad_mod, (-2), total_height / 2, 64, 4, angle=90, holes=[0, 1], hole_func=circle)
    m = 12 + itop
    m = 14
    yt = 8
    start_y = (total_height - (m - 1) * yt) / 2
    real = [[4, 2, 6, '', 10, 12, 8, 18, 14, 16, '', 20, 24, 22], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, '+']]
    for i in range(m):
        if real[itop][i]:
            x1 = (-3)
            y1 = start_y + i * yt
            text(kicad_mod, f'{real[itop][i]}', at=[x1 + 3, y1], size=[4, 2.5], layers=glayers_silk)
            if itop == 1 and i in (0, m - 1):
                kicad_mod.append(Pad(number=f'{i}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x1 + 3, y1], size=[2, 1], layers=['F.Cu', 'F.Paste', 'F.Mask']))
            else:
                kicad_mod.append(Pad(number=f'{i}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x1, y1], size=[2, 1], layers=['F.Cu', 'F.Paste', 'F.Mask']))
                rectangle_full(kicad_mod, x1, y1, w=3, h=3, layers=['F.Cu'])
                plated_hole(kicad_mod, x1, y1, 0.95, size=1)
            yh = total_height / 2 + (i - (m - 1) / 2) * (yt - 1)
            non_plated_hole(kicad_mod, x1 - 6, yh, 1.6)
            non_plated_hole(kicad_mod, x1 - 6.25, yh, 1.6)
            non_plated_hole(kicad_mod, x1 - 12, total_height / 2 + (i - (m - 1) / 2) * (yt - 3), 1.6)
            non_plated_hole(kicad_mod, x1 - 12.25, total_height / 2 + (i - (m - 1) / 2) * (yt - 3), 1.6)
            text(kicad_mod, f'{real[itop][i]}', at=[x1 - 5, yh], size=[2, 1.5], layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3x8(rows=3, itop=0, m6=6, zip=0, margin=1.5, cuw=20):
    """创建3行8列紧密排列的圆形阵列，直径34.5mm"""
    d = 34.5
    cols = 8
    spacing = d
    total_width = cols * spacing + 2 * margin
    total_height = rows * spacing + 2 * margin
    start_x = margin + spacing / 2
    start_y = margin + spacing / 2
    kicad_mod = new_kicad_mod(w=total_width, h=total_height, itop=itop, time=U.stime()[12:20])
    round_rect(kicad_mod, total_width, total_height, a=5)
    cx = total_width / 2
    cy = total_height / 2
    rectline_center(kicad_mod, cx, cy, cols * spacing, rows * spacing)
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y + row * spacing
            circle(kicad_mod, x, y, diameter=d, layers=glayers_silk)
            circle_filled(kicad_mod, x, y, cuw - 8, layer=glayers_FB_Cu, lceda=zip)
            if not zip:
                kicad_mod.append(KicadModTree.Circle(center=[x, y], radius=1, layer='F.Cu', width=cuw - 4))
            m4_4j(kicad_mod, x, y, d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5)
            plated_hole(kicad_mod, x, y, 5.8, size=6, shape=Pad.SHAPE_CIRCLE)
    for row in range(rows - 1):
        for col in range(cols - 1):
            x_hole = start_x + (col + 0.5) * spacing
            y_hole = start_y + (row + 0.5) * spacing
            non_plated_hole(kicad_mod, x_hole, y_hole, m6)
    de = 3 + margin
    for y in [de, total_height - de]:
        for x in [start_x + (col + 0.5) * spacing for col in range(cols - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for x in [de, total_width - de]:
        for y in [start_y + (row + 0.5) * spacing for row in range(rows - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for n, (x, y) in enumerate(edge_distance_turn(total_width, total_height, [de - 0.3, de - 0.3])):
        non_plated_hole(kicad_mod, x, y, 4)
    for row_group in range(2):
        for col_group in range(0, cols - itop - itop, 2):
            x_center = (col_group + itop + 1) * spacing
            y_center = start_y + (row_group + 0.5) * spacing
            dr = spacing / 2 - 1
            w = 2 * dr + cuw
            h = cuw
            rectangle_full(kicad_mod, x_center, y_center - dr, w=w, h=h, layers=glayers_FB_Cu)
            rectangle_full(kicad_mod, x_center, y_center + dr, w=w, h=h, layers=glayers_FB_Cu)
            text(kicad_mod, f'{U.ct(kicad_mod) + 1}', at=[x_center - 5, y_center], size=[8, 4], layers=['F.SilkS'])
    if itop == 1:
        ph = 4.9
        dx = dy = 4
        plated_hole(kicad_mod, dx, dy, ph, size=ph + 2)
        plated_hole(kicad_mod, total_width - dx, total_height - dy, ph, size=ph + 2)
        w = cuw
        h = 2 * dr + cuw
        cx = margin + spacing * 0.5 - 1
        we = 26
        rectangle_full(kicad_mod, cx, spacing * 0.5, w=we, h=we, layers=glayers_FB_Cu)
        rectangle_full(kicad_mod, total_width - cx, total_height - spacing * 0.5, w=we, h=we, layers=glayers_FB_Cu)
        cx = margin + spacing * 0.5
        rectangle_full(kicad_mod, total_width - cx, spacing * 1, w=w, h=h, layers=glayers_FB_Cu)
        rectangle_full(kicad_mod, cx, spacing * 2, w=w, h=h, layers=glayers_FB_Cu)
    return write_kicad_mod(kicad_mod, zip=zip)
def jk_BD6A24_bottom(W=73, zip=0):
    kicad_mod = new_kicad_mod(w=73, h=17.5, add_time=0)
    yh5 = 9
    non_plated_hole(kicad_mod, W - 4.5, yh5, 3)
    non_plated_hole(kicad_mod, 4.5, yh5, 3)
    rectline_center(kicad_mod, W - 4.5, 1, 9, 2, layers=glayers_edge_pure)
    rectline_center(kicad_mod, W - 14.7, 2.7, 11, 5.6, layers=glayers_edge_pure)
    rectline_center(kicad_mod, 8, 1, 16, 2, layers=glayers_edge_pure)
    rectline_center(kicad_mod, 22.3, 2.4, 10, 5.6, layers=glayers_edge_pure)
    x0, y0 = (W - 10.5, 9.3)
    size = [1, 1]
    drill_screw = 0.9
    def add_pad_pair(kmod, x, y, pin_num):
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_THT, shape=Pad.SHAPE_RECT, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x, y - 0.6], size=[1, 1.5], drill=0, layers=['F.Cu']))
    groups = [(x0, 15, 0), (x0 - 28.0 - 2.5 - 1.5, 11, 15)]
    dln = {}
    for start_x, pin_count, start_num in groups:
        for i in range(pin_count):
            n = start_num + i
            x = start_x - 2.0 * i
            add_pad_pair(kicad_mod, x, y0, f'{n}')
            layer = ['F.Cu', ('User.1', 'In1.Cu'), ('User.2', 'In2.Cu'), 'B.Cu'][n // 2 % 4]
            if py.istuple(layer):
                layer = layer[zip]
            if layer in dln:
                dln[layer] += 0.5
            else:
                dln[layer] = 1.3
            dy = dln[layer]
            dy = 1.2
            if n % 2 == 1 and n not in [25]:
                dy = 0.9
                multi_dot_line(kicad_mod, [(x, y0), (x, y0 + dy)], width=1, layers=layer)
            else:
                multi_dot_line(kicad_mod, [(x, y0), (x, y0 - dy)], width=1, layers=layer)
    multi_dot_line(kicad_mod, [(0, 17.8), (W, 17.8)], segments=10, width=1.6, layers=glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=zip)
def smt_array(n=12, spacing1=6, spacing2=2.54, spacing_y=3, width=1.0, height=1.5, h2=1, zip=0):
    """双排SMT焊盘阵列：上排用spacing1，下排用spacing2，垂直间距spacing_y，整体X居中于(0,0)"""
    w1 = (n - 1) * spacing1 if n > 1 else 0
    w2 = (n - 1) * spacing2 if n > 1 else 0
    total_width = max(w1, w2)
    total_height = spacing_y + height * 2
    kicad_mod = new_kicad_mod(w=total_width + 4, h=total_height, start=[-total_width / 2 - 2, total_height / 2], spacing1=spacing1, spacing2=spacing2)
    start_x1 = -w1 / 2
    start_x2 = -w2 / 2
    y1 = total_height - spacing_y / 2
    y2 = total_height + spacing_y / 2
    itop0 = [9, 5, 1, 10, 6, 2, 3, 7, 11, 4, 8, 12]
    real = ['4', '5', '12', '3', '6', '11', '10', '7', '2', '9', '8', '1']
    if n == 13:
        itop0 = U.range(n)
        real = [5, 13, 4, 6, 12, 11, 3, 7, 10, 8, 2, 9, 1]
    for i in range(n):
        pin_num = i + 1
        x1 = start_x1 + i * spacing1
        x2 = start_x2 + i * spacing2
        mid_n = abs(pin_num - 6)
        kicad_mod.append(Pad(number=f'{real[i]}-{pin_num}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x1, y1], size=[width, height], layers=['F.Cu', 'F.Paste', 'F.Mask']))
        text(kicad_mod, f'{real[i]}', at=[x1, y1 + 3], size=[3, 2], layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=zip)
def hole_array(W=100, zip=0):
    kicad_mod = new_kicad_mod(w=0, h=66, add_time=1)
    round_trapezoid(kicad_mod, 150, 100, 70)
    return write_kicad_mod(kicad_mod, zip=zip)
def jk_BD6A24_up(W=73, zip=0):
    kicad_mod = new_kicad_mod(w=73, h=17.5, add_time=0)
    yh5 = 9
    non_plated_hole(kicad_mod, 4.5, yh5, 3)
    non_plated_hole(kicad_mod, W - 4.5, yh5, 3)
    rectline_center(kicad_mod, 4.5, 1, 9, 2, layers=glayers_edge_pure)
    rectline_center(kicad_mod, 14.7, 2.7, 11, 5.6, layers=glayers_edge_pure)
    rectline_center(kicad_mod, W - 8, 1, 16, 2, layers=glayers_edge_pure)
    rectline_center(kicad_mod, W - 22.3, 2.4, 10, 5.6, layers=glayers_edge_pure)
    x0, y0 = (10.5, 9.3)
    size = [1, 1]
    drill_screw = 0.9
    def add_pad_pair(kmod, x, y, pin_num):
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_THT, shape=Pad.SHAPE_RECT, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
        kmod.append(Pad(number=pin_num, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x, y - 0.6], size=[1, 1.5], drill=0, layers=['F.Cu']))
    groups = [(x0, 15, 0), (x0 + 28.0 + 2.5 + 1.5, 11, 15)]
    dln = {}
    for start_x, pin_count, start_num in groups:
        for i in range(pin_count):
            n = start_num + i
            x = start_x + 2.0 * i
            add_pad_pair(kicad_mod, x, y0, f'{n}')
            layer = ['F.Cu', ('User.1', 'In1.Cu'), ('User.2', 'In2.Cu'), 'B.Cu'][n // 2 % 4]
            if py.istuple(layer):
                layer = layer[zip]
            if layer in dln:
                dln[layer] += 0.5
            else:
                dln[layer] = 1.3
            dy = dln[layer]
            dy = 1.2
            if n % 2 == 1 and n not in [25]:
                dy = 0.9
                multi_dot_line(kicad_mod, [(x, y0), (x, y0 + dy)], width=1, layers=layer)
            else:
                multi_dot_line(kicad_mod, [(x, y0), (x, y0 - dy)], width=1, layers=layer)
    multi_dot_line(kicad_mod, [(0, 17.8), (W, 17.8)], segments=10, width=1.6, layers=glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=zip)
def jk_BD6A24(W=73, zip=0):
    kicad_mod = new_kicad_mod(w=73, h=100)
    x = 36.5
    non_plated_hole(kicad_mod, 5, 5, 4)
    non_plated_hole(kicad_mod, W - 5, 5, 4)
    return write_kicad_mod(kicad_mod, zip=zip)
def box_header_254(kicad_mod=None, pins=16, rows=2, mount_holes=True, add_text=False):
    """\n    创建2.54mm间距牛角插座封装\n    :param kicad_mod: KiCad模块对象\n    :param pins: 总引脚数\n    :param rows: 行数 (1或2)\n    :param angle: 插座角度 (0=直插, 90=直角)\n    :param mount_holes: 是否添加安装孔\n    :param add_text: 是否添加文本标签\n    :return: KiCad模块对象\n    """
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    pitch = 2.54
    pad_size = [1, 1.6]
    drill_size = 0.9
    pin_rows = pins // rows
    width = (pin_rows - 1) * pitch
    height = (rows - 1) * pitch
    for row in range(rows):
        for col in range(pin_rows):
            pin_num = row * pin_rows + col + 1
            x = col * pitch
            y = row * pitch
            kicad_mod.append(Pad(number=pin_num, type=Pad.TYPE_THT, shape=Pad.SHAPE_RECT, layers=Pad.LAYERS_THT, at=[x, y], size=pad_size, drill=drill_size, rotation=0))
    if mount_holes:
        mount_hole_dia = 2.0
    outline_margin = 0.5
    outline_points = [[-pitch - outline_margin, -pitch - outline_margin], [width + pitch + outline_margin, -pitch - outline_margin], [width + pitch + outline_margin, height + pitch + outline_margin], [-pitch - outline_margin, height + pitch + outline_margin], [-pitch - outline_margin, -pitch - outline_margin]]
    for i in range(len(outline_points) - 1):
        kicad_mod.append(Line(start=outline_points[i], end=outline_points[i + 1], layer='F.SilkS', width=0.12))
    if add_text:
        text_pos = [width / 2, height + pitch + 1.5]
        kicad_mod.append(Text(text=f'{pins}P {rows}x{pin_rows}', at=text_pos, layer='F.SilkS', size=[1, 1]))
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=1)
    else:
        return kicad_mod
def mgn12c_rail_2block(kicad_mod=None, cx=0, y=0, wm=34.7, W=100, cut_rail_outline=True, zip=0):
    """创建MGN12C导轨安装模块（包含三角形支架和方块）"""
    hm = 27
    dh = 37.5 - hm
    x0 = cx - wm / 2
    cy = y + hm / 2
    yr = hm + dh
    for i in [(-2), (-1), 2, 3]:
        circle(kicad_mod, cx, y + yr + i * 25, 3)
    for i in range(2):
        non_plated_hole(kicad_mod, cx, y + yr + i * 25, 2.9)
    x2b = cx - wm / 2 + 5
    for x2 in [x2b, x2b + 20.8, x2b + 21]:
        non_plated_hole(kicad_mod, x2, 62.5, 2.9)
        non_plated_hole(kicad_mod, x2, 37.5, 2.9)
    mgn12c_block(kicad_mod=kicad_mod, x=cx, y=hm / 2, wm=wm)
    mgn12c_block(kicad_mod=kicad_mod, x=cx, y=W - hm / 2, wm=wm)
    if not cut_rail_outline:
        return
    else:
        wa = 0.8
        wa = 0
        multi_dot_line(kicad_mod, [(x0 + wa, y + hm + wa), (cx - 6 - wa, y + hm + wa), (cx - 6 - wa, W - hm - wa), (x0 + wa, W - hm - wa), (x0 + wa, y + hm + wa)], width=wa * 2, layers=glayers_edge_pure, segments=100)
        multi_dot_line(kicad_mod, [(x0 + wm - wa, y + hm + wa), (cx + 6 + wa, y + hm + wa), (cx + 6 + wa, W - hm - wa), (x0 + wm - wa, W - hm - wa), (x0 + wm - wa, y + hm + wa)], width=wa * 2, layers=glayers_edge_pure, segments=100)
def mgn12c_rail_2block_3(W=100, zip=0):
    kicad_mod = new_kicad_mod(w=W, h=W)
    wm = 34.7
    dx = (wm * 3 - 100) / 2
    x_spacing = 35
    x = 17.5
    mgn12c_rail_2block(kicad_mod, x, 0, cut_rail_outline=0)
    x = x + x_spacing
    mgn12c_rail_2block(kicad_mod, x, 0)
    x = x + x_spacing
    mgn12c_rail_2block(kicad_mod, x, 0)
    round_rect(kicad_mod, W, W, a=3)
    round_rect(kicad_mod, 35, W, a=2.4, width=1.6)
    hm = 27
    xru = 35
    non_plated_hole(kicad_mod, xru, hm / 2, 2.9)
    for xr in [xru - 25, xru, xru + 25, xru + 50]:
        non_plated_hole(kicad_mod, xr, hm / 2, 0.9)
    return write_kicad_mod(kicad_mod, zip=zip)
def b6x8(rows=6, itop=0, m6=6, zip=0, margin=1.5, cuw=20):
    """创建6行8列紧密排列的圆形阵列，直径34.5mm"""
    d = 34.5
    cols = 8
    spacing = d
    total_width = cols * spacing + 2 * margin
    total_height = rows * spacing + 2 * margin
    start_x = margin + spacing / 2
    start_y = margin + spacing / 2
    kicad_mod = new_kicad_mod(w=total_width, h=total_height, itop=itop, time=U.stime()[12:20])
    round_rect(kicad_mod, total_width, total_height, a=5)
    cx = total_width / 2
    cy = total_height / 2
    rectline_center(kicad_mod, cx, cy, cols * spacing, rows * spacing)
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y + row * spacing
            circle(kicad_mod, x, y, diameter=d, layers=glayers_silk)
            circle_filled(kicad_mod, x, y, cuw - 8, layer=glayers_FB_Cu, lceda=zip)
            if not zip:
                kicad_mod.append(KicadModTree.Circle(center=[x, y], radius=1, layer='F.Cu', width=cuw - 4))
            m4_4j(kicad_mod, x, y, d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5)
            plated_hole(kicad_mod, x, y, 5.8, size=6, shape=Pad.SHAPE_CIRCLE)
    for row in range(rows - 1):
        for col in range(cols - 1):
            x_hole = start_x + (col + 0.5) * spacing
            y_hole = start_y + (row + 0.5) * spacing
            non_plated_hole(kicad_mod, x_hole, y_hole, m6)
    de = 3 + margin
    for y in [de, total_height - de]:
        for x in [start_x + (col + 0.5) * spacing for col in range(cols - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for x in [de, total_width - de]:
        for y in [start_y + (row + 0.5) * spacing for row in range(rows - 1)]:
            non_plated_hole(kicad_mod, x, y, 4)
    for n, (x, y) in enumerate(edge_distance_turn(total_width, total_height, [de - 0.3, de - 0.3])):
        non_plated_hole(kicad_mod, x, y, 4)
    for row_group in range(0, rows - 1, 2):
        for col_group in range(0, cols + itop * 2, 2):
            x_center = start_x + (col_group + 0.5 - itop) * spacing
            y_center = start_y + (row_group + 0.5) * spacing
            dr = spacing / 2 - 1
            w = 2 * dr + cuw
            h = cuw
            if itop == 1 and col_group in (0, cols):
                    h = 30
            rectangle_full(kicad_mod, x_center, y_center - dr, w=w, h=h, layers=glayers_FB_Cu)
            rectangle_full(kicad_mod, x_center, y_center + dr, w=w, h=h, layers=glayers_FB_Cu)
            rectangle_full(kicad_mod, x_center - dr, y_center, w=h, h=w, layers=glayers_FB_Cu)
            rectangle_full(kicad_mod, x_center + dr, y_center, w=h, h=w, layers=glayers_FB_Cu)
            text(kicad_mod, f'{U.ct(kicad_mod) + 1}', at=[x_center - 5, y_center], size=[8, 4], layers=['F.SilkS'])
    if itop == 1:
        ph = 4.9
        plated_hole(kicad_mod, 6, 37.5, ph, size=ph + 2)
        plated_hole(kicad_mod, total_width - 6, total_height - 37.5, ph, size=ph + 2)
    return write_kicad_mod(kicad_mod, zip=zip)
def hex_nut_hole(kicad_mod=None, x=0, y=0, across_flats=5.5, angle=0, layers=glayers_edge_pure, crosshair=False):
    """\n    创建六边形螺母孔零件\n    across_flats: 六边形平行边距离(对边距离/Across Flats)\n    """
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    circumradius = across_flats / math.sqrt(3)
    dots = []
    for i in range(6):
        theta = math.radians(30 + angle + i * 60)
        dots.append((x + circumradius * math.cos(theta), y + circumradius * math.sin(theta)))
    dots.append(dots[0])
    polyline(kicad_mod, dots, layers=layers, width=0.15)
    if crosshair:
        cs = across_flats * 0.15
        polyline(kicad_mod, [(x - cs, y), (x + cs, y)], layers=layers, width=0.1)
        polyline(kicad_mod, [(x, y - cs), (x, y + cs)], layers=layers, width=0.1)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=0)
    else:
        return kicad_mod
def m4_14(kicad_mod=None, x=0, y=50, angle=0, base_hole_x=2.75, hole=3):
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    center = (x, y)
    base_center_x = 7
    hole_pos = rotate_point(x + base_hole_x, y, angle, *center)
    non_plated_hole(kicad_mod, *hole_pos, hole)
    circle_pos = rotate_point(x + base_center_x, y, angle, *center)
    circle(kicad_mod, *circle_pos, 4)
    rect_pos = rotate_point(x + base_center_x, y, angle, *center)
    rectline_center(kicad_mod, *rect_pos, 14, angle=angle)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=1)
    else:
        return kicad_mod
def mgn12c_bottom_gear(w=100, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w)
    wm = 34.7
    hm = 27
    dx = 5.85
    ka = dict(up_rail=2.5)
    mgn12c_block(kicad_mod, wm / 2 - dx, hm / 2, **ka)
    mgn12c_block(kicad_mod, 100 - wm / 2 + dx, hm / 2, angle=180, **ka)
    mgn12c_block(kicad_mod, wm / 2 - dx, 100 - hm / 2, **ka)
    mgn12c_block(kicad_mod, 100 - wm / 2 + dx, 100 - hm / 2, angle=180, **ka)
    dcube = 5
    dy = 12.5
    non_plated_hole(kicad_mod, dcube, 50 + dy, 2.9)
    rectline_center(kicad_mod, dcube, 50 + dy, 10)
    non_plated_hole(kicad_mod, dcube, 50 - dy, 2.9)
    rectline_center(kicad_mod, dcube, 50 - dy, 10)
    non_plated_hole(kicad_mod, 100 - dcube, 50 + dy, 2.9)
    rectline_center(kicad_mod, 100 - dcube, 50 + dy, 10)
    non_plated_hole(kicad_mod, 100 - dcube, 50 - dy, 2.9)
    rectline_center(kicad_mod, 100 - dcube, 50 - dy, 10)
    n = 4
    W, x0, y0 = (100, 50, 50)
    R = 35
    non_plated_hole(kicad_mod, x0, y0, 7.9)
    circle(kicad_mod, x0, y0, d=2 * R, crosshair=0, layers=glayers_Cmts)
    for i in range(4):
        angle = i * (2 * math.pi / 4)
        x, y = (x0 + R * math.cos(angle), y0 + R * math.sin(angle))
        circle(kicad_mod, x, y, d=17)
        non_plated_hole(kicad_mod, x, y, 5.9)
        text(kicad_mod, f'{i}', at=[x - 6, y], size=[2, 1.6], layers=glayers_silk)
    x0 = y0 = w / 2
    return write_kicad_mod(kicad_mod, zip=zip)
def mgn12c_bottom_m6(w=100, hole=43, bear_hole=5.9, zip=0):
    kicad_mod = new_kicad_mod(w=w, h=w, d=hole, b=bear_hole)
    wm = 34.7
    hm = 27
    dx = 5.85
    ka = dict(up_rail=2.5)
    mgn12c_block(kicad_mod, wm / 2 - dx, hm / 2, **ka)
    mgn12c_block(kicad_mod, 100 - wm / 2 + dx, hm / 2, angle=180, **ka)
    mgn12c_block(kicad_mod, wm / 2 - dx, 100 - hm / 2, **ka)
    mgn12c_block(kicad_mod, 100 - wm / 2 + dx, 100 - hm / 2, angle=180, **ka)
    dcube = 5
    dy = 12.5
    non_plated_hole(kicad_mod, dcube, 50 + dy, 2.9)
    rectline_center(kicad_mod, 7, 50, 14)
    non_plated_hole(kicad_mod, dcube, 50 - dy, 2.9)
    non_plated_hole(kicad_mod, 100 - dcube, 50 + dy, 2.9)
    non_plated_hole(kicad_mod, 100 - dcube, 50 - dy, 2.9)
    n = 4
    W, x0, y0 = (100, 50, 50)
    R = 35
    circle(kicad_mod, x0, y0, d=2 * R, crosshair=1)
    non_plated_hole(kicad_mod, x0, y0, hole)
    for i in range(4):
        angle = i * 1.5708
        x, y = (x0 + R * math.cos(angle), y0 + R * math.sin(angle))
        circle(kicad_mod, x, y, d=17)
        if i == 0:
            circle(kicad_mod, x, y, d=25)
        non_plated_hole(kicad_mod, x, y, bear_hole)
        text(kicad_mod, f'{i}', at=[x - 6, y], size=[2, 1.6], layers=glayers_silk)
    text(kicad_mod, f'n=4,d=49.5,D={2 * R}', at=[x - 40, (-10)], size=[4, 3], layers=glayers_Cmts)
    x, y = (x0 + R, y0)
    step_motor_42(kicad_mod, *rotate_point(x + 12.5, y, 0, x, y), d=5, angle=45)
    return write_kicad_mod(kicad_mod, zip=zip)
def mgn12c_z_board_m6(n=4, **ka):
    g2 = 1.4142135623730951
    return mgn12c_z_board(n=4, d=35 * g2, hex_a=0, hole=5.9, angle_offset=0, **ka)
def mgn12c_z_board(n=10, d=24.12, hex_a=4.45, hole=3, bear_hole=8.9, angle_offset=18, zip=0):
    W = 100
    kicad_mod = new_kicad_mod(w=W, h=W, n=n, d=d)
    r = d / 2
    r2 = 5
    R = r / math.sin(math.pi / n)
    D = 2 * R
    Ri = R - r
    Ri2 = R - r2
    Di2 = D - r2 * 2
    if n == 0:
        return
    else:
        x0, y0 = (W / 2, W / 2)
        non_plated_hole(kicad_mod, x0, y0, 9.9)
        xd = 14.5
        non_plated_hole(kicad_mod, x0 - xd, y0, 4)
        non_plated_hole(kicad_mod, x0 + xd, y0, 4)
        non_plated_hole(kicad_mod, x0, y0, 17.4)
        kicad_mod.append(Circle(center=[x0, y0], radius=R, layer='F.SilkS', width=0.15))
        kicad_mod.append(Circle(center=[x0, y0], radius=Ri, layer='F.SilkS', width=0.15))
        circle(kicad_mod, x0, y0, d=Di2)
        theta = 2 * math.pi / n
        for i in range(n):
            angle = i * theta + math.radians(angle_offset)
            x = x0 + R * math.cos(angle)
            y = y0 + R * math.sin(angle)
            circle(kicad_mod, x, y, d=r)
            if hex_a:
                hex_nut_hole(kicad_mod, x, y, hex_a, layers=glayers_edge_pure)
            non_plated_hole(kicad_mod, x, y, hole)
            text(kicad_mod, f'{i}', at=[x - 6, y], size=[2, 1.6], layers=glayers_silk)
        text(kicad_mod, f'n={n},d={d},D={D},Di={Ri * 2},Di2={Di2}', at=[x - 40, (-10)], size=[4, 3], layers=glayers_Cmts)
        crosshair(kicad_mod, x0, y0, w=W, h=W)
        wm = 34.7
        hm = 27
        dcube = 5
        dy = 12.5
        non_plated_hole(kicad_mod, dcube, 50 + dy, 2.9)
        non_plated_hole(kicad_mod, dcube, 50 - dy, 2.9)
        non_plated_hole(kicad_mod, 100 - dcube, 50 + dy, 2.9)
        non_plated_hole(kicad_mod, 100 - dcube, 50 - dy, 2.9)
        non_plated_hole(kicad_mod, 50 + dy, dcube, 2.9)
        non_plated_hole(kicad_mod, 50 - dy, dcube, 2.9)
        non_plated_hole(kicad_mod, 50 + dy, 100 - dcube, 2.9)
        non_plated_hole(kicad_mod, 50 - dy, 100 - dcube, 2.9)
        rectline_center(kicad_mod, 9, hm / 2, 8, 12, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 9, 100 - hm / 2, 8, 12, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 91, hm / 2, 8, 12, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 91, 100 - hm / 2, 8, 12, layers=glayers_edge_pure)
        hd = 10.1
        rectline_center(kicad_mod, 5, hm / 2, hd, hm, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 95, hm / 2, hd, hm, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 5, 100 - hm / 2, hd, hm, layers=glayers_edge_pure)
        rectline_center(kicad_mod, 95, 100 - hm / 2, hd, hm, layers=glayers_edge_pure)
        return write_kicad_mod(kicad_mod, zip=zip)
def mgn12c_block_up_rail_x(w=100, h=32.2, zip=0):
    """ 拼板 """
    kicad_mod = new_kicad_mod(w=w, h=h, edge_layers=glayers_Cmts)
    hm = 27
    y = h - hm / 2
    wm = 34.7
    dx = w / 3
    x0 = dx / 2
    mgn12c_block(kicad_mod, x0, y, up_rail=4.75, angle=180)
    mgn12c_block(kicad_mod, x0 + dx * 1, y, up_rail=4.75)
    mgn12c_block(kicad_mod, x0 + dx * 2, y, up_rail=4.75)
    multi_dot_line(kicad_mod, [(dx, (-1)), (dx, h + 2)], width=1.6, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(dx * 2, (-1)), (dx * 2, h + 2)], width=1.6, layers=glayers_edge_pure)
    yc = h - hm - 0.8
    multi_dot_line(kicad_mod, [((-1), yc), (101, yc)], width=1.6, segments=2, layers=glayers_edge_pure)
    for x in range(1, 99, 1):
        plated_hole(kicad_mod, x, h - hm - 0.4, 0.6)
    return write_kicad_mod(kicad_mod, zip=zip)
def fs100p():
    # ***<module>.fs100p: Failure: Different bytecode
    min_x, max_x = ((-24.13984), 30.86016)
    min_y, max_y = ((-12.0926), 12.1074)
    W, H = (max_x - min_x, max_y - min_y)
    W = 50.5
    H = 22.6
    kicad_mod = new_kicad_mod(w=W, h=H, edge_layers=glayers_Cmts, start=[(-24.14), (-11.3)])
    ref_x, ref_y = (3.36016, (-12.0926))
    kicad_mod.append(Text(type='reference', text='REF-fs100p', at=[ref_x, ref_y], layer='F.SilkS', size=[1, 1], thickness=0.15))
    val_x, val_y = (3.36016, 12.1074)
    kicad_mod.append(Text(type='value', text='fs100p', at=[val_x, val_y], layer='F.Fab', size=[1, 1], thickness=0.15))
    silk_lines = [[(-24.13984), (-11.2926), 26.36016, (-11.2926)], [(-24.13984), (-8.8726), (-21.59984), (-8.8726)], [(-24.13984), 8.9074, (-24.13984), (-8.8726)], [(-24.13984), 8.9074, (-21.59984), 8.9074], [(-24.13984), 11.3074, (-24.13984), (-11.2926)], [(-24.13984), 11.3074, 26.36016, 11.3074], [(-21.59984), 8.9074, (-21.59984), (-8.8726)], [19.05985, (-11.17), 24.13985, (-11.17)], [19.05985, (-8.63), 19.05985, (-11.17)], [19.05985, 11.17, 19.05985, 8.63], [19.05985, 11.17, 24.13985, 11.17], [24.13985, (-8.63), 24.13985, 8.63], [26.36016, (-7.9926), 30.86016, (-7.9926)], [26.36016, 8.0074, 30.86016, 8.0074], [26.36016, 11.3074, 26.36016, (-11.2926)], [30.86016, 8.0074, 30.86016, (-7.9926)]]
    for line in silk_lines:
        kicad_mod.append(Line(start=line[:2], end=line[2:], layer='F.SilkS', width=0.2))
    pad_size = 1.5
    drill_size = 0.9
    pads = [(1, (-22.86984), 7.6374, 90), (2, (-22.86984), 5.0974, 90), (3, (-22.86984), 2.5574, 90), (4, (-22.86984), 0.0174, 90), (5, (-22.86984), (-2.5226), 90), (6, (-22.86984), (-5.0626), 90), (7, (-22.86984), (-7.6026), 90), (8, 20.32985, (-9.9), 0), (9, 22.86985, (-9.9), 0), (10, 22.86985, 9.9, 0), (11, 20.32985, 9.9, 0)]
    for num, x, y, rot in pads:
        kicad_mod.append(Pad(number=num, type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, at=[x, y], rotation=rot, size=[pad_size, pad_size], drill=drill_size, layers=Pad.LAYERS_THT))
    return write_kicad_mod(kicad_mod, zip=1)
def b_2x2_m3_4j(d=33.9, hole=33.9, margin=4, zip=0):
    """绘制四个上下左右对称的圆模块（基于圆中心距离d）"""
    # ***<module>.b_2x2_m3_4j: Failure: Different bytecode
    mod_size = d * 2
    kicad_mod = new_kicad_mod(w=mod_size, h=mod_size)
    center = mod_size / 2
    dh = d - 3
    def d_hole(kicad_mod, x, y, ad):
        non_plated_hole(kicad_mod, x, y, ad)
        circle(kicad_mod, x, y, 10)
    d_hole(kicad_mod, center + dh, center, 5.9)
    d_hole(kicad_mod, center - dh, center, 5.9)
    d_hole(kicad_mod, center, center + dh, 5.9)
    d_hole(kicad_mod, center, center - dh, 5.9)
    d_hole(kicad_mod, center, center, 5.9)
    offset = d / 2
    positions = [(center - offset, center - offset), (center + offset, center - offset), (center - offset, center + offset), (center + offset, center + offset)]
    rectangle_full(kicad_mod, center - offset, center, w=20, h=66, layers=glayers_FB_Cu)
    rectangle_full(kicad_mod, center + offset, center, w=20, h=66, layers=glayers_FB_Cu)
    func_d_list = [(m4_4j, dict(d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5, inner_delta=0.1)), (m4_4j, dict(d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5, inner_delta=0.15)), (m4_4j, dict(d=1.2, thickness=1.6, j_long=1, hole_func=plated_hole, hole=5.8, size=6.5, inner_delta=0.2))]
    for n, (x, y) in enumerate(positions):
        circle(kicad_mod, x, y, hole, layers='F.SilkS', width=0.02)
        circle_filled(kicad_mod, x, y, 20, layers=glayers_FB_Mask)
        func, ka = func_d_list[n]
        func(kicad_mod, x, y, **ka)
    text(kicad_mod, f'd={d}', at=[center, mod_size + 5], size=[3, 2.5], layers='F.Cmts.User')
    return write_kicad_mod(kicad_mod, zip=zip)
def m3_4j(kicad_mod=None, x=0, y=0, d=1.4, thickness=1.2, j_long=1.4, hole_func=non_plated_hole):
    """创建M3四爪螺母的Kicad封装"""
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    circle(kicad_mod, x, y, 12.4, crosshair=1, layers=glayers_FB_Cu, width=0.1)
    circle(kicad_mod, x, y, 12, crosshair=0, layers=glayers_FB_Cu, width=0.1)
    hole_func(kicad_mod, x, y, 4)
    r_end = 6.2 - thickness / 2
    r_start = r_end - j_long
    num_holes = max(1, int(j_long / 0.2))
    for i in range(num_holes + 1):
        r = r_start + i * (j_long / num_holes)
        hole_func(kicad_mod, x + d, y - r, thickness)
        hole_func(kicad_mod, x - d, y + r, 1.2)
        hole_func(kicad_mod, x - r, y - d, 1.2)
        hole_func(kicad_mod, x + r, y + d, 1.2)
    text(kicad_mod, f'd={d} j={j_long} t={thickness}', at=[x + 14.5, y], size=[2, 1.6], layers=glayers_silk)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=1)
    else:
        return kicad_mod
def m4_4j_old(kicad_mod=None, x=0, y=0, d=1.3, thickness=1.8, j_long=1, D=15, hole=5.8, hole_func=non_plated_hole, add_text=False):
    """创建M4四爪螺母的Kicad封装  j_long 实际 是j_long+thickness 圆直径占据 """
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
    circle(kicad_mod, x=x, y=y, d=D, crosshair=1, layers='F.Cu', width=0.1)
    circle(kicad_mod, x=x, y=y, d=11, crosshair=0, layers='F.Cu', width=0.1)
    hole_func(kicad_mod, x=x, y=y, diameter=hole)
    r_end = D / 2 - thickness / 2
    r_start = r_end - j_long
    num_holes = max(1, int(j_long / 0.2))
    for i in range(num_holes + 1):
        r = r_start + i * (j_long / num_holes)
        hole_func(kicad_mod, x=x + d, y=y - r, diameter=thickness)
        hole_func(kicad_mod, x=x - d, y=y + r, diameter=thickness)
        hole_func(kicad_mod, x=x - r, y=y - d, diameter=thickness)
        hole_func(kicad_mod, x=x + r, y=y + d, diameter=thickness)
        if i == 0:
            d0 = 1.1
            hole_func(kicad_mod, x=x + d0, y=y - r, diameter=thickness)
            hole_func(kicad_mod, x=x - d0, y=y + r, diameter=thickness)
            hole_func(kicad_mod, x=x - r, y=y - d0, diameter=thickness)
            hole_func(kicad_mod, x=x + r, y=y + d0, diameter=thickness)
            kicad_mod.append(Pad(number=f'{x}-{y - r},{thickness}', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, layers=Pad.LAYERS_THT, at=[x + d, y - r - 0.5], size=[1.616, 3], drill=[1.5, 2.6]))
    if add_text:
        text(kicad_mod, f'd={d} j={j_long} t={thickness}', at=[x + 16.5, y], size=[2, 1.6], layers='F.SilkS')
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=1)
    else:
        return kicad_mod
def circle_on_circle(n, d=24.12, bear_hole=8.9, angle_offset=0, zip=0):
    W = 100
    kicad_mod = new_kicad_mod(w=W, h=W, add_time=1)
    r = d / 2
    r2 = 5
    R = r / math.sin(math.pi / n)
    D = 2 * R
    Ri = R - r
    Ri2 = R - r2
    Di2 = D - r2 * 2
    if n == 0:
        return
    else:
        x0, y0 = (W / 2, W / 2)
        non_plated_hole(kicad_mod, x0, y0, 9.9)
        xd = 14.5
        non_plated_hole(kicad_mod, x0 - xd, y0, 4)
        non_plated_hole(kicad_mod, x0 + xd, y0, 4)
        non_plated_hole(kicad_mod, x0, y0, 17.4)
        non_plated_hole(kicad_mod, x0, y0, 43)
        kicad_mod.append(Circle(center=[x0, y0], radius=R, layer='F.SilkS', width=0.15))
        kicad_mod.append(Circle(center=[x0, y0], radius=Ri, layer='F.SilkS', width=0.15))
        circle(kicad_mod, x0, y0, d=Di2)
        theta = 2 * math.pi / n
        for i in range(n):
            angle = i * theta + math.radians(angle_offset)
            x = x0 + R * math.cos(angle)
            y = y0 + R * math.sin(angle)
            circle(kicad_mod, x, y, d=d)
            circle(kicad_mod, x, y, d=6, layers=glayers_Cmts)
            circle(kicad_mod, x, y, d=8.9, layers=glayers_Cmts)
            circle(kicad_mod, x, y, d=25)
            non_plated_hole(kicad_mod, x, y, 5.9)
            text(kicad_mod, f'{i}', at=[x - 6, y], size=[2, 1.6], layers=glayers_silk)
        text(kicad_mod, f'n={n},d={d},D={D},Di={Ri * 2},Di2={Di2}', at=[x - 40, (-10)], size=[4, 3], layers=glayers_Cmts)
        crosshair(kicad_mod, x0, y0, w=W, h=W)
        wm = 34.7
        hm = 27
        dx = 5.85
        ka = dict(up_rail=2.5)
        mgn12c_block(kicad_mod, wm / 2 - dx, hm / 2, **ka)
        mgn12c_block(kicad_mod, 100 - wm / 2 + dx, hm / 2, angle=180, **ka)
        mgn12c_block(kicad_mod, wm / 2 - dx, 100 - hm / 2, **ka)
        mgn12c_block(kicad_mod, 100 - wm / 2 + dx, 100 - hm / 2, angle=180, **ka)
        dcube = 5
        dy = 12.5
        non_plated_hole(kicad_mod, dcube, 50 + dy, 2.9)
        non_plated_hole(kicad_mod, dcube, 50 - dy, 2.9)
        non_plated_hole(kicad_mod, 100 - dcube, 50 + dy, 2.9)
        non_plated_hole(kicad_mod, 100 - dcube, 50 - dy, 2.9)
        return write_kicad_mod(kicad_mod, zip=zip)
def mgn12c_rail_triangle_2(wm=36.5, W=100, zip=0):
    kicad_mod = new_kicad_mod(w=W, h=W, add_time=1)
    hm = 27
    xmid = 32.65
    y0 = (100 - 2 * wm) / 2 - hm / 2
    ka = dict(dh=10.5)
    mgn12c_rail_triangle(kicad_mod, xmid - wm, y0, **ka)
    dxm = 1.8
    mgn12c_rail_triangle(kicad_mod, xmid + dxm, y0, **ka)
    mgn12c_rail_triangle(kicad_mod, xmid + wm, y0, **ka)
    ka = {}
    xmid += 17.35
    y0 += hm / 2 + 100 - hm
    mgn12c_block(kicad_mod, xmid - wm, y0, **ka)
    mgn12c_block(kicad_mod, xmid + dxm, y0, **ka)
    mgn12c_block(kicad_mod, xmid + wm, y0, **ka)
    return write_kicad_mod(kicad_mod, zip=zip)
def jp57_silk_angle_ray(W=570, H=167, zip=0):
    """创建带角度射线的JP57网格丝印（精细版）"""
    import math
    kicad_mod = new_kicad_mod(w=W, h=H)
    grid_spacing = 10
    silk_line_width = 0.1
    silk_layer = 'F.SilkS'
    text_size = 1.0
    ray_length = (W ** 2 + H ** 2) ** 0.5
    for angle in range(0, 91, 10):
        angle_rad = math.radians(angle)
        end_x = ray_length * math.cos(angle_rad)
        end_y = ray_length * math.sin(angle_rad)
        kicad_mod.append(Line(start=(0, 0), end=(end_x, end_y), layer=silk_layer, width=0.5))
    fine_ray_length = W - 11
    fine_text_offset = (-2)
    for fine_angle in range(1, 33):
        angle_rad = math.radians(fine_angle)
        end_x = fine_ray_length * math.cos(angle_rad)
        end_y = fine_ray_length * math.sin(angle_rad)
        if 16 < fine_angle:
            for ia in range(999):
                text_y = end_y + fine_text_offset * math.sin(angle_rad)
                if text_y > H - fine_angle:
                    fine_ray_length -= 1
                    end_x = fine_ray_length * math.cos(angle_rad)
                    end_y = fine_ray_length * math.sin(angle_rad)
                else:
                    break
        ap = 100
        kicad_mod.append(Line(start=(end_x, end_y), end=(end_x + ap * math.cos(angle_rad), end_y + ap * math.sin(angle_rad)), layer=silk_layer, width=0.25))
        text_x = end_x + fine_text_offset * math.cos(angle_rad)
        text_y = end_y + fine_text_offset * math.sin(angle_rad)
        kicad_mod.append(Text(type='user', text=f'{fine_angle}°', at=(text_x, text_y), layer=silk_layer, size=(4, 4), halign='center', valign='center'))
    fine_ray_length = 580
    for fine_angle in range(130, 170, 2):
        angle_rad = math.radians(fine_angle / 10)
        end_x = fine_ray_length * math.cos(angle_rad)
        end_y = fine_ray_length * math.sin(angle_rad)
        ap = 50
        kicad_mod.append(Line(start=(end_x, end_y), end=(end_x + ap * math.cos(angle_rad), end_y + ap * math.sin(angle_rad)), layer=silk_layer, width=0.1))
    return write_kicad_mod(kicad_mod, zip=zip)
def jp57_silk(W=100, H=100, margin=7, zip=0):
    """创建带1cm×1cm网格丝印及刻度标记的Kicad模块"""
    kicad_mod = new_kicad_mod(w=W, h=H)
    grid_spacing = 10
    silk_line_width = 0.1
    silk_layer = 'F.SilkS'
    unit = 2
    cm = 10
    for y in range(0, H + 1, grid_spacing):
        kicad_mod.append(Line(start=(0, y), end=(W, y), layer=silk_layer, width=silk_line_width))
    for x in range(0, W + 1, grid_spacing):
        kicad_mod.append(Line(start=(x, 0), end=(x, H), layer=silk_layer, width=silk_line_width))
    for i in range(0, max(W, H) + 1):
        iu = unit
        if i % cm == 0:
            iu = unit * 3
        else:
            if i % (cm // 2) == 0:
                iu = unit * 2
        if i <= W:
            kicad_mod.append(Line(start=(i, H), end=(i, H - iu), layer=silk_layer, width=0.1))
            kicad_mod.append(Line(start=(i, 0), end=(i, iu), layer=silk_layer, width=0.1))
        if i <= H:
            kicad_mod.append(Line(start=(0, i), end=(iu, i), layer=silk_layer, width=0.1))
            kicad_mod.append(Line(start=(W, i), end=(W - iu, i), layer=silk_layer, width=0.1))
    text_size = 2.0
    text_offset = 1.5
    for x in range(0, W + 1, 50):
        if x > 0 and x < W:
                kicad_mod.append(Text(type='user', text=f'{x // 10}', at=(x, H - text_offset), layer=silk_layer, size=(text_size, text_size), halign='center', valign='top'))
                kicad_mod.append(Text(type='user', text=f'{x // 10}', at=(x, text_offset), layer=silk_layer, size=(text_size, text_size), halign='center', valign='bottom'))
    for y in range(0, H + 1, 50):
        if y > 0 and y < H:
                kicad_mod.append(Text(type='user', text=f'{y // 10}', at=(text_offset, y), layer=silk_layer, size=(text_size, text_size), halign='left', valign='center', angle=90))
                kicad_mod.append(Text(type='user', text=f'{y // 10}', at=(W - text_offset, y), layer=silk_layer, size=(text_size, text_size), halign='right', valign='center', angle=90))
    for x in range(0, W + 10, 10):
        kicad_mod.append(Text(type='user', text=f'{x // 10}', at=(x - 5, margin), layer=silk_layer, size=(5, 2)))
        kicad_mod.append(Text(type='user', text=f'{x // 10}', at=(x - 5, H - 5 - margin), layer=silk_layer, size=(5, 2)))
    for x in range(50, W, 50):
        for y in range(50, H, 50):
            if x % grid_spacing == 0 and y % grid_spacing == 0:
                    kicad_mod.append(Text(type='user', text=f'{x // 10},{y // 10}', at=(x, y), layer=silk_layer, size=(text_size, text_size), halign='center', valign='center'))
    kicad_mod.append(Text(type='user', text=f'{W // 10},{H // 10}', at=(W - margin, H - margin), layer=silk_layer, size=(text_size, text_size), halign='right', valign='top'))
    return write_kicad_mod(kicad_mod, zip=zip)
def jp57_cu(W=570, H=170, zip=0):
    kicad_mod = new_kicad_mod(w=W, h=H)
    simple_serpentine(kicad_mod, W / 2, H / 2, W, H, w=0.4, interval=0.2)
    return write_kicad_mod(kicad_mod, zip=zip)
def simple_serpentine(kicad_mod, x, y, W, H, w=0.4, interval=0.2, layer='F.Cu'):
    """简单蛇形走线函数（起点和终点都在左侧）\n    x, y: 蛇形走线区域的中心坐标\n    W: 走线区域宽度\n    H: 走线区域高度\n    w: 线宽\n    interval: 线间距\n    layer: 走线所在层\n    """
    margin = max(min(w * 2, 1), 0.5)
    margin_x = margin + w
    start_x = x - W / 2 + w * 0.5
    start_y = y - H / 2 + w * 0.8
    eff_width = W - 2 * margin
    eff_height = H - 2 * margin
    pitch = w + interval
    num_lines = max(2, int(eff_height / pitch))
    if num_lines % 2!= 0:
        num_lines += 1
    actual_height = num_lines * pitch
    center_offset = (eff_height - actual_height) / 2
    current_y = start_y + margin + center_offset
    points = []
    direction = 1
    for i in range(num_lines):
        if direction == 1:
            x1 = start_x + margin_x
            x2 = start_x + eff_width
        else:
            x1 = start_x + eff_width
            x2 = start_x + margin_x
        points.append([(x1, current_y), (x2, current_y)])
        if i < num_lines - 1:
            next_y = current_y + pitch
            points.append([(x2, current_y), (x2, next_y)])
            current_y = next_y
            direction *= (-1)
    for start, end in points:
        kicad_mod.append(Line(start=start, end=end, layer=layer, width=w))
    pdx = 5 / w
    pdy = 0.2
    rectangle_full(kicad_mod, start_x + margin + w * pdx / 1.5, points[0][0][1] - w * pdy, w=w * pdx, h=w * (1 + pdy / 2), layers=[layer, 'F.Mask'])
    last_point = points[(-1)][0] if points[(-1)][0][0] < points[(-1)][1][0] else points[(-1)][1]
    rectangle_full(kicad_mod, start_x + margin + w * pdx / 1.5, last_point[1] + w * pdy, w=w * pdx, h=w * (1 + pdy / 2), layers=[layer, 'F.Mask'])
    return kicad_mod
def m6_square_16x16(kicad_mod, x, y, d=7, layers=glayers_silk):
    rectline_center(kicad_mod, x, y, w=16, width=0.1, crosshair=1, layers=layers)
    non_plated_hole(kicad_mod, x, y, d=d)
def round_rect(kicad_mod=None, mod_w=100, mod_h=100, a=8, width=0.254, zip=1, sides=None, arc_angle=60, **ka):
    """绘制圆角边框\n    参数:\n        mod_w: 矩形宽度 (mm)\n        mod_h: 矩形高度 (mm)\n        a: 圆角半径 (mm)\n        width: 线宽 (mm)\n        sides: 需要绘制的圆角边 [0:左上, 1:右上, 2:右下, 3:左下]\n        \n    通用说明:\n        仅需修改下方的 arc_angle 即可切换圆弧角度，自动保证中心对称\n        支持0~90之间任意角度，改完不用动其他参数\n    """
    write_kicad = False
    if not kicad_mod:
        kicad_mod = new_kicad_mod(f'round_rect {mod_w},{mod_h},{a} {U.stime()[12:17]}', w=mod_w, h=mod_h)
        write_kicad = True
    wa = width
    if not sides:
        sides = [0, 1, 2, 3]
    offset_angle = (90 - arc_angle) / 2
    offset_rad = math.radians(offset_angle)
    r = a + wa / 2
    if 0 in sides:
        start_x = a - r * math.cos(offset_rad)
        start_y = a - r * math.sin(offset_rad)
        arc(kicad_mod, center=[a, a], start=[start_x, start_y], angle=arc_angle, layers=glayers_edge_pure, width=wa)
    if 1 in sides:
        start_x = mod_w - a + r * math.sin(offset_rad)
        start_y = a - r * math.cos(offset_rad)
        arc(kicad_mod, center=[mod_w - a, a], start=[start_x, start_y], angle=arc_angle, layers=glayers_edge_pure, width=wa)
    if 2 in sides:
        start_x = mod_w - a + r * math.cos(offset_rad)
        start_y = mod_h - a + r * math.sin(offset_rad)
        arc(kicad_mod, center=[mod_w - a, mod_h - a], start=[start_x, start_y], angle=arc_angle, layers=glayers_edge_pure, width=wa)
    if 3 in sides:
        start_x = a - r * math.sin(offset_rad)
        start_y = mod_h - a + r * math.cos(offset_rad)
        arc(kicad_mod, center=[a, mod_h - a], start=[start_x, start_y], angle=arc_angle, layers=glayers_edge_pure, width=wa)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=zip)
    else:
        return kicad_mod
def filled_circle(W=100, zip=0):
    kicad_mod = new_kicad_mod()
    circle(kicad_mod, 0, 0, 33, crosshair=0, layers=glayers_FB_Cu, width=0)
    return write_kicad_mod(kicad_mod, zip=zip)
def pcbnew_filled_circle(W=100):
    footprint = pcbnew.FOOTPRINT(None)
    footprint.SetReference('FILLED_CIRCLE')
    footprint.SetValue('FilledCircle')
    footprint.SetPosition(pcbnew.VECTOR2I(0, 0))
    circle = pcbnew.PCB_SHAPE()
    circle.SetShape(pcbnew.S_CIRCLE)
    circle.SetCenter(pcbnew.VECTOR2I(0, 0))
    radius_nm = int(pcbnew.FromMM(W / 2))
    circle.SetStart(pcbnew.VECTOR2I(radius_nm, 0))
    circle.SetLayer(pcbnew.F_Cu)
    circle.SetWidth(99999)
    footprint.Add(circle)
    return footprint
def b_8x6(d=35.5, hole=33.9, aluminum=False, margin=4, zip=0, cols=8, rows=6, round_edge=True):
    """绘制8列×6行的圆网格函数（无间隙、无颜色区分、带序号文本和模块中心大圆）"""
    mod_w = 2 * margin + cols * d
    mod_h = 2 * margin + rows * d - margin
    kicad_mod = new_kicad_mod(f'b{cols}x{rows}_d{d}_margin{margin}_a{aluminum}_{U.stime()[12:17]}', w=mod_w, h=mod_h)
    if round_edge:
        a = 12
        day = 0
        ay = a + day
        wa = 1
        arc(kicad_mod, center=[a, ay], start=[0 - wa / 2, ay], angle=90, layers=glayers_edge_pure, width=wa)
        arc(kicad_mod, center=[mod_w - a, ay], start=[mod_w - a, 0 - wa / 2 + day], angle=90, layers=glayers_edge_pure, width=wa)
        arc(kicad_mod, center=[mod_w - a, mod_h - ay], start=[mod_w + wa / 2, mod_h - ay], angle=90, layers=glayers_edge_pure, width=wa)
        arc(kicad_mod, center=[a, mod_h - ay], start=[a, mod_h + wa / 2 - day], angle=90, layers=glayers_edge_pure, width=wa)
    idx = 1
    da = (d - hole) / 2 + 0.05
    dy = -(margin / 2)
    for yi in range(rows):
        base_y = margin + d / 2 + yi * d + dy
        if yi % 2 == 0:
            current_y = base_y + da
        else:
            current_y = base_y - da
        if yi % 2 == 1:
            prev_base_y = margin + d / 2 + (yi - 1) * d + dy
            prev_y = prev_base_y + da
            midpoint_y = (prev_y + current_y) / 2
            rectline_center(kicad_mod, mod_w / 2, midpoint_y, w=mod_w - 6, h=50, width=0.1, crosshair=1, layers=glayers_silk)
        for xi in range(cols):
            x = margin + d / 2 + xi * d
            circle(kicad_mod, x, current_y, hole, crosshair=not aluminum, layers=glayers_silk, width=0.02)
            circle(kicad_mod, x, current_y, 16, crosshair=1, layers=glayers_Cmts, width=0.1)
            if aluminum:
                circle(kicad_mod, x, current_y, hole, crosshair=0, layers=glayers_edge_pure)
                if yi % 2 == 1:
                    xd = 18
                    cr = 8
                    ca = 33
                    arc_start_end(kicad_mod, center=[x - xd, midpoint_y], radius=cr, start_angle=-ca, end_angle=ca, layers=glayers_edge_pure)
                    arc_start_end(kicad_mod, center=[x + xd, midpoint_y], radius=cr, start_angle=-ca - 180, end_angle=ca - 180, layers=glayers_edge_pure)
            else:
                n = yi * rows + xi
                m3_4j(kicad_mod, x, current_y, d=1.3 + n * 0.06)
                dia = hole
                circle_filled(kicad_mod, x, current_y, dia, layers=glayers_FB_Cu, lceda=zip)
                circle_filled(kicad_mod, x, current_y, dia - 6, layers=glayers_FB_Mask, lceda=zip)
                if yi % 2 == 1:
                    rectangle_full(kicad_mod, x, midpoint_y, w=24, h=50, layers=glayers_FB_Cu)
            idx += 1
    for yi in range(rows + 1):
        for xi in range(cols + 1):
            x = margin + xi * d
            y = margin + yi * d + dy
            ds = 4
            if xi in [0]:
                x += 2
            if xi in [cols]:
                x -= 2
            if yi in [0]:
                y += ds
            if yi in [rows]:
                y -= ds
            bx = xi % 2 == 1
            by = yi % 2 == 1
            if (bx or by) and (not (bx and by)):
                    circle(kicad_mod, x, y, 12, layers=glayers_silk)
                    if yi in (1, 3, 5) and xi not in (0, 8):
                        if aluminum:
                            non_plated_hole(kicad_mod, x, y, d=5.9)
                    else:
                        non_plated_hole(kicad_mod, x, y, d=5.9)
                    non_plated_hole(kicad_mod, x, y, d=5.9)
    text(kicad_mod, f'{mod_w}x{mod_h} d={d} margin={margin}', at=[mod_w / 2, mod_h + 5], size=[d / 5, d / 5], layers=glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=zip)
def hexagonal_packing(n=37, d=33, zip=0):
    """生成1，7，19，37，61，91，127，169，217，271...（OEIS:A003215） 数量圆的六边形密堆积（基于中心六边形数规律）"""
    import math
    r = d / 2
    circles = []
    if n < 1:
        raise ValueError('圆数量n必须≥1')
    else:
        if n == 1:
            k = 0
        else:
            k = int(math.sqrt((n - 1) / 3 + 0.25) - 0.5)
            while 1 + 3 * (k + 1) * (k + 2) <= n:
                k += 1
            total = 1 + 3 * k * (k + 1)
            if total!= n:
                print(f'警告：n={n}不是中心六边形数，自动生成最接近的{total}个圆（壳层数k={k}）')
        for q in range(-k, k + 1):
            for r_coord in range(-k, k + 1):
                s = -q - r_coord
                if abs(s) > k:
                    continue
                else:
                    x = (2 * q + r_coord) * r
                    y = math.sqrt(3) * r_coord * r
                    circles.append((x, y))
        assert len(circles) == total, f'生成失败：{len(circles)}个圆（应为{total}个）'
        min_x = min((p[0] for p in circles))
        max_x = max((p[0] for p in circles))
        min_y = min((p[1] for p in circles))
        max_y = max((p[1] for p in circles))
        module_w = (max_x - min_x + d) * 1.02
        module_h = (max_y - min_y + d) * 1.02
        offset_x = module_w / 2 - (max_x + min_x) / 2
        offset_y = module_h / 2 - (max_y + min_y) / 2
        circles_abs = [(x + offset_x, y + offset_y) for x, y in circles]
        kicad_mod = new_kicad_mod(name=f'hex_{total}circles_d{d}', w=module_w, h=module_h)
        colors = [[0, 0, 0]] + [[1 - i / k, i / k, 0] for i in range(1, k + 1)]
        if len(colors) < k + 1:
            colors += [[0, 0, 1]] * (k + 1 - len(colors))
        skip_count = 0
        for idx, (x, y) in enumerate(circles_abs, 1):
            circle(kicad_mod, x, y, d, layers=glayers_silk)
            q = (x - offset_x) / d - (y - offset_y) / (math.sqrt(3) * d)
            r_coord = (y - offset_y) / (math.sqrt(3) * d)
            shell = max(abs(round(q)), abs(round(r_coord)), abs(round(-q - r_coord)))
            if idx in [1, 5, 35, 61, 57, 27, 36, 44, 51, 28, 37, 45, 52]:
                skip_count += 1
            else:
                text(kicad_mod, f'{idx - skip_count} ', at=[x, y], size=[d / 10, d / 10], layers=glayers_FB_Cu, color=colors[min(shell, k)])
            if len(circles_abs) == 61 and idx == 31:
                    circle(kicad_mod, x, y, 270, layers=glayers_FB_Cu)
        text(kicad_mod, f'密堆积：{total}圆（壳层数k={k}，直径{d}mm）', at=[module_w / 2, module_h + 5], size=[d / 8, d / 8], layers=glayers_FB_Cu)
        text(kicad_mod, f'中心六边形数：1 + 3k(k+1) = {total}（相邻间距={d}mm）', at=[module_w / 2, module_h + 15], size=[d / 8, d / 8], layers=glayers_FB_Cu)
        return write_kicad_mod(kicad_mod, zip=zip)
def c127(d=33, zip=0):
    """生成127个圆的密堆积（修正间距错误，确保相邻圆心距=直径d）"""
    import math
    r = d / 2
    circles = []
    for q in range((-6), 7):
        for r_coord in range((-6), 7):
            s = -q - r_coord
            if abs(s) > 6:
                continue
            else:
                x = (2 * q + r_coord) * r
                y = math.sqrt(3) * r_coord * r
                circles.append((x, y))
    assert len(circles) == 127, f'总圆数错误：{len(circles)}（应为127）'
    if len(circles) > 1:
        dx = circles[1][0] - circles[0][0]
        dy = circles[1][1] - circles[0][1]
        dist = math.hypot(dx, dy)
        assert abs(dist - d) < 0.1, f'间距错误：{dist:.1f}mm（应为{d}mm）'
    min_x = min((p[0] for p in circles))
    max_x = max((p[0] for p in circles))
    min_y = min((p[1] for p in circles))
    max_y = max((p[1] for p in circles))
    module_w = (max_x - min_x + d) * 1.02
    module_h = (max_y - min_y + d) * 1.02
    offset_x = module_w / 2 - (max_x + min_x) / 2
    offset_y = module_h / 2 - (max_y + min_y) / 2
    circles_abs = [(x + offset_x, y + offset_y) for x, y in circles]
    kicad_mod = new_kicad_mod(name=f'hex_127密堆积_d{d}', w=module_w, h=module_h)
    colors = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1]]
    for idx, (x, y) in enumerate(circles_abs, 1):
        circle(kicad_mod, x, y, d, layers=glayers_silk)
        q = (x - offset_x) / d - (y - offset_y) / (math.sqrt(3) * d)
        r_coord = (y - offset_y) / (math.sqrt(3) * d)
        shell = max(abs(round(q)), abs(round(r_coord)), abs(round(-q - r_coord)))
        text(kicad_mod, str(idx), at=[x, y], size=[d / 10, d / 10], layers=glayers_FB_Cu, color=colors[min(shell, 6)])
    text(kicad_mod, f'密堆积：127圆（直径{d}mm，间距{d}mm，完美相切）', at=[module_w / 2, module_h + 5], size=[d / 8, d / 8], layers=glayers_FB_Cu)
    text(kicad_mod, f'验证：相邻圆心距={dist:.1f}mm（理论{d}mm）', at=[module_w / 2, module_h + 15], size=[d / 8, d / 8], layers=glayers_FB_Cu)
    return write_kicad_mod(kicad_mod, zip=zip)
def hexagonal_packing_3layer(d=33, zip=0):
    import math
    a = d
    circles = [(0.0, 0.0)]
    R2 = a
    angles2 = [math.radians(30 + 60 * i) for i in range(6)]
    for angle in angles2:
        x = R2 * math.cos(angle)
        y = R2 * math.sin(angle)
        circles.append((x, y))
    R3 = 2 * a * math.cos(math.pi / 6)
    angles3 = [math.radians(60 * i) for i in range(6)]
    for angle in angles3:
        x = R3 * math.cos(angle)
        y = R3 * math.sin(angle)
        circles.append((x, y))
    R3a = 2 * a
    angles3a = [math.radians(30 + 60 * i) for i in range(6)]
    for angle in angles3a:
        x = R3a * math.cos(angle)
        y = R3a * math.sin(angle)
        circles.append((x, y))
    max_xy = max((math.hypot(x, y) for x, y in circles)) + a / 2
    module_size = 2 * max_xy * 1.02
    center = module_size / 2
    circles_abs = [(x + center, y + center) for x, y in circles]
    kicad_mod = new_kicad_mod(name=f'hex_3layer_d{d}', w=module_size, h=module_size)
    for idx, (x, y) in enumerate(circles_abs, 1):
        circle(kicad_mod, x, y, a, layers=glayers_silk)
        color = [1, 0, 0] if idx <= 13 else [0, 0, 1]
        text(kicad_mod, str(idx), at=[x, y], size=[a / 6, a / 6], layers=glayers_FB_Cu, color=color)
    text(kicad_mod, f'3a公式推导：R3a=2a（d={d}mm时={2 * a}mm，与第2/3层相切）', at=[center, module_size + 5], size=[a / 5, a / 5], layers=glayers_FB_Cu)
    text(kicad_mod, f'Layers=3+3a, Total=19, R3={R3:.1f}mm', at=[center, module_size + 15], size=[a / 5, a / 5], layers=glayers_FB_Cu)
    return write_kicad_mod(kicad_mod, zip=zip)
def add_footprint_to_pcb(fp_path='C:\\Program Files\\KiCad\\9.0\\share\\kicad\\footprints\\Symbol.pretty\\Symbol_Danger_18x16mm_Copper.kicad_mod'):
    import os
    import pcbnew
    IU_PER_MM = 1000000
    board = pcbnew.GetBoard()
    lib_path = os.path.dirname(fp_path)
    footprint_name = os.path.splitext(os.path.basename(fp_path))[0]
    footprint = pcbnew.FootprintLoad(lib_path, footprint_name)
    if footprint is None:
        raise RuntimeError(f'无法加载封装: {fp_path}')
    else:
        board_bbox = board.GetBoardEdgesBoundingBox()
        center_x = board_bbox.GetX() + board_bbox.GetWidth() / 2
        center_y = board_bbox.GetY() + board_bbox.GetHeight() / 2
        position = pcbnew.VECTOR2I(int(center_x), int(center_y))
        footprint.SetPosition(position)
        footprint.SetReference('DNG')
        board.Add(footprint)
        mm_x = center_x / IU_PER_MM
        mm_y = center_y / IU_PER_MM
        return f'成功添加封装 \'{footprint.GetReference()}\' 到位置 ({mm_x:.2f}mm, {mm_y:.2f}mm)'
def packed_circles_in_circle(D=100, d=10, zip=0):
    import math
    import random
    def pack_circles(D, d):
        """\n        Packs small circles of diameter d into a large circle of diameter D.\n        This version tries to place circles until a certain number of consecutive failures.\n        """
        R = D / 2
        r = d / 2
        packed_circles = []
        if r > R:
            return []
        else:
            max_failures = 1000
            failures = 0
            while failures < max_failures:
                angle = random.uniform(0, 2 * math.pi)
                distance_from_center = math.sqrt(random.uniform(0, 1)) * (R - r)
                x = distance_from_center * math.cos(angle)
                y = distance_from_center * math.sin(angle)
                overlap = False
                for cx, cy in packed_circles:
                    if math.sqrt((x - cx) ** 2 + (y - cy) ** 2) < d:
                        overlap = True
                        break
                if not overlap:
                    packed_circles.append((x, y))
                    failures = 0
                else:
                    failures += 1
            return packed_circles
    kicad_mod = new_kicad_mod(name=f'packed_circles_D{D}_d{d}', w=D, h=D)
    center_x = D / 2
    center_y = D / 2
    circle(kicad_mod, center_x, center_y, radius=D / 2, layers=glayers_silk)
    small_circles = pack_circles(D, d)
    for x, y in small_circles:
        non_plated_hole(kicad_mod, center_x + x, center_y + y, d)
    info_text = f'D={D}, d={d}, Count={len(small_circles)}'
    text(kicad_mod, info_text, at=[D / 2, (-5)], size=[1, 1], layers=glayers_FB_Cu + glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=zip)
def super_capacitor_500F_6(W=100, H=100, D=35.5, pin_distance=15, zip=0):
    kicad_mod = new_kicad_mod(w=W, h=H)
    via_params = dict(type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, size=[0.6, 0.6], drill=0.3, layers=['*.Cu'])
    def super_capacitor_500F(kicad_mod, x, y):
        circle(kicad_mod, x, y, radius=D / 2, layers=glayers_silk, width=0.1)
        circle(kicad_mod, x, y, radius=D / 2 - 5, layers=glayers_silk, width=0.12)
        circle(kicad_mod, x, y, radius=6.5, layers=glayers_silk, width=0.1)
        pka = dict(type=Pad.TYPE_THT, shape=Pad.SHAPE_RECT, size=[12, 3], drill=[9.4, 1.4], layers=Pad.LAYERS_THT)
        kicad_mod.append(Pad(number='1', at=[x - 11, y], rotation=90, **pka))
        kicad_mod.append(Pad(number='2', at=[x + 6, y + 5], rotation=0, **pka))
        pad1_x, pad1_y = (x - 11, y)
        for dx in range((-5), 6, 2):
            for dy in range((-5), 6, 2):
                kicad_mod.append(Pad(number=0, at=[pad1_x + dx, pad1_y + dy], **via_params))
        pad2_x, pad2_y = (x + 6, y + 5)
        for dx in range((-5), 6, 2):
            for dy in range((-5), 6, 2):
                kicad_mod.append(Pad(number=0, at=[pad2_x + dx, pad2_y + dy], **via_params))
    y = 50 - D
    super_capacitor_500F(kicad_mod, 32, y)
    super_capacitor_500F(kicad_mod, 32, y + D)
    super_capacitor_500F(kicad_mod, 32, y + D * 2)
    super_capacitor_500F(kicad_mod, W - 32, y)
    super_capacitor_500F(kicad_mod, W - 32, y + D)
    super_capacitor_500F(kicad_mod, W - 32, y + D * 2)
    plated_hole(kicad_mod, 13, y + D, 4.9, size=12, shape=Pad.SHAPE_RECT)
    plated_hole(kicad_mod, 11, y + D * 2, 4.9, size=12, shape=Pad.SHAPE_RECT)
    y = 0
    for i in range(1, 10):
        y = y + i * 2
        plated_hole(kicad_mod, 92, y, i, size=i * 1.5, shape=Pad.SHAPE_RECT)
    if zip:
        for dx in range(2, 100, 3):
            for dy in range(2, 100, 3):
                kicad_mod.append(Pad(number=3, at=[dx, dy], **via_params))
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_8x7_full_parking(D=33.2, zip=True):
    layers = glayers_silk + glayers_FB_Cu
    import math
    grid_rows = 8
    grid_cols_max = 7
    R = D / 2.0
    step_x = D
    step_y = D * math.sqrt(3) / 2
    W = (grid_cols_max - 1) * step_x + D
    H = (grid_rows - 1) * step_y + D
    kicad_mod = new_kicad_mod(name=f'Circle_8x7_D{D}_Interstitial_v2', w=W, h=H, edge_layers=glayers_edge_fsilk)
    circle_count_large = 0
    circle_count_small = 0
    large_circle_centers = []
    for r in range(grid_rows):
        y_current = R + r * step_y
        x_start = R
        cols_in_this_row = grid_cols_max
        if r % 2!= 0:
            x_start += R
            cols_in_this_row = grid_cols_max - 1
        for c in range(cols_in_this_row):
            cx = x_start + c * step_x
            cy = y_current
            circle(kicad_mod, cx, cy, radius=R, layers=layers)
            text(kicad_mod, circle_count_large + 1, at=[cx, cy], size=[3, 3], layers=layers)
            large_circle_centers.append((cx, cy))
            circle_count_large += 1
    d_small = 3.9
    r_small = d_small / 2.0
    centers_set = {(round(cx, 5), round(cy, 5)) for cx, cy in large_circle_centers}
    small_circles_to_add = py.set()
    for cx, cy in large_circle_centers:
        p_right = (round(cx + step_x, 5), round(cy, 5))
        p_upper_right = (round(cx + R, 5), round(cy + step_y, 5))
        p_upper_left = (round(cx - R, 5), round(cy + step_y, 5))
        p_lower_left = (round(cx - R, 5), round(cy - step_y, 5))
        p_lower_right = (round(cx + R, 5), round(cy - step_y, 5))
        if p_right in centers_set and p_upper_right in centers_set:
                small_cx = round((cx + p_right[0] + p_upper_right[0]) / 3, 5)
                small_cy = round((cy + p_right[1] + p_upper_right[1]) / 3, 5)
                small_circles_to_add.add((small_cx, small_cy))
        if p_right in centers_set and p_lower_right in centers_set:
                small_cx = round((cx + p_right[0] + p_lower_right[0]) / 3, 5)
                small_cy = round((cy + p_right[1] + p_lower_right[1]) / 3, 5)
                small_circles_to_add.add((small_cx, small_cy))
    for scx, scy in small_circles_to_add:
        circle(kicad_mod, scx, scy, radius=r_small, layers=layers)
        circle_count_small += 1
    info_text = f'W:{W:.2f} H:{H:.2f} Large:{circle_count_large} Small:{circle_count_small}'
    text(kicad_mod, info_text, at=[W / 2, (-5)], size=[1, 1], layers=glayers_FB_Cu + glayers_Cmts)
    rectangle_outline(kicad_mod, 0, (H - 225) / 2, w=217, h=225, layers=layers)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_52_full_parking(D=32.5, zip=0):
    import math
    grid_rows = 7
    grid_cols_max = 8
    R = D / 2.0
    step_x = D
    step_y = D * math.sqrt(3) / 2
    W = (grid_cols_max - 1) * step_x + D
    H = (grid_rows - 1) * step_y + D
    kicad_mod = new_kicad_mod(name=f'Circle_8x7_D{D}_Packing_49pcs_Corrected', w=W, h=H, edge_layers=glayers_edge_fsilk)
    layers = glayers_silk + glayers_FB_Cu
    circle_count = 0
    for r in range(grid_rows):
        y_current = R + r * step_y
        x_start = R
        cols_in_this_row = grid_cols_max
        if r % 2!= 0:
            x_start += R
            cols_in_this_row = grid_cols_max - 1
        for c in range(cols_in_this_row):
            x_current = x_start + c * step_x
            if c == 0 and r in [2, 4, 6]:
                    continue
            circle(kicad_mod, x_current, y_current, radius=R, layers=layers)
            text(kicad_mod, circle_count + 1, at=[x_current, y_current], size=[3, 3], layers=layers)
            circle_count += 1
    info_text = f'W:{W:.2f} H:{H:.2f} Count:{circle_count}'
    text(kicad_mod, info_text, at=[W / 2, (-5)], size=[1, 1], layers=glayers_FB_Cu + glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_8x6_full_parking(D=33, zip=0):
    import math
    grid_rows = 8
    grid_cols = 6
    R = D / 2.0
    step_x = D
    step_y = D * math.sqrt(3) / 2
    W = (grid_cols - 1) * step_x + D
    H = (grid_rows - 1) * step_y + D
    kicad_mod = new_kicad_mod(name=f'Circle_8x6_D{D}_Packing', w=W, h=H, edge_layers=glayers_edge_fsilk)
    layers = glayers_silk + glayers_FB_Cu
    y_current = R
    circle_count = 0
    for r in range(grid_rows):
        x_current = R
        cols_in_this_row = grid_cols
        if r % 2!= 0:
            x_current += R
            cols_in_this_row -= 1
        for c in range(cols_in_this_row):
            circle(kicad_mod, x_current, y_current, radius=R, layers=layers)
            circle_count += 1
            x_current += step_x
        y_current += step_y
    info_text = f'W:{W:.2f} H:{H:.2f} Count:{circle_count}'
    text(kicad_mod, info_text, at=[W / 2, (-5)], size=[1, 1], layers=glayers_FB_Cu + glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=zip)
def full_parking_circle(W=272, H=250, D=33, zip=0):
    import math
    kicad_mod = new_kicad_mod(name=f'full_parking_circle_{W}x{H}_D{D}', w=W, h=H, edge_layers=glayers_edge_fsilk)
    layers = glayers_silk + glayers_FB_Cu
    R = D / 2.0
    step_x = D
    step_y = D * math.sqrt(3) / 2
    y_current = R
    row_index = 0
    circle_count = 0
    max_x_used, max_y_used = (0, 0)
    while y_current <= H - R:
        x_current = R
        if row_index % 2!= 0:
            x_current += R
        while x_current <= W - R:
            circle(kicad_mod, x_current, y_current, radius=R, layers=layers)
            circle_count += 1
            if x_current + R > max_x_used:
                max_x_used = x_current + R
            x_current += step_x
        if y_current + R > max_y_used:
            max_y_used = y_current + R
        y_current += step_y
        row_index += 1
    info_text = f'Actual W: {max_x_used:.2f}, H: {max_y_used:.2f}, Count: {circle_count}'
    text(kicad_mod, info_text, at=[W / 2, (-5)], size=[1, 1], layers=glayers_FB_Cu + glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_3x3_aluminum(W=100, H=100, zip=0):
    kicad_mod = new_kicad_mod(w=W, h=H, text_at=[W / 2, (-5)], edge_layers=glayers_edge_fsilk)
    d = W / 3
    for yi in range(3):
        for xi in range(3):
            x = (xi + 0.5) * d
            y = (yi + 0.5) * d
            non_plated_hole(kicad_mod, x, y, d=3.85)
    non_plated_hole(kicad_mod, 0.5 * d, 0.5 * d, d=4.85)
    non_plated_hole(kicad_mod, 1.5 * d, 0.5 * d, d=5.85)
    non_plated_hole(kicad_mod, 2.5 * d, 0.5 * d, d=7.85)
    return write_kicad_mod(kicad_mod, zip=zip)
def link_bar(W=347, H=180, bar_width=7.0, cut_width=1.2, zip=0):
    if zip:
        test_layer = []
    else:
        test_layer = ['B.Cu', 'B.Mask']
    kicad_mod = new_kicad_mod(name=f'Link_Bar_{W}x{H}={U.stime()[12:17]}', w=W, h=H, text_at=[W / 2, (-5)], edge_layers=glayers_edge_fsilk)
    rectline_center(kicad_mod, W / 2, H / 2, w=W, h=66, width=0.01, crosshair=1, layers=glayers_silk + test_layer)
    dry = 44.5
    rectline_center(kicad_mod, W / 2, H / 2 + dry, w=W, h=23, width=0.01, crosshair=1, layers=glayers_silk + test_layer)
    rectline_center(kicad_mod, W / 2, H / 2 - dry, w=W, h=23, width=0.01, crosshair=1, layers=glayers_silk + test_layer)
    end_margin = 5.0
    num_bars = int((W + cut_width) / (bar_width + cut_width))
    total_content_width = num_bars * bar_width + (num_bars - 1) * cut_width
    start_x_offset = (W - total_content_width) / 2
    bar_height = H - 2 * end_margin
    for i in range(num_bars):
        bar_start_x = start_x_offset + i * (bar_width + cut_width)
        bar_center_x = bar_start_x + bar_width / 2
        rectangle_full(kicad_mod, bar_center_x, H / 2, w=bar_width, h=bar_height, layers=glayers_F_Cu)
        rectangle_full(kicad_mod, bar_center_x, H / 2 + 33 + 12, w=bar_width, h=24, layers=glayers_F_Mask)
        rectangle_full(kicad_mod, bar_center_x, H / 2 - 33 - 12, w=bar_width, h=24, layers=glayers_F_Mask)
        rectline_center(kicad_mod, bar_center_x, H / 2, w=bar_width, h=bar_height, width=0.01, crosshair=1, layers=['F.SilkS'] + test_layer)
        non_plated_hole(kicad_mod, bar_center_x, H / 2, d=2.9)
        rectangle_full(kicad_mod, bar_center_x, H / 2, w=bar_width, h=8, layers=glayers_F_Mask)
        dhy = 70
        yna = H / 2 + dhy + (i + 1) // 8 * 0.05
        non_plated_hole(kicad_mod, bar_center_x, yna, d=2.9)
        rectangle_full(kicad_mod, bar_center_x, yna, w=bar_width, h=8, layers=glayers_F_Mask)
        ynb = yna = H / 2 - dhy - (i + 1) // 8 * 0.05
        non_plated_hole(kicad_mod, bar_center_x, ynb, d=2.9)
        rectangle_full(kicad_mod, bar_center_x, ynb, w=bar_width, h=8, layers=glayers_F_Mask)
        text(kicad_mod, bar_center_x, H / 2 - 33 + 3, t=i % 24 + 1, size=3, layers=['F.SilkS'] + test_layer)
        if i < num_bars - 1:
            cutout_center_x = bar_start_x + bar_width + cut_width / 2
            rectangle_full(kicad_mod, cutout_center_x, H / 2, w=cut_width, h=bar_height, layers=glayers_edge_pure)
            rectangle_full(kicad_mod, bar_start_x, 5 - cut_width / 2, w=2, h=cut_width, layers=glayers_edge_pure)
            rectangle_full(kicad_mod, bar_start_x + bar_width, 5 - cut_width / 2, w=2, h=cut_width, layers=glayers_edge_pure)
            yc = H - (5 - cut_width / 2)
            rectangle_full(kicad_mod, bar_start_x, yc, w=2, h=cut_width, layers=glayers_edge_pure)
            rectangle_full(kicad_mod, bar_start_x + bar_width, yc, w=2, h=cut_width, layers=glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_8x6(W=272, H=250, zip=0):
    kicad_mod = new_kicad_mod(name=f'b3265_8x6={W}x{H}={U.stime()[12:17]}', w=W, h=H, text_at=[W / 2, (-4)], edge_layers=glayers_edge_fsilk)
    d32 = 32.5
    gap = W / 8 - d32
    step_x = d32 + gap
    step_y = d32 + gap
    step_x = step_y = 34
    start_x = (W - 272) / 2 + 17.0
    start_y = (H - 204) / 2 + 17.0
    U.set('x,y mid', [W / 2, start_y + 85.0])
    for c in range(8):
        for r in range(6):
            center_x = start_x + c * step_x
            center_y = start_y + r * step_y
            circle(kicad_mod, center_x, center_y, radius=d32 / 2, width=0.1, layers=glayers_silk)
            strong_plated_hole(kicad_mod, center_x, center_y, d=3.9, size=10, cu_size=11.8, number=f'{c + 1}-{r + 1}')
    rectline_center(kicad_mod, *U.get('x,y mid'), w=272, h=204, width=0.01, crosshair=1, layers=glayers_silk + [])
    num_gb30 = 24
    for i in range(num_gb30):
        x = (i + 0.5) * (W / num_gb30)
        gb30(kicad_mod, x, 11.5, number=25 - i, mask='F.Mask')
        gb30(kicad_mod, x, H - 11.5, number=i + 1, mask='B.Mask')
    xm = W / 2
    ym = H / 2
    dx = 103
    non_plated_hole(kicad_mod, x=xm, y=ym, d=9.9)
    hole_rect_center(kicad_mod, xm, ym, side_len_x=98, angle=45, d=5.9)
    return write_kicad_mod(kicad_mod, zip=zip)
def gb30(kicad_mod, x, y, d=3.9, number=0, mask='B.Mask', **ka):
    """ 铝型材 国标 30 弹片 m4"""
    rectline_center(kicad_mod, x, y, w=9, h=23, width=0.05, crosshair=1, layers=glayers_silk + [])
    multi_dot_line(kicad_mod, [(x, y - 8.8), (x, y + 8.6)], width=7, layers=glayers_FB_Cu + [mask])
    ka['d'] = 3.9
    ka['size'] = 8
    ka['number'] = number
    if mask == 'F.Mask':
        plated_hole(kicad_mod, x, y + 5.5, **ka)
        plated_hole(kicad_mod, x, y - 5.5, **ka)
        plated_hole(kicad_mod, x, y - 6, **ka)
    if mask == 'B.Mask':
        plated_hole(kicad_mod, x, y - 5.5, **ka)
        plated_hole(kicad_mod, x, y + 5.5, **ka)
        plated_hole(kicad_mod, x, y + 6, **ka)
def b3265_7x7(W=244, H=274.5, zip=0):
    kicad_mod = new_kicad_mod(name=f'b3265_7x7_{W}x{H}', w=W, h=H, text_at=[W + 2, H / 2], edge_layers=glayers_edge_fsilk)
    d32 = 32.5
    grid_size = 7
    gap = 2.0
    step_x = d32 + gap
    step_y = d32 + gap
    total_grid_width = (grid_size - 1) * step_x + d32
    total_grid_height = (grid_size - 1) * step_y + d32
    start_x = d32 / 2 + gap + 0.25
    start_y = start_x + 8
    for c in range(grid_size):
        for r in range(grid_size):
            center_x = start_x + c * step_x
            center_y = start_y + r * step_y
            if c == r == 3:
                    U.set('x,y mid', [center_x, center_y])
            circle(kicad_mod, center_x, center_y, radius=d32 / 2, width=1, layers=glayers_silk)
            strong_plated_hole(kicad_mod, center_x, center_y, d=3.9, size=10, cu_size=12, number=f'{c + 1}-{r + 1}')
    rectline_center(kicad_mod, *U.get('x,y mid'), w=239.5, width=0.1, crosshair=1, layers=glayers_FB_Cu)
    num_gb30 = 24
    for i in range(num_gb30):
        x = (i + 0.5) * (W / num_gb30)
        gb30(kicad_mod, x, H - 11.5, number=i + 1)
    return write_kicad_mod(kicad_mod, zip=zip)
def b3265_5x5(W=258, zip=0):
    """ 244x275  价格 0.88\n    244x274.5  免费\n"""
    H = W
    kicad_mod = new_kicad_mod(name=f'Circle_Grid_5x5_D32.5_{W}x{H}', w=W, h=H, text_at=[W + 2, H / 2])
    d32 = 32.5
    grid_size = 5
    step_x = W / grid_size
    step_y = H / grid_size
    step_x = step_y = d32 + 2
    start_x = step_x / 2
    start_y = step_y / 2
    for c in range(grid_size):
        for r in range(grid_size):
            center_x = start_x + c * step_x
            center_y = start_y + r * step_y
            circle(kicad_mod, center_x, center_y, radius=d32 / 2, layers=glayers_silk)
    rectangle_outline(kicad_mod, 0, 0, w=W, h=H, layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=zip)
def circle32_4(d=32, W=100, j=1, zip=1):
    kicad_mod = new_kicad_mod(name=f'circle32_4d{d}W{W}', w=W, h=W)
    x = y = W / 2
    e = d / 2 + j
    non_plated_hole(kicad_mod, x=x - e, y=y - e, d=32.5)
    non_plated_hole(kicad_mod, x=x + e, y=y - e, d=32.6)
    non_plated_hole(kicad_mod, x=x - e, y=y + e, d=32.7)
    non_plated_hole(kicad_mod, x=x + e, y=y + e, d=32.8)
    dsh = 3.9
    non_plated_hole(kicad_mod, x=x, y=y, d=5.9)
    s = d - 3
    non_plated_hole(kicad_mod, x=x + s, y=y, d=dsh)
    non_plated_hole(kicad_mod, x=x - s, y=y, d=dsh)
    non_plated_hole(kicad_mod, x=x, y=y + s, d=dsh)
    non_plated_hole(kicad_mod, x=x, y=y - s, d=dsh)
    hole_rect_center(kicad_mod, x, y, side_len_x=W - 7, d=dsh)
    return write_kicad_mod(kicad_mod, zip=zip)
def circle32_td(d=32, n=12, zip=0):
    """ td 可变 直径测试 """
    import math
    kicad_mod = new_kicad_mod(name=f'Hole_Line_Variable_d{d}_n{n}', w=0, h=0)
    x_center_current = 0
    max_diameter = 0
    for i in range(n):
        td = d + 0.04 * (i - 3)
        if td > max_diameter:
            max_diameter = td
        if i == 0:
            x_start = -td / 2
            x_center_current = 0
            x_end_previous = td / 2
        else:
            x_center_current = x_end_previous + td / 2
            x_end_previous = x_center_current + td / 2
        non_plated_hole(kicad_mod, x=x_center_current, y=0, d=td)
    x_end = x_end_previous
    total_width = x_end - x_start
    rect_center_x = (x_start + x_end) / 2
    rectline_center(kicad_mod, rect_center_x, 0, w=total_width, h=max_diameter, layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=zip)
def circle32(d=32, n=12, zip=0):
    import math
    kicad_mod = new_kicad_mod(name=f'Hole_Line_d{d}_n{n}', w=0, h=0, text_at=[d / 2 + 2, 0])
    start_x = 0
    for i in range(n):
        td = d
        non_plated_hole(kicad_mod, x=start_x, y=0, d=td)
        start_x = start_x + td
    rectline_center(kicad_mod, d * (n / 2) - d / 2, 0, w=d * n, h=d, layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=zip)
def jp_led_27(xm=248, wm=270, led_interval_y=10, led_interval_x=10, wire_width=0.8, zip=True):
    kicad_mod = new_kicad_mod(name=f'jp_led_panel_3-series_{xm}x{wm}_ix{led_interval_x}_iy{led_interval_y}', w=xm, h=wm, text_at=[wm / 2, (-5)], edge_layers=glayers_edge_fsilk)
    margin_x = max(xm / 110, led_interval_x / 2)
    pad_w, pad_h, pad_y_dist = (1.2, 1.6, 1.8)
    layers_cu_mask, layer_cu, layer_silk = (['F.Cu', 'F.Mask'], ['F.Cu'], ['F.SilkS'])
    grid_area_w = xm - 2 * (margin_x + led_interval_x)
    grid_area_h = wm
    num_cols = int(grid_area_w / led_interval_x) - 1
    num_rows = int(grid_area_h / led_interval_y)
    if num_rows % 3!= 0:
        num_rows = num_rows // 3 * 3
    main_bus_width = min(wire_width + num_cols * 0.4, margin_x * 1.9)
    start_x = (xm - (num_cols - 1) * led_interval_x) / 2 + led_interval_x / 10
    start_y = (wm - (num_rows - 1) * led_interval_y) / 2
    v_plus_rail_x = xm - main_bus_width / 2
    rectangle_full(kicad_mod, v_plus_rail_x, wm / 2, w=main_bus_width, h=wm, layers=['F.Cu', 'B.Cu'])
    gnd_rail_x = main_bus_width / 2
    rectangle_full(kicad_mod, gnd_rail_x, wm / 2, w=main_bus_width, h=wm, layers=['F.Cu', 'B.Cu'])
    input_pad_h = 6.0
    for input_y in [input_pad_h / 2, wm - input_pad_h / 2]:
        dpx = 2
        rectangle_full(kicad_mod, v_plus_rail_x, input_y, w=main_bus_width, h=input_pad_h, layers=['F.Cu', 'F.Mask', 'B.Mask', 'B.Cu'])
        km_text(kicad_mod, '+', at=[v_plus_rail_x - main_bus_width, input_y], size=[3, 3])
        plated_hole(kicad_mod, xm - dpx, input_y, 1.4, size=3)
        rectangle_full(kicad_mod, gnd_rail_x, input_y, w=main_bus_width, h=input_pad_h, layers=['F.Cu', 'F.Mask', 'B.Mask', 'B.Cu'])
        km_text(kicad_mod, '-', at=[gnd_rail_x + main_bus_width, input_y], size=[2, 2])
        plated_hole(kicad_mod, dpx, input_y, 1.4, size=3)
    for c in range(num_cols):
        for r in range(0, num_rows, 3):
            if r + 2 >= num_rows:
                continue
            else:
                cx = start_x + c * led_interval_x
                cy_centers = [start_y + (r + i) * led_interval_y for i in range(3)]
                dfix = 2
                pads_y = []
                for cy_center in cy_centers:
                    pads_y.append(cy_center + pad_y_dist / 2 - dfix)
                    pads_y.append(cy_center - pad_y_dist / 2 + dfix)
                p1_y, p2_y, p3_y, p4_y, p5_y, p6_y = pads_y
                for i, p_y in enumerate(pads_y):
                    kicad_mod.append(Pad(number=f'P{c}_{r + i // 2}_{i % 2 + 1}', type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[cx, p_y], size=[pad_w, pad_h], layers=layers_cu_mask))
                rect_w = pad_w + 0.6
                rect_h = pad_y_dist + pad_h
                for i in range(3):
                    rectangle_outline(kicad_mod, cx - rect_w / 2, cy_centers[i] - rect_h / 2, w=rect_w, h=rect_h, layers=layer_silk)
                    circle(kicad_mod, cx - rect_w / 2 - 0.5, pads_y[i * 2 + 1], radius=0.2, layers=layer_silk)
                hw = led_interval_y / 2 - 6 / led_interval_y
                dhw = hw * 0.3
                d防短路 = 1.5
                multi_dot_line(kicad_mod, [(v_plus_rail_x - main_bus_width / 2, p1_y - dhw), (cx + d防短路, p1_y - dhw)], width=hw, layers=layer_cu)
                multi_dot_line(kicad_mod, [(cx, p2_y), (cx, p3_y)], width=wire_width, layers=layer_cu)
                multi_dot_line(kicad_mod, [(cx, p4_y), (cx, p5_y)], width=wire_width, layers=layer_cu)
                multi_dot_line(kicad_mod, [(cx - d防短路, p6_y + dhw), (gnd_rail_x + main_bus_width / 2, p6_y + dhw)], width=hw, layers=layer_cu)
    dy18650_box = 53.2
    two_hole(kicad_mod, xm / 2, dy18650_box, 20, 2.9, angle=0, holes=[0, 1], func=non_plated_hole)
    two_hole(kicad_mod, xm / 2, wm - dy18650_box, 20, 2.9, angle=0, holes=[0, 1], func=non_plated_hole)
    multi_dot_line(kicad_mod, [(xm, (-6)), (xm, wm + 6)], width=12, layers=glayers_silk)
    for yi in range(10):
        non_plated_hole(kicad_mod, 5.7, 2.5 + yi * led_interval_y * 3, 1.5)
    return write_kicad_mod(kicad_mod, zip=zip)
def plug3(W=26.5, H=18, pin_length=5, zip=True):
    kicad_mod = new_kicad_mod(name=f'Socket_IEC_C14_{W}x{H}', w=W, h=H, text_at=[0, 15])
    top_edge_length = 16.0
    pin_thickness = 0.9
    pin_spacing_horiz = 14.0
    pin_spacing_vert = 5.0
    cx, cy = (W / 2, H / 2)
    drill_slot_size = [pin_thickness, pin_length]
    pad_size = [drill_slot_size[0] + 1.6, drill_slot_size[1] + 1.6]
    p_gnd_y = cy + pin_spacing_vert / 2
    p_ln_y = cy - pin_spacing_vert / 2
    p_l_x = cx - pin_spacing_horiz / 2
    p_n_x = cx + pin_spacing_horiz / 2
    kicad_mod.append(Pad(number='L', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, at=[p_l_x, p_ln_y], size=pad_size, drill=drill_slot_size, layers=Pad.LAYERS_THT))
    kicad_mod.append(Pad(number='N', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, at=[p_n_x, p_ln_y], size=pad_size, drill=drill_slot_size, layers=Pad.LAYERS_THT))
    kicad_mod.append(Pad(number='G', type=Pad.TYPE_THT, shape=Pad.SHAPE_OVAL, at=[cx, p_gnd_y], size=pad_size, drill=drill_slot_size, layers=Pad.LAYERS_THT))
    half_w, half_h = (W / 2, H / 2)
    cutout_corner_cut_x = (W - top_edge_length) / 2
    cutout_nodes = [(cx + half_w, cy - half_h), (cx + half_w, cy + half_h - cutout_corner_cut_x), (cx + half_w - cutout_corner_cut_x, cy + half_h), (cx - half_w + cutout_corner_cut_x, cy + half_h), (cx - half_w, cy + half_h - cutout_corner_cut_x), (cx - half_w, cy - half_h)]
    multi_dot_line(kicad_mod, cutout_nodes, layers=glayers_edge_pure, width=1)
    multi_dot_line(kicad_mod, [(cx - half_w, cy - half_h), (cx + half_w, cy - half_h)], layers=glayers_edge_pure, width=1, segments=1, segments_d=2)
    return write_kicad_mod(kicad_mod, zip=zip)
def parallel_18650(wm=100, hm=100, spring=3.1, spring_D=0.7, zip=True):
    kicad_mod = new_kicad_mod(w=wm, h=hm, text_at=[9, (-2)])
    def one(x, y, spring=spring, D=0.8, L=65.3):
        LA = L + 10
        rectline_center(kicad_mod, x, y, w=LA, h=18.3, layers=glayers_edge_pure)
        rectangle_full(kicad_mod, x - 44, y, layers=('F.Cu', 'B.Cu'), w=11, h=20)
        rectangle_full(kicad_mod, x + 44, y, layers=('F.Cu', 'B.Cu'), w=11, h=20)
        for xi in range(3):
            dx = LA / 2 + 1.8 + xi * spring
            dy = 3.5 - spring_D / 2
            size = spring - 0.1
            plated_hole(kicad_mod, x - dx - 1, y + dy, D, size=size)
            plated_hole(kicad_mod, x - dx + 1, y - dy, D, size=size)
            plated_hole(kicad_mod, x + dx - 1, y + dy, D, size=size)
            plated_hole(kicad_mod, x + dx + 1, y - dy, D, size=size)
        dx = LA / 2 + 1.8 + 3 * spring
        plated_hole(kicad_mod, x - dx + 1, y - dy, D, size=size)
        plated_hole(kicad_mod, x + dx - 1, y + dy, D, size=size)
    x = wm / 2
    m = 4
    mi = hm / m
    for yi in range(m):
        y = mi / 2 + mi * yi
        if yi == 3:
            continue
        else:
            one(x, y, spring=spring - yi * 0.1, D=0.85 + yi * 0.05)
    for y in [25, 75]:
        multi_dot_line(kicad_mod, [(5, y - 5), (5, y - 1), (43, y - 1)], width=1, layers=('F.Cu', 'B.Cu'))
        multi_dot_line(kicad_mod, [(95, y - 5), (95, y - 1), (57, y - 1)], width=1, layers=('F.Cu', 'B.Cu'))
        plated_hole(kicad_mod, 57, y, 1.35, size=2)
        plated_hole(kicad_mod, 43, y, 1.35, size=2, shape=Pad.SHAPE_RECT)
        plated_hole(kicad_mod, 53.75, y, 1.35, size=2)
        plated_hole(kicad_mod, 46.25, y, 1.35, size=2, shape=Pad.SHAPE_RECT)
    return write_kicad_mod(kicad_mod, zip=zip)
def rv097ns_up(wm=9.5, hm=11.4, z=0, edge=None):
    kicad_mod = new_kicad_mod(w=wm, h=hm + 5, text_at=[9, (-2)])
    x = wm / 2
    y = hm / 2
    hq = 0.2
    rectline_center(kicad_mod, x, y, w=wm, h=hm, layers=glayers_edge_pure)
    rectline_center(kicad_mod, x, hm + hq / 2, w=2, h=hq, layers=glayers_edge_pure)
    for i in range((-1), 2):
        xi = x + i * 2.5
        kicad_mod.append(Pad(number=i + 2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[xi, hm + 2.6], size=0.9, drill=0, layers=['*.Cu', '*.Mask']))
        for yi in range(10):
            plated_hole(kicad_mod, xi, hm + yi * 0.3, 0.9, size=0.9)
    return write_kicad_mod(kicad_mod, zip=z)
def rv097ns_cut_pcb(wm=9.6, hm=7.1, z=0, edge=None):
    if edge:
        edge = glayers_edge_pure
    else:
        edge = ('F.SilkS',)
    kicad_mod = new_kicad_mod(w=wm + 1, h=hm + 15, text_at=[9, (-2)], edge_layers=edge)
    x = wm / 2
    y = hm / 2
    for i in range((-1), 2):
        xi = x + i * 2.5
        rectangle_full(kicad_mod, xi, (-2), layers=('B.Cu',), w=1.2, h=4)
        rectangle_full(kicad_mod, xi, (-1.5), layers=('B.Mask',), w=1, h=3)
        kicad_mod.append(Pad(number=i + 2, type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[xi, (-1.5)], size=1, drill=0, layers=['B.Cu', 'B.Mask']))
    hq = 0.7
    rectline_center(kicad_mod, x, hm + hq / 2, w=2, h=hq, layers=glayers_edge_pure)
    rectline_center(kicad_mod, x, y, w=wm, h=hm, layers=glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=z)
def socket_916(wm=56.5, hm=48.5, z=0):
    """ 三面七孔插座 型号916  10A 250V """
    kicad_mod = new_kicad_mod(w=wm, h=hm, text_at=[9, (-2)])
    x = wm / 2
    y = hm / 2
    hole_rect_center(kicad_mod, x, y, 40, side_len_y=30, d=3.1, holes=[0, 2], angle=0)
    two_hole(kicad_mod, x, y - 7, 40, hole=2.9)
    return write_kicad_mod(kicad_mod, zip=z)
def miniature_circuit_breaker_C1(wm=73.5, hm=17.88, z=0):
    kicad_mod = new_kicad_mod(w=wm, h=hm, text_at=[9, (-2)])
    x = wm / 2
    y = hm / 2
    dc = 7
    rectangle_full(kicad_mod, 0 - dc / 2, y, layers=glayers_FB_Cu, w=dc, h=3)
    rectangle_full(kicad_mod, 0 - dc / 2, y, layers=glayers_FB_Mask, w=dc, h=1)
    ec = glayers_edge_pure + glayers_silk
    du = 20.6
    rectline_center(kicad_mod, du / 2, y, w=du, h=hm, layers=glayers_Cmts)
    u2 = 1
    rectline(kicad_mod, start=[0, 0], end=[du - u2, hm], layers=ec)
    u2h = 4.1
    rectline_center(kicad_mod, du - u2 / 2, u2h / 2, w=u2, h=u2h, layers=ec)
    rectline_center(kicad_mod, du - u2 / 2, hm - u2h / 2, w=u2, h=u2h, layers=ec)
    hx = 24.2
    dhy = 2.5
    non_plated_hole(kicad_mod, hx, dhy, 2.5)
    non_plated_hole(kicad_mod, hx, hm - dhy, 2.5)
    d = 17
    rectline_center(kicad_mod, wm - d / 2, y, w=d, h=hm, layers=ec)
    d11 = 0.3
    rectline_center(kicad_mod, wm - d - d11 / 2, y, w=d11, h=11.3, layers=ec)
    non_plated_hole(kicad_mod, wm + 7.3 - 1.4 - 2, y, 3.9)
    return write_kicad_mod(kicad_mod, zip=z)
def motor_220v_4mm(kicad_mod, x, y, angle=0, hole=17.4):
    """ 外径最小 42.2  ，42.1  放不进"""
    if hole > 17:
        m4 = 3.9
        m5 = 5
        cs = [0.1, 4, 12, 17.5, 42.2]
    else:
        m4 = 1
        m5 = 1
        cs = [42.2]
    non_plated_hole(kicad_mod, x, y, hole)
    circle(kicad_mod, x, y, cs)
    xd = 14.5
    non_plated_hole(kicad_mod, *rotate_point(x - xd, y, angle, x, y), m4)
    non_plated_hole(kicad_mod, *rotate_point(x + xd, y, angle, x, y), m4)
    non_plated_hole(kicad_mod, *rotate_point(x, y - 12.6, angle, x, y), m5)
def hgr20_flange_block(kicad_mod, x, y, angle=0, hole=5.9, holes=(0, 1, 2, 3), zip=0):
    """  hgr20_flange_block 法兰款"""
    write_kicad = False
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=100, h=100)
        write_kicad = True
    rectline_center(kicad_mod, x, y, 76, 43, crosshair=1, layers=glayers_F_Cu + glayers_silk, angle=angle)
    rectline_center(kicad_mod, x, y, 50.9, 63, crosshair=1, layers=glayers_F_Cu, angle=angle)
    hole_rect(kicad_mod, x, y, side_len_x=40, side_len_y=53, d=hole, angle=angle, holes=holes)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=zip)
    else:
        return None
HGW20CC = hgr20_flange_block
def hgr20_block(kicad_mod, x, y, angle=0, hole=4.9, holes=(0, 1, 2, 3), write_kicad=False, z=0):
    """  hgr20_block 普通 无法兰"""
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=100, h=100)
        write_kicad = False
    rectline_center(kicad_mod, x, y, 75, 44, crosshair=1, layers=glayers_F_Cu, angle=angle)
    rectline_center(kicad_mod, x, y, 78, 44, crosshair=1, layers=glayers_silk, angle=angle)
    hole_rect(kicad_mod, x, y, side_len_x=36, side_len_y=32, d=hole, angle=angle, holes=holes)
    if write_kicad:
        kicad_mod.write(f'HGR20_{h}mm.kicad_mod')
def hgr20_rail(kicad_mod, x, y, angle=0, h=300, hole=5.9, mid_hole=None, write_kicad=False, z=0):
    """ 生成HGR20直线导轨封装  not hgr20_block """
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=wm, h=hm)
        write_kicad = False
    rectline_center(kicad_mod, x, y, w=h, h=20, width=0.012, angle=angle, layers=glayers_silk)
    n = h // 60
    if n % 2 == 1:
        n += 1
    for i in range(n // 2):
        offset = i * 60
        if i == 0 and mid_hole:
            non_plated_hole(kicad_mod, *rotate_point(x, y, angle, x, y), mid_hole)
        else:
            non_plated_hole(kicad_mod, *rotate_point(x + offset, y, angle, x, y), hole)
            non_plated_hole(kicad_mod, *rotate_point(x - offset, y, angle, x, y), hole)
    if hole:
        circle(kicad_mod, x, y, diameter=[0.1, 1, 2, 20], crosshair=1, layers=glayers_Cmts)
    if write_kicad:
        kicad_mod.write(f'HGR20_{h}mm.kicad_mod')
def chainwheel_04c(kicad_mod, x, y, hole=10, n=17):
    """dnD={\n11:[25.5],    \n14:[31.5],    \n15:[33.5],    \n16:[35.5],    \n17:[37.5],    \n    }\n    \ndnW={\n17:40\n}    \n    \n    """
    non_plated_hole(kicad_mod, x, y, hole)
    D = 3.5 + 2 * n
    W = 3.5 + 2 * n + 2
    bw = W / 2
    circle(kicad_mod, x, y, diameter=[hole + 0.2, 25, D, W], crosshair=0, layers=glayers_silk)
    for yw in [y + bw, y - bw]:
        multi_dot_line(kicad_mod, [((-11), yw), (x, yw)], width=0.01, layers='F.SilkS')
def two_hole(kicad_mod, x, y, distance, hole=5.9, angle=0, hole_func=py.No('hole_func=non_plated_hole'), **ka):
    """ zcz  """
    if not hole_func:
        hole_func = non_plated_hole
    distance = U.get_duplicated_kargs(ka, 'distance', 'd', 'D', default=distance)
    r = distance / 2
    if U.len(hole)!= 2:
        hole = [hole, hole]
    x0, y0 = rotate_point(x - r, y, angle, x, y)
    hole_func(kicad_mod, x0, y0, hole[0])
    x1, y1 = rotate_point(x + r, y, angle, x, y)
    hole_func(kicad_mod, x1, y1, hole[1])
    return ((x0, y0), (x1, y1))
def gear_1m_70_10(motor_hole=17.4, long_hole=False, z=0):
    """ chain wheel """
    kicad_mod = new_kicad_mod(name=f'gear_1m_70_10={motor_hole}', w=100, h=100, text_at=(10, 1), edge_layers=glayers_edge_fsilk)
    dg = 40.0
    y = 52.5
    x = 33
    circle(kicad_mod, x, y, diameter=[0.1, 10, 15, 67.5, 72], crosshair=0, layers=glayers_silk)
    chainwheel_04c(kicad_mod, x, y, n=15)
    motor_220v_4mm(kicad_mod, *rotate_point(x + dg, y, 0, x, y), hole=motor_hole, angle=(-90))
    zcz10 = 46
    zcz_15 = 53
    if motor_hole > 40:
        p0, p1 = two_hole(kicad_mod, x, y, distance=zcz10, angle=(-77.3), hole=5, hole_func=non_plated_hole)
    else:
        two_hole(kicad_mod, x, y, distance=zcz10, angle=(-45), hole=5, hole_func=non_plated_hole)
        p1 = (38.05646270011526, 30.0627054892453)
    yr = 90
    hgr20_rail(kicad_mod, 20, yr, angle=0)
    rectline_center(kicad_mod, x + 2, yr, 78, 44, crosshair=1, layers=glayers_Cmts + glayers_silk)
    if long_hole:
        nh = 2
        for i in range(-nh, nh + 1):
            non_plated_hole(kicad_mod, 20 + i * 2, 90, 5.9)
            non_plated_hole(kicad_mod, 80 + i * 2, 90, 5.9)
    xb = p1[0] - 16
    yb = p1[1] + 18
    hgr20_rail(kicad_mod, xb, yb, hole=0, angle=90)
    if motor_hole > 40:
        hgr20_block(kicad_mod, xb, yb, angle=90, hole=4.9, holes=[0, 1, 2])
        hgr20_block(kicad_mod, xb, yb, angle=90, hole=4.2, holes=[3])
    non_plated_hole(kicad_mod, 6, 6, 5.9)
    non_plated_hole(kicad_mod, 6 + (xb - 6) * 2, 6, 3.9)
    non_plated_hole(kicad_mod, 80, 10, 5.9)
    non_plated_hole(kicad_mod, 20, 10, 5)
    return write_kicad_mod(kicad_mod, zip=z)
def jp65_heatbed(W=650, H=118, w=0.4, interval=0.2, margin=3, margin_w=7, z=0):
    """ hotbed heatbed  297 """
    kicad_mod = new_kicad_mod(w=W, h=H, text_at=(10, 1), edge_layers=glayers_edge_fsilk)
    for x in [5, 6, 7, 8, 9, 10]:
        multi_dot_line(kicad_mod, [(x, 0), (x, H)], width=0.01, layers='F.SilkS')
    s = w + interval
    sensor_width = 22
    eff_H = H - 2 * margin
    loop_count = int(eff_H // (2 * s))
    actual_eff_H = loop_count * 2 * s
    total_height = actual_eff_H + 2 * margin
    mid = loop_count // 2
    open_range = range(mid - 3, mid + 3)
    left_start = margin_w + 3
    right = W - margin_w
    current_y = margin + (w + interval) / 2
    points = []
    sa, sb = (H / 2 - 4.5, H / 2 + 4.5)
    is_once = 1
    for i in range(loop_count):
        left = left_start
        if sa < current_y < sb:
                left += sensor_width
        zrow = [(left, current_y), (right, current_y), (right, current_y + s), (left, current_y + s)]
        if current_y > sb and is_once:
                is_once = 0
                zrow[0] = (left_start + sensor_width, current_y)
        points.append((zrow[0], zrow[1]))
        points.append((zrow[1], zrow[2]))
        points.append((zrow[2], zrow[3]))
        if i < loop_count - 1:
            points.append((zrow[3], (zrow[3][0], current_y + 2 * s)))
        if i == open_range.start:
            points.append(((left_start, current_y), (left, current_y)))
        current_y += 2 * s
    for start, end in points:
        for ilayer in ['F.Cu']:
            kicad_mod.append(Line(start=start, end=end, layer=ilayer, width=w))
    dsy = H / 2 + 1
    rectline_center(kicad_mod, sensor_width - 2, dsy, w=sensor_width, h=7.5, width=0.01, layers=glayers_edge_pure)
    mlayers = ['F.Cu']
    pad_offset = 0
    fka = py.dict(layers=mlayers, w=6, h=w + 0.1)
    rectangle_full(kicad_mod, left_start + pad_offset, margin - pad_offset, **fka)
    rectangle_full(kicad_mod, left_start + pad_offset, total_height - margin + pad_offset, **fka)
    pad_offset = -interval
    fka = py.dict(layers=mlayers, w=6, h=w)
    rectangle_full(kicad_mod, left_start + pad_offset, margin - pad_offset, **fka)
    rectangle_full(kicad_mod, left_start + pad_offset, total_height - margin + pad_offset, **fka)
    a = 2.8
    lx2 = left_start - 2
    fka = py.dict(layers=mlayers, w=2.5, h=5)
    rectangle_full(kicad_mod, lx2, margin + a, **fka)
    rectangle_full(kicad_mod, lx2, total_height - margin - a, **fka)
    fka = py.dict(layers=['F.Cu', 'F.Mask'], w=1.3, h=4)
    rectangle_full(kicad_mod, lx2, total_height - margin - a, **fka)
    if dsy < 66:
        rectangle_full(kicad_mod, lx2, margin + a, **fka)
    else:
        rectangle_full(kicad_mod, lx2, dsy - 60, **fka)
        multi_dot_line(kicad_mod, [(lx2, margin + a), (lx2, dsy - 60)], width=1.3, layers='F.Cu')
    hn = H // 25
    hn_mid = hn // 2
    ydh = (H - hn * 25) / 2
    if 100 < H < 125:
            if hn == 4:
                hn = 5
    if not ydh:
        ydh = 12.5
    if hn > 5 and hn % 2 == 0:
        his = [hn_mid - 1, hn_mid]
    else:
        his = [hn_mid]
    for i in range(hn):
        m3 = 2.85
        non_plated_hole(kicad_mod, W - margin_w / 2, ydh + 25 * i, m3)
        if i in his:
            m3 = 1.3
        non_plated_hole(kicad_mod, margin_w / 2, ydh + 25 * i, m3)
    dh = margin / 2
    dx = margin_w / 2 + 1
    dx = 25
    for i in range(W // 25):
        if W - i * 25 <= dx:
            continue
        else:
            non_plated_hole(kicad_mod, dx + 25 * i, dh, 1)
            non_plated_hole(kicad_mod, dx + 25 * i, H - dh, 1)
    if W == 650:
        for i in [(-1), 25]:
            circle(kicad_mod, dx + i * 25, dh, [1, 3])
        for i in range(hn):
            circle(kicad_mod, dx + 625 + 1, ydh + 25 * i, [1, 3])
    mb = margin + 1.5
    current_x = 32
    loop_count = int((W - current_x - margin_w) // (2 * s))
    points = []
    for i in range(loop_count):
        zrow = [(current_x, margin), (current_x, H - mb), (current_x + s, H - mb), (current_x + s, margin)]
        points.append((zrow[0], zrow[1]))
        points.append((zrow[1], zrow[2]))
        points.append((zrow[2], zrow[3]))
        points.append((zrow[3], (current_x + 2 * s, margin)))
        current_x += 2 * s
        if i == loop_count - 1:
            yb = H - margin - 0.7
            points.append([(current_x, margin), (current_x, yb)])
            points.append([(current_x, yb), (32 - s, yb)])
    bl2 = ['B.Cu']
    for start, end in points:
        for ilayer in bl2:
            kicad_mod.append(Line(start=start, end=end, layer=ilayer, width=w))
    dw = margin_w + 2.9
    wf = 23.5
    hf = 52.5
    serpentine_line(kicad_mod, x=dw + wf / 2, y=3 + hf / 2, w=wf, h=hf, angle=0, wire_width=w, interval=interval, layers=bl2, pop_indexes=[(-1), (-1)])
    rectangle_full(kicad_mod, 8.15, 6.4, layers=bl2, w=4, h=7)
    dw -= 0.6
    hf -= 2.8
    serpentine_line(kicad_mod, x=dw + wf / 2, y=H - 0.72 - (3 + hf / 2), w=wf, h=hf, angle=0, wire_width=w, interval=interval, layers=bl2, pop_indexes=[0, (-1)])
    rectangle_full(kicad_mod, 8.15, H - 0.72 - 6.4, layers=bl2, w=4, h=7)
    return write_kicad_mod(kicad_mod, zip=0)
def stepper_mgn12(W=100, H=100, dy=0, z=0):
    kicad_mod = new_kicad_mod(w=W, h=H, text_at=(4, (-3)))
    x = W / 2
    for i in range(3):
        yi = 80 + i * 5
        if yi == 95:
            continue
        else:
            non_plated_hole(kicad_mod, x, yi, 1)
    multi_dot_line(kicad_mod, [(x, 0), (x, 101)], width=0.01, layers=glayers_silk + glayers_Cmts)
    step_motor_42(kicad_mod, x, 21.0, d=4.99, hole_func=circle)
    step_motor_42(kicad_mod, x, 29.702970297029704, d=4.99, angle=45)
    step_motor_57(kicad_mod, x, 28.3, d=6.35, hole_func=circle)
    step_motor_57(kicad_mod, x, 40.02828854314003, d=6.35, angle=45)
    gt17_d = 9.7
    gt20_d = 13.4
    d9gt = (gt20_d - 9) / 2 - 1.4
    xm = x + (gt20_d / 2 + 4.5 + 10)
    y = 29.72
    mgn12c_rail(kicad_mod, xm, y, h=200)
    rectline_center(kicad_mod, xm, 50, 20, 200, crosshair=1, layers=glayers_Cmts + glayers_silk)
    xm = x - (gt20_d / 2 + 4.5 + 10)
    mgn12c_rail(kicad_mod, xm, y, h=200, hole=4.9, mid_hole=2.9)
    y = 95
    non_plated_hole(kicad_mod, x - d9gt, y, 2.9)
    circle(kicad_mod, x - d9gt, y, d=[3, 9], layers=glayers_F_Cu)
    return write_kicad_mod(kicad_mod, zip=z)
def jp30x20_mgn12_heatbed(W=297, H=200, wd=277, z=0):
    kicad_mod = new_kicad_mod(w=W, h=H, text_at=(4, (-3)))
    def non_plated_hole(kicad_mod, x, y, d=0, width=0.001):
        kicad_mod.append(KicadModTree.Circle(center=[x, y], radius=d / 2, layer='Edge.Cuts', width=width))
        qgb.kicad.non_plated_hole(kicad_mod, x, y, d=d)
    bd = (W - wd) / 2
    d3 = 3.4
    for i in range(8):
        yi = 12.5 + i * 25
        non_plated_hole(kicad_mod, bd, yi, 2.9)
        non_plated_hole(kicad_mod, W - bd, yi, 2.9)
        tbd = bd - 2
        rectangle_full(kicad_mod, W - tbd / 2, yi, tbd, d3)
        if i == 0:
            yi += 1
        if i == 7:
            yi -= 1
        rectangle_full(kicad_mod, tbd / 2, yi, tbd, d3)
    w = 0.9
    interval = 0.2
    max = 200
    dy_start = 9
    silk_line = True
    d = w + interval
    M = py.int(max / (2 * d)) - 1
    x0 = bd + 2.5
    x0 = y0 = (max - ((M + 1) * 2 * d - interval)) / 2 + w / 2
    zrow = ([x0, y0], [W - x0, y0], [W - x0, y0 + d], [x0, y0 + d], [x0, y0 + d + d])
    for i in range(M + 1):
        z0 = None
        for n, z in py.enumerate(zrow):
            z = U.deepcopy(z)
            z[1] += i * d * 2
            if abs(z[1] % 25 - 12.5) < d3 and n in [1, 2]:
                    z[0] -= bd + 2
            if abs(z[1] % 25 - 12.5) < d3 and n in [3, 4, 0]:
                    z[0] += bd + 2
            if abs(z[1]) < dy_start or abs(H - z[1]) < dy_start:
                if n in [3, 4, 0]:
                    z[0] += dy_start * 1.33
            if i == M and n == 4:
                    break
            if n!= 0:
                kicad_mod.append(KicadModTree.Line(start=z0, end=z, layer='F.Cu', width=w))
                zs0, zs = (z0.copy(), z.copy())
                if n in (1, 3) and silk_line:
                        sw_interval = interval - 0.01
                        zs0[1] = zs[1] = zs[1] - d / 2
                        dxs = w / 2 + 0.06
                        if n == 1:
                            zs0[0] += dxs
                            zs[0] = W
                            if i == 0:
                                zs0[0] = 0
                        if n == 3:
                            zs0[0] -= dxs
                            zs[0] = 0
                            if i == M:
                                zs0[0] = W
                        kicad_mod.append(KicadModTree.Line(start=zs0, end=zs, layer='F.SilkS', width=sw_interval))
            z0 = z
    dp = 1.35
    x = y = dy_start / 2 * 1.4
    y -= 0.2
    circle(kicad_mod, x, y, dy_start, width=1, layers=['F.Cu', 'F.Mask'])
    rectangle_full(kicad_mod, dy_start * 0.66, dp - 0.18, 2, 0.8)
    rectangle_full(kicad_mod, dy_start, dp, dy_start, 1.15)
    non_plated_hole(kicad_mod, x, y, 5)
    y = H - dy_start / 2 * 1.4 + 0.2
    circle(kicad_mod, x, y, dy_start, width=1, layers=['F.Cu', 'F.Mask'])
    rectangle_full(kicad_mod, dy_start * 0.66, H - dp + 0.18, 2, 0.8)
    rectangle_full(kicad_mod, dy_start, H - dp, dy_start, 1.15)
    non_plated_hole(kicad_mod, x, y, 5)
    return write_kicad_mod(kicad_mod, zip=z)
def tc_2020_wheel(W=100, H=100, z=0):
    """ 36.7-23.2 == 13.5  # 6.75 """
    kicad_mod = new_kicad_mod(w=W, h=H)
    crosshair(kicad_mod, 50, 10, w=100, h=21)
    ka2020 = dict(hole=2.9, layers=glayers_silk)
    last_ka = dict(hole2=3.9, dh2=(-2.3))
    dx = 11.2
    dy = 10.1
    a = (-90)
    y = dy
    ntc_2020(kicad_mod, dx, y, dh=2.9, angle=a, **ka2020)
    ntc_2020(kicad_mod, 40 - dx, y, dh=3, angle=a, **ka2020)
    ntc_2020(kicad_mod, 100 - (40 - dx), y, dh=3.1, angle=a, **ka2020)
    ntc_2020(kicad_mod, 100 - dx, y, dh=3.2, angle=a, **ka2020)
    multi_dot_line(kicad_mod, [(41.5, 0), (41.5, 13)], width=3, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(58.5, 0), (58.5, 13)], width=3, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(43, 2.2), (57.8, 2.2)], width=4.4, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(0, 21), (100, 21)], width=1.6, layers=glayers_edge_pure, segments=10)
    a = 90
    y = 100 - dy
    ntc_2020(kicad_mod, dx, y, dh=3.25, angle=a, **ka2020)
    ntc_2020(kicad_mod, 40 - dx, y, dh=3.3, angle=a, **ka2020)
    ntc_2020(kicad_mod, 100 - (40 - dx), y, dh=3.4, angle=a, **ka2020)
    ntc_2020(kicad_mod, 100 - dx, y, dh=3.5, angle=a, **ka2020, **last_ka)
    multi_dot_line(kicad_mod, [(41.5, 100), (41.5, 87)], width=3, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(58.5, 100), (58.5, 87)], width=3, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(43, 97.8), (57.8, 97.8)], width=4.4, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(0, 79), (100, 79)], width=1.6, layers=glayers_edge_pure, segments=10)
    crosshair(kicad_mod, 50, 50, w=100, h=57)
    wm = 34.7
    hm = 27
    x = hm / 2 + 13
    x = 50
    y = 50
    rectline_center(kicad_mod, x - (hm + 13) / 2, y, w=13, h=44, width=0.1, layers=glayers_silk)
    rectline_center(kicad_mod, x + (hm + 13) / 2, y, w=13, h=44, width=0.1, layers=glayers_silk)
    mgn12c_block(kicad_mod, x, y, angle=90)
    bw = wm / 2 + 1
    for i in range(1, 10):
        non_plated_hole(kicad_mod, i * 10, y + bw, 1)
        non_plated_hole(kicad_mod, i * 10, y - bw, 1)
    hdz = 10
    x = 50 + hm / 2 + hdz
    multi_dot_line(kicad_mod, [(x, 21), (x, 79)], width=0.01, layers=glayers_silk)
    mgn12c_block(kicad_mod, x + hm / 2, y, angle=90)
    x = 50 - hm / 2 - hdz
    multi_dot_line(kicad_mod, [(x, 21), (x, 79)], width=0.01, layers=glayers_silk)
    mgn12c_block(kicad_mod, x - hm / 2, y, angle=90)
    return write_kicad_mod(kicad_mod, zip=z)
def g3030_j45(W=100, k16=1.6, m4=3.9, m5=4.9, m6=5.9, z=0):
    kicad_mod = new_kicad_mod(w=W, h=W)
    multi_dot_line(kicad_mod, [(0, 0), (99, 99)], width=0.01, layers=glayers_silk, segments=6, segments_d=1)
    return write_kicad_mod(kicad_mod, zip=z)
def a2020_j45(W=100, k16=1.6, m4=3.9, m5=4.9, m6=5.9, z=0):
    kicad_mod = new_kicad_mod(w=W, h=W)
    x = y = W / 2
    multi_dot_line(kicad_mod, [(0, 0), (100, 100)], width=0.01, layers=glayers_silk)
    multi_dot_line(kicad_mod, [(100, 0), (0, 100)], width=0.01, layers=glayers_silk)
    lmh = 42.36
    non_plated_hole(kicad_mod, lmh, W - lmh, m5)
    non_plated_hole(kicad_mod, W - lmh, lmh, m5)
    a = 100
    xr = 62.42623562373095 + k16 / 2 * 1.4142135623730951
    sx = 25.274
    lx = 87.3951
    krh = dict(w_holes={10: m5, sx: m5, 50: m5, W - sx: m5, 90: m5}, w_holes_d=4.9, w=a, h=20, layers=glayers_silk, width=0.01, angle=0)
    kr = dict(w_holes=[22.5, lx], w_holes_d=m5, crosshair=1, h=20, layers=glayers_silk, width=0.01, w=a)
    rectline_center(kicad_mod, a / 2, 10, **krh)
    rectline_center(kicad_mod, xr, 48.2841, angle=45, **kr)
    rectline_center(kicad_mod, a / 2, W - 10, **krh)
    rectline_center(kicad_mod, W - xr, W - 48.2841, angle=225, **kr)
    d = 2.5
    q = 28.284271247461902
    multi_dot_line(kicad_mod, [(d, 20), (20, 20), (W - 20, W - 20), (W - d, W - 20)], width=1.6, layers=glayers_edge_pure, segments=17.6, segments_d=0.1)
    for yi in krh['w_holes']:
        if yi == W - sx:
            continue
        else:
            npd = m5
            non_plated_hole(kicad_mod, 10, yi, npd)
            non_plated_hole(kicad_mod, W - 10, W - yi, npd)
    multi_dot_line(kicad_mod, [(10, 0), (10, 100)], width=0.01, layers=glayers_silk)
    multi_dot_line(kicad_mod, [(20, 0), (20, 100)], width=0.01, layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=z)
def ntc_2020(kicad_mod, x, y, angle=0, hole=4.9, dh=0, w2=2.2, h6=4.6, layers=py.No('glayers_Cmts'), hole2=None, dh2=None):
    """  ￥0.7 两个"""
    if not layers:
        layers = glayers_Cmts
    e = glayers_edge_pure
    circle(kicad_mod, *rotate_point(x + 10, y, angle, x, y), 2, layers=layers)
    rectline_center(kicad_mod, *rotate_point(x + 7.45, y, angle, x, y), w=w2, h=h6, width=0.01, layers=e, angle=angle)
    non_plated_hole(kicad_mod, *rotate_point(x + dh, y, angle, x, y), hole)
    rectline_center(kicad_mod, *rotate_point(x - 7.550000000000001, y, angle, x, y), w=w2, h=h6, width=0.01, layers=e, angle=angle)
    rectline_center(kicad_mod, x, y, w=20.2, h=17, layers=layers, angle=angle)
    rounded_rectangle(kicad_mod, x, y, w=8.6, h=6, width=0.01, layers=layers, angle=angle)
    if hole2:
        if not dh2:
            dh2 = 0
        non_plated_hole(kicad_mod, *rotate_point(x + dh2, y, angle, x, y), hole2)
def tc_2028(kicad_mod, x, y, angle=0, hole=4.9, w2=2.2):
    """ 天成五金 2028 连接件  angle 负逆时针。正顺"""
    h6 = 5.9
    e = glayers_edge_pure
    circle(kicad_mod, *rotate_point(x + 14, y, angle, x, y), 2, layers=glayers_Cmts)
    rectline_center(kicad_mod, *rotate_point(x + 10.629999999999999, y, angle, x, y), w=w2, h=h6, width=0.01, layers=e, angle=angle)
    non_plated_hole(kicad_mod, *rotate_point(x - 2, y, angle, x, y), hole)
    non_plated_hole(kicad_mod, *rotate_point(x + 2, y, angle, x, y), 1)
    rectline_center(kicad_mod, *rotate_point(x - 10.77, y, angle, x, y), w=w2, h=h6, width=0.01, layers=e, angle=angle)
    rectline_center(kicad_mod, x, y, w=28, h=20, layers=glayers_Cmts, angle=angle)
def aluminum_profile_2020_wheel(mw=59, m5=4.9, m6=5.9, z=0):
    """ 普通欧标2020 1.8 ，不是推荐的V型槽\n\n白色（5*21.5*7mm）\n黑色（5*21.5*7mm）    \n625zz 5*16*5\n    """
    kicad_mod = new_kicad_mod(w=100, h=mw)
    x = 50
    y = mw / 2
    non_plated_hole(kicad_mod, x, y, 2.9)
    rectline_center(kicad_mod, x, y, 20, 20, layers=glayers_silk)
    tc_2028(kicad_mod, x - 10 - 14, y, angle=0, hole=1.2, w2=2)
    tc_2028(kicad_mod, x + 10 + 14, y, angle=180, hole=1.2, w2=2)
    ya = (-20.2)
    rectline_center(kicad_mod, x, y + ya, w=19.9, h=19.9, width=0.01, layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(10, y + ya), (90, y + ya)], width=0.5, layers=glayers_Cmts)
    tc_2028(kicad_mod, x, y + ya - 10 - 14, angle=90)
    tc_2028(kicad_mod, x, y + ya + 10 + 14, angle=(-90), hole=m5)
    ntc_2020(kicad_mod, x - 10 - 10, y + ya, angle=0, hole=m5)
    ntc_2020(kicad_mod, x + 10 + 10, y + ya, angle=180, hole=m5)
    xi = 38.8
    bd = 18.35
    circle(kicad_mod, x - xi, y + bd, r=11)
    non_plated_hole(kicad_mod, x - xi, y + bd, m5)
    non_plated_hole(kicad_mod, x - xi, y - bd, m5)
    non_plated_hole(kicad_mod, x + xi, y + bd, m5)
    non_plated_hole(kicad_mod, x + xi, y - bd, m5)
    ntc_2020(kicad_mod, x - xi, y - bd, angle=90, layers=glayers_silk)
    rectline_center(kicad_mod, x - xi, y, w=16, h=7.5, width=0.01, layers=glayers_edge_pure)
    ntc_2020(kicad_mod, x - xi, y + bd, angle=(-90), layers=glayers_silk)
    ntc_2020(kicad_mod, x + xi, y - bd, angle=90)
    rectline_center(kicad_mod, x + xi, y, w=16, h=7.5, width=0.01, layers=glayers_edge_pure)
    ntc_2020(kicad_mod, x + xi, y + bd, angle=(-90))
    step_motor_42(kicad_mod, x, y + ya - 10 - 21, d=1)
    step_motor_57(kicad_mod, x, y + ya - 10 - 28.3, d=1)
    return write_kicad_mod(kicad_mod, zip=z)
def brushless_wheel(W=240, k16=1.2, z=0):
    kicad_mod = new_kicad_mod(w=W, h=W)
    x = y = W / 2
    non_plated_hole(kicad_mod, x, y, 16.7)
    non_plated_hole_circle(kicad_mod, x, y, r=56.5, d=3.8, n=6, angle=0)
    non_plated_hole_circle(kicad_mod, x, y, r=56.5, d=1, n=6, angle=30)
    circle(kicad_mod, x, y, 130)
    circle(kicad_mod, x, y, 160)
    circle(kicad_mod, x, y, W, crosshair=1, layers=glayers_Cmts)
    rd = W / 2 + 0.6
    ac = 23
    for i in range(4):
        radian = math.radians(i * 90 + ac / 2)
        xi = x + rd * math.cos(radian)
        yi = y + rd * math.sin(radian)
        arc(kicad_mod, center=[x, y], start=[xi, yi], angle=90 - ac, layers=glayers_edge_pure, width=k16)
    for i in range(10):
        non_plated_hole_circle(kicad_mod, x, y, r=W / 2 - i * 4 - 4, d=4.9, n=1, angle=28 + i * 36)
    d2028 = 20.4
    d = 30
    w = 60
    whs = [30, 50]
    for n, (x, y) in enumerate(edge_distance_turn(W, W, [d, 10])):
        rectline_center(kicad_mod, x, y, w, 20, angle=n * 90 + 180, w_holes=whs)
    for n, (x, y) in enumerate(edge_distance_turn(W, W, [10, d])):
        rectline_center(kicad_mod, x, y, w, 20, angle=n * 90 - 90, w_holes=whs)
    for n, (x, y) in enumerate(edge_distance_turn(W, W, [10, 10])):
        non_plated_hole(kicad_mod, x, y, d=4.9)
    return write_kicad_mod(kicad_mod, zip=z)
def vacuum(z=0):
    """吸尘器 空气滤芯 口径 57.2  \n六味地黄丸 蜜丸瓶子 外径 58    \n    """
    kicad_mod = new_kicad_mod(w=100, h=100)
    x = y = 50
    non_plated_hole(kicad_mod, x, y, 57.2)
    return write_kicad_mod(kicad_mod, zip=z)
def xn_j_48v(wm=100, hm=22, drill_screw=0.95, z=0):
    x, y = (wm / 2, hm / 2)
    kicad_mod = new_kicad_mod(w=wm, h=hm, text_at=[x, y])
    rectline_center(kicad_mod, x, y, w=174, h=hm, width=0.01, layers=glayers_silk)
    d = 37.5
    non_plated_hole(kicad_mod, x - d, y, 3)
    non_plated_hole(kicad_mod, x + d, y, 3)
    non_plated_hole(kicad_mod, x, y, 10)
    return write_kicad_mod(kicad_mod, zip=z)
def esp32c3_mini(wm=18, hm=23, drill_screw=0.95, z=0):
    """ 上typec 下天线 进入下载模式：按住ESP32C3的BOOT按键，然后按下RESET按键，松开RESET按键，再松开BOOT按键，此时ESP32C3会进入下载模式。（每次连接都需要重新进入下载模式，有时按一遍，端口不稳定会断开，可以通过端口识别声音来判断）\n新模块插入typec一直有端口识别声，无法使用，烧录micropython后串口可以直接使用。    \n# stm32(    \n    """
    x, y = (wm / 2, hm / 2)
    kicad_mod = new_kicad_mod(w=wm, h=hm, text_at=[x, y])
    s2 = [['5V', ' GND', '3V3', '4SCK', '3', '2', '1', '0'], ['5MIS', '6MOS', '7SS', '8SDA', '9SCL', '10', '20RX', '21TX']]
    for i in range(len(s2[0])):
        for xi, si in {1: 0, (-1): 1}.items():
            x, y = (wm / 2 + 7.54 * xi, 2 + 2.54 * i)
            text(kicad_mod, s2[si][i], at=[x + 3 * xi, y])
            size = [drill_screw, drill_screw]
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x, y], size=[2, 0.8], drill=drill_screw, layers=Pad.LAYERS_THT))
    rectline_center(kicad_mod, wm / 2, 3, w=9, h=7.4, width=0.01, layers=glayers_silk)
    rectline_center(kicad_mod, wm / 2, (-7), w=10, h=8, width=0.01, layers=glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=z)
def xl7015(wm=16.1, hm=44, z=0):
    """ 80v > 5v """
    kicad_mod = new_kicad_mod(w=wm, h=hm)
    x, y = (wm / 2, hm / 2)
    hole_square(kicad_mod, x, y, w=12.5, h=40, d=1.9, angle=0, holes=[0, 1, 2, 3], func=plated_hole)
    return write_kicad_mod(kicad_mod, zip=z)
def XH_A232(wm=53.2, hm=45.4, z=0):
    """ 30w x2 """
    kicad_mod = new_kicad_mod(w=wm, h=hm)
    x, y = (wm / 2, hm / 2)
    hole_square(kicad_mod, x, y, w=46, h=38, d=3, angle=0, holes=[0, 1, 2, 3], func=non_plated_hole)
    non_plated_hole(kicad_mod, 17.3, 24.4, 3.5)
    non_plated_hole(kicad_mod, 35.9, 24.4, 3.5)
    wr = 4.4
    rectline_center(kicad_mod, 13, 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 20, 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 33, 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 40.2, 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 13, hm - 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 20, hm - 2, w=wr, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, 36, hm - 1.9, w=7.1, h=3.8, width=0.01, layers=glayers_silk + glayers_edge_pure)
    return write_kicad_mod(kicad_mod, zip=z)
def speaker_48x48(M=48, d=44, z=0):
    """  """
    kicad_mod = new_kicad_mod(w=M, h=M)
    x = y = M / 2
    hole_square(kicad_mod, x, y, 39, d=3, angle=0, holes=[0, 1, 2, 3], func=non_plated_hole)
    circle(kicad_mod, x, y, 33.4)
    circle(kicad_mod, x, y, d)
    radius = d / 2
    initial_hole_spacing = 5
    num_rings = int(d / 6)
    for ring in range(1, num_rings + 1):
        current_radius = radius * (ring / num_rings)
        circumference = 2 * math.pi * current_radius
        hole_spacing = initial_hole_spacing * (1 + (ring - 1) * 0.1)
        n = int(circumference / hole_spacing)
        for i in range(n):
            angle = 2 * math.pi * i / n
            xi = x + current_radius * math.cos(angle)
            yi = y + current_radius * math.sin(angle)
            non_plated_hole(kicad_mod, xi, yi, 1)
    return write_kicad_mod(kicad_mod, zip=z)
def mgn12c_rail(kicad_mod, x, y, angle=0, h=150, hole=2.95, mid_hole=None, write_kicad=False, z=0):
    """  """
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=wm, h=hm)
        write_kicad = False
    rectline_center(kicad_mod, x, y, w=12, h=h, width=0.012, angle=angle, layers=glayers_silk)
    n = h // 25
    if n % 2 == 1:
        n += 1
    for i in range(n // 2):
        if i == 0 and mid_hole:
            non_plated_hole(kicad_mod, *rotate_point(x, y + i * 25, angle, x, y), mid_hole)
        else:
            non_plated_hole(kicad_mod, *rotate_point(x, y + i * 25, angle, x, y), hole)
            non_plated_hole(kicad_mod, *rotate_point(x, y - i * 25, angle, x, y), hole)
    circle(kicad_mod, x, y, diameter=[0.1, 1, 2, 12], crosshair=1, layers=glayers_Cmts)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=z)
def mgn12c_block(kicad_mod, x, y, angle=0, wm=34.7, hm=27, write_kicad=False, up_rail=False, z=0):
    """ ,wm=12,hm=200"""
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=wm, h=hm)
        write_kicad = False
    circle(kicad_mod, x, y, 1, layer=glayers_Cmts)
    hole_square(kicad_mod, x, y, w=15, h=20, d=2.95, angle=angle, holes=[0, 1, 2, 3], func=non_plated_hole)
    rectline_center(kicad_mod, x, y, w=wm, h=hm, width=0.012, angle=angle, layers=glayers_silk)
    multi_dot_line(kicad_mod, [(x - 50, y), (x + 50, y)], layers=glayers_Cmts)
    if py.isnum(up_rail):
        rotate_point
        if py.isfloat(up_rail):
            if angle == 180:
                rectline_center(kicad_mod, x + up_rail, y, w=7.9, h=11.9, width=0.01, angle=angle, layers=glayers_edge_pure)
                non_plated_hole(kicad_mod, x + up_rail - 4 - 5, y, 2.9)
            else:
                rectline_center(kicad_mod, x - up_rail, y, w=7.9, h=11.9, width=0.01, angle=angle, layers=glayers_edge_pure)
                non_plated_hole(kicad_mod, x - up_rail + 4 + 5, y, 2.9)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=z)
    else:
        return None
def mgn12c_rail_triangle(kicad_mod=None, x0=0, y0=0, dh=12.5, wm=34.7, hm=27, z=0):
    """ MGN12C导轨安装三角形支架 """
    write_kicad = not kicad_mod
    if not kicad_mod:
        kicad_mod = new_kicad_mod(w=wm, h=hm)
    cx, cy = (x0 + wm / 2, y0 + hm / 2)
    hole_square(kicad_mod, cx, cy, w=15, h=20, d=2.95, angle=0, holes=[0, 1, 2, 3], func=non_plated_hole)
    multi_dot_line(kicad_mod, [(x0 - 50, cy), (x0 + 50, cy)])
    rectangle_outline(kicad_mod, cx - 6, y0 + hm, w=12, h=100 - hm, width=0.1, layers=glayers_Cmts)
    yr = hm + dh
    for i in [(-2), (-1)]:
        circle(kicad_mod, cx, y0 + yr + i * 25, 3)
    for i in [0, 1, 2, 3]:
        non_plated_hole(kicad_mod, cx, y0 + yr + i * 25, 3.2)
    multi_dot_line(kicad_mod, [(x0, y0), (x0, y0 + hm), (cx - 6, y0 + hm), (cx - 6, y0 + 100), (cx + 6, y0 + 100), (cx + 6, y0 + hm), (x0 + wm, y0 + hm), (x0 + wm, y0), (x0, y0)], width=0.01, layers=glayers_edge_pure, segments=100)
    if write_kicad:
        return write_kicad_mod(kicad_mod, zip=z)
    else:
        return kicad_mod
def boost3470(wm=36, hm=70, z=0):
    """ 适配 250w铝基板升压模块"""
    kicad_mod = new_kicad_mod(w=wm, h=hm)
    for i in range(30):
        if i in (12, 25):
            continue
        else:
            non_plated_hole(kicad_mod, (-0.4), i * 0.9, 0.8)
    x, y = (wm / 2, hm / 2)
    plated_hole(kicad_mod, x + 10, 0, 2.5)
    plated_hole(kicad_mod, x - 10, 0, 2.5)
    non_plated_hole(kicad_mod, x - 15, 4, 3.1)
    non_plated_hole(kicad_mod, x + 15, 4, 3.1)
    drx = 5.5
    non_plated_hole(kicad_mod, x - drx, 10, 10.2)
    non_plated_hole(kicad_mod, x + drx, 10, 10.2)
    rectline_center(kicad_mod, 22, 19, w=21, h=5, width=0.01, layers=glayers_silk + glayers_edge_pure)
    h = 23.4
    multi_dot_line(kicad_mod, [(0, h), (wm, h)], width=0.01, layers=glayers_silk + glayers_edge_pure)
    multi_dot_line(kicad_mod, [(0, 28), (wm, 28)], width=0.01)
    multi_dot_line(kicad_mod, [(6, 0), (6, hm)], width=0.01)
    return write_kicad_mod(kicad_mod, zip=z)
def SSR(wm=45.5, hm=58.5, drill_screw=4.1, z=0):
    kicad_mod = new_kicad_mod(w=wm, h=hm)
    x, y = (wm / 2, hm / 2)
    non_plated_hole(kicad_mod, x, 4.5, drill_screw)
    non_plated_hole(kicad_mod, x - 0.5, 8, drill_screw)
    non_plated_hole(kicad_mod, x, 52.2, drill_screw)
    non_plated_hole(kicad_mod, x - 0.5, 54.5, drill_screw)
    rectangle_outline(kicad_mod, wm, 0, w=-wm, h=-hm - 2, width=0.1, layers=glayers_Cmts)
    return write_kicad_mod(kicad_mod, zip=z)
def trapezoid_socket(drill_screw=2.5, z=0, wm=57, hm=93.5):
    """ 1+2+2 插线板 """
    kicad_mod = new_kicad_mod(w=wm, h=hm)
    x, y = (wm / 2, hm / 2)
    ss = 51.5
    trapezoid(kicad_mod, x, y, ss, wm, hm)
    x0 = x - ss / 2
    y0 = y - hm / 2
    non_plated_hole(kicad_mod, x0 + 11.5, y0 + 8.9, drill_screw)
    non_plated_hole(kicad_mod, x0 + ss - 11.5, y0 + 8.9, drill_screw)
    non_plated_hole(kicad_mod, x - wm / 2 + 0.6 + 5.8, y0 + 73, drill_screw)
    non_plated_hole(kicad_mod, x + wm / 2 - 0.6 - 5.8, y0 + 73, drill_screw)
    non_plated_hole(kicad_mod, x, y0 + 8.7, 3.9)
    non_plated_hole(kicad_mod, x, y0 + 14.7, 7.85)
    yzw = hm + 3.5
    non_plated_hole(kicad_mod, x, yzw, 4)
    non_plated_hole(kicad_mod, x0 + 11.5 + 0.3, 3.3, 4)
    drill_screw = 2.9
    bx = 15.5
    non_plated_hole(kicad_mod, x - bx, yzw - 18, drill_screw)
    non_plated_hole(kicad_mod, x + bx, yzw - 18, drill_screw)
    bx = 17.75
    non_plated_hole(kicad_mod, x - bx, yzw - 18 - 61.3, drill_screw)
    non_plated_hole(kicad_mod, x + bx, yzw - 18 - 61.3, drill_screw)
    return write_kicad_mod(kicad_mod, zip=z)
def stm32f103_board_typec(drill_screw=0.95, djz=0, psize=1.2, pad_size=[1.5, 0.8], z=0):
    """ usb micro 口 在左，丝印从左至右"""
    wm, hm = (23, 53.3)
    kicad_mod = new_kicad_mod(w=wm, h=hm, d=drill_screw, p=pad_size, text_at=[11, (-9)])
    s2 = [['GND', 'GND', '3N', 'RST', 'B11', 'B10', 'B1', 'B0', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1', 'A0', 'C15', 'C14', 'C13', '3B'], ['B12', 'B13', 'B14', 'B15', 'A8', 'A9', 'A10', 'A11', 'A12', 'A15', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', '5V', 'GND', '3V']]
    for i in range(len(s2[0])):
        for xi, si in {1: 0, (-1): 1}.items():
            x = wm / 2 + xi * 7.6
            y = hm / 2 - 25.4 + 1.27 + 2.54 * i - 0.1
            y = hm / 2 - 24.23 + 2.54 * i
            y = 2.5 + 2.54 * i
            text(kicad_mod, s2[si][i], x + 2.1 * xi, y + 0.2)
            size = [drill_screw, drill_screw]
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x - xi * pad_size[0] * 0.2, y], size=pad_size, drill=0, layers=Pad.LAYERS_THT))
    rectline_center(kicad_mod, wm / 2, 4.3, w=9, h=8.6, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, 14, w=11, h=8, width=0.01, layers=glayers_silk + glayers_edge_pure, crosshair=1)
    rectline_center(kicad_mod, wm / 2, 26.5, w=8.5, h=8.5, width=0.01, layers=glayers_edge_pure, angle=45)
    rounded_rectangle(kicad_mod, wm / 2, 35.6, w=10.2 + djz, h=4 + djz, radius=2, width=0.01, layers=glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, 41, w=8.3, h=3.4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    for i in range(8):
        xe = (i - 1) * 0.2
        dw = 7.8
        dxled = (-0.2)
        y = 45
        non_plated_hole(kicad_mod, dw + xe + dxled, y, 1.4)
        non_plated_hole(kicad_mod, wm - dw - xe + dxled, y, 1.4)
    rectline_center(kicad_mod, wm / 2, 48.5, w=10.2, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    for yi in range(18):
        for i in range(4):
            plated_hole(kicad_mod, wm / 2 - 3.8 + 2.54 * i, 50.5 + yi * 0.3, 0.9, size=1.1, number=f'4p{i}')
    rectline_center(kicad_mod, wm / 2, hm / 2, w=wm, h=hm, width=0.1, layers=glayers_silk)
    multi_dot_line(kicad_mod, [(0, 0), (wm, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(wm, 0), (0, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2), (wm, hm / 2)], width=0.01)
    multi_dot_line(kicad_mod, [(wm / 2, 0), (wm / 2, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2 + 1.27), (wm, hm / 2 + 1.27)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2 - 1.27), (wm, hm / 2 - 1.27)], width=0.01)
    return write_kicad_mod(kicad_mod, zip=z)
def stm32f103_board_extend(d=[3, 3.5], xd=3, dxi=7.48, z=0):
    if py.isnum(d):
        d = [d]
    assert d
    if py.isnum(xd):
        xd_temp = []
        for i, di in enumerate(d):
            xd_temp.append(xd + i * 0.1)
        xd = xd_temp
    wm, hm = (22.7, 53.3)
    kicad_mod = new_kicad_mod(text_at=[11, (-9)], w=wm, h=hm, d=d)
    s2 = [['GND', 'GND', '3N', 'RST', 'B11', 'B10', 'B1', 'B0', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1', 'A0', 'C15', 'C14', 'C13', '3B'], ['B12', 'B13', 'B14', 'B15', 'A8', 'A9', 'A10', 'A11', 'A12', 'A15', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', '5V', 'GND', '3V']]
    center_y = hm / 2 - 25.4 + 1.27 + 24.13
    for i in range(len(s2[0])):
        for xi, si in {1: 0, (-1): 1}.items():
            x_orig = wm / 2 + xi * dxi
            y_orig = hm / 2 - 25.4 + 1.27 + 2.54 * i - 0.1
            prev_x = x_orig
            prev_y = y_orig
            sn = s2[si][i]
            ka = dict(number=sn, type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, layers=Pad.LAYERS_THT)
            kicad_mod.append(Pad(at=[prev_x, prev_y], size=[0.4, 0.4], drill=0.4, **ka))
            for level, spacing in enumerate(d):
                x_ext = x_orig + xi * (4.0 + xd[level] * level)
                offset_from_center = (i - 9.5) * spacing
                y_ext = center_y + offset_from_center
                drill_size = 1.0 + 0.1 * level
                drill_size = min(1.4, drill_size)
                pad_size = min(1.2 + 0.4 * level, 1.8)
                kicad_mod.append(Pad(at=[x_ext, y_ext], drill=drill_size, size=[pad_size, pad_size], **ka))
                multi_dot_line(kicad_mod, [(prev_x, prev_y), (x_ext, y_ext)], layers=glayers_F_Cu, width=0.3 + 0.1 * level)
                prev_x = x_ext
                prev_y = y_ext
                if level == len(d) - 1:
                    text(kicad_mod, sn, x_ext - xi * 1, y_ext - 1.4)
                else:
                    text(kicad_mod, sn[(-1)], x_ext + xi * 1, y_ext)
    return write_kicad_mod(kicad_mod, zip=z)
def stm32f103_board(drill_screw=0.95, djz=0, psize=1.2, pad_size=[1.5, 0.8], z=0):
    """ usb micro 口 在左，丝印从左至右"""
    wm, hm = (22.7, 53.3)
    kicad_mod = new_kicad_mod(w=wm, h=hm, d=drill_screw, p=pad_size)
    s2 = [['GND', 'GND', '3N', 'RST', 'B11', 'B10', 'B1', 'B0', 'A7', 'A6', 'A5', 'A4', 'A3', 'A2', 'A1', 'A0', 'C15', 'C14', 'C13', '3B'], ['B12', 'B13', 'B14', 'B15', 'A8', 'A9', 'A10', 'A11', 'A12', 'A15', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', '5V', 'GND', '3V']]
    for i in range(len(s2[0])):
        for xi, si in {1: 0, (-1): 1}.items():
            x = wm / 2 + xi * 7.48
            y = hm / 2 - 25.4 + 1.27 + 2.54 * i - 0.1
            text(kicad_mod, s2[si][i], x + 2.3 * xi, y + 0.2)
            size = [drill_screw, drill_screw]
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_THT, shape=Pad.SHAPE_CIRCLE, at=[x, y], size=size, drill=drill_screw, layers=Pad.LAYERS_THT))
            kicad_mod.append(Pad(number=s2[si][i], type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x - xi * pad_size[0] * 0.2, y], size=pad_size, drill=0, layers=Pad.LAYERS_THT))
    rectline_center(kicad_mod, wm / 2, 3, w=8.5, h=6.3, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, 12.4, w=11.4, h=6, width=0.01, layers=glayers_silk + glayers_edge_pure)
    for x, y in U.range2d(2, 3):
        x = wm - 8 - 2.54 + x * 2.54
        y = 10 + y * 2.54
    rectline_center(kicad_mod, wm / 2, 12.54, w=11, h=7.7, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, 26.8, w=8.1, h=8.1, width=0.01, layers=glayers_edge_pure, angle=45)
    rounded_rectangle(kicad_mod, wm / 2, hm - 17.8, w=10.2 + djz, h=4 + djz, radius=2, width=0.01, layers=glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, hm - 17.8 + 5.2, w=8.3, h=3.3, width=0.01, layers=glayers_silk + glayers_edge_pure)
    rectline_center(kicad_mod, wm / 2, hm - 17.8 + 5.2, w=8.3, h=3.4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    for i in range(8):
        xe = (i - 1) * 0.2
        dw = 7.8
        dxled = (-0.2)
        non_plated_hole(kicad_mod, dw + xe + dxled, hm - 8.8, 1.4)
        non_plated_hole(kicad_mod, wm - dw - xe + dxled, hm - 8.8, 1.4)
    rectline_center(kicad_mod, wm / 2, hm - 4.1, w=10.2, h=4, width=0.01, layers=glayers_silk + glayers_edge_pure)
    for i in range(4):
        non_plated_hole(kicad_mod, wm / 2 - 3.8 + 2.54 * i, hm - 2 - 4, 0.9, size=1.1, number=f'4p{i}')
        non_plated_hole(kicad_mod, wm / 2 - 3.8 + 2.54 * i, hm - 2 - 4.2, 0.9, size=1.1, number=f'4p{i}')
        non_plated_hole(kicad_mod, wm / 2 - 3.8 + 2.54 * i, hm - 2 - 4.4, 0.9, size=1.1, number=f'4p{i}')
    for yi in range(21):
        for i in range(4):
            plated_hole(kicad_mod, wm / 2 - 3.8 + 2.54 * i, hm - 2 + yi * 0.3, 0.9, size=1.1, number=f'4p{i}')
    rectline_center(kicad_mod, wm / 2, hm / 2, w=wm, h=hm, width=0.1, layers=glayers_silk)
    multi_dot_line(kicad_mod, [(0, 0), (wm, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(wm, 0), (0, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2), (wm, hm / 2)], width=0.01)
    multi_dot_line(kicad_mod, [(wm / 2, 0), (wm / 2, hm)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2 + 1.27), (wm, hm / 2 + 1.27)], width=0.01)
    multi_dot_line(kicad_mod, [(0, hm / 2 - 1.27), (wm, hm / 2 - 1.27)], width=0.01)
    return write_kicad_mod(kicad_mod, zip=z)
def stm32_7segment_display(z=0):
    kicad_mod = new_kicad_mod()
    x, y = (24.1, 15)
    w4 = 30.25
    h4 = 14.25
    wm = 41.7
    hm = 23.5
    rectline_center(kicad_mod, x, y, w=wm, h=hm, width=0.1, layers=glayers_silk)
    dw, dh = (36.5, 19.7)
    x1 = x - dw / 2 - 0.4
    x2 = x + dw / 2
    non_plated_hole(kicad_mod, x1, y - dh / 2, 2.95)
    non_plated_hole(kicad_mod, x2, y - dh / 2, 2.95)
    non_plated_hole(kicad_mod, x1, y + dh / 2, 2.95)
    non_plated_hole(kicad_mod, x2, y + dh / 2, 2.95)
    rectline_center(kicad_mod, x + (6.3 - (wm - w4) / 2), y + 0.1, w=w4, h=h4, width=0.1, layers=glayers_edge_pure + glayers_silk)
    multi_dot_line(kicad_mod, [(0, 0), (100, 100)], layers=glayers_silk)
    return write_kicad_mod(kicad_mod, zip=z)
def as5600(x=50, y=50, w=23.0, h=23.599999999999998, zip=0, drill_screw=3.5, kicad_mod=None):
    """磁铁直径 4  """
    is_write = False
    if not kicad_mod:
        kicad_mod = new_kicad_mod()
        is_write = True
    rectline_center(kicad_mod, x, y, w, h)
    hole_square(kicad_mod, x, y, 15.8, drill_screw, angle=0, holes=[0, 1, 2, 3], func=non_plated_hole)
    hole_square(kicad_mod, x, y, 15.8, drill_screw, angle=45, holes=[0, 1, 2, 3], func=circle)
    if is_write:
        return write_kicad_mod(kicad_mod, zip=zip)
def esp32c3(drill_screw=0.95):
    kicad_mod = new_kicad_mod(w=21, h=52)
    s2 = [['GND', '5V', 'BOOT', 'IO08', 'IO04', 'IO05', '3.3V', 'GND', 'PB_11', 'IO07', 'IO06', 'IO10', 'IO03', 'IO02', '3.3V', 'GND'], ['5V', 'PWB', 'GND', '3.3V', 'RESET', 'NC', 'IO13', 'U0_TX', 'U0_RX', 'GND', 'IO19', 'IO18', 'IO12', 'IO01', 'IO00', 'GND']]
    for i in range(len(s2[0])):
        plated_hole(kicad_mod, 1.5, 6.5 + 2.54 * i, drill_screw, number=s2[0][i])
        plated_hole(kicad_mod, 19.5, 6.5 + 2.54 * i, drill_screw, number=s2[1][i])
    return write_kicad_mod(kicad_mod, zip=1)
def SOP8(body_width=3.9, zip=0):
    kicad_mod = new_kicad_mod(name=f'sop8_w{body_width}', w=6, h=0)
    pad_width = 0.6
    pad_height = 2
    pitch = 1.27
    h = 6
    x0 = pitch
    x0 = 0
    y0 = 0
    for i in range(8):
        x = i % 4 * pitch
        y = (i // 4 - 0.5) * h
        if i % 4 in [0, 3]:
            t = 0.95
        else:
            t = 1
        kicad_mod.append(Pad(number=str(i + 1), type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x0 + x, y0 + y], size=[pad_width, pad_height * t], layers=Pad.LAYERS_SMT))
        mka = py.dict(kicad_mod=kicad_mod, width=0.2, layer=['F.Cu'])
        x2, y2 = (x0 + i % 4 * 2.54 - 2.54 + 0.2, y0 + y * 2)
        multi_dot_line(dots=([x0 + x, y0 + y], [x2, y2]), **mka)
        kicad_mod.append(Pad(number=str(i + 1), type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x2, y2 * 1.08], size=[1, 2], layers=Pad.LAYERS_SMT))
        if i == 0:
            kicad_mod.append(Pad(number=str(i + 1), type=Pad.TYPE_SMT, shape=Pad.SHAPE_CIRCLE, at=[x2, y2 * 1.08], size=[1.5, 1.5], layers=Pad.LAYERS_SMT))
    x, y = (1.5 * pitch, 0)
    circle(kicad_mod, x, y, diameter=[1, 12], crosshair=1)
    D = 1
    non_plated_hole(kicad_mod, x - body_width / 2 - D, y0, D)
    non_plated_hole(kicad_mod, x + body_width / 2 + D, y0, D)
    return write_kicad_mod(kicad_mod, zip=zip)
def TSSOP20():
    kicad_mod = new_kicad_mod(w=7, h=0)
    pad_width = 0.5
    pad_height = 1.2
    pitch = 0.65
    body_width = 6.5
    h = 4.4
    h = 5.6
    x0 = pitch
    x0 = 0
    y0 = 0
    for i in range(20):
        x = i % 10 * pitch
        y = (i // 10 - 0.5) * h
        if i % 10 in [0, 9]:
            t = 0.95
        else:
            t = 1
        kicad_mod.append(Pad(number=str(i), type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x0 + x, y0 + y], size=[0.2, 2.8 * t], layers=Pad.LAYERS_SMT))
        mka = py.dict(kicad_mod=kicad_mod, width=0.2, layer=['F.Cu', 'B.SilkS'])
        x2, y2 = (x0 + 2.54 / pitch * x - 8.49, y0 + y * 3)
        multi_dot_line(dots=([x0 + x, y0 + y * 1.5 * t ** 3], [x2, y2]), **mka)
        kicad_mod.append(Pad(number=str(i), type=Pad.TYPE_SMT, shape=Pad.SHAPE_RECT, at=[x2, y2 * 1.08], size=[1, 2], layers=Pad.LAYERS_SMT))
    D = 1
    non_plated_hole(kicad_mod, x0 - D - 0.7, y0, D)
    non_plated_hole(kicad_mod, x0 + 6.5 + D, y0, D)
    return write_kicad_mod(kicad_mod)
def szj25_pillow_block(w100=100, de=2.5, drill_screw=3.9, m6=5.85, z=0):
    """  """
    # ***<module>.szj25_pillow_block: Failure detected at line number 3026 and instruction offset 8: Different bytecode
    kicad_mod = new_kicad_mod(name='pillow-mid')
    crosshair(kicad_mod, 50, 50)
    ayz = 27.7
    x, y = get_szj25_57(kicad_mod, drill_screw=drill_screw, m6=m6, zd=24.88, h=81.8, dls2x=(-0.2), ayz=ayz, axz=0, m57=False, f_dz57x=lambda: 23.5 + w_szj / 2 + drill_screw / 2, f_dz57y=lambda: 0)
    step_motor_57(kicad_mod, x, y, drill_screw=3)
    hole_square(kicad_mod, x, y, 47, 3, angle=0, holes=[0, 1, 2, 3], func=circle)
    non_plated_hole(kicad_mod, x, y, 9.88)
    non_plated_hole(kicad_mod, x - dz57x, y, 1)
    step_motor_57(kicad_mod, x, y, drill_screw=1, angle=45)
    z = ([0, 0], [0, 4.2], [3.45, 7.4], [3.45, 10.2], [0, 13.3], [0, 17.5])
    symmetric_x(kicad_mod, z, xm=19.7, xmid=x, y0=0, angle=0, width=0.01, layers=glayers_silk + glayers_Cmts)
    multi_dot_line(kicad_mod, [(x - 22, 30), (x + 22, 30)], layers=glayers_silk)
    zcz = 47
    azcz = 45
    cz_holes = (1, 3)
    if m6 < 5:
        cz_holes = (0, 1, 2, 3)
    hole_rect_center(kicad_mod, x, y, zcz / 1.4142, d=m6, angle=azcz, holes=cz_holes)
    hole_rect_center(kicad_mod, x, y, zcz / 1.4142, d=[0.1, 1, 3, 5.85, 6.5], angle=azcz, func=circle)
    hole_rect_center(kicad_mod, x, y, zcz / 1.4142, d=[0.1, 1, 3, 5.85, 6.5], angle=45, func=circle)
    hole_rect_center(kicad_mod, x, y, 45.25526799604017, d=1, angle=10, holes=cz_holes)
    xz3 = x - dz57y
    yz3 = y + dz57x
    non_plated_hole(kicad_mod, x=xz3, y=yz3, d=m6)
    rectline_center(kicad_mod, xz3 + dyz_szj, yz3, w=h_szj, h=w_szj)
    crosshair(kicad_mod, xz3 + dyz_szj, yz3, w=h_szj, h=w_szj)
    circle(kicad_mod, x=xz3 + dyz_ls2, y=yz3 - 8, d=m6)
    circle(kicad_mod, x=xz3 + dyz_ls2, y=yz3 + 8, d=m6)
    return write_kicad_mod(kicad_mod, zip=z)
def hua4_铜螺母42h(w100=100, de=2.5, drill_screw=3.9, z=1):
    kicad_mod = new_kicad_mod()
    x = 21.0
    y = 100 - x
    circle(kicad_mod, x, y, diameter=[1, 3, 4, 5, 6, 6.35, 8, 10, 12], crosshair=1, layers=glayers_silk)
    non_plated_hole(kicad_mod, x, y, 4.9)
    hole_square(kicad_mod, x, y, 31, 2.95, angle=0)
    rectline_center(kicad_mod, x, y, w=42, angle=0, width=0.1, layers=glayers_F_Cu + glayers_silk)
    multi_dot_line(kicad_mod, [(x, y), (x, 101)], layers=glayers_edge_pure, width=4.8)
    return write_kicad_mod(kicad_mod, zip=z)
def yygj28_szj25(w100=100, de=2.5, drill_screw=3.9, z=0):
    """ x 45  斜 28液压管夹 45 """
    kicad_mod = new_kicad_mod()
    x, y = (50, 50)
    a = 11
    hole_square(kicad_mod, x, y, 60, 24.85, angle=a, holes=[1, 2])
    rectline_center(kicad_mod, x, y, w=60, h=60, angle=a, width=0.1, layers=glayers_F_Cu + glayers_silk)
    return write_kicad_mod(kicad_mod, zip=z)
def pro_test(z=1):
    kicad_mod = new_kicad_mod()
    non_plated_hole(kicad_mod, 50, 50, 11)
    multi_dot_line(kicad_mod, [(0, 50), (77, 50)], layers='F.SilkS', width=0.01)
    multi_dot_line(kicad_mod, [(50, 0), (50, 50)], layers='B.SilkS', width=0.01)
    return write_kicad_mod(kicad_mod, zip=z)
def get_szj25(kicad_mod, xz, yz, zd=24.85, h=81.8):
    w_szj = 32.1
    h_szj = h
    xz = x + 27 + 1.3 + 3
    yz = y - dz57
    y_szj = h_szj / 2
    rectline_center(kicad_mod, xz, y_szj, w=w_szj, h=h_szj)
    crosshair(kicad_mod, xz, y_szj, w=w_szj, h=h_szj)
def get_szj25_57(kicad_mod, h=81.8, zd=24.85, ayz=24.5, axz=None, dyz2=24.5, dls2x=0, drill_screw=3.9, m6=5.85, m57=True, f_dz57x=None, f_y_szj=None, f_dz57y=None):
    global yz2
    global d57x2
    global h_szj
    global dyz_szj
    global dls
    global dz57x
    global w_szj
    global w57
    global xz
    global y_szj
    global yz
    global dz57y
    global dyz_ls2
    angle = 0
    w57 = 56.6
    yz = ayz
    if py.callable(f_dz57y):
        dz57y = f_dz57y()
    else:
        dz57y = 3.8
    y = yz + dz57y
    if py.callable(f_dz57x):
        dz57x = f_dz57x()
    else:
        dz57x = w57 / 2 + 3
    w_szj = 32.2
    h_szj = h
    if axz:
        xz = axz
    else:
        xz = 100 - w_szj / 2
    x = xz - dz57x
    circle(kicad_mod, x=xz, y=yz, crosshair=1, diameter=[25, 28, 40])
    if m57:
        step_motor_57(kicad_mod, x, y, drill_screw=2.9, circle_diameter=[10, 12, 14, 22, 26, 28, 30, 32])
        step_motor_57(kicad_mod, x, y, drill_screw=drill_screw, holes=[2, 3])
    d57x2 = x - w57 / 2
    if d57x2 > 20:
        step_motor_57(kicad_mod, w57 / 2, y, drill_screw=drill_screw)
        step_motor_57(kicad_mod, w57 / 2, w57 / 2, drill_screw=drill_screw)
    dyz_szj = 16.4
    if py.callable(f_y_szj):
        y_szj = f_y_szj()
    else:
        y_szj = yz + dyz_szj
    rectline_center(kicad_mod, xz, y_szj, w=w_szj, h=h_szj)
    crosshair(kicad_mod, xz, y_szj, w=w_szj, h=100)
    non_plated_hole(kicad_mod, x=xz, y=yz, d=zd)
    yz2 = y_szj + h_szj / 2 - dyz2
    rectline_center(kicad_mod, xz + 25, yz2, w=50, h=25, layers=glayers_F_Cu + glayers_silk)
    multi_dot_line(kicad_mod, [(xz - 26, yz2), (xz + 16, yz2)], layers=glayers_F_Cu + glayers_silk, width=0.01)
    yls2 = 75.8 - (25 - yz)
    dls = 7
    dyz_ls2 = 50.35
    yls2 = yz + dyz_ls2
    non_plated_hole(kicad_mod, x=xz - 8 + dls2x, y=yls2, d=m6)
    non_plated_hole(kicad_mod, x=xz + 8 + dls2x, y=yls2, d=m6)
    non_plated_hole(kicad_mod, x=xz - 8, y=yls2, d=m6)
    non_plated_hole(kicad_mod, x=xz + 8, y=yls2, d=m6)
    y2 = yz2 - dz57y
    non_plated_hole(kicad_mod, 100, y2, 1)
    non_plated_hole(kicad_mod, 84.3, y2, 1)
    zc2 = 12.75
    multi_dot_line(kicad_mod, [(81, y2 - zc2), (100, y2 - zc2)], layers=glayers_F_Mask + glayers_silk, width=0.5)
    multi_dot_line(kicad_mod, [(81, y2), (100, y2)], layers=glayers_F_Mask + glayers_silk, width=0.5)
    multi_dot_line(kicad_mod, [(81, y2 + zc2), (100, y2 + zc2)], layers=glayers_F_Mask + glayers_silk, width=0.5)
    multi_dot_line(kicad_mod, [(82, y2 - 13), (82, y2 + 13)], layers=glayers_F_Mask + glayers_silk, width=1)
    multi_dot_line(kicad_mod, [(100, y2 - 13), (100, y2 + 13)], layers=glayers_F_Mask + glayers_silk, width=1)
    return (x, y)
def szj25_mid(w100=100, de=2.5, drill_screw=3.9, z=0):
    kicad_mod = new_kicad_mod()
    x, y = get_szj25_57(kicad_mod, zd=5.9)
    x, y = (xz - 20, yz2 - dz57y)
    rectline_center(kicad_mod, x, y, w=8, h=26, layers=glayers_F_Cu + glayers_silk)
    multi_dot_line(kicad_mod, [(x - 6, y), (x + 6, y)], layers=glayers_silk, width=0.01)
    x, y = (15, 75)
    non_plated_hole(kicad_mod, x, y, 25.9)
    circle(kicad_mod, x, y, crosshair=1, diameter=[26, 28, 30, 40])
    x, y = (50, 80)
    non_plated_hole(kicad_mod, x, y, 29.9)
    circle(kicad_mod, x, y, crosshair=1, diameter=[26, 28, 30, 40])
    return write_kicad_mod(kicad_mod, zip=z)
def szj25_818(w100=100, de=2.5, drill_screw=3.9, z=0):
    """  """
    kicad_mod = new_kicad_mod()
    crosshair(kicad_mod, 50, 50)
    zd = 24.85
    zd = 5.86
    x, y = get_szj25_57(kicad_mod, zd=zd, h=81.8)
    b57 = w57 / 2 + (100 - x - w_szj)
    yb57 = 100 - b57
    xb57 = 100 - w_szj - 0.8
    multi_dot_line(kicad_mod, [((-1), yb57), (xb57, yb57)], layers=glayers_edge_pure, width=0.01)
    multi_dot_line(kicad_mod, [((-1), yb57), (xb57, yb57)], layers=glayers_edge_pure, width=1.6)
    multi_dot_line(kicad_mod, [(xb57, yb57), (xb57, h_szj)], layers=glayers_edge_pure, width=1.6)
    t = 4
    for i in range(int(20 // t) + 2):
        non_plated_hole(kicad_mod, x=xb57, y=yb57 + t * i, d=1)
    t = 1
    for i in range(int(9 // t)):
        non_plated_hole(kicad_mod, x=100 - w_szj + t * i, y=h_szj + 0.5, d=1)
    t = 1.4
    for i in range(int(12 // t) + 2):
        non_plated_hole(kicad_mod, x=100 - w_szj + t * i, y=h_szj + 0.5, d=1)
    multi_dot_line(kicad_mod, [(100 - w_szj - 1, h_szj + 0.5), (100 - w_szj + 14, h_szj + 0.5)], layers=glayers_F_Mask, width=2)
    t = 2.4
    for ix, iy in U.iter2d(9, 9):
        non_plated_hole(kicad_mod, x=h_szj + 0.5 + t * ix, y=h_szj + 0.5 + t * iy, d=1)
    square(kicad_mod, 91, 91, 18.3, layers=glayers_F_Mask)
    circle(kicad_mod, x=xz, y=yz, crosshair=1, diameter=[25, 28, 40])
    x = w57 / 2
    y = 100 - (dz57x - w_szj / 2)
    step_motor_57(kicad_mod, x, y, drill_screw=3.9, holes=[], d=25.83)
    step_motor_57(kicad_mod, x, y - d57x2, drill_screw=3.9, holes=[0, 3], d=2.95, rectline_layers=glayers_Cmts)
    circle(kicad_mod, x=x, y=y, crosshair=1, diameter=[25, 28, 30])
    dzls = h_szj - xz - 7
    rectline_center(kicad_mod, h_szj / 2, y, w=h_szj, h=w_szj)
    non_plated_hole(kicad_mod, h_szj - dls, y + 8, 3.9)
    non_plated_hole(kicad_mod, h_szj - dls, y - 8, 1)
    multi_dot_line(kicad_mod, [(h_szj - yz, y - 8), (h_szj - yz, y + 8)], layers=glayers_silk, width=5.85)
    multi_dot_line(kicad_mod, [(h_szj - yz, y - w_szj / 2), (h_szj - yz, 101)], layers=glayers_silk, width=0.01)
    non_plated_hole(kicad_mod, h_szj - yz, yb57 + 1, 1)
    non_plated_hole(kicad_mod, h_szj - yz, 100.2, 1)
    multi_dot_line(kicad_mod, [(dls, y - w_szj / 2), (dls, 101)], layers=glayers_silk, width=0.01)
    multi_dot_line(kicad_mod, [(dls, y - 7), (dls, y - 8)], layers=glayers_silk, width=5.85)
    non_plated_hole(kicad_mod, dls, yb57 + 1, 1)
    non_plated_hole(kicad_mod, dls, 100.2, 1)
    return write_kicad_mod(kicad_mod, zip=z)
def yygj25(w100=100, de=2.5, drill_screw=3.9, z=0):
    kicad_mod = new_kicad_mod()
    crosshair(kicad_mod, 50, 50)
    x = 50
    y = 76
    angle = 0
    rc_ka = dict(kicad_mod=kicad_mod, x0=x, y0=y, angle=angle, width=0.1, layers=glayers_F_Cu + glayers_silk)
    rectline_center(**rc_ka, w=83, h=48)
    multi_dot_line(kicad_mod, [(x - 42, y), (x + 42, y)], layers=glayers_silk, width=0.01)
    for i in [(-1), 1]:
        non_plated_hole(kicad_mod, x + 22.5 * i, y, 24.9)
        circle(kicad_mod, x + 22.5 * i, y, crosshair=1, diameter=[25, 28, 40])
    y -= 5.7
    rc_ka['y0'] = y
    circle(kicad_mod, x, y, diameter=[1, 3, 4, 5, 6, 6.35, 8, 10, 12, 141.4243], crosshair=1, layers=glayers_silk)
    non_plated_hole(kicad_mod, x, y, 4.9)
    hole_square(kicad_mod, x, y, 31, 2.95, angle=45)
    rectline_center(**U.dict_update_return_new(rc_ka, angle=45), w=42)
    hole_square(kicad_mod, x, y, 47, 3.9, angle=angle)
    rectline_center(**rc_ka, w=56.5)
    e = 5
    non_plated_hole(kicad_mod, 100 - e, e, 2.95)
    e = 5.05
    non_plated_hole(kicad_mod, e, 100 - e, 2.95)
    e = 4.9
    non_plated_hole(kicad_mod, 100 - e, 100 - e, 2.95)
    dj = 4.8
    j1 = 10.5 - dj
    j2 = 16.5 - dj
    for x, y in [[j1 + 3, j1 + 3], [50, j1 + 3], [97 - j1, j1 + 3]]:
        non_plated_hole(kicad_mod, x - 3, y - 3, drill_screw)
        non_plated_hole(kicad_mod, x + 3, y + 3, drill_screw)
    y0 = (j1 + 3) * 2
    multi_dot_line(kicad_mod, [(0, y0), (101, y0)], layers=glayers_silk, width=0.01)
    j1 = 10.5
    yz = y0 + j1 + 3
    for x, y in [[j1 + 3, yz], [50, yz], [97 - j1, yz]]:
        non_plated_hole(kicad_mod, x - 3, y - 3, drill_screw)
        non_plated_hole(kicad_mod, x + 3, y + 3, drill_screw)
    return write_kicad_mod(kicad_mod, zip=z)
def hua4fl(w100=100, de=2.5, drill_screw=3.9, z=0):
    kicad_mod = new_kicad_mod()
    x, y = (50, 50)
    angle = 0
    circle(kicad_mod, x, y, diameter=[1, 3, 4, 5, 6, 25, 28, 40, 141.4243], crosshair=1, layers=glayers_silk)
    rc_ka = dict(kicad_mod=kicad_mod, x0=x, y0=y, angle=angle, width=0.1, layers=glayers_F_Cu + glayers_silk)
    hole_square(kicad_mod, x, y, 31, 2.95, angle=angle)
    rectline_center(**rc_ka, w=42)
    hole_square(kicad_mod, x, y, 47, 3.9, angle=angle)
    rectline_center(**rc_ka, w=56.5)
    de = 20
    for n, (x, y) in enumerate(edge_distance(w100, w100, [de, de])):
        non_plated_hole(kicad_mod, x, y, 5.95)
        circle(kicad_mod, x, y, crosshair=1, diameter=[6, 12])
        hole_square(kicad_mod, x, y, 14.143, 2.95, angle=angle)
    return write_kicad_mod(kicad_mod, zip=z)
def hua4ce(w100=100, de=2.5, drill_screw=3.9, z=0):
    kicad_mod = new_kicad_mod()
    crosshair(kicad_mod, 50, 50)
    dj = 4.8
    j1 = 10.5 - dj
    j2 = 16.5 - dj
    for x, y in edge_distance(w100, w100, [j1 + 3, j1 + 3]):
        non_plated_hole(kicad_mod, x + 3, y - 3, drill_screw)
        non_plated_hole(kicad_mod, x - 3, y + 3, drill_screw)
    return write_kicad_mod(kicad_mod, zip=z)
def z25(w100=100, de=2.5, drill_screw=3.9, z=0):
    kicad_mod = new_kicad_mod()
    crosshair(kicad_mod, 50, 50)
    d47 = 4.75
    w57 = 56.6
    x = y = w57 / 2
    for x, y in [(x, y), (100 - x, 100 - y)]:
        if x == w57 / 2:
            non_plated_hole(kicad_mod, x, y, 24.95)
        else:
            non_plated_hole(kicad_mod, x, y, 2.95)
        for angle in [0, 45]:
            rc_ka = dict(kicad_mod=kicad_mod, x0=x, y0=y, angle=angle, width=0.1, layers=glayers_F_Cu + glayers_silk)
            hole_square(kicad_mod, x, y, 31, 2.95, angle=angle)
            rectline_center(**rc_ka, w=42)
            hole_square(kicad_mod, x, y, 47, 3.9, angle=angle)
            rectline_center(**rc_ka, w=w57)
    U.dict_multi_pop(rc_ka, 'x0', 'y0', 'angle')
    rc_ka['layers'] = glayers_silk
    x, y = (79, 21)
    non_plated_hole(kicad_mod, x, y, 6.8)
    hole_square(kicad_mod, x, y, 31, 2.95, angle=0)
    rectline_center(**rc_ka, x0=x, y0=y, w=42)
    x, y = (21, 79)
    non_plated_hole(kicad_mod, x, y, 8.4)
    hole_square(kicad_mod, x, y, 31, 2.95, angle=0)
    rectline_center(**rc_ka, x0=x, y0=y, w=42)
    return write_kicad_mod(kicad_mod, zip=z)
def hua4(w100=100, de=2.5, drill_screw=3.9, z=1):
    kicad_mod = new_kicad_mod()
    dx = 50
    circle(kicad_mod, dx, 50, diameter=[1, 3, 4, 5, 6, 8, 10, 12, 43.833999999999996], crosshair=1, layers=glayers_silk)
    non_plated_hole(kicad_mod, dx, 50, 8.85)
    hole_square(kicad_mod, dx, 50, 31, 2.95, angle=45)
    rectline_center(kicad_mod, dx, 50, w=42, h=42, angle=45, width=0.1, layers=glayers_F_Cu + glayers_silk)
    de = 20
    for n, (x, y) in enumerate(edge_distance(w100, w100, [de, de])):
        non_plated_hole(kicad_mod, x, y, 5.95)
        circle(kicad_mod, x, y, crosshair=1, diameter=[6, 12, 15, 19, 21, 28, 40])
    dj = 4.8
    j1 = 10.5 - dj
    j2 = 16.5 - dj
    for x, y in edge_distance(w100, w100, [j1 + 3, j1 + 3]):
        non_plated_hole(kicad_mod, x + 3, y - 3, drill_screw)
        non_plated_hole(kicad_mod, x - 3, y + 3, drill_screw)
    non_plated_hole(kicad_mod, j1, 53, drill_screw)
    non_plated_hole(kicad_mod, j2, 47, drill_screw)
    non_plated_hole(kicad_mod, w100 - j2, 53, drill_screw)
    non_plated_hole(kicad_mod, w100 - j1, 47, drill_screw)
    non_plated_hole(kicad_mod, 47, j1, drill_screw)
    non_plated_hole(kicad_mod, 53, j2, drill_screw)
    non_plated_hole(kicad_mod, 53, w100 - j1, drill_screw)
    non_plated_hole(kicad_mod, 47, w100 - j2, drill_screw)
    as5600(kicad_mod=kicad_mod)
    return write_kicad_mod(kicad_mod, zip=z)
def m3_main3(dy2b=30, dx=12.3, angle=45, w=33, write=True):
    kicad_mod = new_kicad_mod(f'm3main_{dy2b}', w=w, h=100)
    if write:
        dx = w / 2
    circle(kicad_mod, dx, 50, diameter=[1, 22, 66.6], crosshair=1, layers=glayers_silk)
    non_plated_hole(kicad_mod, dx, 50 - dy2b, 8.85)
    hole_square(kicad_mod, dx, 50 - dy2b, 31, 2.95, angle=0, holes=(0, 1, 2))
    non_plated_hole(kicad_mod, dx, 50, 8.85)
    hole_square(kicad_mod, dx, 50, 31, 2.95, angle=0)
    rectline_center(kicad_mod, dx, 50, w=42, h=42, width=0.1, layers=glayers_F_Cu + glayers_silk)
    non_plated_hole(kicad_mod, dx, 50 + dy2b, 8.85)
    hole_square(kicad_mod, dx, 50 + dy2b, 31, 2.95, angle=0, holes=(0, 2, 3))
    if write:
        km, fname = write_kicad_mod(kicad_mod)
        return (km, fname)
    else:
        return kicad_mod
def m3_hua_gai(w100=100, de=2.5):
    kicad_mod = new_kicad_mod(m3_hua.__name__)
    dz = 27
    non_plated_hole(kicad_mod, 50, dz, 8.9)
    rectline_center(kicad_mod, 50, dz, w=42, h=42, width=0.1, layers=glayers_F_Cu + glayers_silk)
    circle(kicad_mod, 50, dz, diameter=[1, 3, 5, 9, (100 - dz) * 2 * (1.116 + 0.0035 * dz)], crosshair=1, layers=glayers_silk)
    for i in range(3):
        if i == 1:
            continue
        else:
            x = 16.6665 + 33.333 * i
            non_plated_hole(kicad_mod, x, dz, 8.95)
    hole_square(kicad_mod, 50, dz, 31, 2.95, angle=0)
    y = dz + 50 + 19
    w = 59.8
    non_plated_hole(kicad_mod, 50 - w / 2, y, 5.9)
    non_plated_hole(kicad_mod, 50 + w / 2, y, 5.9)
    multi_dot_line(kicad_mod, [(15, y), (85, y)], layers=glayers_silk, width=2)
    kicad_mod.append(km)
    return write_kicad_mod(kicad_mod)
def m3_hua(w100=100, de=2.5):
    kicad_mod = new_kicad_mod(m3_hua.__name__)
    dz = 6
    non_plated_hole(kicad_mod, 50, dz, 4.4)
    circle(kicad_mod, 50, dz, diameter=[1, 3, 5, 9, (100 - dz) * 2 * 1.137], crosshair=1, layers=glayers_silk)
    for i in range(3):
        if i == 1:
            continue
        else:
            x = 16.6665 + 33.333 * i
            non_plated_hole(kicad_mod, x, dz, 8.95)
    bj = [(0, dz + 50 - 4.8 - 17), (22.3, dz + 50 - 4.8 - 17), (22.3, dz + 50 - 4.8), (0, dz + 50 - 4.8), (0, dz + 50 - 4.8 - 17)]
    multi_dot_line(kicad_mod, bj, layers=glayers_silk, width=0.01)
    symmetric_x(kicad_mod, bj, xm=100, xmid=50, x0=0, y0=0, angle=0, layer=['Edge.Cuts', 'F.SilkS', 'Edge.Cuts', 'B.SilkS'], width=0.01)
    y = dz + 50
    multi_dot_line(kicad_mod, [(0, y), (100, y)], layers=glayers_silk, width=0.01)
    y = dz + 50 + 9
    non_plated_hole(kicad_mod, 50, y, 1)
    circle(kicad_mod, 50, y, diameter=[1, 2, 2.8, 4, 5, 6], crosshair=1, layers=glayers_silk)
    hole_square(kicad_mod, 50, y - 23.5, 47, 2.9, angle=0)
    hole_square(kicad_mod, 50, y - 23.5, 47, 3.9, angle=0, func=circle)
    circle(kicad_mod, 50, y - 23.5, diameter=[1, 3, 6.35, 156.6], crosshair=1, layers=glayers_silk)
    non_plated_hole(kicad_mod, 50, y - 23.5, d=1)
    y = dz + 50 + 19
    w = 59.8
    non_plated_hole(kicad_mod, 50 - w / 2, y, 6)
    non_plated_hole(kicad_mod, 50 + w / 2, y, 6)
    multi_dot_line(kicad_mod, [(15, y), (85, y)], layers=glayers_silk, width=2)
    y = dz + 50 + 19 + 20
    multi_dot_line(kicad_mod, [(44, y), (56, y)], layers=glayers_silk, width=0.5)
    for nx, x in enumerate(range(10, 100, 10)):
        for y in [60, 70, 80, 90]:
            if y == 60 and nx in [1, 2, 6, 7]:
                    continue
            if y == 70 and nx in [2, 3, 4, 5, 6]:
                    continue
            non_plated_hole(kicad_mod, x, y + 5, 1.95)
    return write_kicad_mod(kicad_mod)
def m345_42motor(w100=100, de=2.5):
    kicad_mod = new_kicad_mod(m345.__name__)
    circle(kicad_mod, 50, 50, diameter=[1, 141.4], crosshair=1, layers=glayers_silk)
    d = 0.8
    dnd = {0: 2.95, 1: 4.95, 2: 8.9, 3: 22.1}
    for n, (x, y) in enumerate(edge_distance(w100, w100, [25 - d, 25 - d])):
        hole_square(kicad_mod, x, y, 31, 2.95, angle=0)
        non_plated_hole(kicad_mod, x, y, dnd[n])
        multi_dot_line(kicad_mod, [(x, 0), (x, 100)], layers=glayers_silk, width=0.01)
        multi_dot_line(kicad_mod, [(0, y), (100, y)], layers=glayers_silk, width=0.01)
    multi_dot_line(kicad_mod, [(0 + de, 50), (100 - de, 50)], layers=glayers_silk, width=0.1)
    multi_dot_line(kicad_mod, [(50, 0 + de), (50, 100 - de)], layers=glayers_silk, width=0.1)
    for i in range(50):
        non_plated_hole(kicad_mod, i * 2, 50, 1)
        non_plated_hole(kicad_mod, 50, i * 2, 1)
    d = 0.2
    rectangle_outline(kicad_mod, 0 + d, 0 + d, w=100 - d * 2, h=100 - d * 2, width=0.1, layers=glayers_F_Cu)
    return write_kicad_mod(kicad_mod)
m345_hole = m345_42motor
def m3(w100=100, dx=12.3, dy2b=30, drill_screw=3.3):
    """ dy2b      两边的孔距离中心  """
    kicad_mod = new_kicad_mod(f'm3_{drill_screw}')
    ha = 17
    hr = 11.5
    hl = ha - hr
    ja = 22.3
    jbd = 25.9 - ja
    j1 = 10.5
    j2 = 16.5
    hy0 = 7.5
    for x, y in edge_distance(w100, w100, [j1 + 3, j1 + 3]):
        non_plated_hole(kicad_mod, x + 3, y - 3, drill_screw)
        non_plated_hole(kicad_mod, x - 3, y + 3, drill_screw)
    for x, y in [[j1, j2], [j2, j1]]:
        non_plated_hole(kicad_mod, x, 50 - j1 - 3 + y, drill_screw)
    for x, y in [[j1, j1], [j2, j2]]:
        non_plated_hole(kicad_mod, w100 - x, 50 - j1 - 3 + y, drill_screw)
    non_plated_hole(kicad_mod, 47, j1, drill_screw)
    non_plated_hole(kicad_mod, 53, j2, drill_screw)
    circle(kicad_mod, 53, j1 - 6, drill_screw)
    circle(kicad_mod, 53, j1 - 6, drill_screw)
    non_plated_hole(kicad_mod, 53, w100 - j1, drill_screw)
    non_plated_hole(kicad_mod, 47, w100 - j2, drill_screw)
    circle(kicad_mod, 53, j1 - 6, drill_screw)
    circle(kicad_mod, w100 - j2, j1 - 6, drill_screw)
    f6 = 16.666
    for i in range(1, 6):
        y = f6 * i
        multi_dot_line(kicad_mod, [(0, y), (w100, y)], layers=glayers_silk)
        multi_dot_line(kicad_mod, [(y, 0), (y, w100)], layers=glayers_silk)
    return write_kicad_mod(kicad_mod)
def gear_15_10_jz():
    kicad_mod = new_kicad_mod(gear_15_10_jz.__name__)
    xh = 42.4
    w57 = 56.5
    x0 = 100 - (xh + w57)
    multi_dot_line(kicad_mod, [(x0, 0), (x0, 100)], layers=glayers_silk)
    mx = x0 + xh
    multi_dot_line(kicad_mod, [(mx, 0), (mx, 100)], layers=glayers_silk)
    multi_dot_line(kicad_mod, [(x0, 10), (mx, 10)], layers=glayers_silk)
    mx = x0 + xh / 2
    multi_dot_line(kicad_mod, [(mx, 0), (mx, 100)], layers=glayers_silk)
    n = 4
    ni = 90 / n
    for i in range(1, n):
        circle(kicad_mod, mx, 100 - ni * i, [0.2, 2, 3, 4, 5, 6, 8])
        non_plated_hole(kicad_mod, mx, 100 - ni * i, 1.9)
    hz57 = 45.5
    multi_dot_line(kicad_mod, [(0, hz57), (100, hz57)], layers=glayers_silk)
    x57 = 100 - w57 / 2
    non_plated_hole(kicad_mod, x57, hz57, 6.35)
    hole_rect_center(kicad_mod, x57, hz57, 47, d=3.9, func=non_plated_hole, holes=[0, 1, 2, 3])
    rectline_center(kicad_mod, x57, hz57, w57, w57, layers=glayers_silk)
    hole_rect_center(kicad_mod, mx + 23.5, hz57, 47, d=1.9, func=non_plated_hole, holes=[2, 3])
    hole_rect_center(kicad_mod, mx + 23.5, hz57, 47, d=[0.2, 2, 3, 4, 5, 6, 8], func=circle, holes=[2, 3])
    non_plated_hole(kicad_mod, x0 + 2.9 + 1.6, 7.1, 5.85)
    non_plated_hole(kicad_mod, x0 + xh - 2.9 - 1.6, 7.1, 5.85)
    non_plated_hole(kicad_mod, mx, hz57, 1.9)
    non_plated_hole(kicad_mod, mx, hz57 + 47, 1.9)
    return write_kicad_mod(kicad_mod)
def gear_15_50():
    import math
    kicad_mod = new_kicad_mod(gear_15_50.__name__ + 'f', w=0, h=0)
    glayers_silk = glayers_silk
    kicad_mod.append(KicadModTree.RectLine(start=[0, 0], end=[100, 100], layer='F.SilkS'))
    ek = 30
    multi_dot_line(kicad_mod, [(0, 50 - ek), (0, 50 + ek)], layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(100, 50 - ek), (100, 50 + ek)], layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(50 - ek, 0), (50 + ek, 0)], layers=glayers_edge_pure)
    multi_dot_line(kicad_mod, [(50 - ek, 100), (50 + ek, 100)], layers=glayers_edge_pure)
    x0 = y0 = 50
    rd = 57.5
    for i in range(4):
        radian = math.radians(i * 90 + 29.5)
        x = x0 + rd * math.cos(radian)
        y = y0 + rd * math.sin(radian)
        arc(kicad_mod, center=[x0, y0], start=[x, y], angle=31, layers=['F.SilkS', 'Edge.Cuts'], width=0.01)
    non_plated_hole(kicad_mod, x0, y0, 7.8)
    circle(kicad_mod, x0, y0, diameter=[8.5, 9.8, 11, 12, 16, 18, 20, 24, 73, 74, 74.8, 76, 109, 115], crosshair=1, layers=glayers_silk)
    r = 11.9
    n = 6
    a = 360 / n
    for i in range(n):
        if i % 2 == 0:
            r = 11
        else:
            r = 14
        radian = math.radians(i * a + a / 4)
        x = x0 + r * math.cos(radian)
        y = y0 + r * math.sin(radian)
        radian = math.radians(i * a + a / 2)
        cx = x0 + r * math.cos(radian)
        cy = y0 + r * math.sin(radian)
        dk = 1.95
        if i in (4, 1):
            dk = 1.95
        if i in (2, 5):
            dk = 3
        if i in (0, 3):
            dk = 3.9
        non_plated_hole(kicad_mod, cx, cy, dk)
        circle(kicad_mod, cx, cy, diameter=[2.5, 3.1, 4], layers=glayers_silk)
    return write_kicad_mod(kicad_mod)