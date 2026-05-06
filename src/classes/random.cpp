
#include "random.h"
#include <math.h>

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

  if(*idum <=0){
    if (-(*idum)<1) *idum =1;
    else *idum = -(*idum);
    idum2=(*idum);
    for (j=NTABa+7;j>=0;j--){
      k = (*idum)/IQ1a;
      *idum=IA1a*(*idum-k*IQ1a)-k*IR1a;
      if (*idum < 0) *idum += IM1a;
      if (j < NTABa) iv[j] = *idum;
    }
    iy = iv[0];
  }
  k =(*idum)/IQ1a;
  *idum=IA1a*(*idum-k*IQ1a)-k*IR1a;
  if(*idum < 0) *idum += IM1a;
  k = idum2/IQ2a;
  idum2 = IA2a*(idum2-k*IQ2a)-k*IR2a;
  if(idum2 < 0) idum2 += IM2a;
  j = iy/NDIVa;
  iy = iv[j]-idum2;
  iv[j] = *idum;
  if (iy < 1) iy += IMM1a;
  if ((temp =AMa*iy) > RNMXa) return RNMXa;
  else return temp;
}


float ran3(long *idum){

  static int inext,inextp;
  static long ma[56];
  static int iff = 0;
  long mj,mk;
  int i,ii,k;

  if( *idum < 0 || iff ==0){
    iff = 1;
    mj=MSEED-(*idum < 0 ? -*idum : *idum);
    mj %= MBIG;
    ma[55] = mj;
    mk = 1;
    for (i=1;i<54;i++){
      ii=(21*i) % 55;
      ma[ii]=mk;
      mk=mj-mk;
      if(mk < MZ) mk += MBIG;
      mj=ma[ii];
    }
    for (k=1;k<=4;k++)
      for (i = 1;i<=55;i++) {
	ma[i] -= ma[1+(i+30) % 55];
	if (ma[i] < MZ) ma[i] += MBIG;
      }
    inext = 0;
    inextp = 31;
    *idum = 1;
  }
  if (++inext == 56) inext = 1;
  if (++inextp == 56) inextp = 1;
  mj=ma[inext] - ma[inextp];
  if (mj < MZ) mj += MBIG;
  ma[inext] = mj;
  return mj*FAC;
}

double gammln(double xx)
{
  //returns the natural log of the Gamma function for positive xx
  double x,y,tmp,ser;
  //static double cof[6]={76.18009172947146,-86.50532032941677,24.01409824083091,-1.231739572450155,0.1208650973866179e-2,-0.5395239384953e-5};
  //int j;

  y=x=xx;
  tmp=x+5.5;
  tmp -= (x+0.5)*log(tmp);
  //ser=1.000000000190015;
  ser=1.000000000190015 + 76.18009172947146/(y+1) + -86.50532032941677/(y+2) + 24.01409824083091/(y+3) + -1.231739572450155/(y+4) + 0.1208650973866179e-2/(y+5) + -0.5395239384953e-5/(y+6);
  //for(j=0;j<=5;j++) ser+=cof[j]/++y;
  return -tmp+log(2.5066282746310005*ser/x);
}

//Poisson distribution

double poisson(double mean, long* idum)
{
  static double sqr,alxm,g,oldm=-1.0;
  const double pi=3.1415926535897932384626433;
  double em,t_,y;

  //if(mean<=0||!finite(mean)) return 0;
  //else 
  if(mean<12.0) //use the direct method
    {
      if(mean!=oldm) //has the mean changed since the larst call?
	{
	  oldm=mean;
	  g=exp(-mean); //if mean is new compute the exponentiial
	}
      em=-1.0;
      t_=1.0;
      do       //multiply uniform deviates rather than adding
	{      //exponential ones. We don't have to take the log.
	  ++em;
	  t_ *= ran2(idum);
	} while (t_ > g);
    }
  else     //use the rejection method
    {
      if(mean != oldm)  //if the mean has changed, precompute some stuff
	{
	  oldm=mean;
	  sqr=sqrt(2.0*mean);
	  alxm=log(mean);
	  g=mean*alxm - gammln(mean+1.0);
	}
      do
	{
	  do
	    {
	      y=tan(pi*ran2(idum));
	      em=sqr*y+mean;
	    } while (em<0.0);
	  em=floor(em);
	  t_=0.9*(1.0+y*y)*exp(em*alxm-gammln(em+1.0)-g);
	} while (ran2(idum) > t_);
    }
  return em;
}

bool gulls_random_is_stub() { return false; }
const char* gulls_random_backend_name() { return "numerical_recipes"; }