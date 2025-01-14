"""
Implements Performance Check (PC) Method according to technical standard ISO/DIS 24194.

HowTo
=====

See :py:mod:main docstring.

Why
===

The Performance Check (PC) method can be used to decide whether the measured performance of a solar thermal plant
matches the performance estimated based on given information (data sheets, boundary conditions etc).

From the ISO/DIS 24194:
"
    # 1 Scope
    [This method allows to] verify the performance of solar thermal collector fields. The
    collectors in the fields can be glazed flat plate collectors, evacuated tube collectors and/or
    tracking, concentrating collectors.
    [...]

    # 5 Procedure for checking the power performance of solar thermal collector fields
    The estimated power output of the collector array is given as an equation depending on collector parameters
    according to ISO 9806 and operating conditions. The measured power shall comply with the corresponding
    calculated power according to this equation. Measured and calculated power are only compared under some specific
    conditions to avoid too large uncertainties - see section 5.4.

    # 5.2 Calculating power output
    The estimate is given by stating the equation to be used for calculating the power output, including specific values
    for the parameters in equation. The three possible equations are given in the next three subsections.
    The collector module efficiency parameters eta0_hem, eta0_b, Kb(theta) Kd, a1, a2, a5 [1] and a8 should be based on
    certified test results. When an estimate is given it shall always be stated which equation shall be used for
    checking the performance:

    a) Simple check, using total radiation on the collector plane when checking the power output
    (ISO this standard, eq 1).
    b) Advanced check, using direct and diffuse radiation on collector plane when checking the power output
    (ISO this standard, eq 2).
    c) Advanced check, using only direct radiation on collector plane when checking the power output
    (ISO this standard, eq3)

    [1] in the older Solar Keymark data sheets a5 is denoted c_eff
"

# Notes & usage hints

- Assumes tilted beam and diffuse radiations available (no radiation splitting inside this code)
- Assumes wind velocity available. There is an `ignore_wind` flag to ignore wind measurements at all.
- Power is assumed to be measured once (for the plant object). If multiple power measurements are available,
consider treating them as separate plants and running the PC method on each of them separately.
- Current implementation assumes that temperatures (`te_in`, `te_out`) are available for all collector arrays.
Application to other configurations is yet unclear.
- Radiations (`rd_bti`, `rd_dti`) are defined and assumed to be available for each array.
- Details concerning radiation modeling / radiation conversion algorithms are not in this algorithm.
e.g. available = GHI, GTI, beam/diffuse separated, multiple radiation sensors for multiple arrays etc.

# Collector parameter names

The collector parameter names are taken from ISO 24194:2021 (ISO 24194:2022 introduced some name clashes /
unusual symbols, as confirmed in personal communication with the standard developers):
    `a1`: Heat loss coefficient at (theta_m - theta_a = 0)  (named a1_DeltaQ in ISO 24194:2022)
    `a2`: Temperature dependence of the heat loss coefficient (named T_DeltaQ in ISO 24194:2022)
    `a5`: Effective thermal capacity
    `eta0b`: Peak collector efficiency (etab at theta_m -theta_a = 0 K) based on beam irradiance Gb
    `eta0hem`: Peak collector efficiency (`eta0hem` at theta_m - theta_a = 0 K) based on
              hemispherical irradiance G_hem
    `kd`: Incidence angle modifier for diffuse solar radiation (named as Kd in ISO 24194:2022)
"""

import enum
# from .wrapper import run_performance_check
# from .plotting import plot_all, plot_bars
# from .plotting_TMP import plot_square, plot_time, plot_sensor_data

# from .wrapper import run_performance_check, pc_strategy_generator
# from .main import PCMethod, PCSettings, PCMethodISO, PCMethodExtended
# from .equation import Equation1, Equation2
# from .verify_validate import verify_config, validate_data


class AvailablePCEquations(enum.IntEnum):
    one = 1
    two = 2


class AvailablePCMethods(str, enum.Enum):
    iso = 'iso'
    extended = 'extended'


class OutputUnits(str, enum.Enum):
    tp = 'pint[kW]'
    tp_sp = 'pint[W m**-2]'
    rd = 'pint[W m**-2]'
    iam = 'pint[dimensionless]'
    te = 'pint[degC]'
    te_deriv = 'pint[K hour**-1]'
    angle = 'pint[deg]'
