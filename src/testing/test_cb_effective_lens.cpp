#include "cbEffectiveLens.h"

#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <string>

int main(int argc, char** argv)
{
  if(argc != 6 && argc != 8)
    {
      std::cerr << "Usage: test_cb_effective_lens.x sb qb sp qp psi [y1 y2]\n";
      return 2;
    }

  const double sb = std::atof(argv[1]);
  const double qb = std::atof(argv[2]);
  const double sp = std::atof(argv[3]);
  const double qp = std::atof(argv[4]);
  const double psi = std::atof(argv[5]);

  EffectiveLensParams eff;
  if(!cb_effective_parameters(sb, qb, sp, qp, psi, &eff))
    {
      std::cerr << "zero_shear\n";
      return 1;
    }

  std::cout << std::setprecision(16)
	    << eff.s_eff << " " << eff.qp << " " << eff.psi_eff << " "
	    << eff.host_position.real() << " " << eff.host_position.imag();

  if(argc == 8)
    {
      const double y1 = std::atof(argv[6]);
      const double y2 = std::atof(argv[7]);
      const std::complex<double> z_vbm =
	cb_to_vbm_frame(std::complex<double>(y1, y2), eff.s_eff, qp, eff.psi_eff, eff.host_position);
      std::cout << " " << z_vbm.real() << " " << z_vbm.imag();
    }
  std::cout << "\n";
  return 0;
}
