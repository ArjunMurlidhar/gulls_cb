#include<cmath>
#include<cstdlib>
#include<complex>
#include<cstdio>
#include<iostream>
#include<string>
#include "zroots2.h"

using namespace std;
/*
zr::zr()
{
}

zr::~zr()
{
}
*/
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::laguer
//		Numerically finds a root of the polynomial given in a[]
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

bool laguer(complex<double> a[], int m, complex<double> *x, int *its, string s)
{
  //returns true only if there is a problem
  const double EPSS = 1.0e-13;
  const int MR = 8;
  const int MT = 10;
  const int MAXIT = (MR*MT);
  
  int iter, j;
  double abx, abp, abm, err, fm;
  complex<double> dx, x1, b, d, f, g, h, sq, gp, gm, g2;
  static const double frac[MR+1] = {0.0,0.5,0.25,0.75,0.13,0.38,0.62,0.88,1.0};
  
  for(iter=1; iter<=MAXIT; iter++)
    {
      *its=iter;
      b=a[m];
      err=abs(b);
      d=f=complex<double>(0.0,0.0);
      abx=abs(*x);
      
      for(j=m-1;j>=0;j--)
	{
	  f=(*x)*f+d;
	  d=(*x)*d+b;
	  b=(*x)*b+a[j];
	  err=abs(b)+abx*err;
	}
      
      err*=EPSS;
      
      if(abs(b)<=err) return false;
      g=d/b;
      g2=g*g;
      h=g2-(2.0*(f/b));
      fm=double(m);
      sq=sqrt((fm-1.0)*(fm*h-g2));
      gp=g+sq;
      gm=g-sq;
      abp=abs(gp);
      abm=abs(gm);
      if(abp<abm) gp=gm;
      dx=(FMAX(abp,abm) > 0.0 ? (fm/gp) : polar(1.0+abx,double(iter)));
      x1=(*x)-dx;
      if (x->real() == x1.real() && x->imag() == x1.imag()) return false;
      if(iter%MT) *x=x1;
      else *x=(*x)-frac[iter/MT]*dx;
    }
  cerr << "WARNING IN zroots: Too many iterations in Laguer at step " << s << endl;
  return true;
  
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::FMAX
//		Returns the larger of the two inputs
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


double FMAX(double f1, double f2)
{
  if(f1>f2) return f1;
  else return f2;
}

//////////////////////////////////////////////////////////////////////////
//
//
//  zr::zroots
//    Driver function for laguer - Finds all the roots of the polynomial 
//    of order m given in a[m+1], optionally polishes them, and then 
//    sorts them in order of increasing real components.
//
//
//////////////////////////////////////////////////////////////////////////


bool zroots(complex<double> a[], int m, complex<double> roots[], int polish, string s)
{
  const double EPS = 2.0e-14;
  const int MAXM = 100;
  
  bool flag=false;
  
  int i,its,j,jj;
  complex<double> x,b,c,ad[MAXM];
	
  for (j=0;j<=m;j++) ad[j]=a[j];
  for(j=m;j>=1;j--)
    {
      x=complex<double>(0.0,0.0);
      flag=flag || laguer(ad,j,&x,&its, s);
      if(abs(x.imag()) <= 2.0*EPS*abs(x.real())) x=complex<double>(x.real(),0.0);
      roots[j]=x;
      b=ad[j];
      for(jj=j-1;jj>=0;jj--)
	{
	  c=ad[jj];
	  ad[jj]=b;
	  b=x*b+c;
	}
    }
  if(polish)
    for (j=1;j<=m;j++)
      flag=flag || laguer(a,m,&roots[j],&its, s);
  
  //  if (s>=0)  always sort
  //{
  for(j=2;j<=m;j++)
    {
      x=roots[j];
      for(i=j-1;i>=1;i--)
	{
	  if (roots[i].real()<=x.real()) break;
	  roots[i+1]=roots[i];
	}
      roots[i+1]=x;
    }
      //}

  return flag;
}
/*
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::SolveQuartic
//		Returns the area of the trapezium defined by the points (x1,0), (x1, y1), (x2,y2), (x2,0)
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

vector<complex<double> > zr::SolveQuartic(vector<complex<double> > a)
{
	if(int(a.size()) > 5)
	{
		cout << "The equation you are trying to solve has an order greater than 4." << endl;
		exit(1);
	}
	else if(int(a.size()) < 5)
	{
		for (int i=0; i<5-int(a.size());i++) a.push_back(complex<double>(0.0,0.0));
	}
	
	complex<double> alpha, beta, gamma;
	complex<double> P, Q, U, V, y;
	complex<double> A, B, C, D, E;
	complex<double> a2, a3, a4, b2, b3, b4, al2, al3;
	complex<double> z1, z2, z3, z4, z5, z;
	vector<complex<double> > result;

	A = a[4]; B = a[3]; C = a[2]; D = a[1]; E = a[0];
	
	a2 = A*A;
	a3 = A*a2;
	a4 = A*a3;
	
	b2 = B*B;
	b3 = B*b2;
	b4 = B*b3;
		
	alpha = complex<double>(-3.0,0.0)*b2/(complex<double>(8.0,0)*a2) + C/A;
	beta = b3/(complex<double>(8.0,0.0)*a3) - B*C/(complex<double>(2.0,0.0)*a2) + D/A;
	gamma = complex<double>(-3.0,0.0)*b4/(complex<double>(256.0,0.0)*a4) + C*b2/(complex<double>(16.0,0.0)*a3) - B*D/(complex<double>(4.0,0.0)*a2) + E/A;
	
	al2 = alpha*alpha;
	al3 = alpha*al2;
	
	P = al2/complex<double>(-12.0,0.0) - gamma;
	Q = al3/complex<double>(-108.0,0.0) + alpha*gamma/complex<double>(3.0,0.0) - beta*beta/complex<double>(8.0,0.0);
	
	U = complex<double>(( complex<double>(Q/complex<double>(-2.0,0.0) + sqrt(Q*Q/complex<double>(4.0,0.0) + P*P*P/complex<double>(27.0,0.0))) ,(1.0/3.0)));
	
	if (U==complex<double>(0.0,0.0))
	{
		V = -complex<double>(pow(complex<double>(Q),(1.0/3.0)));
	}
	else
	{
		V = P/(complex<double>(-3.0,0.0)*U);
	}
	
	y = complex<double>(-5.0/6.0,0.0)*alpha + U + V;
	
	z1 = B/(complex<double>(-4.0,0.0)*A);
	z2 = sqrt(alpha + complex<double>(2.0,0.0)*y);
	z3 = complex<double>(3.0,0.0)*alpha + complex<double>(2.0,0.0)*y;
	z4 = complex<double>(2.0,0.0)*beta/z2;
	
	z5 = sqrt(complex<double>(-1.0,0.0)*(z3+z4));
			
	//ps pt
	
	z = z1 + (z2 + z5)/complex<double>(2.0,0.0);
	result.push_back(z);
	
	//ps mt
	
	z = z1 + (z2 - z5)/complex<double>(2.0,0.0);
	result.push_back(z);
	
	z5 = sqrt(complex<double>(-1.0,0.0)*(z3-z4));
	
	//ms pt
	
	z = z1 + (-z2 + z5)/complex<double>(2.0,0.0);
	result.push_back(z);
	
	//ms mt
	
	z = z1 + (-z2 - z5)/complex<double>(2.0,0.0);
	result.push_back(z);
	
	return result;
	
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::TrapArea
//		Returns the area of the trapezium defined by the points (x1,0), (x1, y1), (x2,y2), (x2,0)
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

double zr::TrapArea(double x1, double y1, double x2, double y2)
{	
	return (x2-x1)*(y1 + 0.5*(y2-y1));
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::TrapInt
//		Returns the area under the points defined by y using the trapezium rule
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//For two vectors with x and y

double zr::TrapInt(vector<double> x, vector<double> y)
{
	int i, Size = x.size();
	double Total;
	
	if(Size!=int(y.size()))
	{
		cout << "ERROR IN zroots: Integration vectors x and y do not have the same number of elements." << endl;
		exit(1);
	}
	
	for(i=1;i<Size;i++)
	{
		Total+=TrapArea(x[i-1],y[i-1],x[i],y[i]);
	}
	
	return Total;
}

//For a complex list with x=Re(z) and y=Im(z)

double zr::TrapInt(list<complex<double> > z)
{
	double Total, x1, y1, x2, y2;
	list<complex<double> >::iterator i;
		
	for(i=z.begin();i!=z.end();i++)
	{
		x1=(*i).real();
		y1=(*i).imag();
		i++;
		x2=(*i).real();
		y2=(*i).imag();	
		if (i!=z.end())
		{
			Total+=TrapArea(x1,y1,x2,y2);
		}
		i--;
	}
	
	return Total;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//
//	zr::PeakFind
//		Returns the x position of the peak of the quadratic that passes through points 0,1 and 2
//
//
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

double zr::PeakFind(double x0, double y0, double x1, double y1, double x2, double y2)
{
	double yd0, yd1, yd2;
	
	yd0 = y0*(x1-x2);
	yd1 = y1*(x0-x2);
	yd2 = y2*(x0-x1);
	
	return 0.5*(yd0*(x1+x2) - yd1*(x0+x2) + yd2*(x0+x1))/(yd0-yd1+yd2);
	
}

*/
