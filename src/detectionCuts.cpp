#include "lightcurveFitter.h"
#include "detectionCuts.h"

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
	  Event->chi2_bin[obsgroup] = chi2_bin;
	  Event->Afit_bin = Event->Afit;

	  Event->Atrue = Event->Atrue_pl;
	  Event->Aobs = Event->Aobs_pl;
	  Event->Aerr = Event->Aerr_pl;
	  Event->Atrueerr = Event->Atrueerr_pl;
	  double chi2_pl = fit_current_series(obsgroup);
	  Event->chi2_pl[obsgroup] = chi2_pl;
	  Event->Afit_pl = Event->Afit;

	  Event->Atrue = Event->Atrue_bin;
	  Event->Aobs = Event->Aobs_bin;
	  Event->Aerr = Event->Aerr_bin;
	  Event->Atrueerr = Event->Atrueerr_bin;
	  Event->Afit = Event->Afit_bin;

	  if(chi2_bin > Paramfile->minChiSquared && chi2_pl > Paramfile->minChiSquared)
	    Event->detected=1;
	}
      else
	{
	  double chi2 = fit_current_series(obsgroup);
	  if(chi2 > Paramfile->minChiSquared) Event->detected=1;
	}
    
    } //for each obsgroup
}
