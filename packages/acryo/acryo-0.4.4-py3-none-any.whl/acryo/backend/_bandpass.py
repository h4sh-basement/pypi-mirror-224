from __future__ import annotations
from functools import lru_cache, reduce
from typing import TYPE_CHECKING
import numpy as np

if TYPE_CHECKING:
    from ._api import Backend, AnyArray

# Backend-independent implementation of low-pass/high-pass filters.


def lowpass_filter_ft(
    backend: Backend,
    img: AnyArray[np.float32],
    cutoff: float,
    order: int = 2,
):
    """Apply a low-pass filter and return the result in Fourier space."""
    if cutoff >= 0.5 * np.sqrt(img.ndim) or cutoff <= 0:
        return backend.fftn(img)
    weight = nd_butterworth_weight(
        img.shape,
        cutoff,
        order,
        real=False,
        backend=backend,
    )
    return weight * backend.fftn(img)


def lowpass_filter(
    backend: Backend,
    img: AnyArray[np.float32],
    cutoff: float,
    order: int = 2,
):
    """Apply a low-pass filter and return the result in real space."""
    if cutoff >= 0.5 * np.sqrt(img.ndim) or cutoff <= 0:
        return img
    weight = nd_butterworth_weight(
        img.shape,
        cutoff,
        order,
        real=True,
        backend=backend,
    )
    out = backend.irfftn(weight * backend.rfftn(img))
    return out.real


def highpass_filter_ft(
    backend: Backend,
    img: AnyArray[np.float32],
    cutoff: float,
    order: int = 2,
):
    """Apply a high-pass filter and return the result in Fourier space."""
    if cutoff >= 0.5 * np.sqrt(img.ndim) or cutoff <= 0:
        return backend.zeros(img.shape, img.dtype)
    weight = 1 - nd_butterworth_weight(
        img.shape,
        cutoff,
        order,
        real=False,
    )
    return weight * backend.fftn(img)


def highpass_filter(
    backend: Backend,
    img: AnyArray[np.float32],
    cutoff: float,
    order: int = 2,
):
    """Apply a high-pass filter and return the result in real space."""
    if cutoff >= 0.5 * np.sqrt(img.ndim) or cutoff <= 0:
        return backend.zeros(img.shape, img.dtype)
    weight = 1 - nd_butterworth_weight(
        img.shape,
        cutoff,
        order,
        real=True,
    )
    out = backend.irfftn(weight * backend.rfftn(img))
    return out.real


# Modified from skimage.filters._fft_based
@lru_cache(maxsize=4)
def nd_butterworth_weight(
    shape: tuple[int, ...],
    cutoff: float,
    order: int,
    real: bool,
    backend: Backend,
) -> AnyArray[np.complex64]:
    ranges = []
    for d in shape:
        axis = backend.arange(
            -(d - 1) // 2, (d - 1) // 2 + 1, dtype=np.float32
        ) / (d * cutoff)
        ranges.append(backend.ifftshift(axis**2))
    if real:
        limit = shape[-1] // 2 + 1
        ranges[-1] = ranges[-1][:limit]
    q2 = reduce(backend._xp_.add, backend.meshgrid(*ranges, indexing="ij", sparse=True))
    wfilt = 1 / (1 + q2**order)
    return wfilt
