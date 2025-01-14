from __future__ import annotations
from typing import Union
import torch
from torch import Tensor
from .score_model import ScoreModel, EnergyModel

def denoising_score_matching(score_model: Union[ScoreModel, EnergyModel], samples: Tensor):
    B, *D = samples.shape
    sde = score_model.sde
    z = torch.randn_like(samples)
    t = torch.rand(B).to(score_model.device) * (sde.T - sde.epsilon) + sde.epsilon
    mean, sigma = sde.marginal_prob(t, samples)
    return torch.sum((z + sigma * score_model(t, mean + sigma * z)) ** 2) / B

