![Pyversion](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fgeojson-rewind%2Fjson)
![PyPI](https://img.shields.io/pypi/v/dspawpy?label=pypi%20package)
![PyPI - Downloads](https://static.pepy.tech/badge/dspawpy/month)

# Introduction （简介）

dspawpy is a post-processing tool mainly for DFT package [DS-PAW](https://cloud.hzwtech.com/web/product-service?id=10), which provides some functions of data capture, conversion, structure conversion, and drawing. （dspawpy 主要是 [DS-PAW](https://cloud.hzwtech.com/web/product-service?id=10) 软件的后处理辅助工具，提供一些数据抓取、换算、结构转化、绘图功能）

## Installation （安装）

```bash
pip install dspawpy -U --user
```

## CHANGELOG （版本更新简述）

### 1.0.7

- BUG修复： 准备弃用的 build_Structures_from_datafile() 未返回结构，read() 不受影响；其他调用 build_Structures_from_datafile() 的函数改为调用 read

### 1.0.6

- BUG修复： 修复 io.read.get_band_data() 考虑自旋且设置了zero_to_efermi时，自旋向下能带数据解析错误的问题
- 功能强化： io.structure模块新增 read() 代替 build_Structures_from_datafile()，write() 代替 io.write.to_file()，convert() 封装 read() 和 write() 函数，便于快速调用

### 1.0.5

- 功能强化： to_file() 写pdb文件时，结构可以不含晶胞信息

### 1.0.4

- BUG修复： build_Structures_from_datafile()选择原子序号时上限设置，h5文件里最后一个离子步信息改成尝试读取
- 功能强化： build_Structures_from_datafile()支持读取pdb格式
- 细节修改： AIMD读不到PressureKinetic信息时增加相应警告

### 1.0.3

- BUG修复： 解决浮点数过大时volumetricData相关文件浮点数粘在一起的问题
- BUG修复： plot_barrier()读取neb.h5/json绘制能垒图时，反应坐标依旧累加
- BUG修复： plot_bandunfolding()能带反折叠费米能级被默认置零
- 功能强化： 新增cube格式用于保存volumetricData
- 功能强化： 全局支持相对路径与绝对路径混写
- 功能强化： datafile参数以及io.read以及diffusion.nebtools模块中的相应参数，可以是文件位置，也可以是文件所在的文件夹路径
- 功能强化： build_Structures_from_datafile()增加task参数，用于配合datafile为文件夹路径的情况
- 重要变更： 移除中文提示语句，精简提示信息
- 重要变更： volumetricData默认使用cube格式写入
- 重要变更： 移除thermo_correction()，一个单纯的外包装函数
- 细节修改： 保存图片或文件时，统一使用 ==> 标记文件绝对路径

### 1.0.2

- BUG修复：  当存在Fix或Mag信息时，structure.as 坐标类型可能解析错误的问题
- 功能强化： 预览NEB链条函数改名 write_xyz(json)_chain，增加dst参数制定保存路径
- 功能强化： potential 中数据集不预作限制
- 功能强化： get_lagtime_msd, get_lagtime_rmsd 自动从数据文件中读取timestep（以前必须手动指定）
- 细节修改： 优化部分提示语句

### 1.0.1

- BUG修复： to_file绑定filename参数，避免老版本pymatgen的兼容性问题
- BUG修复： average_along_axis的task参数改成大小写敏感，避免rhoBound任务类型解析错误
- 功能强化： 将文件存入不存在的目录前，先创建（支持相对路径）
- 功能强化： write_VESTA和average_along_axis增加subtype参数，指定TotalLocalPotential数据

### 1.0.0

- BUG修复： 文件开头增加utf8编码声明
- 功能强化： 电荷密度差分支持更多组分（不限二元）
- 重要变更： io.utils的getZPE、getTSads、getTSgas函数，增加参数用于将计算结果存入文件
- 重要变更： io.write.write_VESTA() data_type参数可选值从boundcharge改成rhoBound，且大小写敏感，从而保持与DS-PAW输出文件名相同

### 0.9.9

- BUG修复： 修复新版numpy不支持混用array和list生成数组的问题
- BUG修复： 修复从json文件读能带时zero_to_efermi不生效的问题
- 新增功能： build_Structures_from_datafile模块支持读取 neb.h5 和 phonon.h5 文件
- 重要变更： 移除io模块中冗余的 _json.py （相关功能已整合进其他模块中并有所加强）
- 重要变更： 删除 setup.py 中不需要的 joblib 依赖库

### 0.9.8

- BUG修复： to_file 和 build_Structures_from_datafile 接口统一
- BUG修复： io.write模块涉及的保存文件操作，当目标路径上层文件夹不存在时将自动创建
- BUG修复： io.read.get_band_data的zero_to_efermi参数设置为True时，数据的处理逻辑
- BUG修复： io.read.get_sinfo读取relax.json不再因FixLattice而报错
- 新增选项： nebtools的summary函数，新增show_converge用于控制是否显示收敛图，outdir用于指定收敛图的路径
- 新增功能： 写文件涉及的操作，支持传入路径，而不单是文件名
- 新增功能： nebtools的restart函数支持在Windows机器上操作，不必在旧NEB路径执行，备份路径可随意指定
- 新增功能： nebtools的get_neb_subfolder函数新增return_abs参数，用于返回子文件夹的绝对路径
- 重要变更： nebtools的restart函数删除inputin参数，采用压缩较快的zip方法，将生成zip压缩包而不是tar.xz
- 重要变更： io.read.get_band_data的zero_to_fermi参数改名zero_to_efermi

### 0.9.7

- BUG修复： get_rdf 元素对自己计算RDF时的索引
- 新增选项：to_file 增加 si 参数，支持读入单个structure以及Structure列表

### 0.9.6

- BUG修复： pymatgen支持的几类结构文件的读取接口

### 0.9.5

- 重要变更： get_band_data 的 shift_efermi 参数改名为 zero_to_fermi

### 0.9.4

- 新增功能： get_band_data 增加 shift_efermi 参数
- BUG修复： 电荷密度差分函数移除 numpy 多维数组的 shape 参数
- BUG修复： Fe_1 -> Fe+, Fe_2 -> Fe2+ 用于能带、态密度绘图

### 0.9.3

- 新增功能： 接入pymatgen支持的几类结构文件的读写操作
- 新增功能： 支持通过 `dspawpy.__version__` 查看版本号
- 重要变更： write_xyz_traj, write_dump_traj 并入 to_file 函数
- 细节优化： 大幅提高RDF计算效率

### 0.9.2

- 新增功能： 支持从as文件中解析磁矩和FIX信息
- 新增功能： 从h5/json文件中读取数据时支持指定读取的离子步（从1开始）

### 0.9.1

- 重要变更： 精简合并多个函数，统一调用方法
- 新增功能： 支持合并多个xyz和dump文件
- 细节优化： 读取h5或json文件后若无错误，不再打印空行
- 细节优化： 耗时的RDF计算显示进度百分比

### 0.9.0

- 重要变更： 一些函数合并、所在模块迁移，请确认版本
- 新增功能： 支持读取含多离子步计算结果的h5/json文件中的磁矩信息
- BUG修复： get_band_data 函数指定efermi不生效

### 0.8.9

- BUG修复： d_band 脚本运行错误

### 0.8.8

- 新增功能： 支持读取正在进行中的NEB信息，生成movie轨迹文件（可用DS打开观察）
- 新增功能： 支持NEB转XYZ轨迹文件（可用OVITO打开观察）
- 新增功能： plot_aimd 支持读取多个h5文件画在同一张图中
- BUG修复： 电荷差分处理json文件报错
- BUG修复： 极化曲线标记的数值错误
- BUG修复： neb_movie_*.json 中反应坐标重复累加错误

### 0.8.7

- 代码重构，大幅修改数据结构，加速处理过程
- 支持读取h5格式的输出文件
- 新增AIMD, NEB等部分常用功能

### 0.3.0

- 对应2021A版本DS-PAW，辅助处理一些常见数据文件
