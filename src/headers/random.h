#ifndef RANDOM_HEADER
#define RANDOM_HEADER

#include <math.h>

// Absolute value of a signed idum as unsigned long, including magnitudes
// above 2^31-1 and LONG_MIN. Clock seeds are stored negative.
inline unsigned long random_seed_magnitude(long idum)
{
  if(idum >= 0) return static_cast<unsigned long>(idum);
  return static_cast<unsigned long>(-(idum + 1L)) + 1UL;
}

// Seed the shared GSL mt19937 from an unsigned magnitude. ran1/ran2/gasdev/
// poisson do not reseed; a later negative idum must not restart the generator.
void seed_random(unsigned long seed);

float ran1(long *idum);
float gasdev(long *idum);
float ran3(long *idum);
float ran2(long *idum);
double gammln(double xx);
double poisson(double mean, long* idum);

inline double normal(double mean, double sigma, long* idum)
{
  return mean + sigma*gasdev(idum);
}

inline double logNormal(double mean, double sigma, long* idum)
{
  return exp(log(mean)+sigma*gasdev(idum));
}

inline long randint(long min, long max, long* idum)
{
  return min + int(ran2(idum)*(max-min+1));
}

#endif
