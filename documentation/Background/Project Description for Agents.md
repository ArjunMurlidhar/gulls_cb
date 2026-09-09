# Circumbinary Planet Predictions

The aim of this project is to predict the microlensing yield and sensitivity to circumbinary planet systems using a modified version of gulls. This code (gulls_cb) is going to be that modified version that will run the simulation to find circumbinary planet predictions.

## Aim

 The broad goal of this project is to understand the following in the context of the Roman microlensing survey:
 - For what fraction of binary star events do we expect to see additional planet perturbations assuming some planet dist.
- Which regions of CB planet parameter space are we most sensitive to and what kind of binary hosts will we find?
- What fraction of planet detections will actually have binary star hosts?
- What should our modelling strategy be? Is it worth developing different pipelines for different types of circumbinary detections?
- How many circumbinary planets will Roman detect?

## Methodology

### Circumbinary planet simulations

We will use gulls_general for these simulations. We will only input planet files with a single planet. So gulls_general will produce events due to single-star-planet systems and planets in binary star systems. We are not concerned with planets orbiting a single star with a wide binary companion(S-type circumbinary planets). We only want to assess the detectability of stable P-type circumbinary planets where the planet orbits both stars in a closer binary system. 

### Circumbinary Detection Criteria

For small binary separations, if the planet is not in a resonant configuration (not on the critical curve of the binary), the caustics of the circumbinary can be approximated as individual binary and shifted planet caustics. For wider binaries, this is true only if the planet is much further away from the binary critical curve, but even then, the agreement is not exact. 

We can define our detection criteria as a chi-squared threshold to detect both binary and planetary perturbations in this separable case. For resonant or overlapping caustics, we can say that the circumbinary will be detectable if the perturbation due to the smaller of the two caustic components is detectable.

## Light curve generation and fitting

For each circumbinary planet event, we will need to generate two binary lens light curves - one for a system that only has the binary stars, and one for a system where the planet orbits a single star with the combined mass of the binary located at the center of mass of the binary star system (both for the same source trajectory). The parameters of this planet are shifted with respect to the actual circumbinary planet to ensure the planetary caustic overlaps with the planet component of the circumbinary caustic (see below for the exact transformation).

These two light curves are fit with single lens models (PSPL or FSPL) and the chi-squared values for both the binary star light curve and the planet light curve are noted. In post-processing, a chi-squared cut is applied to determine if both the binary star light curve feature and planet light curve feature are detected to determine if the circumbinary system was detected.

**We will need modify the light curve generator and light curve fitting module of gulls_general to implement this.**

## Shifted planet position

Luhn et al 2016: "Caustic Structures and Detectability of Circumbinary Planets in Microlensing" showed that the position of the planetary component of the circumbinary caustic can be reproduced by finding the mass weighted average of the positions of the planetary caustics produced by the planet orbiting each of the two stars in the binary individually. The code below implements this logic to find the shifted position of the planet:

```
#Function to calculate planet offset required to match the planetary part of the circumbinary caustic

def calculate_planet_offset(s3, q3, psi_deg, s2, q2):

	psi = np.deg2rad(psi_deg)
	
	  
	
	# Masses normalized so that total binary mass = 1
	
	m1 = 1.0 / (1.0 + q2)
	
	m2 = q2 * m1
	
	m3 = q3 * (m1 + m2)
	
	  
	
	# Lens positions (binary along x, planet offset by s3 at angle psi)
	
	z1x = -q2 * s2 / (1.0 + q2)
	
	z2x = s2 / (1.0 + q2)
	
	z3x = s3 * np.cos(psi)
	
	z3y = s3 * np.sin(psi)
	
	  
	
	#Position of planet wrt mass 1 and mass 2
	
	pA = (z3x - z1x, z3y)
	
	pB = (z3x - z2x, z3y)
	
	alphaA = np.arctan2(pA[1], pA[0])
	
	alphaB = np.arctan2(pB[1], pB[0])
	
	sA = np.sqrt(pA[0]**2 + pA[1]**2)
	
	sB = np.sqrt(pB[0]**2 + pB[1]**2)
	
	qA = m3/m1
	
	qB = m3/m2
	
	#position of planet caustic due to mass 1 and mass 2 RELATIVE TO THE STARS
	
	rA = ((1-qA)/(1+qA))*(sA - (1./sA))
	
	rB = ((1-qB)/(1+qB))*(sB - (1./sB))
	
	#Positions in our coordinate system
	
	rc1 = (z1x + rA*np.cos(alphaA), rA*np.sin(alphaA))
	
	rc2 = (z2x + rB*np.cos(alphaB), rB*np.sin(alphaB))
	
	#print(rc1, rc2)
	
	  
	
	#Position of circumbinary planet caustic in our coordinate system
	
	rcb = (1./(1+q2))*np.array(rc1) + (q2/(1+q2))*np.array(rc2)
	
	#Since we are placing the single star at the origin, the caustic position relative to the star is the same as the caustic position in our coordinate system
	
	rcb_norm = np.sqrt(rcb[0]**2 + rcb[1]**2)
	
	c = rcb_norm*(1 + q3)/(1 - q3)
	
	if s3 < 1:
	
	splanet = np.abs((c - np.sqrt(c**2 + 4))/2)
	
	psi_new = np.arctan2(-rcb[1], -rcb[0])
	
	else:
	
	splanet = (c + np.sqrt(c**2 + 4))/2
	
	psi_new = np.arctan2(rcb[1], rcb[0])
	
	#print(psi_new)
	
	if psi_new < 0:
	
	psi_new += 2*np.pi
	
	psi_new_deg = np.rad2deg(psi_new)
	
	return splanet, psi_new_deg
```