"""
Amplitude compensation curves
"""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import *
from math import sqrt
import numpy as np


_AMPCOMP_MINLEVEL = -0.1575371167435


class AmpcompA:
    def __init__(self, root=0, minamp=0.32, rootamp=1.0, minlevel=_AMPCOMP_MINLEVEL):
        self.root = root
        self.minamp = minamp
        self.rootamp = rootamp
        rootlevel = acurveAmplitudeCompensation(root)
        self.scale = (rootamp - minamp) / (rootlevel - minlevel)
        self.offset = minamp - self.scale * minlevel

    def level(self, freq):
        return acurveAmplitudeCompensation(freq) * self.scale + self.offset


def acurveAmplitudeCompensationArray(freqs: np.ndarray):
    """
    Calculate the ampltude compensation for freq according to an A-Curve

    Argss:
        freqs: the frequencys to evaluate the curve at

    Returns:
        the resulting amplitude compensation
    """
    k = 3.5041384 * 10e15
    c1 = 20.598997 ** 2
    c2 = 107.65265 ** 2
    c3 = 737.86223 ** 2
    c4 = 12194.217 ** 2
    r = freqs * freqs
    r2 = r*r
    level = r2*r2 * k
    n1 = r + c1
    n2 = r + c4
    levels = level / (n1 * n1 * (c2 + r) * (c3 + r) * n2 * n2)
    return 1 - np.sqrt(levels)


def acurveAmplitudeCompensation(freq: float):
    """
    Calculate the ampltude compensation for freq according to an A-Curve

    Args:
        freq: the frequency to evaluate the curve at

    Returns:

    """
    k = 3.5041384 * 10e15
    c1 = 20.598997 ** 2
    c2 = 107.65265 ** 2
    c3 = 737.86223 ** 2
    c4 = 12194.217 ** 2
    r = freq * freq
    r2 = r*r
    level = k * r2*r2
    n1 = c1 + r
    n2 = c4 + r
    level = level / (n1*n1*(c2+r) * (c3+r) * n2*n2)
    return 1 - sqrt(level)


# Original code from supercollider AmpCompA

"""

const double AMPCOMP_K = 3.5041384 * 10e15;
const double AMPCOMP_C1 = 20.598997 * 20.598997;
const double AMPCOMP_C2 = 107.65265 * 107.65265;
const double AMPCOMP_C3 = 737.86223 * 737.86223;
const double AMPCOMP_C4 = 12194.217 * 12194.217;
const double AMPCOMP_MINLEVEL = -0.1575371167435;

double AmpCompA_calcLevel(double freq)
{
	double r = freq * freq;
	double level = (AMPCOMP_K * r * r * r * r);
	double n1 = AMPCOMP_C1 + r;
	double n2 = AMPCOMP_C4 + r;
	level = level / (
						n1 * n1 *
						(AMPCOMP_C2 + r) *
						(AMPCOMP_C3 + r) *
						n2 * n2
					);
	level = 1. - sqrt(level);
	return level;
}

void AmpCompA_next(AmpCompA *unit, int inNumSamples)
{
	float *out = ZOUT(0);
	float *freq = ZIN(0);

	double scale = unit->m_scale;
	double offset = unit->m_offset;

	LOOP1(inNumSamples,
		ZXP(out) = AmpCompA_calcLevel(ZXP(freq)) * scale + offset;
	);
}

void AmpCompA_Ctor(AmpCompA* unit)
{
	double rootFreq = ZIN0(1);
	double rootLevel = AmpCompA_calcLevel(rootFreq);
	float minLevel = ZIN0(2);
	unit->m_scale = (ZIN0(3) - minLevel) / (rootLevel - AMPCOMP_MINLEVEL);
	unit->m_offset = minLevel - unit->m_scale * AMPCOMP_MINLEVEL;

	SETCALC(AmpCompA_next);
	AmpCompA_next(unit, 1);
}
"""