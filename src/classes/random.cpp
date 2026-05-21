
#include "random.h"
#include "random_backend.h"
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>
#include <gsl/gsl_sf_gamma.h>
#include <gsl/gsl_sf_gamma.h>
#include <iostream>
#include <cmath>

#define IA 16807
#define IM 2147483647
#define AM (1.0/IM)
#define IQ 127773
#define IR 2836
#define NTAB 32
#define NDIV (1+(IM-1)/NTAB)
#define EPS 1.2e-7
#define RNMX (1.0 - EPS)

#define IM1a 2147483563
#define IM2a 2147473399
#define AMa (1.0/IM1a)
#define IMM1a (IM1a-1)
#define IA1a 40014
#define IA2a 40692
#define IQ1a 53668
#define IQ2a 52774
#define IR1a 12211
#define IR2a 3791
#define NTABa 32
#define NDIVa (1+IMM1a/NTABa)
#define EPSa 1.2e-7
#define RNMXa (1.0-EPSa)

#define MBIG 1000000000
#define MSEED 161803398
#define MZ 0
#define FAC (1.0/MBIG)

float ran1(long *idum){

  int j;
  long k;
  static long iy=0;
  static long iv[NTAB];
  float temp;

  if (*idum <= 0 || !iy) {
    if (-(*idum) < 1) *idum=1;
    else *idum = -(*idum);
    for (j=NTAB+7;j>=0;j--){
      k = (*idum)/IQ;
      *idum = IA*(*idum - k*IQ)-IR*k;
      if (*idum<0) *idum += IM;
      if (j<NTAB) iv[j] = *idum;
    }
    iy = iv[0];
  }

  k= (*idum)/IQ;
  *idum = IA*(*idum-k*IQ)-IR*k;
  if (*idum < 0 ) *idum += IM;
  j = iy/NDIV;
  iy = iv[j];
  iv[j] = *idum;
  if ((temp=AM*iy) > RNMX) return RNMX;
  else return temp;
}

float gasdev(long *idum){

  float ran2(long *idum);
  static int iset = 0;
  static float gset;
  float fac,rsq,v1,v2;
  
  if (iset==0){
    do { 
      v1=2.0*ran2(idum)-1.0;
      v2=2.0*ran2(idum)-1.0;
      rsq = v1*v1+v2*v2;
    }
    while (rsq >= 1.0 || rsq ==0.0);
    fac = sqrt(-2.0*log(rsq)/rsq);
    gset = v1*fac;
    iset = 1;
    return v2*fac;
  }
  
  else {
    iset = 0;
    return gset;
  }
}

float ran2(long *idum){
  int j;
  long k;
  static long idum2=123456789;
  static long iy=0;
  static long iv[NTABa];
  float temp;

namespace {
float bounded_uniform_float() {
    constexpr float rnmx = 1.0f - 1.2e-7f;
    const double uniform = gsl_rng_uniform(gsl_rng_fallback);
    return (uniform >= rnmx) ? rnmx : static_cast<float>(uniform);
}

int register_random_backend() {
    gulls_register_random_stub_backend("gsl_fallback_stub");
    return 0;
}

[[maybe_unused]] const int random_backend_registration = register_random_backend();
}

float ran1(long *idum) {
    init_fallback_rng();
    // Only reseed if idum is negative (NR convention for initialization)
    if (idum && *idum < 0) {
        gsl_rng_set(gsl_rng_fallback, -(*idum));
        *idum = 1; // Mark as initialized
    }
    return bounded_uniform_float();
}

float ran2(long *idum) {
    init_fallback_rng();
    // Only reseed if idum is negative (NR convention for initialization)
    if (idum && *idum < 0) {
        gsl_rng_set(gsl_rng_fallback, -(*idum));
        *idum = 1; // Mark as initialized
    }
    return bounded_uniform_float();
}

float ran3(long *idum) {
    return ran2(idum);
}

float gasdev(long *idum) {
    init_fallback_rng();
    // Only reseed if idum is negative (NR convention for initialization)
    if (idum && *idum < 0) {
        gsl_rng_set(gsl_rng_fallback, -(*idum));
        *idum = 1; // Mark as initialized
    }
    return gsl_ran_gaussian(gsl_rng_fallback, 1.0);
}

double gammln(double xx) {
    // Use GSL's log gamma function
    return gsl_sf_lngamma(xx);
}

double poisson(double mean, long *idum) {
    init_fallback_rng();
    // Only reseed if idum is negative (NR convention for initialization)
    if (idum && *idum < 0) {
        gsl_rng_set(gsl_rng_fallback, -(*idum));
        *idum = 1; // Mark as initialized
    }
    return gsl_ran_poisson(gsl_rng_fallback, mean);
}
