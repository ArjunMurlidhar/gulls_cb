#include "cbEffectiveLens.h"

#include <cmath>

using std::complex;

complex<double> cb_to_vbm_frame(complex<double> z, double s_eff, double q,
				double psi_eff, complex<double> host_position)
{
  return (1.0 / std::sqrt(1.0 + q))
    * (std::exp(complex<double>(0.0, -psi_eff)) * (z - host_position)
       - q * s_eff / (1.0 + q));
}
