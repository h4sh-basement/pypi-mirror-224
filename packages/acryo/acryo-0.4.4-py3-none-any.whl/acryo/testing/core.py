from __future__ import annotations

import numpy as np

from acryo._typed_scipy import fftn, ifftn, affine_transform
from acryo.molecules import Molecules
from acryo._utils import compose_matrices
from acryo._rotation import normalize_rotations
from acryo._types import nm, degree


class TomogramGenerator:
    """
    A tester class for subtomogram averaging and alignment.

    Given a template image, this class can create tomogram by assembling
    rotated, noisy template images gridwise. Molecules objects can also
    be sampled with arbitrary positional errors.
    """

    def __init__(
        self,
        template: np.ndarray,
        grid_shape: tuple[int, int] = (10, 10),
        rotations=None,
        noise_sigma: float = 1,
        seed: int = 0,
    ) -> None:
        self._template = template
        self._grid_shape = grid_shape
        self._quaternions = normalize_rotations(rotations)
        self._noise_sigma = noise_sigma
        self._seed = seed

    @property
    def template(self):
        return self._template

    @property
    def grid_shape(self):
        return self._grid_shape

    @property
    def quaternions(self):
        return self._quaternions

    @property
    def noise_sigma(self):
        return self._noise_sigma

    def _get_matrices(self, rng: np.random.Generator):
        gy, gx = self.grid_shape
        quat_idx = rng.choice(self.quaternions.shape[0], size=(gy * gx))

        from scipy.spatial.transform import Rotation

        rotators = [Rotation.from_quat(self.quaternions[idx]) for idx in quat_idx]
        return compose_matrices(np.array(self.template.shape) / 2 - 0.5, rotators)

    def get_tomogram(
        self, pad_width: int = 0, tilt_range: tuple[degree, degree] = (-90, 90)
    ) -> np.ndarray:
        rng = np.random.default_rng(self._seed)
        template = self.template
        if pad_width > 0:
            template = np.pad(template, pad_width, dims="zyx")  # type: ignore

        gy, gx = self.grid_shape

        mols: list[list[np.ndarray]] = [
            [template.copy() for _ in range(gy)] for _ in range(gx)
        ]
        if self.quaternions.shape[0] > 0:
            matrices = self._get_matrices(rng)
            mtx_iterator = iter(matrices)
            for i, j in wrange(gy, gx):
                mtx = next(mtx_iterator)
                mols[i][j] = affine_transform(mols[i][j], mtx)

        for i, j in wrange(gy, gx):
            mols[i][j] += rng.normal(scale=self.noise_sigma, size=template.shape)

        if tilt_range != (-90, 90):
            mw = _missing_wedge_mask(template.shape, tilt_range=tilt_range)
            for i, j in wrange(gy, gx):
                ft = np.fft.fftshift(fftn(mols[i][j]))
                mols[i][j] = np.real(np.fft.ifftshift(ifftn(ft * mw)))

        tomogram: np.ndarray = np.block(mols)  # type: ignore
        return tomogram

    def sample_molecules(self, max_distance: nm = 3.0, scale: nm = 1.0):
        gy, gx = self.grid_shape
        shape_vec = np.array(self.template.shape)
        offset = (shape_vec - 1) / 2 * scale
        vy, vx = shape_vec[1:] * scale
        centers = []
        for i, j in wrange(gy, gx):
            centers.append(offset + np.array([0.0, vy * i, vx * j]))
        centers = np.stack(centers, axis=0)
        return Molecules(centers).translate_random(
            max_distance=max_distance, seed=self._seed
        )


def _missing_wedge_mask(
    shape: tuple[int, int, int], tilt_range: tuple[degree, degree]
) -> np.ndarray:
    """
    Create a missing-wedge binary mask image.

    Mask created by this function should be multiplied to Fourier transformed
    image.

    Parameters
    ----------
    shape : tuple of int
        Shape of the output array.
    tilt_range : tuple[float, float]
        Tomogram tilt range in degree.

    Returns
    -------
    np.ndarray
        A binary mask.
    """
    radmin, radmax = np.deg2rad(tilt_range)
    x0 = (shape[2] - 1) / 2
    z0 = (shape[0] - 1) / 2
    zz, yy, xx = np.indices(shape)
    d0 = zz - z0 - np.tan(radmin) * (xx - x0)
    d1 = zz - z0 - np.tan(radmax) * (xx - x0)
    missing = d0 * d1 < 0
    return missing


def wrange(l0: int, l1: int):
    for i in range(l0):
        for j in range(l1):
            yield i, j
