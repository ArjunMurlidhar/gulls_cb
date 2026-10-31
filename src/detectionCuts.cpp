#include "lightcurveFitter.h"
#include "detectionCuts.h"
#include "cbEffectiveLens.h"

#include <algorithm>

// Same condition as the upeak override in the PSPL and FSPL fitters.
// obsidx is the last observatory of the current group, which is what those
// fitters have left in hand when they choose the seed.
static bool companion_upeak_replaces_seed(struct filekeywords* Paramfile,
					  struct obsfilekeywords World[],
					  struct event* Event)
{
  if(!(Paramfile->multiple_sources && Event->nsrc>1))
    return false;
  const int obsgroup = Event->currentgroup;
  if(obsgroup<0 || obsgroup>=int(Event->obsgroups.size())
     || Event->obsgroups[obsgroup].empty())
    return false;
  if(Event->mu_src.size()<2 || Event->mu_src[0].empty() || Event->mu_src[1].empty())
    return false;
  if(Event->scomp_fsofs1.empty() || Event->scomp_fsofs1[0].empty())
    return false;

  const int obsidx = Event->obsgroups[obsgroup].back();
  if(obsidx<0 || obsidx>=Paramfile->numobservatories)
    return false;
  const int filt = World[obsidx].filter;
  if(filt<0 || filt>=int(Event->scomp_fsofs1[0].size()))
    return false;

  const double max_mu0 = *std::max_element(Event->mu_src[0].begin(), Event->mu_src[0].end());
  const double max_mu1 = *std::max_element(Event->mu_src[1].begin(), Event->mu_src[1].end());
  return Event->scomp_fsofs1[0][filt] * max_mu1 > max_mu0;
}

void detectionCuts(struct filekeywords* Paramfile, struct event *Event, struct obsfilekeywords World[], struct slcat *Sources, struct slcat *Lenses)
{

  int obsidx;
  
  //dont bother if there was an error generating the lightcurve
  if(Event->lcerror) return;
  if(Event->skip_lc) return;

  Event->deterror=0;
  Event->detected=0;

  const bool dual_lc = (Event->Aobs_bin.size()==size_t(Event->nepochs)
			&& Event->Aobs_pl.size()==size_t(Event->nepochs)
			&& Event->Atrue_bin.size()==size_t(Event->nepochs)
			&& Event->Atrue_pl.size()==size_t(Event->nepochs));
  Event->chi2_bin.assign(Event->obsgroups.size(), 0.0);
  Event->chi2_pl.assign(Event->obsgroups.size(), 0.0);
  Event->flatchi2_bin.assign(Event->obsgroups.size(), 0.0);
  Event->flatchi2_pl.assign(Event->obsgroups.size(), 0.0);
  if(dual_lc)
    {
      Event->Afit_bin.assign(Event->nepochs, 0.0);
      Event->Afit_pl.assign(Event->nepochs, 0.0);
    }

  auto reset_pllx = [&]()
    {
      for(obsidx=0;obsidx<Paramfile->numobservatories;obsidx++)
	{
	  Event->pllx[obsidx].provide_murel_h_lb(Event->murel_l,Event->murel_b,
						 Event->piE, Event->thE);
	  Event->pllx[obsidx].compute_tushifts();
	}
    };

  auto fit_current_series = [&](int obsgroup) -> double
    {
      lightcurveFitter(Paramfile, World, Event);
      reset_pllx();
      if(abs(Event->umin) < 10*Event->rs && Event->PSPL[obsgroup].chisq>Paramfile->minChiSquared)
	{
	  Event->flag_needFS[obsgroup]=1;
	  lightcurveFitter_FS(Paramfile, World, Event);
	  reset_pllx();
	}
      if(Paramfile->outputOnDet==2) return Event->flatchi2[obsgroup];
      if(Event->flag_needFS[obsgroup]) return Event->FSPL[obsgroup].chisq;
      return Event->PSPL[obsgroup].chisq;
    };

  for(int obsgroup=0; obsgroup<int(Event->obsgroups.size()); obsgroup++)
    {

      Event->currentgroup=obsgroup;

      if(dual_lc)
	{
	  Event->Atrue = Event->Atrue_bin;
	  Event->Aobs = Event->Aobs_bin;
	  Event->Aerr = Event->Aerr_bin;
	  Event->Atrueerr = Event->Atrueerr_bin;
	  double chi2_bin = fit_current_series(obsgroup);
	  Event->flatchi2_bin[obsgroup] = Event->flatchi2[obsgroup];
	  Event->chi2_bin[obsgroup] = chi2_bin;
	  Event->Afit_bin = Event->Afit;

	  Event->Atrue = Event->Atrue_pl;
	  Event->Aobs = Event->Aobs_pl;
	  Event->Aerr = Event->Aerr_pl;
	  Event->Atrueerr = Event->Atrueerr_pl;

	  // Planet series only: t0, u0, tE of the effective host. The binary
	  // series above already used the catalog primary. Put those back
	  // before the next group so it is not left on the host seeds.
	  const double catalog_u0 = Event->u0;
	  const double catalog_t0 = Event->t0;
	  const double catalog_tE = Event->tE_r;
	  const int catalog_multiple_sources = Paramfile->multiple_sources;
	  double host_u0 = 0.0;
	  double host_t0 = 0.0;
	  double host_tE = 0.0;
	  if(cb_host_single_lens_seeds(Event->cb_t0, Event->cb_u0, Event->cb_tE,
				       Event->cb_alpha, Event->cb_sb, Event->cb_qb,
				       Event->cb_sp, Event->cb_qp, Event->cb_psi,
				       &host_u0, &host_t0, &host_tE))
	    {
	      Event->u0 = host_u0;
	      Event->t0 = host_t0;
	      Event->tE_r = host_tE;
	      if(companion_upeak_replaces_seed(Paramfile, World, Event))
		Paramfile->multiple_sources = 0;
	    }
	  double chi2_pl = fit_current_series(obsgroup);
	  Event->u0 = catalog_u0;
	  Event->t0 = catalog_t0;
	  Event->tE_r = catalog_tE;
	  Paramfile->multiple_sources = catalog_multiple_sources;
	  Event->flatchi2_pl[obsgroup] = Event->flatchi2[obsgroup];
	  Event->chi2_pl[obsgroup] = chi2_pl;
	  Event->Afit_pl = Event->Afit;

	  Event->Atrue = Event->Atrue_bin;
	  Event->Aobs = Event->Aobs_bin;
	  Event->Aerr = Event->Aerr_bin;
	  Event->Atrueerr = Event->Atrueerr_bin;
	  Event->Afit = Event->Afit_bin;

	  if(chi2_bin > Paramfile->minChiSquared || chi2_pl > Paramfile->minChiSquared)
	    Event->detected=1;
	}
      else
	{
	  double chi2 = fit_current_series(obsgroup);
	  if(chi2 > Paramfile->minChiSquared) Event->detected=1;
	}
    
    } //for each obsgroup
}
