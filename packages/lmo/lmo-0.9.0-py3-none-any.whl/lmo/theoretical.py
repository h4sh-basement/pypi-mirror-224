"""
Theoretical (population) L-moments of known univariate probability
distributions.
"""

__all__ = (
    'l_moment_from_cdf',
    'l_moment_from_ppf',
    'l_ratio_from_cdf',
    'l_ratio_from_ppf',
    'l_stats_from_cdf',
    'l_stats_from_ppf',
)

import functools
import warnings
from collections.abc import Callable
from math import exp, gamma, lgamma
from typing import Any, TypeAlias, cast, overload

import numpy as np
import numpy.typing as npt
import scipy.integrate as sci  # type: ignore
import scipy.special as scs  # type: ignore

from ._utils import moments_to_ratio
from .linalg import sh_jacobi
from .typing import AnyFloat, AnyInt, IntVector

_QuadFullOutput: TypeAlias = (
    tuple[float, float, dict[str, Any]]
    | tuple[float, float, dict[str, Any], str]
)


def _l_moment_const(r: int, s: float, t: float, k: int) -> float:
    if r <= k:
        return 1.
    return (
        exp(lgamma(r + s + t + 1) - lgamma(r + s) - lgamma(r + t))
        * gamma(r - k)
        / r
    )


def _quad(
    integrand: Callable[[float], float],
    support: tuple[AnyFloat, AnyFloat],
    limit: int,
    atol: float,
    rtol: float,
) -> float:
    quad_val, _, _, *quad_tail = sci.quad(  # type: ignore
        integrand,
        *support,
        full_output=True,
        limit=limit,
        epsabs=atol,
        epsrel=rtol,
    )
    if quad_tail:
        msg = f"'scipy.integrate.quad' failed: \n{quad_tail[0]}"
        warnings.warn(msg, sci.IntegrationWarning, stacklevel=2)
        return np.nan

    return cast(float, quad_val)


@overload
def l_moment_from_cdf(
    cdf: Callable[[float], float],
    r: AnyInt,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    *,
    support: tuple[AnyFloat, AnyFloat] = ...,
    rtol: float = ...,
    atol: float = ...,
    limit: int = ...,
) -> np.float_:
    ...


@overload
def l_moment_from_cdf(
    cdf: Callable[[float], float],
    r: IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    *,
    support: tuple[AnyFloat, AnyFloat] = ...,
    rtol: float = ...,
    atol: float = ...,
    limit: int = ...,
) -> npt.NDArray[np.float_]:
    ...


def l_moment_from_cdf(  # noqa: C901
    cdf: Callable[[float], float],
    r: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    *,
    support: tuple[AnyFloat, AnyFloat] = (-np.inf, np.inf),
    rtol: float = 1.49e-8,
    atol: float = 1.49e-8,
    limit: int = 100,
) -> np.float_ | npt.NDArray[np.float_]:
    r"""
    Evaluate the population L-moment of a continuous probability distribution,
    using its Cumulative Distribution Function (CDF) $F_X(x) = P(X \le x)$.

    Notes:
        Numerical integration is performed with
        [`scipy.integrate.quad`][scipy.integrate.quad], which cannot verify
        whether the integral exists and is finite. If it returns an error
        message, an `IntegrationWarning` is issues, and `nan` is returned
        (even if `quad` returned a finite result).

    Args:
        cdf:
            Cumulative Distribution Function (CDF), $F_X(x) = P(X \le x)$.
            Must be a continuous monotone increasing function with
            signature `(float) -> float`, whose return value lies in $[0, 1]$.
        r:
            L-moment order(s), non-negative integer or array-like of integers.
        trim:
            Left- and right- trim. Must be a tuple of two non-negative ints
            or floats (!).

    Other parameters:
        support: The subinterval of the nonzero domain of `cdf`.
        rtol: See `epsrel` [`scipy.integrate.quad`][scipy.integrate.quad].
        atol: See `epsabs` [`scipy.integrate.quad`][scipy.integrate.quad].
        limit: See `limit` in [`scipy.integrate.quad`][scipy.integrate.quad].

    Raises:
        TypeError: `r` is not integer-valued or negative
        ValueError: `r` is negative

    Returns:
        lmbda:
            The population L-moment(s), a scalar or float array like `r`.
            If `nan`, consult the related `IntegrationWarning` message.

    References:
        - [E. Elamir & A. Seheult (2003) - Trimmed L-moments](
            https://doi.org/10.1016/S0167-9473(02)00250-5)
        - [J.R.M. Hosking (2007) - Some theory and practical uses of trimmed
            L-moments](https://doi.org/10.1016/j.jspi.2006.12.002)

    See Also:
        - [`theoretical.l_moment_from_ppf`][lmo.theoretical.l_moment_from_ppf]:
          population L-moment, using the inverse CDF
        - [`l_moment`][lmo.l_moment]: sample L-moment

    Todo:
        - The equations used for the r=0, r=1, and r>1 cases.
        - Optional cdf args and kwargs with ParamSpec.

    """
    _r = np.asanyarray(r)
    if not np.issubdtype(_r.dtype, np.integer):
        msg = 'r must be integer-valued, got {_r.dtype.str!r}'
        raise TypeError(msg)
    if np.any(_r < 0):
        msg = 'r must be non-negative'
        raise TypeError(msg)

    if _r.size == 0:
        return np.empty(_r.shape)

    r_vals, r_idxs = np.unique(_r, return_inverse=True)
    s, t = np.asanyarray(trim)
    trimmed = s != 0 or t != 0

    j = sh_jacobi(min(12, r_vals[-1]) - 1, t + 1, s + 1)

    # caching F(x) function only makes sense for multiple quad calls
    _cdf = functools.cache(cdf) if np.count_nonzero(r_vals) > 1 else cdf

    l_r = np.empty(r_vals.shape)
    for i, r_val in np.ndenumerate(r_vals):
        if r_val == 0:
            # zeroth l-moment is always 1
            l_r[i] = 1
            continue

        if r_val == 1:
            def integrand(x: float, *args: Any) -> float:
                # equivalent to E[X_{s+1 : s+t+1}]
                # see Wiley (2003) eq. 2.1.5
                i_p = p = _cdf(x, *args)
                if trimmed:
                    i_p = scs.betainc(s + 1, t + 1, p)  # type: ignore

                return (x >= 0) - i_p

        else:
            k_val = r_val - 2

            if r_val <= 12:
                c_k, lb = j[k_val, :k_val + 1], 0
            else:
                _j_k = scs.jacobi(k_val, t + 1, s + 1)  # type: ignore
                c_k, lb = _j_k.coef[::-1], -1

            j_k = np.polynomial.Polynomial(c_k, domain=[0, 1], window=[lb, 1])

            # avoid overflows: split in sign and log, and recombine later
            # j_k_sgn = np.sign(j_k)
            # j_k_ln = np.log(np.abs(j_k))

            def integrand(x: float, *args: Any) -> float:
                """
                Evaluate the jacobi polynomial for p at r-1 with (t, s)
                and multiply by the weight function.
                """
                p = _cdf(x, *args)
                return p**(s + 1) * (1 - p)**(t + 1) * j_k(p)  # type: ignore

        quad_val = _quad(integrand, support, limit, atol, rtol)
        l_r[i] = _l_moment_const(r_val, s, t, 1) * quad_val

    return (np.round(l_r, 12) + .0)[r_idxs].reshape(_r.shape)[()]


@overload
def l_moment_from_ppf(
    ppf: Callable[[float], float],
    r: AnyInt,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    *,
    support: tuple[AnyFloat, AnyFloat] = ...,
    rtol: float = ...,
    atol: float = ...,
    limit: int = ...,
) -> np.float_:
    ...


@overload
def l_moment_from_ppf(
    ppf: Callable[[float], float],
    r: IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    *,
    support: tuple[AnyFloat, AnyFloat] = ...,
    rtol: float = ...,
    atol: float = ...,
    limit: int = ...,
) -> npt.NDArray[np.float_]:
    ...


def l_moment_from_ppf(
    ppf: Callable[[float], float],
    r: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    *,
    support: tuple[AnyFloat, AnyFloat] = (0, 1),
    rtol: float = 1.49e-8,
    atol: float = 1.49e-8,
    limit: int = 100,
) -> np.float_ | npt.NDArray[np.float_]:
    """
    Evaluate the population L-moment of a continuous probability distribution,
    using its Percentile Function (PPF) $Q_X(p) = F^{-1}_X(p)$,
    i.e. the inverse of the CDF, commonly known as the quantile function.

    Notes:
        Numerical integration is performed with
        [`scipy.integrate.quad`][scipy.integrate.quad], which cannot verify
        whether the integral exists and is finite. If it returns an error
        message, an `IntegrationWarning` is issues, and `nan` is returned
        (even if `quad` returned a finite result).

    Args:
        ppf:
            The quantile function, a monotonically continuous increasing
            function with signature `(float) -> float`, that maps a
            probability in $[0, 1]$, to the domain of the distribution.
        r:
            L-moment order(s), non-negative integer or array-like of integers.
        trim:
            Left- and right- trim. Must be a tuple of two non-negative ints
            or floats (!).

    Other parameters:
        support: The subinterval of the nonzero domain of `ppf`.
        rtol: See `epsrel` [`scipy.integrate.quad`][scipy.integrate.quad].
        atol: See `epsabs` [`scipy.integrate.quad`][scipy.integrate.quad].
        limit: See `limit` in [`scipy.integrate.quad`][scipy.integrate.quad].

    Raises:
        TypeError: `r` is not integer-valued
        ValueError: `r` is empty or negative

    Returns:
        lmbda:
            The population L-moment(s), a scalar or float array like `r`.
            If `nan`, consult the related `IntegrationWarning` message.

    References:
        - [E. Elamir & A. Seheult (2003) - Trimmed L-moments](
            https://doi.org/10.1016/S0167-9473(02)00250-5)
        - [J.R.M. Hosking (2007) - Some theory and practical uses of trimmed
            L-moments](https://doi.org/10.1016/j.jspi.2006.12.002)

    See Also:
        - [`theoretical.l_moment_from_cdf`][lmo.theoretical.l_moment_from_cdf]:
          population L-moment, using the CDF (i.e. the inverse PPF)
        - [`l_moment`][lmo.l_moment]: sample L-moment

    Todo:
        - The equations used for the r=0, r>0 cases.
        - Optional ppf args and kwargs with ParamSpec.

    """
    _r = np.asanyarray(r)
    if not np.issubdtype(_r.dtype, np.integer):
        msg = 'r must be integer-valued, got {_r.dtype.str!r}'
        raise TypeError(msg)
    if np.any(_r < 0):
        msg = 'r must be non-negative'
        raise TypeError(msg)

    if _r.size == 0:
        return np.empty(_r.shape)

    r_vals, r_idxs = np.unique(_r, return_inverse=True)
    s, t = np.asanyarray(trim)

    j = sh_jacobi(min(r_vals[-1], 12), t, s)

    def w(p: float, *args: Any) -> float:
        return p**s * (1 - p)**t * ppf(p, *args)

    # caching the weight function only makes sense for multiple quad calls
    _w = functools.cache(w) if len(r_vals) > 1 else w

    # lazy import (don't worry; python imports are cached)
    from scipy.special import jacobi  # type: ignore

    l_r = np.empty(r_vals.shape)
    for i, r_val in np.ndenumerate(r_vals):
        if r_val == 0:
            # zeroth l-moment is always 1
            l_r[i] = 1
            continue

        if r_val <= 12:
            j_k = np.polynomial.Polynomial(
                j[r_val - 1, :r_val],
                domain=[0, 1],
                window=[0, 1],
            )
        else:
            j_k = np.polynomial.Polynomial(
                jacobi(r_val - 1, t, s).coef[::-1],  # type: ignore
                domain=[0, 1],
                window=[-1, 1],
            )

        def integrand(p: float) -> float:
            return _w(p) * j_k(p)  # type: ignore

        quad_val = _quad(integrand, support, limit, atol, rtol)
        l_r[i] = _l_moment_const(r_val, s, t, 0) * quad_val

    return (np.round(l_r, 12) + .0)[r_idxs].reshape(_r.shape)[()]


@overload
def l_ratio_from_cdf(
    cdf: Callable[[float], float],
    r: AnyInt,
    s: AnyInt,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> np.float_:
    ...


@overload
def l_ratio_from_cdf(
    cdf: Callable[[float], float],
    r: IntVector,
    s: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    ...


@overload
def l_ratio_from_cdf(
    cdf: Callable[[float], float],
    r: AnyInt | IntVector,
    s: IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    ...


def l_ratio_from_cdf(
    cdf: Callable[[float], float],
    r: AnyInt | IntVector,
    s: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    **kwargs: Any,
) -> np.float_ | npt.NDArray[np.float_]:
    """
    Population L-ratio's from a CDF.

    See Also:
        - [`l_ratio_from_ppf`][lmo.theoretical.l_ratio_from_ppf]
        - [`lmo.l_ratio`][lmo.l_ratio]
    """
    rs = np.stack(np.broadcast_arrays(np.asarray(r), np.asarray(s)))
    l_rs = l_moment_from_cdf(cdf, rs, trim, **kwargs)

    return moments_to_ratio(rs, l_rs)


@overload
def l_ratio_from_ppf(
    ppf: Callable[[float], float],
    r: AnyInt,
    s: AnyInt,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> np.float_:
    ...


@overload
def l_ratio_from_ppf(
    ppf: Callable[[float], float],
    r: IntVector,
    s: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    ...


@overload
def l_ratio_from_ppf(
    ppf: Callable[[float], float],
    r: AnyInt | IntVector,
    s: IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = ...,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    ...


def l_ratio_from_ppf(
    ppf: Callable[[float], float],
    r: AnyInt | IntVector,
    s: AnyInt | IntVector,
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    **kwargs: Any,
) -> np.float_ | npt.NDArray[np.float_]:
    """
    Population L-ratio's from a PPF.

    See Also:
        - [`l_ratio_from_cdf`][lmo.theoretical.l_ratio_from_cdf]
        - [`lmo.l_ratio`][lmo.l_ratio]
    """
    rs = np.stack(np.broadcast_arrays(np.asarray(r), np.asarray(s)))
    l_rs = l_moment_from_ppf(ppf, rs, trim, **kwargs)

    return moments_to_ratio(rs, l_rs)


def l_stats_from_cdf(
    cdf: Callable[[float], float],
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    num: int = 4,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    """
    Calculates the population L-loc(ation), L-scale, L-skew(ness) and
    L-kurtosis from a CDF.

    Alias for `l_ratio_from_cdf(cdf, [1, 2, 3, 4], [0, 0, 2, 2], *, **)`.

    See Also:
        - [`l_ratio_from_cdf`][lmo.theoretical.l_ratio_from_cdf]
        - [`l_moment_from_cdf`][lmo.theoretical.l_moment_from_cdf]
        - [`l_stats_from_ppf`][lmo.theoretical.l_ratio_from_ppf]
    """
    r, s = np.arange(1, num + 1), [0] * min(2, num) + [2] * (num - 2)
    return l_ratio_from_cdf(cdf, r, s, trim=trim, **kwargs)


def l_stats_from_ppf(
    ppf: Callable[[float], float],
    /,
    trim: tuple[AnyFloat, AnyFloat] = (0, 0),
    num: int = 4,
    **kwargs: Any,
) -> npt.NDArray[np.float_]:
    """
    Calculates the population L-loc(ation), L-scale, L-skew(ness) and
    L-kurtosis from a PPF.

    Alias for `l_ratio_from_ppf(cdf, [1, 2, 3, 4], [0, 0, 2, 2], *, **)`.

    See Also:
        - [`l_ratio_from_ppf`][lmo.theoretical.l_ratio_from_ppf]
        - [`l_moment_from_ppf`][lmo.theoretical.l_moment_from_ppf]
        - [`l_stats_from_cdf`][lmo.theoretical.l_ratio_from_cdf]
    """
    r, s = np.arange(1, num + 1), [0] * min(2, num) + [2] * (num - 2)
    return l_ratio_from_ppf(ppf, r, s, trim=trim, **kwargs)
