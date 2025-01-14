# -*- coding: utf-8 -*-
import json
import os
import warnings
from typing import List, Union

import h5py
import matplotlib.pyplot as plt
import numpy as np
from dspawpy.io.structure import read
from pymatgen.core import Structure
from scipy.ndimage import gaussian_filter1d


class MSD:
    # 用于实际计算均方位移的类，摘自pymatgen开源项目
    def __init__(
        self,
        structures: List[Structure],
        select: Union[str, List[int]] = "all",
        msd_type="xyz",
    ):
        self.structures = structures
        self.msd_type = msd_type

        self.n_frames = len(structures)
        self.lattice = structures[0].lattice

        self._parse_msd_type()

        if select == "all":
            self.n_particles = len(structures[0])
            self._position_array = np.zeros(
                (self.n_frames, self.n_particles, self.dim_fac)
            )
            for i, s in enumerate(self.structures):
                self._position_array[i, :, :] = s.frac_coords[:, self._dim]
        else:
            if isinstance(select, str):  # ':', '-3:', 'H' or even 'H1'
                if ":" in select:
                    exec(
                        f"self.n_particles = self.structures[0].frac_coords[{select}, :][:, self._dim].shape[0]"
                    )
                    self._position_array = np.zeros(
                        (self.n_frames, self.n_particles, self.dim_fac)
                    )
                    for i, s in enumerate(self.structures):
                        exec(
                            f"self._position_array[i, :, :] = s.frac_coords[{select}, :][:, self._dim]"
                        )
                else:
                    indices = [
                        j
                        for j, s in enumerate(self.structures[0])
                        if select == s.species_string
                    ]
                    assert (
                        indices != []
                    ), f"{select} did not match any element symbol, {self.structures[0].species}"
                    self.n_particles = (
                        self.structures[0]
                        .frac_coords[indices, :][:, self._dim]
                        .shape[0]
                    )
                    self._position_array = np.zeros(
                        (self.n_frames, self.n_particles, self.dim_fac)
                    )
                    for i, s in enumerate(self.structures):
                        self._position_array[i, :, :] = s.frac_coords[indices, :][
                            :, self._dim
                        ]
            else:
                if isinstance(select, int):  # 1
                    indices = [select]
                elif isinstance(select, list) or isinstance(
                    select, np.ndarray
                ):  # [1,2,3] or ['H','O']
                    # if all elements are int, then select by index
                    if all(isinstance(i, int) for i in select):
                        indices = select
                    # if all elements are str, then select by element
                    elif all(isinstance(i, str) for i in select):
                        indices = []
                        for sel in select:
                            indices += [
                                j
                                for j, s in enumerate(self.structures[0])
                                if sel == s.species_string
                            ]
                else:
                    raise ValueError(
                        f"select = {select} should be string, int, list or np.ndarray"
                    )
                # get shape of returned array
                self.n_particles = (
                    self.structures[0].frac_coords[indices, :][:, self._dim].shape[0]
                )
                self._position_array = np.zeros(
                    (self.n_frames, self.n_particles, self.dim_fac)
                )
                for i, s in enumerate(self.structures):
                    self._position_array[i, :, :] = s.frac_coords[indices, :][
                        :, self._dim
                    ]

    def _parse_msd_type(self):
        r"""Sets up the desired dimensionality of the MSD."""
        keys = {
            "x": [0],
            "y": [1],
            "z": [2],
            "xy": [0, 1],
            "xz": [0, 2],
            "yz": [1, 2],
            "xyz": [0, 1, 2],
        }

        self.msd_type = self.msd_type.lower()

        try:
            self._dim = keys[self.msd_type]
        except KeyError:
            raise ValueError(
                "invalid msd_type: {} specified, please specify one of xyz, "
                "xy, xz, yz, x, y, z".format(self.msd_type)
            )

        self.dim_fac = len(self._dim)

    def run(self):
        print("Calculating MSD...")
        result = np.zeros((self.n_frames, self.n_particles))

        rd = np.zeros((self.n_frames, self.n_particles, self.dim_fac))
        for i in range(1, self.n_frames):
            disp = self._position_array[i, :, :] - self._position_array[i - 1, :, :]
            # mic by periodic boundary condition
            disp[np.abs(disp) > 0.5] = disp[np.abs(disp) > 0.5] - np.sign(
                disp[np.abs(disp) > 0.5]
            )
            disp = np.dot(disp, self.lattice.matrix)
            rd[i, :, :] = disp
        rd = np.cumsum(rd, axis=0)
        for n in range(1, self.n_frames):
            disp = rd[n:, :, :] - rd[:-n, :, :]  # [n:-n] window
            sqdist = np.square(disp).sum(axis=-1)
            result[n, :] = sqdist.mean(axis=0)

        return result.mean(axis=1)


class RDF:
    # 用于快速计算径向分布函数的类
    # Copyright (c) Materials Virtual Lab.
    # Distributed under the terms of the BSD License.
    def __init__(
        self,
        structures: Union[Structure, List[Structure]],
        rmin: float = 0.0,
        rmax: float = 10.0,
        ngrid: float = 101,
        sigma: float = 0.0,
    ):
        """This method calculates rdf on `np.linspace(rmin, rmax, ngrid)` points

        Parameter
        ---------
        structures (list of pymatgen Structures): structures to compute RDF
        rmin (float): minimal radius
        rmax (float): maximal radius
        ngrid (int): number of grid points, defaults to 101
        sigma (float): smooth parameter
        """
        if isinstance(structures, Structure):
            structures = [structures]
        self.structures = structures
        # Number of atoms in all structures should be the same
        assert (
            len({len(i) for i in self.structures}) == 1
        ), "Different configurations have different numbers of atoms!"
        elements = [[i.specie for i in j.sites] for j in self.structures]
        unique_elements_on_sites = [len(set(i)) == 1 for i in list(zip(*elements))]

        # For the same site index, all structures should have the same element there
        if not all(unique_elements_on_sites):
            raise RuntimeError("Elements are not the same at least for one site")

        self.rmin = rmin
        self.rmax = rmax
        self.ngrid = ngrid

        self.dr = (self.rmax - self.rmin) / (self.ngrid - 1)  # end points are on grid
        self.r = np.linspace(self.rmin, self.rmax, self.ngrid)  # type: ignore
        self.shell_volumes = 4.0 * np.pi * self.r**2 * self.dr
        self.shell_volumes[self.shell_volumes < 1e-8] = 1e8  # avoid divide by zero

        self.n_structures = len(self.structures)
        self.sigma = np.ceil(sigma / self.dr)

    def _dist_to_counts(self, d):
        """Convert a distance array for counts in the bin

        Parameter
        ---------
            d: (1D np.array)

        Returns:
            1D array of counts in the bins centered on self.r
        """
        counts = np.zeros((self.ngrid,))
        indices = np.array(
            np.floor((d - self.rmin + 0.5 * self.dr) / self.dr), dtype=int
        )  # 将找到配对的距离转换为格点序号 (向下取整)
        unique, val_counts = np.unique(indices, return_counts=True)
        counts[unique] = val_counts
        return counts

    def get_rdf(
        self,
        ref_species: Union[str, List[str]],
        species: Union[str, List[str]],
        is_average=True,
    ):
        """Wrapper to get the rdf for a given species pair

        Parameter
        ---------
        ref_species (list of species or just single specie str):
            The reference species. The rdfs are calculated with these species at the center
        species (list of species or just single specie str):
            the species that we are interested in. The rdfs are calculated on these species.
        is_average (bool):
            whether to take the average over all structures

        Returns
        -------
        (x, rdf)
            x is the radial points, and rdf is the rdf value.
        """
        print("Calculating RDF...")
        if isinstance(ref_species, str):
            ref_species = [ref_species]

        if isinstance(species, str):
            species = [species]
        ref_species_index = []
        species_index = []
        for i in range(len(self.structures[0].species)):
            ele = str(self.structures[0].species[i])
            if ele in ref_species:
                ref_species_index.append(i)
            if (
                ele in species
            ):  # @syyl use if instead of elif in case of `species = ref_species`
                species_index.append(i)
        all_rdfs = [
            self.get_one_rdf(ref_species_index, species_index, i)[1]
            for i in range(self.n_structures)
        ]
        if is_average:
            all_rdfs = np.mean(all_rdfs, axis=0)
        return self.r, all_rdfs

    def get_one_rdf(
        self,
        ref_species_index: Union[str, List[str]],
        species_index: Union[str, List[str]],
        index=0,
    ):
        """Get the RDF for one structure, indicated by the index of the structure
        in all structures"""
        lattice = self.structures[index].lattice
        distances = []
        refsp_frac_coord = self.structures[index].frac_coords[ref_species_index]
        sp_frac_coord = self.structures[index].frac_coords[species_index]
        d = lattice.get_all_distances(refsp_frac_coord, sp_frac_coord)
        indices = (
            (d >= self.rmin - self.dr / 2.0)
            & (d <= self.rmax + self.dr / 2.0)
            & (d > 1e-8)
        )
        distances = d[indices]
        counts = self._dist_to_counts(np.array(distances))  # 统计该距离内目标元素的原子数，列表

        npairs = len(distances)
        rdf_temp = counts / npairs / self.shell_volumes / self.structures[index].volume

        if self.sigma > 1e-8:
            rdf_temp = gaussian_filter1d(rdf_temp, self.sigma)
        return self.r, rdf_temp, npairs

    def get_coordination_number(self, ref_species, species, is_average=True):
        """returns running coordination number

        Parameter
        ---------
        ref_species (list of species or just single specie str):
            the reference species. The rdfs are calculated with these species at the center
        species (list of species or just single specie str):
            the species that we are interested in. The rdfs are calculated on these species.
        is_average (bool): whether to take structural average

        Returns
        --------
        numpy array
        """
        print("Calculating coordination number...")
        # Note: The average density from all input structures is used here.
        all_rdf = self.get_rdf(ref_species, species, is_average=False)[1]
        if isinstance(species, str):
            species = [species]
        density = [sum(i[j] for j in species) for i in self.density]
        cn = [
            np.cumsum(rdf * density[i] * 4.0 * np.pi * self.r**2 * self.dr)
            for i, rdf in enumerate(all_rdf)
        ]
        if is_average:
            cn = np.mean(cn, axis=0)
        return self.r, cn


class RMSD:
    # 用于计算均方根偏差（Root Mean Square Deviation）的类，摘自pymatgen开源项目
    def __init__(self, structures: List[Structure]):
        self.structures = structures

        self.n_frames = len(self.structures)
        self.n_particles = len(self.structures[0])
        self.lattice = self.structures[0].lattice

        self._position_array = np.zeros((self.n_frames, self.n_particles, 3))

        for i, s in enumerate(self.structures):
            self._position_array[i, :, :] = s.frac_coords

    def run(self, base_index=0):
        print("Calculating RMSD...")
        result = np.zeros(self.n_frames)
        rd = np.zeros((self.n_frames, self.n_particles, 3))
        for i in range(1, self.n_frames):
            disp = self._position_array[i, :, :] - self._position_array[i - 1, :, :]
            # mic by periodic boundary condition
            disp[np.abs(disp) > 0.5] = disp[np.abs(disp) > 0.5] - np.sign(
                disp[np.abs(disp) > 0.5]
            )
            disp = np.dot(disp, self.lattice.matrix)
            rd[i, :, :] = disp
        rd = np.cumsum(rd, axis=0)

        for i in range(self.n_frames):
            sqdist = np.square(rd[i] - rd[base_index]).sum(axis=-1)
            result[i] = sqdist.mean()

        return np.sqrt(result)


def get_lagtime_msd(
    datafile: Union[str, List[str]],
    select: Union[str, List[int]] = "all",
    msd_type: str = "xyz",
    timestep: float = None,
):
    r"""计算不同时间步长下的均方位移

    Parameters
    ----------
    datafile : str or list of str
        - aimd.h5/aimd.json文件路径或包含这些文件的文件夹路径（优先寻找aimd.h5）
        - 写成列表将依次读取数据并合并到一起
        - 例如['aimd1.h5', 'aimd2.h5', '/data/home/my_aimd_task']
    select : str or list of int
        选择原子序号或元素，原子序号从0开始；默认为'all'，计算所有原子
    msd_type : str
        计算MSD的类型，可选xyz,xy,xz,yz,x,y,z，默认为'xyz'，即计算所有分量
    timestep : float
        相邻结构的时间间隔，单位为fs，默认None，将从datafile中读取，失败则设为1.0fs；
        若不为None，则将使用该值计算时间序列

    Returns
    -------
    lagtime : np.ndarray
        时间序列
    result : np.ndarray
        均方位移序列

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_lagtime_msd
    >>> lagtime, msd = get_lagtime_msd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5')
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...
    >>> lagtime
    array([0.000e+00, 1.000e+00, 2.000e+00, ..., 1.997e+03, 1.998e+03,
           1.999e+03])
    >>> msd
    array([0.00000000e+00, 8.80447550e-02, 1.83768134e-01, ...,
           9.66185452e+02, 9.66812755e+02, 9.67357702e+02])
    >>> lagtime, msd = get_lagtime_msd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', select='H')
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...
    >>> lagtime, msd = get_lagtime_msd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', select=[0,1])
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...
    >>> lagtime, msd = get_lagtime_msd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', select=['H','O'])
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...
    >>> lagtime, msd = get_lagtime_msd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', select=0)
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...
    """
    strs = read(datafile, task="aimd")
    if timestep is None:
        if isinstance(datafile, str) or len(datafile) == 1:
            ts = _get_time_step(datafile)
        else:
            warnings.warn(
                "For multiple datafiles, you must manually specify the timestep. It will default to 1.0fs."
            )
            ts = 1.0
    else:
        ts = timestep

    msd = MSD(strs, select, msd_type)
    result = msd.run()

    nframes = msd.n_frames
    lagtime = np.arange(nframes) * ts  # make the lag-time axis

    return lagtime, result


def get_lagtime_rmsd(datafile: Union[str, List[str]], timestep: float = None):
    r"""

    Parameters
    ----------
    datafile : str or list of str
        - aimd.h5/aimd.json文件路径或包含这些文件的文件夹路径（优先寻找aimd.h5）
        - 写成列表将依次读取数据并合并到一起
        - 例如['aimd1.h5', 'aimd2.h5', '/data/home/my_aimd_task']
    timestep : float
        相邻结构的时间间隔，单位为fs，默认None，将从datafile中读取，失败则设为1.0fs；
        若不为None，则将使用该值计算时间序列

    Returns
    -------
    lagtime : numpy.ndarray
        时间序列
    rmsd : numpy.ndarray
        均方根偏差序列

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_lagtime_rmsd
    >>> lagtime, rmsd = get_lagtime_rmsd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', timestep=0.1)
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating RMSD...
    >>> lagtime
    array([0.000e+00, 1.000e-01, 2.000e-01, ..., 1.997e+02, 1.998e+02,
           1.999e+02])
    >>> rmsd
    array([ 0.        ,  0.04849931,  0.09181907, ..., 31.09991413,
           31.10077061, 31.10237454])
    """
    strs = read(datafile, task="aimd")
    if timestep is None:
        if isinstance(datafile, str) or len(datafile) == 1:
            ts = _get_time_step(datafile)
        else:
            warnings.warn(
                "For multiple datafiles, you must manually specify the timestep. It will default to 1.0fs."
            )
            ts = 1.0
    else:
        ts = timestep

    rmsd = RMSD(structures=strs)
    result = rmsd.run()

    # Plot
    nframes = rmsd.n_frames
    lagtime = np.arange(nframes) * ts  # make the lag-time axis

    return lagtime, result


def get_rs_rdfs(
    datafile: Union[str, List[str]],
    ele1: str,
    ele2: str,
    rmin: float = 0,
    rmax: float = 10,
    ngrid: float = 101,
    sigma: float = 0,
):
    r"""计算rdf分布函数

    Parameters
    ----------
    datafile : str or list of str
        - aimd.h5/aimd.json文件路径或包含这些文件的文件夹路径（优先寻找aimd.h5）
        - 写成列表将依次读取数据并合并到一起
        - 例如['aimd1.h5', 'aimd2.h5', '/data/home/my_aimd_task']
    ele1 : list
        中心元素
    ele2 : list
        相邻元素
    rmin : float
        径向分布最小值，默认为0
    rmax : float
        径向分布最大值，默认为10
    ngrid : int
        径向分布网格数，默认为101
    sigma : float
        平滑参数

    Returns
    -------
    r : numpy.ndarray
        径向分布网格点
    rdf : numpy.ndarray
        径向分布函数

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_rs_rdfs
    >>> rs, rdfs = get_rs_rdfs(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5',ele1='H',ele2='O')
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating RDF...
    >>> rdfs
    array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           6.90409153e-05, 7.47498606e-04, 2.40555636e-03, 2.57666881e-03,
           2.53257125e-03, 2.37964722e-03, 1.80028135e-03, 1.20224160e-03,
           7.57927477e-04, 3.41004760e-04, 2.85680407e-04, 1.72795412e-04,
           1.49718401e-04, 1.44477999e-04, 2.23702566e-04, 2.11836218e-04,
           1.34146448e-04, 1.78839343e-04, 9.16910363e-05, 1.45492991e-05,
           3.70494493e-05, 3.72784113e-05, 2.82725837e-05, 3.19750004e-05,
           8.46456322e-07, 4.72401470e-06, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
           0.00000000e+00])
    """
    strs = read(datafile, task="aimd")

    # 计算rdf并绘制主要曲线
    obj = RDF(structures=strs, rmin=rmin, rmax=rmax, ngrid=ngrid, sigma=sigma)

    rs, rdfs = obj.get_rdf(ele1, ele2)
    return rs, rdfs


def plot_msd(
    lagtime: np.ndarray,
    result: np.ndarray,
    xlim: List[float] = None,
    ylim: List[float] = None,
    figname: str = None,
    show: bool = True,
    ax=None,
    **kwargs,
):
    r"""AIMD任务完成后，计算均方位移（MSD）

    Parameters
    ----------
    lagtime : np.ndarray
        时间序列
    result : np.ndarray
        均方位移序列
    xlim : list of float
        x轴的范围，默认为None，自动设置
    ylim : list of float
        y轴的范围，默认为None，自动设置
    figname : str
        图片名称，默认为None，不保存图片
    show : bool
        是否显示图片，默认为True
    ax: matplotlib axes object
        用于将图片绘制到matplotlib的子图上
    **kwargs : dict
        其他参数，如线条宽度、颜色等，传递给plt.plot函数

    Returns
    -------
    MSD分析后的图片

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_lagtime_msd, plot_msd

    指定h5文件位置，用 get_lagtime_msd 函数获取数据，select 参数选择第n个原子（不是元素）

    >>> lagtime, msd = get_lagtime_msd('/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', select=[0])
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating MSD...

    用获取的数据画图并保存

    >>> plot_msd(lagtime, msd, figname='/data/home/hzw1002/dspawpy_repo/test/out/MSD.png', show=False)
    ==> /data/home/hzw1002/dspawpy_repo/test/out/MSD.png
    <Axes: xlabel='Time (fs)', ylabel='MSD ($Å^2$)'>
    """
    if ax:
        ishow = False
        ax.plot(lagtime, result, c="black", ls="-", **kwargs)
    else:
        ishow = True
        fig, ax = plt.subplots()
        ax.plot(lagtime, result, c="black", ls="-", **kwargs)
        ax.set_xlabel("Time (fs)")
        ax.set_ylabel(r"MSD ($Å^2$)")

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    plt.tight_layout()
    if figname:
        absfig = os.path.abspath(figname)
        os.makedirs(os.path.dirname(absfig), exist_ok=True)
        plt.savefig(absfig, dpi=300)
        print(f"==> {absfig}")
    if show and ishow:  # 画子图的话，不应每个子图都show
        plt.show()  # show会自动清空图片

    return ax


def plot_rdf(
    rs: np.ndarray,
    rdfs: np.ndarray,
    ele1: str,
    ele2: str,
    xlim: list = None,
    ylim: list = None,
    figname: str = None,
    show: bool = True,
    ax: plt.Axes = None,
    **kwargs,
):
    r"""AIMD计算后分析rdf并画图

    Parameters
    ----------
    rs : numpy.ndarray
        径向分布网格点
    rdfs : numpy.ndarray
        径向分布函数
    ele1 : list
        中心元素
    ele2 : list
        相邻元素
    xlim : list
        x轴范围，默认为None，即自动设置
    ylim : list
        y轴范围，默认为None，即自动设置
    figname : str
        图片名称，默认为None，即不保存图片
    show : bool
        是否显示图片，默认为True
    ax: matplotlib.axes.Axes
        画图的坐标轴，默认为None，即新建坐标轴
    **kwargs : dict
        其他参数，如线条宽度、颜色等，传递给plt.plot函数

    Returns
    -------
    rdf分析后的图片

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_rs_rdfs, plot_rdf

    先获取rs和rdfs数据作为xy轴数据

    >>> rs, rdfs = get_rs_rdfs('/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', 'H', 'O', rmax=6)
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating RDF...

    将xy轴数据传入plot_rdf函数绘图

    >>> plot_rdf(rs, rdfs, 'H','O', figname='/data/home/hzw1002/dspawpy_repo/test/out/RDF.png', show=False)
    ==> /data/home/hzw1002/dspawpy_repo/test/out/RDF.png
    """

    if ax:
        ishow = False
        ax.plot(
            rs,
            rdfs,
            label=r"$g_{\alpha\beta}(r)$" + f"[{ele1},{ele2}]",
            **kwargs,
        )

    else:
        ishow = True
        fig, ax = plt.subplots()
        ax.plot(
            rs,
            rdfs,
            label=r"$g_{\alpha\beta}(r)$" + f"[{ele1},{ele2}]",
            **kwargs,
        )

        ax.set_xlabel(r"$r$" + "(Å)")
        ax.set_ylabel(r"$g(r)$")

    ax.legend()

    # 绘图细节
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    plt.tight_layout()
    if figname:
        absfig = os.path.abspath(figname)
        os.makedirs(os.path.dirname(absfig), exist_ok=True)
        plt.savefig(absfig, dpi=300)
        print(f"==> {absfig}")
    if show and ishow:  # 画子图的话，不应每个子图都show
        plt.show()  # show会自动清空图片


def plot_rmsd(
    lagtime: np.ndarray,
    result: np.ndarray,
    xlim: list = None,
    ylim: list = None,
    figname: str = None,
    show: bool = True,
    ax=None,
    **kwargs,
):
    r"""AIMD计算后分析rmsd并画图

    Parameters
    ----------
    lagtime:
        时间序列
    result:
        均方根偏差序列
    xlim : list
        x轴范围
    ylim : list
        y轴范围
    figname : str
        图片保存路径
    show : bool
        是否显示图片
    ax : matplotlib.axes._subplots.AxesSubplot
        画子图的话，传入子图对象
    **kwargs : dict
        传入plt.plot的参数

    Returns
    -------
    rmsd分析结构的图片

    Examples
    --------
    >>> from dspawpy.analysis.aimdtools import get_lagtime_rmsd, plot_rmsd

    timestep 表示时间步长

    >>> lagtime, rmsd = get_lagtime_rmsd(datafile='/data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5', timestep=0.1)
    Reading /data/home/hzw1002/dspawpy_repo/test/2.18/aimd.h5...
    Calculating RMSD...

    直接保存为RMSD.png图片

    >>> plot_rmsd(lagtime, rmsd, figname='/data/home/hzw1002/dspawpy_repo/test/out/RMSD.png', show=False)
    ==> /data/home/hzw1002/dspawpy_repo/test/out/RMSD.png
    <Axes: xlabel='Time (fs)', ylabel='RMSD (Å)'>
    """
    # 参数初始化
    if not ax:
        ishow = True
    else:
        ishow = False

    if ax:
        ax.plot(lagtime, result, **kwargs)
    else:
        fig, ax = plt.subplots()
        ax.plot(lagtime, result, **kwargs)
        ax.set_xlabel("Time (fs)")
        ax.set_ylabel("RMSD (Å)")

    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    plt.tight_layout()
    if figname:
        absfig = os.path.abspath(figname)
        os.makedirs(os.path.dirname(absfig), exist_ok=True)
        plt.savefig(absfig, dpi=300)
        print(f"==> {absfig}")
    if show and ishow:  # 画子图的话，不应每个子图都show
        plt.show()  # show会自动清空图片

    return ax


def _get_time_step(datafile):
    absfile = os.path.abspath(datafile)
    if absfile.endswith(".h5"):
        hpath = os.path.abspath(absfile)
        hf = h5py.File(hpath)
        try:
            t = np.array(hf["/Structures/TimeStep"])[0]
            timestep = float(t)
        except Exception:
            print(str(Exception))
            timestep = 1.0
    elif absfile.endswith(".json"):
        jpath = os.path.abspath(absfile)
        with open(jpath, "r") as f:
            jdata = json.load(f)
        try:
            t = jdata["Structures"][0]["TimeStep"]
            timestep = float(t)
        except Exception:
            print(str(Exception))
            timestep = 1.0
    else:
        raise ValueError(f"{absfile} must be .h5 or .json")

    return timestep
