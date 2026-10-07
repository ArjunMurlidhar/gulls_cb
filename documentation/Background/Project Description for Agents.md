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

The caustics and light curves of a circumbinary planet can be approximated as a superpositon of a binary star lens and an effective single-star-planet lens. We can define our detection criteria as a chi-squared threshold to detect both binary and planetary perturbations in this separable case. 

## Light curve generation and fitting

For each circumbinary planet event, we will need to generate two binary lens light curves - one for a system that only has the binary stars, and one for the effective single-star-planet lens (see below for the exact transformation).

These two light curves are fit with single lens models (PSPL or FSPL) and the chi-squared values for both the binary star light curve and the planet light curve are noted. In post-processing, a chi-squared cut is applied to determine if both the binary star light curve feature and planet light curve feature are detected to determine if the circumbinary system was detected.

**We will need modify the light curve generator and light curve fitting module of gulls_general to implement this.**

## Superposition Principle

The circumbinary system can be approximated as a superposition of two binary lens systems:

1) Binary star system without the planet

2) An effective single-star-planet system where the star has a mass equal to the combined mass of the two binary stars

The parameters of the effective single-star-planet system can be calculated as follows. The separation between the planet and effective host is calculated by matching the total shear at the planet position to the shear due to the effective host at the planet position. The position of the effective host is found such that the caustic location of this system matches the planetary component of the circumbinary caustic. The location of this planetary component is such that a source at this caustic produces an image at the location of the planet under lensing due to the binary stars. 

### Recipe for calculating the superposition:

Assuming that the circumbinary parameters are defined according to the defined conventions (in units of the stellar binary Einstein ring), define: $\epsilon_1 = 1/(1+q_b)$, $\epsilon_2 = q_b/(1+q_b)$, $z_1 = -\epsilon_2 s_b$, $z_2 = \epsilon_1 s_b$, and $z_p = s_p e^{i\psi}$.

1. Evaluate host deflection and shear at the planet position at $z_p$ and pass effective parameters to VBM (in barycentric coordinates,  normalized to Einstein ring for the total mass of the effective system).

$$
\zeta_0 = z_p - \sum_{j=1}^{2} \frac{\epsilon_j}{\bar{z}_p - \bar{z}_j}, \qquad \gamma_p = \sum_{j=1}^{2} \frac{\epsilon_j}{(\bar{z}_p - \bar{z}_j)^2}, \qquad g = |\gamma_p|, \quad \psi_{\text{eff}} = \frac{1}{2}\arg \gamma_p \quad (\text{closest to } \psi).
$$

Parameters that can be passed to VBM (in VBM coordinate system):


$$\boxed{s = \frac{1}{\sqrt{(1+q_p)g}}, \qquad q = q_p, \qquad \rho_{\text{VB}} = \frac{\rho}{\sqrt{1+q_p}}.}$$


```python
def effective_parameters(sb, qb, sp, qp, psi):
    """Angles: radians. Lengths: Einstein radius of M1+M2.
    qb = M2/M1; qp = mp/(M1+M2).
    """
    m1, m2 = 1/(1 + qb), qb/(1 + qb)
    zp = sp * np.exp(1j*psi)
    d1, d2 = np.conj(zp + m2*sb), np.conj(zp - m1*sb)

    caustic_reference = zp - m1/d1 - m2/d2
    gamma = m1/d1**2 + m2/d2**2
    if abs(gamma) == 0:
        raise ValueError("Zero shear has no finite effective separation.")
    s_eff = abs(gamma)**-0.5 #This is still in units of the binary lens Einstein ring
    psi_eff = np.angle(gamma)/2
    print("psi_eff", np.rad2deg(psi_eff))
    psi_eff += np.pi*np.round((psi - psi_eff)/np.pi)

    host_position = (caustic_reference - np.exp(1j*psi_eff)*(s_eff - 1/s_eff)) #In units of binary lens Einstein ring
    return s_eff, qp, psi_eff, host_position
```
2. Given a source trajectory $\zeta(t) = y_1(t) + iy_2(t)$, convert it to the barycentric frame of the effective single-star-planet lens in the standard VBM geometry of a binary lens, and compute magnification using BinaryMag2. 


$$\boxed{y(t) = \frac{e^{-i\psi_{\text{eff}}}[\zeta(t) - \zeta_0]}{\sqrt{1+q_p}} + \frac{s - s^{-1}}{1+q_p}, \qquad \tilde{y}_1 = \text{Re}[y(t)], \quad \tilde{y}_2 = \text{Im}[y(t)].}$$


Here, $\zeta(t)$ and $\zeta_0$ are defined in units of the binary Einstein ring and $s$ is defined in units of the Einstein ring of the single-star-planet system. $\tilde{\zeta}(t)= \tilde{y}_1 + i\tilde{y}_2$ is the source position passed to BinaryMag2 to calculate the magnification. The python implementation of this can be found below:

```python
def to_vbm_frame(z, s_eff, q, psi_eff, host_position):
    #Rotate from our coordinate system to the VBM coordinate system, shift origin to the barycenter, and scale by the total mass Einstein radius
    z_vbm = 1/np.sqrt(1+q)*(np.exp(-1j*psi_eff)*(z - host_position) + q*s_eff/(1+q))
    return z_vbm

def calculate_planet_mag(y1, y2, s_eff, q, psi_eff, host_position, rho):
    vbm = VBMicrolensing.VBMicrolensing()
    rho_vbm = rho/np.sqrt(1+q)
    z = y1 + 1j*y2
    z_vbm = to_vbm_frame(z, s_eff, q, psi_eff, host_position)
    y1_vbm = z_vbm.real
    y2_vbm = z_vbm.imag
    mag = vbm.BinaryMag2(s_eff, q, y1_vbm, y2_vbm, rho_vbm)
    return mag
```

3. Magnifications for the stellar binary system can be computed by simply removing the planet. This does not require any rescaling of parameters as long as the recommended coordinate system and parameter convention is followed.

