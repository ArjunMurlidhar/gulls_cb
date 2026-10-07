#ifndef CB_EFFECTIVE_LENS_H
#define CB_EFFECTIVE_LENS_H

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
bool cb_effective_parameters(double sb, double qb, double sp, double qp, double psi,
			     EffectiveLensParams* out);

std::complex<double> cb_to_vbm_frame(std::complex<double> z, double s_eff, double q,
				     double psi_eff, std::complex<double> host_position);

#endif
