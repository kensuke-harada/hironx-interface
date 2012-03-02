# -*- coding:utf-8 -*-
import sys
if sys.platform[0:4] == 'java':
    import patch_jython
from math import fabs, sin, cos, acos, sqrt, pi

# 回転行列 rot から、角速度ベクトルω（ロール・ピッチ・ヨー）を求める。(単位はラジアン)
# rot は 3x3 の実数配列だが、3x4でもそのまま実行できる（位置は無視する）
def omegaFromRot(rot):
    alpha = (rot[0][0] + rot[1][1] + rot[2][2] - 1.0)/2.0
    if fabs(alpha - 1.0) < 1.0e-6:
        return [0.0, 0.0, 0.0]
    else:
        th = acos(alpha)
        s = sin(th)
    
        if s < sys.float_info.epsilon:
            return [ sqrt( (rot[0][0]+1)*0.5 ) * th,
                     sqrt( (rot[1][1]+1)*0.5 ) * th,
                     sqrt( (rot[2][2]+1)*0.5 ) * th ]
        k = -0.5 * th / s
        return [ (rot[1][2] - rot[2][1]) * k,
                 (rot[2][0] - rot[0][2]) * k,
                 (rot[0][1] - rot[1][0]) * k,
                ]

# ロール・ピッチ・ヨーから、回転行列 rot を求める。(単位はラジアン)
# rot は [3][4]で、各列の４つめの要素は0。
def rotFromRpy(r, p, y):
    cr = cos(r)
    sr = sin(r)
    cp = cos(p)
    sp = sin(p)
    cy = cos(y)
    sy = sin(y)
    
    return [
            [cp*cy, sr*sp*cy - cr*sy, cr*sp*cy + sr*sy, 0],
            [cp*sy, sr*sp*sy + cr*cy, cr*sp*sy - sr*cy, 0],
            [-sp  , sr*cp           , cr*cp           , 0]
            ]

# ラジアン値から角度を求める。
# リストを受け取った場合、リストのラジアン値に対応する角度値のリストを返す。    
def degFromRad(rad):
    if isinstance(rad, list):
        return map(lambda v: degFromRad(v), rad)
    else:
        return (rad/(2*pi))*360

# 角度からラジアンを求める。
# リストを受け取った場合、角度のリストに対応するラジアンのリストを返す。    
def radFromDeg(deg):
    if isinstance(deg, list):
        return map(lambda v: radFromDeg(v), deg)
    else:
        return 2*pi*(float(deg)/360)
