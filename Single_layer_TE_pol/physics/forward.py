import numpy as np
from .tmm import tmm_reflection
from .one_slay_analytic import r_total as r_one_layer

def forward_model(params, theta, n_layers=1):
    """
    params: [k0, k1, ..., k_{n+1}, h1, h2, ..., hn]
    return: [r(theta1), r(theta2), ...]
    """
    if n_layers == 1:
        k_values = params[:3]
        h = params[3]
        r = r_one_layer(k_val=k_values, h=h, theta=theta)
        return r
    else:
        k_values = params[:n_layers+2]
        h_layers = params[n_layers+2:]
        r = tmm_reflection(k_values=k_values, h_layers=h_layers, incident_angle=theta)
        return r