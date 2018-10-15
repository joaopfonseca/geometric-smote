"""
The :mod:`sklearnext.oversampling` module includes
 various oversampling methods.
"""

from .cgan_oversampler import CGANOversampler
from .geometric_smote import GeometricSMOTE
from ._oversamplers import RandomOverSampler, SMOTE, ADASYN
from .distribution import DensityDistributor

__all__ = [
    'RandomOverSampler',
    'SMOTE',
    'ADASYN',
    'CGANOversampler',
    'GeometricSMOTE',
    'DensityDistributor'
]