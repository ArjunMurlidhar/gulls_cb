#ifndef CB_EFFECTIVE_LENS_H
#define CB_EFFECTIVE_LENS_H

#include <cmath>
#include <complex>

// Python helpers in documentation/Background/Project Description for Agents.md
// (effective_parameters + to_vbm_frame) are the source of truth.
// Lengths: Einstein radius of M1+M2. qb = M2/M1; qp = mp/(M1+M2). Angles in radians.

struct EffectiveLensParams
{
  double s_eff;
  double qp;
  double psi_eff;
  std::complex<double> host_position;
};

// Returns false on zero shear (no finite effective separation).
// Defined here so the planet-fit seed can call it without a new link.
inline bool cb_effective_parameters(double sb, double qb, double sp, double qp, double psi,
				    EffectiveLensParams* out)
{
  if(out == nullptr)
    {
      return false;
    }

  const double m1 = 1.0 / (1.0 + qb);
  const double m2 = qb / (1.0 + qb);
  const std::complex<double> zp = sp * std::exp(std::complex<double>(0.0, psi));
  const std::complex<double> d1 = std::conj(zp + m2 * sb);
  const std::complex<double> d2 = std::conj(zp - m1 * sb);

  const std::complex<double> caustic_reference = zp - m1 / d1 - m2 / d2;
  const std::complex<double> gamma = m1 / (d1 * d1) + m2 / (d2 * d2);
  const double gabs = std::abs(gamma);
  if(gabs == 0.0)
    {
      return false;
    }

  const double pi = std::acos(-1.0);
  const double s_eff = std::pow(gabs, -0.5);
  double psi_eff = std::arg(gamma) / 2.0;
  psi_eff += pi * std::round((psi - psi_eff) / pi);

  const std::complex<double> host_position =
    caustic_reference - std::exp(std::complex<double>(0.0, psi_eff)) * (s_eff - 1.0 / s_eff);

  out->s_eff = s_eff;
  out->qp = qp;
  out->psi_eff = psi_eff;
  out->host_position = host_position;
  return true;
}

// Straight-line closest approach of the cb source track to the effective host.
// cb_alpha_deg and psi_deg are degrees. cb_alpha is in [0, 360): zero is the
// lighter star toward the heavier star. host_position is in the M2-on-+x frame.
// When qb <= 1 that axis is opposite M2, so the track is rotated 180 deg into
// the host frame. tE is cb_tE (Einstein time of M1+M2), not scaled by sqrt(1+qp).
// u0 is the gulls signed impact parameter. Returns false if the host is undefined.
inline bool cb_host_single_lens_seeds(double cb_t0, double cb_u0, double cb_tE,
				      double cb_alpha_deg,
				      double sb, double qb, double sp, double qp,
				      double psi_deg,
				      double* u0, double* t0, double* tE)
{
  if(u0 == nullptr || t0 == nullptr || tE == nullptr)
    return false;
  if(!std::isfinite(cb_t0) || !std::isfinite(cb_u0) || !std::isfinite(cb_tE)
     || !(cb_tE > 0.0) || !std::isfinite(cb_alpha_deg)
     || !std::isfinite(sb) || !std::isfinite(qb) || !(qb > 0.0)
     || !std::isfinite(sp) || !std::isfinite(qp) || !std::isfinite(psi_deg))
    return false;

  const double deg = std::acos(-1.0) / 180.0;
  EffectiveLensParams eff;
  if(!cb_effective_parameters(sb, qb, sp, qp, psi_deg * deg, &eff))
    return false;

  const double hx = eff.host_position.real();
  const double hy = eff.host_position.imag();
  if(!std::isfinite(hx) || !std::isfinite(hy))
    return false;

  const double flip = (qb <= 1.0) ? -1.0 : 1.0;
  const double a = cb_alpha_deg * deg;
  const double sa = std::sin(a);
  const double ca = std::cos(a);
  const double along = hx * ca + hy * sa;
  const double across = hx * sa - hy * ca;
  const double u_host = cb_u0 - flip * across;
  const double t_host = cb_t0 + flip * along * cb_tE;
  if(!std::isfinite(u_host) || !std::isfinite(t_host))
    return false;

  *u0 = u_host;
  *t0 = t_host;
  *tE = cb_tE;
  return true;
}

std::complex<double> cb_to_vbm_frame(std::complex<double> z, double s_eff, double q,
				     double psi_eff, std::complex<double> host_position);

#endif
