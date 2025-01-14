# flake8: noqa

from enum import auto

from boilerdata.models.enums import GetNameEnum


class AxesEnum(GetNameEnum):
    trial = auto()
    run = auto()
    time = auto()
    group = auto()
    rod = auto()
    coupon = auto()
    sample = auto()
    joint = auto()
    good = auto()
    new = auto()
    V = auto()
    I = auto()
    T_0 = auto()
    T_1 = auto()
    T_1_err = auto()
    T_2 = auto()
    T_2_err = auto()
    T_3 = auto()
    T_3_err = auto()
    T_4 = auto()
    T_4_err = auto()
    T_5 = auto()
    T_5_err = auto()
    T_w1 = auto()
    T_w2 = auto()
    T_w3 = auto()
    P = auto()
    T_w = auto()
    T_w_diff = auto()
    T_s = auto()
    T_s_err = auto()
    q_s = auto()
    q_s_err = auto()
    k = auto()
    k_err = auto()
    h_w = auto()
    h_w_err = auto()
    h_a = auto()
    h_a_err = auto()
    DT = auto()
    DT_err = auto()
