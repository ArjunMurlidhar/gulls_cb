#include "cbEffectiveLens.h"

#include <cmath>

using std::complex;

static const double CB_PI = std::acos(-1.0);

bool cb_effective_parameters(double sb, double qb, double sp, double qp, double psi,
			     EffectiveLensParams* out)
{
  if(out == nullptr)
    {
      return false;
    }

  const double m1 = 1.0 / (1.0 + qb);
  const double m2 = qb / (1.0 + qb);
  const complex<double> zp = sp * std::exp(complex<double>(0.0, psi));
  const complex<double> d1 = std::conj(zp + m2 * sb);
  const complex<double> d2 = std::conj(zp - m1 * sb);

  const complex<double> caustic_reference = zp - m1 / d1 - m2 / d2;
  const complex<double> gamma = m1 / (d1 * d1) + m2 / (d2 * d2);
  const double gabs = std::abs(gamma);
  if(gabs == 0.0)
    {
      return false;
    }

  const double s_eff = std::pow(gabs, -0.5);
  double psi_eff = std::arg(gamma) / 2.0;
  psi_eff += CB_PI * std::round((psi - psi_eff) / CB_PI);

  const complex<double> host_position =
    caustic_reference - std::exp(complex<double>(0.0, psi_eff)) * (s_eff - 1.0 / s_eff);

  out->s_eff = s_eff;
  out->qp = qp;
  out->psi_eff = psi_eff;
  out->host_position = host_position;
  return true;
}

complex<double> cb_to_vbm_frame(complex<double> z, double s_eff, double q,
				double psi_eff, complex<double> host_position)
{
  return (1.0 / std::sqrt(1.0 + q))
    * (std::exp(complex<double>(0.0, -psi_eff)) * (z - host_position)
       + q * s_eff / (1.0 + q));
}
