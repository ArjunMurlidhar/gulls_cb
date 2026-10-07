---
abstract: |
  The *Wide Field InfraRed Survey Telescope* (*WFIRST*) is the next NASA
  astrophysics flagship mission, to follow the *James Webb Space
  Telescope* (*JWST*). The *WFIRST* mission was chosen as the
  top-priority large space mission of the 2010 astronomy and
  astrophysics decadal survey in order to achieve three primary goals:
  to study dark energy via a wide-field imaging survey, to study
  exoplanets via a microlensing survey, and to enable a guest observer
  program. Here we assess the ability of the several *WFIRST* designs to
  achieve the goal of the microlensing survey to discover a large sample
  of cold, low-mass exoplanets with semimajor axes beyond roughly one
  AU, which are largely impossible to detect with any other technique.
  We present the results of a suite of simulations that span the full
  range of the proposed *WFIRST* architectures, from the original design
  envisioned by the decadal survey, to the current design, which
  utilizes a 2.4-m telescope donated to NASA. By studying such a broad
  range of architectures, we are able to determine the impact of design
  trades on the expected yields of detected exoplanets. In estimating
  the yields we take particular care to ensure that our assumed Galactic
  model predicts microlensing event rates that match observations,
  consider the impact that inaccuracies in the Galactic model might have
  on the yields, and ensure that numerical errors in lightcurve
  computations do not bias the yields for the smallest mass exoplanets.
  For the nominal baseline *WFIRST* design and a fiducial planet mass
  function, we predict that a total of ${\sim}1400$ bound exoplanets
  with mass greater than ${\sim}0.1~M_{\oplus}$ should be detected,
  including ${\sim}200$ with mass ${\lesssim}3~M_{\oplus}$.
  *WFIRST* should have sensitivity to planets with mass down to
  ${\sim}0.02~M_{\oplus}$, or roughly the mass of Ganymede.
author:
- Matthew T. Penny
- B. Scott Gaudi
- Eamonn Kerins
- Nicholas J. Rattenbury
- Shude Mao
- Annie C. Robin
- Sebastiano Calchi Novati
bibliography:
- libraryshort.bib
- apj-jour.bib
date: 2026-09-14
title: "Predictions of the *WFIRST* Microlensing Survey I: Bound Planet
  Detection Rates"
---

# Introduction {#intro}

The study of the demographics of exoplanets, the end result of the
planet formation process, has entered a statistical age. Large samples
of transiting planets from *Kepler* [e.g., @Thompson2018], massive
planets at small to moderate separations from ground-based radial
velocity surveys of planetary systems in the solar neighborhood [e.g.,
@Udry2007; @Winn2015], and direct imaging studies of young planets at
large separations [e.g., @Bowler2016], are beginning to reveal the
complex distribution of exoplanets as a function of mass and separation
from their host stars, and the properties of the host stars themselves.

Data from the *Kepler* mission has revealed a sharp rise in the
occurrence rate of hot and warm planets as radius decreases down to
about $2.8R_{\earth}$, before leveling off [e.g.,
@Howard2010; @Fressin2013]. Precise spectroscopic measurements of
*Kepler*'s super Earth hosts has revealed a radius dichotomy between
large and small super Earths [@Fulton2017] that is likely due to
atmospheric stripping [@Owen2017]. At large orbital distances
${\gtrsim}10$ AU, direct imaging searches have found young, massive
planets to be present, but rare [e.g.,
@Nielsen2010; @Chauvin2015; @Bowler2015]. However, there remains a large
area of the exoplanet parameter space -- orbits beyond ${\sim}1$ AU and
masses less than that of Jupiter -- that remains relatively unexplored
by transit, radial velocity, and direct imaging techniques.

Indeed, if every planetary system resembled our own, only a handful of
planets would have been discovered by the radial velocity, transit, or
direct imaging techniques to date. This fact begs the question: Is our
solar system architecture rare? If so, why?

To obtain a large sample of exoplanets beyond 1 AU and across a large
range of masses requires a different technique. Gravitational
microlensing enables a statistical survey of exoplanet populations
beyond $1$ AU, because its sensitivity peaks at the Einstein radius of
its host stars [@Mao1991; @Gould1992; @Bennett1996]. For stars along the
line of sight to the Galactic bulge (where the microlensing event rate
is highest) the physical Einstein radius is typically $2$--$3$ AU [see,
e.g., the review of @Gaudi2012]. Thanks to the fact that microlensing is
sensitive directly to a planet's mass and not its light or effect on a
luminous body, the techniques sensitivity extends out to all orbital
radii beyond ${\sim}1$ AU [@Bennett2002].

Perhaps the most important reason to perform a large exoplanetary
microlensing survey is that it opens up a large new region of parameter
space. The history of exoplanet searches has been one of unexpected
discoveries. At every turn, when a new area of parameter space has been
explored, previously unexpected planetary systems have been found. This
process began with the pulsar planets [@Wolszczan1992] and relatively
short-period giant planets discovered by the first precision radial
velocity searches sensitive to
planets [@Mayor1995; @Campbell1988; @Latham1989]. As radial velocity
surveys' sensitivities and durations grew, highly eccentric massive
planets and low mass Neptunes and "Super Earth" planets were
discovered [e.g., @Naef2001; @Butler2004; @Rivera2005]. When originally
conceived, and with the Solar System as a guide, the *Kepler* mission
aimed to detect potentially habitable Earth-sized planets in
${\sim}1$ AU orbits around Solar-like stars [@Borucki2003]. Were all
exoplanet systems like our own, *Kepler* would have found few or no
planets [@Burke2015], and those that it did would have been at the limit
of its signal-to-noise ratio. This result was obviously preempted by the
discovery of hot Jupiters, which demonstrated conclusively that *not*
all planetary systems have architectures like our own. *Kepler* itself
has gone on to discover thousands of planetary systems very unlike ours,
including tightly-packed multiplanet systems [e.g., @Lissauer2011] and
circumbinary planets [e.g., @Doyle2011], to name but a few examples.
Even moving into unprobed areas of the host mass parameter space has
revealed unexpected systems such as TRAPPIST-1 [@Gillon2016] and
KELT-9 [@Gaudi2017]. Direct imaging searches have revealed young, very
massive planets that orbit far from their hosts [e.g., @Chauvin2004],
the most unusual (from our solar-system-centric viewpoint) being the
four-planet system around HR8799 [@Marois2008; @Marois2010].

Despite finding the planetary system that is arguably most similar to
our own [the OGLE-2006-BLG-109 Jupiter-Saturn analogs
@Gaudi2008; @Bennett2010], ground-based microlensing surveys too have
discovered unexpected systems. For example, microlensing searches have
found several massive planets around M-dwarf stars [e.g. @Dong2009a]
that appear to at least qualitatively contradict the prediction of the
core accretion theory that giant planets should be rare around low-mass
stars [@Laughlin2004]. Measurements of planet occurrence rates from
microlensing also superficially appear to contradict previous radial
velocity results, although a more careful analysis indicates that the
microlensing and radial velocity results are
consistent [@Montet2014; @Clanton2014; @Clanton2014a]. Other notable
microlensing discoveries include circumbinary planets [@Bennett2016],
planets on orbits of ${\sim}1$--$10$ AU around components of moderately
wide binary stars [e.g., @Gould2014; @Poleski2014], planets on wide
orbits comparable to Uranus and Neptune [e.g., @Poleski2017], and
planets orbiting ultracool dwarfs [e.g. @Shvartzvald2017].

Having spent over a decade conducting two-stage survey-plus-follow-up
planet searches [see, e.g., @Gould2010 for a review], microlensing
surveys have entered a second generation mode, that relies only on
survey observations. The OGLE [@Udalski2015-ogleiv], MOA [@Sako2007] and
three KMTNet telescopes [@Kim2016] span the southern hemisphere and
provide continuous high-cadence microlensing observations over tens of
square degrees every night that weather allows. Such global, second
generation, pure survey-mode microlensing surveys will enable the
initial promise of microlensing to provide the large statistical samples
of exoplanets necessary to study demographics [@Henderson2014-kmt], and
have begun to deliver [@Shvartzvald2016; @Suzuki2016]. It has long been
recognized [e.g., @Bennett2002; @Beaulieu2008; @Gould2009ds] that
exoplanet microlensing surveys are best conducted from space, thanks to
the greater ability to resolve stars in crowded fields and to
continuously monitor fields without interruptions from weather or the
day-night cycle.

*WFIRST* [@Spergel2015] is a mission conceived of by the 2010 decadal
survey panel [@nwnh] as its top priority large astrophysics mission. It
combines mission proposals to study dark energy with weak lensing,
baryon acoustic oscillations, and supernovae [Joint Dark Enegry
Mission-Omega, JDEM-Omega, @Gehrels2010], with a gravitational
microlensing survey [Microlensing Planet Finder, @Bennett2010mpf], a
near infrared sky survey [Near Infrared Sky Surveyor, @Stern2010] and a
significant guest observer component [@nwnh]. The later addition of a
high-contrast coronagraphic imaging and spectroscopic technology
demonstration instrument [@Spergel2015] addresses a top medium scale
2010 decadal survey priority as well. In this paper we examine only the
microlensing survey component of the mission.

The structure of the paper is as follows. In
[2](#wfirstintro){reference-type="ref+label" reference="wfirstintro"} we
describe the *WFIRST* mission, and each of its design stages. In
[3](#sims){reference-type="ref+label" reference="sims"} we describe the
simulations we have performed.
[4](#baselineyield){reference-type="ref+label"
reference="baselineyield"} presents the yields of the baseline
simulations, while [5](#tradeoffs){reference-type="ref+label"
reference="tradeoffs"} considers the effects of various possible changes
to the mission design. [6](#discuss){reference-type="ref+label"
reference="discuss"} discusses the uncertainties that affect our results
and how they might be mitigated by future observations, modeling, and
simulations. [7](#conclusions){reference-type="ref+label"
reference="conclusions"} gives our conclusions.

# *WFIRST* {#wfirstintro}

## Goals of the *WFIRST* Microlensing Survey {#goals}

A primary science objective of the *WFIRST* mission is to conduct a
statistical census of exoplanetary systems, from 1 AU out to
free-floating planets, including analogs to all of the Solar System
planets with masses greater than Mars, via a microlensing survey. It is
in the region of ${\sim}1$--$10$ AU that the microlensing technique is
most sensitive to planets over a wide range of
masses [@Mao1991; @Gould1992], and where other planet detection
techniques lack the sensitivity to detect low-mass planets within
reasonable survey durations or present-day technological limits.
However, the $1$--$10$ AU region is perhaps the most important region of
protoplanetary disks and planetary systems for determining their
formation and subsequent evolution, and can have important effects on
the habitability of planets.

The enhancement in surface density of solids at the water ice line,
${\sim}1.5$--$4$ AU from the star, is thought to be critical for the
formation of giant planets [@Hayashi1981; @Ida2004; @Kennedy2006].
Nevertheless, all stars do not produce giant planets that survive [e.g.,
@Winn2015]. It remains to be seen whether this is due to inefficient
production of giant planets, or a formation process that is ${\sim}100$%
efficient followed by an effective destruction mechanism, such as
efficient disk migration [e.g., @Goldreich1980], or ejection or host
star collisions caused by dynamics [e.g. @Rasio1996]. In the core
accretion scenario [e.g., @Goldreich1973; @Pollack1996], runaway gas
accretion onto protoplanet cores to produce giant planets is an
inevitability, *if* the cores grow large enough before the gas
dissipates from the protoplanetary disk [@Mizuno1980]. If core growth
rate is the rate limiting step in the production of giant planets, and
the process is indeed inefficient, then we can expect a population of
"failed cores" of various masses with a distribution that peaks near the
location of the ice line. Conversely, if giant planet formation and
subsequent destruction is efficient, we can expect the formed giant
planets to clear their orbits of other bodies, and thus would expect to
see a deficit of low mass planets in *WFIRST*'s region of sensitivity.

It is clear that planetary systems are not static, and the orbits of
planets can evolve during and after the planet formation process, first
via drag forces while the protoplanetary disk is in place [@Lin1996],
and subsequently by $N$-body dynamical processes once the damping effect
of the disk is removed [@Rasio1996]. In addition to rearranging the
orbits of planets that remain bound, the chaotic dynamics of multiplanet
systems can result in planets being ejected [e.g., @Safronov1972]. The
masses and number of ejected planets from the system will be determined
by the number of planets in their original systems, their masses and
orbital distribution [e.g,
@Papaloizou2001; @Juric2008; @Chatterjee2008; @Barclay2017]. So, the
mass function of ejected, or free-floating, planets can be an important
constraint on the statistics of planetary systems as a whole. Because
they emit very little light, only microlensing observations can be used
to detect rocky free-floating planets. For masses significantly below
Earth's, only space-based observations can provide the necessary
combination of photometric precision, cadence, and total number of
sources monitored in order to collect a significant sample of events.

For both bound and free-floating objects it is valuable to extend the
mass sensitivity of an exoplanet survey down past the characteristic
mass scales of planet formation theory, where the growth behavior of
forming planets changes. This is particularly the case for boundaries in
mass between low and high growth rates, as these should be the locations
of either pile-ups or deficits in the mass function, depending on the
sense of the transition. In the core accretion scenario of giant planet
formation, moving from high to low masses, characteristic mass scales
include the critical core mass for runaway gas accretion at
${\sim}10M_{\earth}$ [@Mizuno1980], the isolation mass of planetary
embryos at ${\sim}0.1M_{\earth}$ [@Kokubo2002], and the transition core
mass for pebble accretion at ${\sim}0.01M_{\earth}$ [@Lambrechts2012].
The detection of features due to these characteristic mass scales would
be strong evidence in support of current planet formation theory.
Additionally, a statistical accounting of planets on wider orbits more
generally will be a valuable test of models of planet formation
developed to explain the large occurrence rate of super-Earths closer
than 1 AU.

An estimate of the occurrence rate of rocky planets in the habitable
zones [e.g., @Kasting1993; @Kopparapu2013] of solar-like stars,
$\eta_{\oplus}$, is an important ingredient for understanding the
origins and evolution of life, and the uniqueness of its development on
Earth. However, it is precisely this location that it is both hardest to
detect ${\sim}1M_{\earth}$ planets around ${\sim}1M_{\odot}$ stars,
while also remaining tantalizingly achievable. Tiny signals recurring on
approximately year timescales mean that transit, radial velocity, and
astrometric searches must run for multiple years to make robust
detections. Only the transit technique has demonstrated the necessary
precision to date, and even so, *Kepler* fell just short of the mission
duration necessary to robustly measure $\eta_{\oplus}$ [@Burke2015].
Direct imaging of habitable exoplanets will require significant
technological advances [e.g., @Mennesson2016; @Bolcar2017; @Wang2018],
several of which *WFIRST*'s coronagraphic instrument will demonstrate,
in order to reach the contrast and inner working angles required, and
the observing time required to perform a blind statistical survey to
measure $\eta_{\oplus}$ may be prohibitively expensive. The typical
inner sensitivity limit for a space-based microlensing survey, which is
proportional to the host mass $M^{1/2}$, crosses the habitable zone,
which scales as ${\sim}M^{3.5}$, at ${\sim}1M_{\odot}$. Nevertheless the
detection efficiency for low-mass-ratio planets inside the Einstein ring
($R_{\rm E}\sim 3$ AU) is very small, and solar-mass stars make up only
a small fraction of the lens population, so large, long-duration
microlensing surveys from space are required to robustly measure
$\eta_{\oplus}$ with microlensing. In all likelihood, no one technique
will prove sufficient, and it will be necessary to combine measurements
from multiple techniques to be confident in the accuracy of
$\eta_{\oplus}$ determinations. If the habitable zone is extended
outward [e.g., @Seager2013], by volcanic outgassing of of
H$_2$ [@Ramirez2017] or some other process, the number of habitable
planets space-based microlensing searches are sensitive to increases
significantly.

Each of the goals described above can be addressed in whole or in part
by studying the statistics of a large sample of planets with orbits in
the range of $1$--$10$ AU, and a similar sample of unbound planets. Such
a sample can only be delivered by a space-based microlensing survey.
Astrometry from *Gaia* can be used to discover a large sample of giant
planets in similar orbits, but it will not have the sensitivity to probe
below ${\sim}30M_{\earth}$ [@Perryman2014]. Space-based transit surveys
have sensitivity to very small, and low-mass planets, but would be
required to observe for decades to cover the same range of orbital
separations as does microlensing. Ground-based microlensing searches
have sensitivity to low-mass exoplanets down to ${\sim}1M_{\earth}$, as
recently demonstrated by @Bond2017 and @Shvartzvald2017, but are limited
from gathering large samples of such planets or extending their
sensitivity to masses significantly smaller than this by a combination
of the more limited photometric precision possible from the ground, the
larger angular diameter of source stars for which high precision is
possible, and the lower density of such sources on the sky.

A critical element in measuring the mass function of planets from
microlensing events is actually measuring planets masses. The lightcurve
of a binary microlensing event alone only reveals information about the
mass *ratio* $q$, unless the event is long enough to measure the effect
of annual microlensing parallax on the lightcurve, or the event is
observed from two widely separated observers, e.g., a spacecraft such as
*Spitzer* [e.g., @Udalski2015-spitzer] or *Kepler* [see
@Henderson2016-k2c9 for a review]. It is also necessary to measure
finite source effects in the lightcurve, but this is routinely achieved
for almost all planetary microlensing events observed to date, and will
likely be possible for the majority of *WFIRST*'s planetary
events [e.g., @Zhu2014]. High resolution imaging enables an alternative
method to measure the host and planet mass. Over time, the source and
lens star involved in a microlensing event will separate, and the lens,
if bright enough will be detectable, either as an elongation in the
combined source-lens image, as a shift in the centroid of the pair as a
function of color, or if moving fast enough, the pair will become
resolvable [e.g., @Bennett2007]. The measured separation between the
stars, and the color and magnitude of the lens star can be combined with
the measurement of the event timescale to uniquely determine the mass of
the lens. A principle requirement of the *WFIRST* mission is the ability
to make these measurements routinely for most events. This is made
possible by the resolution achievable from space, and is also greatly
aided by the fainter source stars that space-based observations enable.
For *WFIRST* to make these measurements it is necessary that it observe
the microlensing fields over a time baseline of $4$ or more years.

In this paper we will only address *WFIRST*'s ability to measure the
mass function of bound planets. The challenges and opportunities to
detect free-floating planets, and planets in the habitable zone, differ
somewhat from those for the general bound planet population. We have
therefore elected to give them the full attention that they deserve in
subsequent papers, rather than provide only the limited picture that
would be possible in this paper.

## Evolution of the *WFIRST* Mission: Design Reference Missions, AFTA, and Cycle 7

The *WFIRST* mission is in the process of ongoing design refinement, and
has gone through four major phases so far. This paper presents analysis
of each of these missions, even though some of these designs are no
longer under active development. This is important for two reasons.
First, we are documenting the quantitative simulations that have
informed the *WFIRST* microlensing survey design process from the first
science definition team. Second, each design represents a internally
self consistent set of mission design parameters, that when evolved to a
new mission design necessarily captures the majority of covariance
between all of the possible design choices. These covariances are
difficult to account for in simulations that might aim to investigate
variations in individual parameters that by isolating their effects.

The first *WFIRST* design, the Interim Design Reference Mission (IDRM)
was based directly on the *WFIRST* mission proposed by the decadal
survey and described in the first *WFIRST* Science Definition Team's
(SDT) interim report [@Green2011]. This in turn was based on the design
for the JDEM-Omega mission [@Gehrels2010]. The IDRM consisted of an
unobstructed 1.3-m telescope with a $0.294$ deg$^2$ near-infrared
imaging channel with broadband filters spanning ${\sim}0.76-2.0$ $\mu$m,
including a wide $1-2$ $\mu$m filter for the microlensing survey, and
two slitless spectroscopic channels.

The final report of the first *WFIRST* SDT [@Green2012] presented two
Design Reference Missions (DRM1 and DRM2). DRM1 was an evolution of the
IDRM, adhering to the recommendation of the decadal survey to only use
fully developed technologies. It improved on the IDRM by increasing the
upper wavelength cutoff of the detectors to $2.4$ $\mu$m, and removing
the two spectroscopic channels. The detectors and prism elements were
added to the imaging channel to increase its field of view to
$0.377$ deg$^2$.

DRM2 was a design intended to reduce the cost of the mission. This was
done by reducing the size of the primary mirror to 1.1-m (in order to
fit onto a less costly launch vehicle). It also switched to a larger
format 4k$\times$`<!-- -->`{=html}4k detector to reduce the number of
detectors while increasing the field of view to $0.585$ deg$^2$, at the
cost of additional detector development. The larger field of view also
allowed the mission duration to be shortened to 3 years instead of 5.

The *WFIRST* design process was disrupted in 2012 when NASA was gifted
two $2.4$-m telescope mirrors and optical tube assemblies by another
government agency. The value of these telescopes to the *WFIRST* mission
was initially assessed in a report by @Dressler2012, and the mission
designed around one of the $2.4$-m telescopes was dubbed *WFIRST*-AFTA
(AFTA standing for Astrophysically Focussed Telescope Assets). A new SDT
was assembled to produce an *AFTA* DRM, which added a coronagraphic
instrument channel to the mission [@Spergel2013]. The design of the wide
field instrument (WFI) also changed, requiring a finer pixel scale to
sample the smaller point spread function (PSF) of the $2.4$-m telescope,
and hence a smaller field of view of $0.282$ deg$^2$. Unlike the
previous designs, the telescope has an obstructed pupil, so the PSF has
significant diffraction spikes that the previous versions did not. The
design also required a shorter wavelength cutoff of $2.0$ $\mu$m due to
concerns about the ability to operate the telescope at low temperature
required for $2.4 \mu$m observations. The final results of this design
process were presented by @Spergel2015.

*WFIRST* entered the formulation phase (phase A) in early 2016. The AFTA
design was adopted, and the mission reverted to its simpler naming of
*WFIRST*. Extensive design and testing work has been conducted since
formulation began. This includes a large amount of detector development,
validation of the ability of the telescope to operate cooled, redesign
of the wide field instrument, and consideration of various mission
descopes. Very recently, WFIRST ended into the second phase of mission
development (phase B).

The most significant update to the design affecting the microlensing
survey is a more pessimistic accounting of the observatory's slew time
performance compared to the AFTA design. Another important change was a
rotation of the elongated detector layout by 90$\degr$. While the
mission design continues to evolve, we present simulations here that
most closely match the Cycle 7 design, and so throughout the paper we
will refer to the design as *WFIRST* Cycle 7.

::: table*
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
|                             | IDRM              | DRM1              | DRM2              | AFTA                | ***WFIRST* Cycle 7**      |
+:============================+:=======:+:=======:+:=======:+:=======:+:=======:+:=======:+:========:+:========:+:===========:+:===========:+
| Reference                   | @Green2011        | @Green2012        | @Green2012        | @Spergel2015        | ---$^{1,2}$               |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Mirror diameter (m)         | 1.3               | 1.3               | 1.1               | 2.36                | **2.36**                  |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Obscured fraction (area, %) | 0                 | 0                 | 0                 | 13.9                | **13.9**                  |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Detectors                   | $7{\times}4$      | $9{\times}4$      | $7{\times}2$      | $6{\times}3$        | $\mathbf{6{\times}3}$     |
|                             | H2RG-10           | H2RG-10           | H4RG-10           | H4RG-10             | **H4RG-10**               |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Plate scale ("/pix)         | 0.18              | 0.18              | 0.18              | 0.11                | **0.11**                  |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Field of view (deg$^2$)     | 0.294             | 0.377             | 0.587             | 0.282               | **0.282**                 |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Fields                      | 7                 | 7                 | 6                 | 10                  | **7**                     |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Survey area (deg$^s$)       | 2.06              | 2.64              | 3.52              | 2.82                | **1.97**                  |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Avg. slew and settle Time   | 38                | 38                | 38                | 38                  | **83.1**                  |
| (s)                         |                   |                   |                   |                     |                           |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Orbit                       | L2                | L2                | L2                | Geosynchronous      | L2                        |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Total Survey length (d)     | 432               | 432               | 266               | 411$^{\ast\ast}$    | **432**                   |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Season length (d)           | 72                | 72                | 72                | 72                  | **72**                    |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Seasons                     | 6                 | 6                 | 3.7               | 6                   | **6**                     |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Baseline mission duration   | 5                 | 5                 | 3                 | 6                   | **5**                     |
| (yr)                        |                   |                   |                   |                     |                           |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Primary bandpass ($\mu$m)   | $1.0$--$2.0$      | $1.0$--$2.4$      | $1.0$--$2.4$      | $0.93$--$2.00$      | **0.93--2.00 (W149)**     |
|                             | (W149)            | (W169)            | (W169)            | (W149)              |                           |
+-----------------------------+-------------------+-------------------+-------------------+---------------------+---------------------------+
| Secondary bandpass ($\mu$m) | $0.74$--$1.0$     | $0.74$--$1.0$     | $0.74$--$1.0$     | $0.76$--$0.98$      | **0.76--0.98 (Z087)**     |
|                             | (Z087)            | (Z087)            | (Z087)            | (Z087)              |                           |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
|                             | W149    | Z087    | W169    | Z087    | W169    | Z087    | W149     | Z087     | **W149**    | **Z087**    |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Zeropoint$^{\ast}$ (mag)    | 26.315  | 25.001  | 26.636  | 24.922  | 25.990  | 24.367  | 27.554   | 26.163   | **27.615**  | **26.387**  |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Exposure time (s)           | 88      | 116     | 85      | 290     | 112     | 412     | 52       | 290      | **46.8**    | **286**     |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Cadence                     | 14.98   | 11.89   | 14.35   | 12.0 hr | 15.0    | 12.0 hr | 15.0 min | 12.0 hr  | **15.16     | **12.0 hr** |
|                             | min     | hr      | min     |         | min     |         |          |          | min**       |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Bias (counts/pix)           | 380     | 380     | 1000    | 1000    | 1000    | 1000    | 1000     | 1000     | **1000**    | **1000**    |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Readout noise$^{\star}$     | 9.1     | 9.1     | 7.6     | 4.2     | 9.1     | 9.1     | 8.0      | 8.0      | **12.12**   | **12.12**   |
| (counts/pix)                |         |         |         |         |         |         |          |          |             |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Thermal + dark$^{\dagger}$  | 0.36    | 0.36    | 0.76    | 0.76    | 0.76    | 0.76    | 1.30     | 0.05     | **1.072**   | **0.130**   |
| (counts/pix/s)              |         |         |         |         |         |         |          |          |             |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Sky background$^{\ddagger}$ | 21.48   | 21.54   | 21.53   | 21.48   | 21.52   | 21.50   | 21.47    | 21.50    | **21.48**   | **21.55**   |
| (mag/arcsec$^2$)            |         |         |         |         |         |         |          |          |             |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Sky background              | 2.78    | 0.79    | 3.57    | 0.77    | 1.99    | 0.45    | 3.28     | 0.89     | **3.43**    | **1.04**    |
| (counts/pix/s)              |         |         |         |         |         |         |          |          |             |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Error floor (mmag)          | 1.0     | 1.0     | 1.0     | 1.0     | 1.0     | 1.0     | 1.0      | 1.0      | **1.0**     | **1.0**     |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+
| Saturation$^{\mathsection}$ | 65.5    | 65.5    | 80      | 80      | 80      | 80      | 679      | 2037     | **679**     | **679**     |
| ($10^3$ counts/pix)         |         |         |         |         |         |         |          |          |             |             |
+-----------------------------+---------+---------+---------+---------+---------+---------+----------+----------+-------------+-------------+

\
**Notes:** Parameters listed in the table are those used in the main
simulations whose results are described in
Sections [4](#baselineyield){reference-type="ref"
reference="baselineyield"} and [5](#tradeoffs){reference-type="ref"
reference="tradeoffs"} and are not necessarily the same as described in
the relevant *WFIRST* reports. Where parameters are incorrect, the
impact they would have was judged to be too insignificant to justify a
repeated run of the simulations with the correct parameters (see text
for further justifications). For correct parameter values the reader
should refer to the appropriate Science Definition Team (SDT) report, or
the reference information currently listed on the *WFIRST* websites
below.\
$^1$<https://wfirst.gsfc.nasa.gov/science/WFIRST_Reference_Information.html>\
$^2$<https://wfirst.ipac.caltech.edu/sims/Param_db.html>\
$^{\ast}$Magnitude that produces $1$ count per second in the detector.\
$^{\star}$Effective readout noise after multiple non-destructive reads.
All values are inaccurate, as they depend on the chosen readout scheme.
However, the readout noise will not be larger than the correlated double
sampling readout noise of ${\sim}20$ e$^{-}$, which is still
sub-dominant relative to the combination of zodiacal light and blended
stars.\
$^{\dagger}$Sum of dark current and thermal backgrounds (caused by
infrared emission of the telescope and its support structures etc.).\
$^{\ddagger}$Evaluated using zodiacal light model at a season midpoint;
in our simulations we use a time dependent model of the Zodiacal
background (see [8](#mabulsimprovements){reference-type="ref+label"
reference="mabulsimprovements"} for details).\
$^{\mathsection}$Effective saturation level after full exposure time.
For the designs preceding AFTA, we assumed saturation would occur when
the pixel's charge reached the full-well depth. For AFTA we assume that,
thanks to multiple reads, useful data can be measured from pixels that
saturate after two reads, so for a constant full well depth, the
saturation level increases with exposure time.\
$^{\ast\ast}$Accounts for time lost to moon angle constraints.
[]{#designparams label="designparams"}
:::

![Total throughput curves for each of the mission designs, compared to
spectra of stars of different spectral types, suffering differing
amounts of extinction. The spectrum of a $T_{\mathrm{eff}}=5800$ K,
$\log g=4.5$ G-dwarf taken from the NEXTGEN grid [@Hauschildt1999] is
plotted with no extinction (orange line) and with $A_H=0.66$ (gray
line), which is typical for the expected *WFIRST* fields shown in
[3.3](#fields){reference-type="ref+label" reference="fields"}. G-dwarfs
will be the bluest stars that will act as source stars in significant
numbers, because more massive stars have evolved off the main sequence
in the old bulge population. The $y$-axis units of the spectra are
proportional to the photons per unit wavelength
($\mathrm{d}N/\mathrm{d}\lambda$), but each is arbitrarily normalized.
The throughput curves show the total system throughput including
detector quantum efficiency, and are only shown for the $Z087$ and
$W149$ filters. The *WFIRST* microlensing survey will likely use a wider
selection of filters than this.](wfirstfilters.pdf){#bandpasses
width="\\columnwidth"}

[\[designparams\]](#designparams){reference-type="ref+label"
reference="designparams"} summarizes the parameters of each mission
design that we study. We use these parameters for the results presented
in [4](#baselineyield){reference-type="ref+label"
reference="baselineyield"} and
[4.1](#lowmass){reference-type="ref+label" reference="lowmass"}. In
[5](#tradeoffs){reference-type="ref+label" reference="tradeoffs"} we
present the results of "trade-off" simulations that were conducted
during the design process, when many of the mission parameters changed
regularly. Between any given set of trade-off simulations, the exact
values of many of the simulation parameters changed by small amounts.
Rather than tediously detail each of these parameter changes that have
little effect on the absolute yields, we will only indicate changes to
parameters where they are important to each study. Invariably, these
will be the independent variables of each study, or parameters closely
related to these. As the unimportant parameters do not change internal
to each trade-study, we compute differential yield measurements, i.e.,
yields relative to a fiducial design.

## The *WFIRST* Microlensing Survey

The full operations concept for the *WFIRST* mission must ensure that
the spacecraft can conduct all the observations necessary to meet its
primary mission requirements, while maintaining sufficient flexibility
to conduct a significant fraction of potential general observer
observations. These considerations must feed into the spacecraft
hardware requirements while simultaneously being constrained by
practical design considerations in an iterative process. An example of
an observing time line that results from this process in given in the
@Spergel2015 report.

While constructing a sample observing schedule for *WFIRST* is a
complicated optimization task, requirements set by the nature of
microlensing events significantly simplify the process for the
microlensing survey. First, the microlensing event rate is highly
concentrated towards the Galactic bulge, close to the ecliptic. This
means that a spacecraft with a single solar panel structure parallel to
its telescope's optical axis can only perform microlensing observations
twice per year when the Galactic bulge lies perpendicular to the
Sun-spacecraft axis. Second, microlensing events last roughly twice the
microlensing timescale $t_{\mathrm{E}}$, with
$2t_{\mathrm{E}}{\sim}60$ d, and planetary deviations last between an
hour and a day [see, e.g., @Gaudi2012]. This means that a microlensing
survey must observe for at least $60$ days in order to characterize the
whole microlensing event, while also observing at high cadence
continually for periods ${\gtrsim}1$ day in order to catch and
characterize microlensing events. To operate at maximum efficiency it
should continuously observe for the entire duration of its survey
windows. Finally, the survey requirement to detect ${\sim} 100$
Earth-mass planets combined with a detection efficiency of ${\sim}0.01$
per event and a microlensing event rate of a
${\sim}$few$\times10^{-5}$ yr$^{-1}$ star$^{-1}$ imposes a requirement
of monitoring a ${\sim}$few$\times10^8$ star years over the duration of
the survey.

The duration of planetary deviations places a requirement on the cadence
of the microlensing observations. The timescale of planetary deviations
is comparable to the Einstein crossing timescale of an isolated lens of
the same mass, $t_{\mathrm{E}}\approx 2$ hr $\sqrt{M/M_{\earth}}$, and
the deviation must be sampled by several data points in order to
robustly extract parameters. Furthermore, the duration of finite source
effects in the lightcurve, which carry information about the angular
Einstein radius $\theta_{\mathrm{E}}$, and also need to be resolved by
several data points are ${\sim}1$ hr. Combined, these require an
observing cadence of ${\sim}15$ min. If stars are well resolved,
accurate photometry is possible for much of the bulge main sequence in
exposures ${\sim}1$ minute on ${\sim}1$ m-class telescopes, and so it
should be possible to observe between 5 and 10 fields within the cadence
requirements if the observatory can slew fast enough.

The microlensing event rate is highest within a few degrees of the
Galactic center, but these regions are also affected by a large amount
of extinction. Observations in the near infrared drastically reduce the
effect of the extinction. The *WFIRST* microlensing survey maximizes its
photometric precision by using a wide (1--2 $\mu$m) bandpass for most of
its observations, shown in [1](#bandpasses){reference-type="ref+label"
reference="bandpasses"}. Combining the wide filter with its wide
${0.28}$ deg$^{2}$ field of view, the current design of *WFIRST* can
monitor a sufficient number of microlensing events with sufficient
precision with ${\sim}400$ days of microlensing observations. Less
frequent observations will be taken in more typical broadband filters,
here we assume $Z087$ in order to measure the colors of microlensing
source stars and to measure color-dependent centroid shifts for luminous
lenses when the source and lens separate; the range of intrinsic
$Z087-W149$ colors of stars is shown in
[22](#cmd){reference-type="ref+label" reference="cmd"} in
[8.1](#customfilters){reference-type="ref+label"
reference="customfilters"}. Note that *WFIRST* magnitudes are on the AB
system [@Oke1983], and all magnitudes in this paper will be expressed in
this system, unless denoted by a subscript Vega.

  ----------------------------------------------- ------------------------------
  Area                                            1.96 deg$^2$
  Baseline                                        4.5 years
  Seasons                                         $6\times 72$ days
  $W149$ Exposures                                ${\sim}41,000$ per field
  $W149$ Cadence                                  $15$ minutes
  $W149$ Saturation                               ${\sim}14.8$
  Phot. Precision                                 0.01 mag @ $W149{\sim}21.15$
  $Z087$ Exposures                                ${\sim}860$ per field
  $Z087$ Saturation                               ${\sim}13.9$
  $Z087$ Cadence                                  $\lesssim12$ hours
  Stars ($W149<15$)                               ${\sim}0.3\times10^{6}$
  Stars ($W149<17$)                               ${\sim}1.4\times10^{6}$
  Stars ($W149<19$)                               ${\sim}5.8\times10^{6}$
  Stars ($W149<21$)                               ${\sim}38\times10^{6}$
  Stars ($W149<23$)                               ${\sim}110\times10^{6}$
  Stars ($W149<25$)                               ${\sim}240\times10^{6}$
  Microlensing events $|u_{\mathrm{0}}|<1$        ${\sim}27,000$
  Microlensing events $|u_{\mathrm{0}}|<3$        ${\sim}54,000$
  Planet detections ($0.1$--$10^{4}M_{\earth}$)   ${\sim}1400$
  Planet detections ($<3M_{\earth}$)              ${\sim}200$
  ----------------------------------------------- ------------------------------

  : The *WFIRST* Microlensing Survey at a Glance {#wfirstsummary}

**Notes**: Assumes the Cycle 7 design. Saturation estimates assumes the
brightest pixel accumulates $10^5$ electrons before the first read. Star
counts have been corrected for the Besançon  model's under-prediction
(see [3.2.1](#starcounts){reference-type="ref+label"
reference="starcounts"}). The exposure time and cadence of observations
in the $Z087$ and other filters has not been set; we have assumed a $12$
hour cadence here, but observations in the other filters are likely to
be more frequent. []{#wfirstsummary label="wfirstsummary"}

*WFIRST*'s microlensing survey therefore looks similar across all
designs of the spacecraft, with $72$ continuous days of observations
occurring around vernal and autumnal equinoxes. Six of these seasons are
required, with three occurring at the start of the mission and three at
the end in order to maximize the baseline over which relative
source-lens proper motion can be measured [see, e.g., @Bennett2007]. The
2.4 m telescope designs of *WFIRST* have a smaller field of view than
the ${\sim}1$ m class designs, but can monitor significantly fainter
stars at a given photometric precision due to their smaller PSF and
larger collecting area, resulting in a similar number of fields being
required to reach the same number of stars, despite the difference in
field of view. After these two effects cancel, the designs with larger
diameter mirrors come out as significantly more capable scientifically
due to their improvement in ability to measure relative lens-source
proper motions. [1](#wfirstsummary){reference-type="ref+label"
reference="wfirstsummary"} summarizes the parameters of the latest
iteration of the *WFIRST* microlensing survey design and the survey
yields that we will describe in later sections.

# Simulating the *WFIRST* microlensing survey {#sims}

We performed our simulations using the  code, of which we only give a
brief overview here, and refer the reader to @Penny2013 [hereafter ] for
full details.[^1] In order to fully simulate *WFIRST* we have made a
number of upgrades to , which are described in the Appendix.

![*Left column:* Section of a VVV $H$ band image [@Saito2012] from near
$(\ell,b)=(1\fdg1,-1\fdg2)$, which lies close to the center of the
expected *WFIRST* fields. *Right four columns:* Simulated images in the
primary wide band of the IDRM, DRM1, DRM2, and AFTA *WFIRST* designs of
the same mock star field drawn from the Besançon  model sight line at
$(\ell,b)=(1\fdg1,-1\fdg2)$. The top panels show a
$1{\times}1$ arcmin$^2$ region and the bottom panels show a
$4.6{\times}4.6$ arcsec$^2$ ($\approx 13\times$) zoom-in. The pixel
sizes are $0\farcs339$, $0\farcs18$, $0\farcs18$, $0\farcs18$ and
$0\farcs11$ from left to right respectively. Note that the apparent
dark, tenuous, serpentine feature on the left side of the simulated
images is a result of random fluctuations in the stellar density, and is
not due to spatially varying extinction (e.g., a dust lane). The VVV
image based on data products from observations made with ESO Telescopes
at the La Silla or Paranal Observatories under ESO programme ID
179.B-2002.](wfirst_image_comparison_yellow.jpg){#images
width="\\textwidth"}

![Simulated color images of an example bulge field at
$(\ell,b)=(0\fdg0,-1\fdg5)$ imaged using *WFIRST*'s Cycle 7 detector,
compared with a ground-based observatory based on OGLE's 1.3-m telescope
[e.g., @Udalski2015-ogleiv] in optical filters. The *WFIRST* image is
built from a single simulated exposure of $290$, $52$, and $145$ s in
$Z087$, $W149$, and $F184$ filters, respectively; the OGLE image was
built from single simulated exposures of $150$, $125$, and $100$ s in
$V$, $R$, and $I$ filters, respectively, i.e., typical of the standard
OGLE survey exposures. Note the different sizes of the images compared
to the previous figure, and that at least some of the *WFIRST* fields
will be amenable to observations with ground-based optical
telescopes.](cycle6ground.jpg){#cycle7image width="\\columnwidth"}

 simulates large numbers of individual microlensing events involving
source and lens stars that are drawn from star catalogs produced by a
population synthesis Galactic model. Source stars are drawn from a
catalog with a faint magnitude limit (here $H_{\rm Vega}=25$), and lens
stars from a catalog with no magnitude limit; source lens pairs where
the distance of the source is less than the distance of the lens are
rejected. Each catalog is drawn from a small solid angle $\delta\Omega$,
but represents a larger $0\fdg25\times0\fdg25$ sight line at its
specified Galactic coordinates $(\ell,b)$. The impact parameter
$u_{\mathrm{0}}$ and time of the event $t_{\mathrm{0}}$ are drawn from
uniform distributions with limits $[-u_{0,{\rm max}},+u_{0,{\rm max}}]$
and $[0,T_{\rm sim}]$, respectively, where $u_{0,{\rm max}}=3$ is the
maximum impact parameter and $T_{\rm sim}$ is the simulation duration.

Each simulated event $i$ is assigned a normalized weight $w_i$
proportional to its contribution to the total event rate in the sight
line $$\begin{equation}
w_i = 0.25^2\text{deg}^{2} f_{1106,WFIRST} \Gamma_{{\rm deg}^2} T_{\rm sim} u_{0,{\rm max}} \frac{2 \mu_{{\rm rel},i} \theta_{{\rm E},i}}{W},
\label{rateweight}
\end{equation}$$ where $\Gamma_{{\rm deg}^2}$ is the event rate per
square degree computed via Monte Carlo integration of the event rate
using the source and lens catalogs (see and @Awiphan2016 for details),
$f_{1106,WFIRST}$ is the event rate scaling factor that we use to scale
the event rate computed from the Galactic model to match measured event
rates (see [3.2](#ratecorr){reference-type="ref+label"
reference="ratecorr"} for details), $\mu_{{\rm rel},i}$ is the relative
lens-source proper motion of simulated event $i$, $\theta_{{\rm E},i}$
is the angular Einstein radius of event $i$, and $$\begin{equation}
W = \sum_i 2 \mu_{{\rm rel},i} \theta_{{\rm E},i}
\end{equation}$$ is the sum of un-normalized "event rate weights" for
all simulated events in a given sight line. As such, the sum of $w_i$
for all events is simply the number of microlensing events we expect to
occur in the sight line during the simulation duration with source stars
matching the source catalog's selection criteria. Similarly, the
prediction for the number of events matching a given criteria (e.g., a
$\Delta\chi^2>160$ detection threshold due to a planetary deviation) is
simply the sum of normalized weights of events that pass the cut, e.g.,
$$\begin{equation}
N(\Delta\chi^2>160) = \sum_i w_i H(\Delta\chi_i^2-160),
\end{equation}$$ where $H(x)$ is the Heaviside step function.

Binary (planetary) microlensing lightcurves are computed using a
combination of the hexadecapole approximation [@Pejcha2009; @Gould2008],
contour integration [@Gould1997; @Dominik1998] and rayshooting [when
errors are detected in the contour integration routines, @Kayser1986].
Realistic photometry of each event is simulated by constructing images
of star fields (drawn from the same population synthesis Galactic model)
for each observatory and filter considered, such that the same stars
populate images with different pixel scales and filters. The PSF of the
baseline source and lens stars are added at the same position on the
image. As the event evolves, the source star brightness is updated and
photometry is performed on the image for each data point. For some of
the simulations we have implemented a faster photometry scheme that
bypasses the need to create a realization of an image for each data
point, and which is described in the Appendix.
[2](#images){reference-type="ref+label" reference="images"} shows
examples of simulated images for IDRM, DRM1, DRM2, and AFTA designs
compared to a ground-based IR image, and
[3](#cycle7image){reference-type="ref+label" reference="cycle7image"}
shows an example simulated color image comparing *WFIRST*'s performance
to a simulated ground-based optical telescope in a field typical for the
*WFIRST* microlensing survey.

Each star is added using realistic numerical PSFs that are integrated
over the detector pixels for a range of sub-pixel offsets and stored in
a lookup table for rapid access. For IDRM, DRM1 and DRM2, which all have
unobstructed apertures, we used an Airy function averaged over the
bandpass of the filter. For AFTA we used numerical PSFs produced using
the ZEMAX software package (D. Content priv. comm.). For the Z087 filter
we used the monochromatic PSF computed at $1$ $\mu$m and for the wide
filter we averaged the PSFs computed at $1.0$, $1.5$ and $2.0$ $\mu$m
with equal weights. This crude integration procedure insufficiently
samples the changing size of the Airy rings as a function of wavelength,
so the resulting PSFs have much more prominent higher-spatial frequency
rings than the actual PSF. The real PSF will be much smoother in the
wings [see, e.g., @Gould2014]. The spacing of the unrealistic rings is
smaller than the photometric aperture we use, so the inaccurate PSF will
have little effect on our results because maxima and minima will average
out over the aperture). For the Cycle 7 design we used well sampled
numerical PSFs generated using the WebbPSF tool [@WebbPSF] with
parameters from Cycle 5; while the diffraction spikes of these PSFs are
rotated 90 degrees relative to the Cycle 7 design, this has no practical
effect on our simulated results.

![Single epoch photometric precision for isolated point sources as a
function of magnitude for the Cycle 7 design's assumed exposure time
($46.8$ s) assuming no blending. The vertical dashed line indicates the
approximate point of saturation in a single
read.](snrcurve.pdf){#snrplot width="\\columnwidth"}

The capabilities of crowded field photometric techniques are
approximated by performing aperture photometry on the image with fixed
pointing. We found that a $3{\times}3$ pixel square aperture produced
the best results in the crowded *WFIRST* fields. This simple photometry
scheme enables us to accurately simulate all the sources of photon and
detector noise that arise in the conversion of photons to data units on
an image of minimal size. Aperture photometry is sub-optimal in crowded
fields, but we can use this fact to compensate for the effect of any
un-modeled causes of additional photometric noise resulting from
imperfect data analysis (the precision of any method can only
asymptotically approach the theoretically possible photon noise, and
sometimes may be far from it), systematic errors (e.g., we do not
simulate pointing shifts or variations in pixel response), or data loss.
The resultant photometric precision as a function of magnitude is shown
in [4](#snrplot){reference-type="ref+label" reference="snrplot"},
assuming no blending. Properly simulating all sources of systematic or
red noise would require a more detailed simulation of the photometry
pipeline (for example, by performing difference imaging on images that
suffer pointing shifts) and would be significantly more computationally
expensive as a significantly larger image would need to be recomputed
for each data point. Rather than do this, we simply add in quadrature a
Gaussian systematic error floor to the photometry we measure.

We note that we have not correctly simulated the read out schemes
employed by the HAWAII HgCdTe detectors *WFIRST* will use. Our
simulations simulate the CCD readout process, i.e., an image is exposed
for a time $t_{\rm exp}$ before being read out pixel by pixel by a one
or a small number of amplifiers in a destructive process. Individual
pixels in an infrared HgCdTe array have their own amplifier and can be
read out non destructively multiple times per exposure at a chosen rate.
HgCdTe amplifiers typically have higher read noise than CCD amplifiers,
and so multiple non-destructive reads are employed to reduce the
effective read noise in the image. Multiple image "frames" can
potentially be stored and downlinked, or processed on-board the
spacecraft, enabling retrieval of useful data from pixels that would
saturate in the full exposure time or that get hit by cosmic rays.

Our photometry simulations assume a single readout at the end of an
exposure with a gain of $1$ e$^{-}$/ADU. The actual gain value will be
different, but any digitization uncertainty will be small compared to
the readout noise. We approximate the effective readout noise in
*WFIRST* images using the erratum correction of the formula given by
@Rauscher2007, based on the correlated double sampling readout noise
requirements of each design, an assumed readout rate, and the exposure
time. The full well depth parameter in our simulations is applied to the
full exposure time, so we increase the detector full well depth
requirement by a factor of $t_{\rm exp}/t_{\rm read}$, where
$t_{\rm read}$ is the time interval between reads of a given pixel, to
simulate the ability to extract a measurement from a pixel that does not
saturate before the first read. This workaround results in an
underestimate of the Poisson noise component of photometry, but the
addition of a 0.001 mag systematic uncertainty in quadrature to the
final photometric measurement involving 9 pixels prevents a severe
underestimate of the uncertainty in such situations. We note that it
should be possible to extract accurate photometry from any pixels that
do not saturate before the first read [see @Gould2015].

To assess whether a simulated event contains a detectable planet we use
a simple $\Delta\chi^2$ selection criteria $$\begin{equation}
\Delta\chi^2 \equiv \chi_{\rm FSPL}^2 - \chi_{\rm true}^2 > 160,
\end{equation}$$ where $\chi_{\rm FSPL}$ is the $\chi^2$ of the
simulated data lightcurve relative to the best fitting finite source
single point (FSPL) lens model lightcurve [@Witt1994], and
$\chi_{\rm true}^2$ is the $\chi^2$ of the simulated data relative to
the true simulated lightcurve. In practice we only fit a FSPL model if a
point source point lens model fit produces a $\Delta\chi^2$ above the
detection threshold. We do not consider whether the lightcurve can be
distinguished from potentially ambiguous binary lens models or binary
source models.

Our choice of $\Delta\chi^2$ threshold is the de facto standard among
microlensing simulations [e.g.,
@Bennett2002; @Bennett2003; @Penny2013; @Henderson2014-kmt]. @Yee2012
and @Yee2013 discussed the issue of the detection threshold in survey
data for high magnification events, and concluded that for one
particular event a clear planetary anomaly in the full data set might be
marginally undetectable in a truncated survey data set at
$\Delta\chi^2\approx 170$. For a uniform survey data set, and a search
that included low-magnification events, @Suzuki2016 used a
$\Delta\chi^2$ threshold of $100$. We expect systematic errors for a
space based survey to be lower than for a ground-based survey, therefore
our choice of $\Delta\chi^2=160$ should be reasonably conservative.
Additionally, except near the edges of its survey sensitivity, the
number of planet detections *WFIRST* can detect is only weakly dependent
of $\Delta\chi^2$ as discussed in
[5](#tradeoffs){reference-type="ref+label" reference="tradeoffs"}. This
means that our yields will be relatively insensitive to any
innaccuracies in our simulations or models that affect $\Delta\chi^2$.
Additionally, because we have chosen relatively conservative assumptions
for the systematic noise floor and the $\Delta\chi^2$ threshold, it is
possible that the yield of the hardest-to-detect planets could be
significantly larger than we predict.

For the smallest mass planets we do not expect binary lens ambiguity be
an issue for many events. Most low-mass planet detections will come from
planetary anomalies in the wings of low-magnification events. In such
events the caustic location is well constrained and hence also the
projected lens source separation $s$. Once $s$ is constrained, the
caustic size and anomaly duration scales only with the mass ratio $q$ of
the lens as $q^{1/2}$ [e.g., @Han2006]. Binary source stars with extreme
flux ratios can potentially produce false positives for low-mass
planetary microlensing [@Gaudi1998]. As *WFIRST* will observe source
stars much closer to the bottom of the luminosity function, and the near
infrared luminosity function is shallower than the optical luminosity
function, we can expect a smaller fraction of *WFIRST*'s binary source
stars to have the properties required to mimic a planetary microlensing
event. We leave a detailed reassessment of the importance of binary
source star false positives for *WFIRST*'s microlensing survey to future
work.

## Galactic Model

In this work we use version 1106 of the Besançon  Galactic model,
hereafter BGM1106. This version of the model is described in full detail
by and references therein. It is intermediate to the original, publicly
available version [@Robin2003], and a more recent version [@Robin2012].
It also differs from the model versions used by @Kerins2009 and
@Awiphan2016 to compute maps of microlensing observables.

As the model has been detailed in other papers we only give an overview
of the most important features here. The BGM1106 bulge is a boxy
triaxial structure following the @Dwek1995 $G_2$ model with scale
lengths of $(1.63,0.51,0.39)$ kpc and orientated with the long axis
$12\fdg5$ from the Sun-Galactic center line. The thin disk uses the
@Einasto1979 density law with a scale length of $2.36$ kpc for all but
the youngest stars, which have a scale length of $5$ kpc. The disk has a
central hole with a scale length of 1.31 kpc, except for the youngest
stars where the hole scale length is $3$ kpc. The disk scale height is
set by self consistency requirements between kinematics and Galactic
potential [@Bienayme1987]. The model also has thick disk and halo
components, but they do not provide a significant fraction of sources or
lenses. The full form of the density laws are given in @Robin2003 Table
3.

Stellar magnitudes are computed from stellar evolution models and model
atmospheres based on stellar ages determined by separate star formation
histories and metallicity distributions of the different components.
Stellar masses are drawn from an initial mass function (IMF) that
differs between the disk and bulge. Each is a broken power law,
$\mathrm{d}N/\mathrm{d}M\propto M^{\alpha}$, where $M$ is the stellar
mass, with $\alpha=-1.6$ for $0.079<M<1M_{\odot}$ and $\alpha=-3$ for
$M>1M_{\odot}$ in the disk, and $\alpha=-1$ for $0.15<M<0.7M_{\odot}$
and $\alpha=-2.35$ for $M>0.7M_{\odot}$ in the bulge. Extinction is
determined by the 3-d extinction map of [@Marshall2006], expressed as
measurements of $E(J-K)$ reddening at various distances and with a
resolution of $0\fdg25\times 0\fdg25$ on the sky. Reddening is converted
to extinction in other bands using the @Cardelli1989 extinction law with
a value of total to selective extinction $R_V=3.1$.

## Normalizing the event rate {#ratecorr}

 computes microlensing event rates by performing Monte Carlo integration
of star catalogs produced by the population synthesis Galactic model. In
we found that BGM1106 under-predicted the microlensing optical depth by
a factor of $f_{\rm od,P13}=1.8$ and star counts in Baade's Window by a
factor of $f_{\rm sc,P13}=1.3$. To account for this we applied a
correction factor, $$\begin{equation}
f_{\rm 1106,P13}=f_{\rm od,P13}f_{\rm sc,P13}=1.8\times1.3=2.33
\end{equation}$$ to the BGM1106 event rates. Here we will update this
event rate correction factor by making comparisons of the Galactic model
predictions to new star count and microlensing event rate measurements.

### Comparison to Star Counts {#starcounts}

used a comparison between the BGM1106 and *HST* star counts in Baade's
window at $(\ell,b)=(1\fdg00,-3\fdg90)$ as measured by @Holtzman1998 to
derive a partial correction to the event rate of $f_{\rm sc,P13}=1.30$.
This field lies more than 2 degrees further away from the Galactic plane
than the center of the likely *WFIRST* fields at $b\approx-1\fdg7$. The
Sagittarius Window Eclipsing Extrasolar Planet Search [SWEEPS @Sahu2006]
field, originally studied by @Kuijken2002, lies at
$(\ell,b)=(1\fdg25,-2\fdg65)$ and is significantly closer to the
*WFIRST* fields, but still slightly outside the nominal survey area. The
field has been observed by *HST* multiple times over a long time
baseline, enabling extremely deep proper motion
measurements [@Clarkson2008; @Calamida2015] and now star
counts [@Calamida2015]. By comparing star counts closer to the
*WFIRST* fields we can hope to reduce the impact of any extrapolation
errors when estimating an event rate correction.

![Comparison of Besançon  model star counts for the bulge population as
a function of magnitude $F814W_{\rm Vega}$ at
$(\ell,b)=(1\fdg35,-2\fdg70)$ to those measured in the *HST* SWEEPS
field at $(\ell,b)=(1\fdg25,-2\fdg65)$, which lies close to the expected
*WFIRST* fields. Green squares show bulge-only star counts from
*HST* @Calamida2015 and diamonds show counts of red giant branch stars
in the same area from OGLE-III [@Szymanski2011]. The *HST* stars were
selected to be bulge stars by proper motion cuts, and have been
corrected for the approximate efficiency of this cut. The solid black
line shows the BGM1106 prediction, with error bars denoting the Poisson
uncertainty of the catalogs. While there are differences in the detailed
shape of the star count distribution, integrated over the range
$F814W=19$--$26.5$, BGM1106 under-predicts the total number of stars by
$33$%; the blue line shows the BGM1106 scaled up by this factor. The
dashed black line shows the BGM1106 model star counts if the mass
function is changed in the bulge to match mass function 1 of @Sumi2011,
namely a broken power law with slopes of -1.3 and -2.0
($\mathrm{d}N/\mathrm{d}M$) each side of a break at
$0.7M_{\odot}$.](calamida.pdf){#calamida width="\\columnwidth"}

@Calamida2015 measured the magnitude distribution of bulge stars by
selecting stars with a proper motion cut designed to exclude disk stars.
@Calamida2015 correct for completeness using artificial star tests, but
we add additional corrections for the efficiency of the proper motion
cut ($34$ percent, A. Calamida, priv. comm.) and the field area
($3.3\arcmin\times3.3\arcmin$), in order to plot the absolute stellar
density as a function of magnitude in
[5](#calamida){reference-type="ref+label" reference="calamida"}. We do
not consider the bins at the extremes of the magnitude distribution
which are likely affected by saturation or large incompleteness. To
compare to the observed distribution, we computed the magnitude
distribution of bulge stars in the BGM1106 sight line at
$(\ell,b)=(1\fdg35,-2\fdg70)$, which is the closest to the SWEEPS field.

BGM1106 matches the measured magnitude distribution reasonably well
between $F814W_{\rm Vega}=19.5$ and $23$, though with minor differences
in shape. BGM1106 starts to significantly underpredict the number of
stars fainter than $F814W_{\rm Vega}=23$. Brighter than
$F814W_{\rm Vega}=22.9$, @Calamida2015 find 10 percent more stars than
the BGM1106 predicts. Integrated over the magnitude range
$F814W_{\rm Vega}=19$--$26.5$ BGM1106 under-predicts star counts by
$33$ percent. The magnitude of the discrepancy is very similar to that
we found between the BGM1106 and the @Holtzman1998 luminosity function,
giving us some confidence that there is no significant gradient in the
BGM1106's star count discrepancy. We adopt the star count scaling factor
of $f_{\rm sc}=1.33$.

The cause of the discrepancy between model and data can be partially
explained by the BGM1106's choice of initial mass function (IMF) in the
bulge, $\mathrm{d}N/\mathrm{d}M \propto M^{-1.0}$. Adopting a more
reasonable mass function [e.g., mass function number 1 from @Sumi2011
$\mathrm{d}N/\mathrm{d}M \propto M^{-2.0}$ for $M>0.7M_{\odot}$ and
$\mathrm{d}N/\mathrm{d}M \propto M^{-1.3}$ for $0.08<M<0.7M_{\odot}$],
and assuming that the BGM1106 star counts were normalized using turn-off
stars of $1.0M_{\odot}$, produces the luminosity function prediction
shown by the dashed line in the plot. This mass function over-predicts
the star counts fainter than $F814W_{\rm Vega}\approx 20$, but better
matches the shape of the entire observed luminosity function between
$I_{\rm Vega}\approx 19$--$26$. Both the original and modified BGM1106
mass functions slightly under-predict the number of giant branch star
counts from the same sight line detected by OGLE [@Szymanski2011], which
have not been corrected for incompleteness. We note here that we do not
adopt an alternative mass function [e.g, mass function 1 from
@Sumi2011], but discuss the impact of the mass function on our results
in section [6](#discuss){reference-type="ref" reference="discuss"}.

### Comparison to Microlensing Event Rates {#eventrates}

Since writing , @Sumi2013 published measurements of the microlensing
event rate towards the bulge, in addition to optical depth measurements.
Measurements of the event rate per source star allow a more direct route
to estimating any corrections to the model's predicted event rates, so
here we only perform a comparison to the event rates and not the optical
depths. For the comparison we use the event rates from @Sumi2016, which
corrected the @Sumi2013 event rates and optical depths for a systematic
error in estimates of the number of source stars monitored.

@Sumi2013 present event rates for two samples of events, the "extended
red clump" (ERC) sample composed of events with source stars brighter
than $I=17.5$ and colors selected to only include the bulge giant
branch, and the "all stars" (AS) sample composed of all events with
$I<20$ and no color cut. We selected star catalogs from the BGM1106 to
match these samples, and computed event rates per source $\Gamma$ by
Monte Carlo integration over this source catalog and a lens catalog with
no magnitude or color cuts [see @Awiphan2016 for a detailed description
of such calculations]. The small angle of the Galactic bar to the line
of sight in the BGM1106 (${\sim}12\degr$) results in the bulk of our AS
sample source stars lying in front of most of the bulge stars. This
leads to significantly smaller event rates per source than would be
expected for a more reasonable bar angle of ${\sim}30\degr$ [e.g.
@Wegg2013; @Cao2013], which could lead us to over-correcting the event
rates. We therefore only compare to the ERC sample event rates.

![Comparison of the microlensing event rate per source predicted by the
Besançon model to the [@Sumi2016] revision of measurements by
[@Sumi2013]. Black data points show measurements for all source stars,
while red data points show measurements for the extended red clump
source stars (see text for details). The thin line shows the BGM1106's
prediction of extended red clump event rates, and the thick red line
shows this prediction after multiplication by the best fit scaling
parameter $f_{\Gamma}=2.11\pm0.29$.](gammasumipenny.pdf){#gammacomp
width="\\columnwidth"}

[6](#gammacomp){reference-type="ref+label" reference="gammacomp"} shows
the predicted model event rates, averaged over the range
$-0.53<\ell\le +2.73$, and the data from @Sumi2016, which was averaged
over the range $|\ell|<5$. BGM1106 predicts a lower event rate than is
measured. At latitudes $|b|<1.5$ the predicted ERC event rate turns over
likely because extinction begins to limit the range of distances over
which significant numbers of bulge giants pass the ERC color and
magnitude cuts; at more negative latitudes, where the observations we
compare to were made, the extinction likely has a smaller impact. We
find that multiplying the BGM1106 event rates by a constant scaling
factor $f_{\Gamma} = 2.11 \pm 0.29$ yields a good match to the observed
ERC rates, with $\chi^2=1.58$ for $3$ degrees of freedom. Although the
model predictions cover a smaller range of $\ell$ than the measurements,
@Sumi2016 results binned by $\ell$ indicate only a relatively weak
dependence of $\Gamma$ on $|\ell|$.

### Adopted Event Rate Scaling {#scaling}

In we scaled the microlensing event rates computed using the BGM1106 by
making the assumption that all of the relevant distributions (e.g.,
kinematics, mass, and density) were reasonable, but that there could be
errors in the normalization of the numbers of source and lens stars. To
make a correction for the number of source stars we directly compared
the BGM1106 predictions to deep star counts measured by HST. To estimate
the correction for the number of lens stars, we compared model
predictions to measurements of the microlensing optical depth. This has
the advantage that, should the density distribution and mass function of
stars in the model be reasonable, the necessary correction to the event
rate due to lenses should scale with the optical depth discrepancy
between model and data. However, as we have described in the preceding
subsections and will expand on in
[6](#discuss){reference-type="ref+label" reference="discuss"}, the
density distribution (specifically the bar angle of the bulge), the
bulge mass function, and the kinematics of bulge stars in the BGM1106
are inconsistent with current measurements. These will affect the event
rate and optical depth in different ways that are not trivial to
calculate. This makes any simple scaling of the event rate based on
optical depth comparisons suspect. In contrast, a scaling based on
measured event rates is far more direct with fewer assumptions.
Therefore, to correct the event rates predicted by the Galactic model,
we adopt the event rate scaling factor $$\begin{equation}
f_{1106,WFIRST} = f_{\rm sc} f_{\Gamma},
\end{equation}$$ where $$\begin{equation}
f_{\rm sc} = 1.33, \text{and} f_{\Gamma}=2.11,
\end{equation}$$ for a total event rate correction of $$\begin{equation}
f_{1106,WFIRST} = 2.81,
\end{equation}$$ which is about $20$% larger than the scaling adopted in
. We will discuss the impact of uncertainties and innaccuracies in the
Galactic model beyond the event rate scaling in
[6](#discuss){reference-type="ref+label" reference="discuss"}.

We apply the $f_{1106,WFIRST}$ scaling throughout the paper as our
fiducial event rate normalization. However, we will also present our
main results with the scalings used for each of the *WFIRST* reports in
order to aid comparison to these earlier works; these results using
obsolete scalings are presented in
[\[cassan_table_report\]](#cassan_table_report){reference-type="ref+label"
reference="cassan_table_report"} in
[4](#baselineyield){reference-type="ref+label"
reference="baselineyield"}. We note, however, that when applying the
obsolete scaling, we did not include a factor of $1.475$ in the scaling
that was used in the @Green2012. This factor was used to account for a
factor of 2.2 discrepancy in the microlensing detection efficiency of
our  simulations and simulations performed by D. Bennett, based on
@Bennett2002 and updated for simulations of *WFIRST* [@Green2011]; 1.475
was the geometric mean of the relative detection efficiencies for
planets of $1M_{\earth}$ with a period of $2$ years. The cause of the
difference in detection efficiencies was not conclusively tracked down.
However, at fixed period, the projected separation $s\propto M^{-5/6}$,
and the detection efficiency is a strong function of $s$, so a
difference between the host mass function of the simulations (see
[3.2.1](#starcounts){reference-type="ref+label" reference="starcounts"}
and [6.2.3](#bulgeimf){reference-type="ref+label" reference="bulgeimf"})
is likely to cause a significant difference in the detection efficiency
at fixed period. Averaged over a range of semimajor axis, as we have
done in the simulations presented in
[4](#baselineyield){reference-type="ref+label"
reference="baselineyield"}, we can expect any difference in the
detection efficiency at fixed planet mass to be significantly smaller.

## The *WFIRST* fields {#fields}

<figure id="fieldplacement">
<p><embed src="all_fields.pdf" /><br />
<embed src="cycle6field.pdf" /></p>
<figcaption>Assumed field placement for each <em>WFIRST</em> design,
plotted over a map of
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>H</mi><annotation encoding="application/x-tex">H</annotation></semantics></math>-band
extinction <span class="citation" data-cites="Gonzalez2012"></span>. The
gaps between IDRM, DRM1 and DRM2 fields were included to mimic the
effects of gaps between detectors. For the AFTA and Cycle 7 simulations
we accounted for the individual detector placement within each field
more carefully, so fields are close-butted (note the curved focal
plane). Note also that in reality the 1-m-class designs would also
likely have curved detector layouts and that, unlike the AFTA and Cycle
7 designs, the fields would probably not be orientated with their
principle axes aligned with Galactic coordinates. The black diamond in
the top panels shows the location of the <em>HST</em> SWEEPS field. In
the Cycle 7 panel, colored dots show the detection rate of
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><msub><mi>M</mi><mi>♁</mi></msub></mrow><annotation encoding="application/x-tex">1M_{\earth}</annotation></semantics></math>
planets per square degree as a function of position for the Cycle 7
design. A version of the Cycle 7 plot is available at <a
href="https://github.com/mtpenny/wfirst-ml-figures"
class="uri">https://github.com/mtpenny/wfirst-ml-figures</a>.</figcaption>
</figure>

For the IDRM, DRM1, DRM2, and AFTA simulations, the field placement was
not rigorously optimized. We show the fields we adopted for each design
in [7](#fieldplacement){reference-type="ref+label"
reference="fieldplacement"}. For IDRM, DRM1 and DRM2, the field
placement is significantly different than what it would be in reality if
each design were flown. This is due to uncertainties in the orientation
of the detectors in the instrument bay. We therefore chose the simplest
field orientation we could, aligning the principle axes of the fields
with Galactic latitude and longitude. Note however, that this is an
optimistic assumption, as the extinction and event rate at zeroth order
depend strongly on $b$ but weakly on $\ell$, so detector orientations
that align the long axis with $\ell$ are likely to be close to optimal.
For the IDRM, DRM1 and DRM2 field layouts we accounted for gaps between
detectors in the focal plan by placing the twice the sum of all chip
gaps between each of the fields.

For AFTA we considered the field layout more carefully. The telescope
instrument bay already exists, setting the orientation of the field and
constraining the layout of detectors within it. Coincidently the
orientation of the WFI focal plane for AFTA is within a couple of
degrees of aligned with Galactic coordinates. From spring to fall
seasons the orientation of the detector will be rotated by $180\degr$,
which means that with the curved geometry of the active focal plane, the
fields observed will not be exactly the same. For the layout shown this
results in ${\sim}90$% of stars that fall on a chip in spring seasons
also falling on a chip in the fall seasons. Occasional gap filling
dithers could be used to ensure some observations in both spring and
fall for all events.

Between the AFTA design and Cycle 7, the *WFIRST* wide field instrument
was redesigned and consequently the field orientation was rotated by
$90\degr$. Additionally, the spacecraft's slew and settle time estimates
were updated, and were more than twice that we had assumed for the AFTA
design. These two changes led us to conduct an optimization of the field
layouts. This optimization is described in
[5.4](#fieldopt){reference-type="ref+label" reference="fieldopt"}. With
this field layout we can expect to detect ${\sim}27,000$ microlensing
events with $|u_{\mathrm{0}}|<1$ and roughly twice this with
$|u_{\mathrm{0}}|<3$ during the course of the mission. While there are
three times as many events with $|u_{\mathrm{0}}|<3$ compared to
$|u_{\mathrm{0}}|<1$, the maximum magnification of a @Paczynski1986
single lens lightcurve at $|u_{\mathrm{0}}|=3$ is only $1.017$, compared
to $1.34$ at $|u_{\mathrm{0}}|=1$, so only on brighter stars will it be
possible for *WFIRST* to detect these low-magnification events.

# Baseline *WFIRST* planet yields {#baselineyield}

To assess the performance of each *WFIRST* design we ran a series of
simulations to investigate the number of planets that would be detected
during the *WFIRST* microlensing survey. To assess the performance of
the survey over a broad range of masses and orbits we simulated single
planet events with fixed masses in the range
$0.1\le M\le 10^4$ $M_{\earth}$ with semimajor axes distributed
logarithmically in the range $0.3\le a< 30$ AU -- roughly a factor of
$10$ either side of the typical Einstein radius ($2$--$3$ AU).

:::: table*
::: tabularx
lR@c@LR@c@LR@c@LR@c@LR@c@L\
**Mission** & & & & &\
**Duration** & & & & &\
**Area** & & & & &\
**Rate Norm.** & & & & &\
**Mass** ($\mathbf{M_{\oplus}}$) &&& &&& &&& &&& &&&\
\
\
$\mathbf{0.1}$ & $8.1$ & $\pm$ & $0.6$ & $11.1$ & $\pm$ & $0.4$ & $7.0$
& $\pm$ & $0.2$ & $18.0$ & $\pm$ & $0.3$ & $\mathbf{   9.9}$ &
$\mathbf{\pm}$ & $\mathbf{0.4}$\
$\mathbf{1}$ & $79.8$ & $\pm$ & $3.6$ & $87.5$ & $\pm$ & $2.1$ & $66.1$
& $\pm$ & $1.5$ & $138$ & $\pm$ & $2$ & $\mathbf{  87.5}$ &
$\mathbf{\pm}$ & $\mathbf{2.6}$\
$\mathbf{10}$ & $366$ & $\pm$ & $15$ & $496$ & $\pm$ & $9$ & $350$ &
$\pm$ & $6$ & $643$ & $\pm$ & $6$ & $\mathbf{   439}$ & $\mathbf{\pm}$ &
$\mathbf{  8}$\
$\mathbf{100}$ & $1610$ & $\pm$ & $47$ & $2110$ & $\pm$ & $39$ & $1500$
& $\pm$ & $26$ & $2440$ & $\pm$ & $51$ & $\mathbf{  1780}$ &
$\mathbf{\pm}$ & $\mathbf{ 84}$\
$\mathbf{1000}$ & $5480$ & $\pm$ & $150$ & $6610$ & $\pm$ & $110$ &
$4790$ & $\pm$ & $80$ & $7670$ & $\pm$ & $130$ & $\mathbf{  5210}$ &
$\mathbf{\pm}$ & $\mathbf{ 86}$\
$\mathbf{10^4}$ & $12700$ & $\pm$ & $230$ & $15400$ & $\pm$ & $190$ &
$11400$ & $\pm$ & $130$ & $17500$ & $\pm$ & $200$ & $\mathbf{ 11300}$ &
$\mathbf{\pm}$ & $\mathbf{150}$\
\
:::

\
**Notes:** The table presents planet yields for each simulated survey,
with the uncertainties due to Poisson shot noise in the drawn event
parameters; this uncertainty does not include any systematic component,
due, e.g., to the normalization of event rates; see
[6](#discuss){reference-type="ref+label" reference="discuss"} for a
discussion of the magnitude of these errors. The survey duration, total
field area and event rate normalization are shown in the header lines of
the table. The yields assume a planet of fixed mass and an occurrence
rate of one planet per decade of semimajor axis in the range
$0.3\le a<30$ AU per star. []{#raw_table label="raw_table"}
::::

[\[raw_table\]](#raw_table){reference-type="ref+label"
reference="raw_table"} shows the raw results of these simulations for
each *WFIRST* design, and the same numbers are plotted in
[8](#yieldplot){reference-type="ref+label" reference="yieldplot"} below.
The table is not particularly useful for assessing the number of planets
that *WFIRST* will detect, because the mass function that it implies
(one planet per decade of mass and semimajor axis, we will call this the
log mass function) is a significant overestimate at larger masses. It is
however the most convenient form from which other mass functions can be
applied. The results for IDRM1, DRM1 and DRM2 were first presented in ,
though using a different set of event rate corrections (see
[3.2](#ratecorr){reference-type="ref+label" reference="ratecorr"} above
for a description of the event rate corrections) and included a small
number of additional detections of planets with semimajor axis between
$0.03\le a<0.3$ AU. The results for DRM2 differ further from the report
due to a correction factor used to the correction of a mistake in the
number of fields and the exposure times that was made in the simulations
presented in the @Green2012 report. The AFTA simulations were rerun
completely to incorporate the changes introduced at Cycle 4 of the
*WFIRST* design. In hindsight these yields are overly optimistic due to
an unrealistic assumption of the spacecraft's slew performance. The
yields for Cycle 7 stand as the most realistic and most up-to-date
estimates, and so we have made these bold in the table.

:::: table*
::: tabularx
lR@c@LR@c@LR@c@LR@c@LR@c@L\
**Mission** & & & & &\
**Duration** & & & & &\
**Area** & & & & &\
**Rate Norm.** & & & & &\
**Mass** ($\mathbf{M_{\oplus}}$) &&& &&& &&& &&& &&&\
\
\
$\mathbf{0.1}$ & $16.7$ & $\pm$ & $1.3$ & $22.8$ & $\pm$ & $0.8$ &
$14.4$ & $\pm$ & $0.5$ & $37.1$ & $\pm$ & $0.6$ & $\mathbf{  20.5}$ &
$\mathbf{\pm}$ & $\mathbf{0.8}$\
$\mathbf{1}$ & $164$ & $\pm$ & $8$ & $180$ & $\pm$ & $4$ & $136$ & $\pm$
& $3$ & $284$ & $\pm$ & $3$ & $\mathbf{   180}$ & $\mathbf{\pm}$ &
$\mathbf{  5}$\
$\mathbf{10}$ & $455$ & $\pm$ & $19$ & $615$ & $\pm$ & $11$ & $434$ &
$\pm$ & $7$ & $799$ & $\pm$ & $8$ & $\mathbf{   545}$ & $\mathbf{\pm}$ &
$\mathbf{  9}$\
$\mathbf{100}$ & $371$ & $\pm$ & $11$ & $488$ & $\pm$ & $9$ & $346$ &
$\pm$ & $6$ & $563$ & $\pm$ & $12$ & $\mathbf{   412}$ & $\mathbf{\pm}$
& $\mathbf{ 19}$\
$\mathbf{1000}$ & $236$ & $\pm$ & $6$ & $284$ & $\pm$ & $5$ & $206$ &
$\pm$ & $4$ & $330$ & $\pm$ & $6$ & $\mathbf{   224}$ & $\mathbf{\pm}$ &
$\mathbf{  4}$\
$\mathbf{10^4}$ & $101$ & $\pm$ & $2$ & $124$ & $\pm$ & $2$ & $91.3$ &
$\pm$ & $1.1$ & $141$ & $\pm$ & $2$ & $\mathbf{  90.7}$ & $\mathbf{\pm}$
& $\mathbf{1.2}$\
\
**Total (0.1--**$\mathbf{10^4 M_{\oplus})}$ & & & & &\
:::

\
**Notes:** In this table the yields presented in
[\[raw_table\]](#raw_table){reference-type="ref+label"
reference="raw_table"} have been multiplied by our fiducial mass
function ([\[fiducialmf\]](#fiducialmf){reference-type="ref+label"
reference="fiducialmf"}). The total survey yield is found by integration
of the tabulated values with the extended trapezoidal rule.
[]{#cassan_table label="cassan_table"}
::::

:::: table*
::: tabularx
lR@c@LR@c@LR@c@LR@c@LR@c@L\
**Mission** & & & & &\
**Duration** & & & & &\
**Area** & & & & &\
**Rate Norm.** & & & & &\
**Mass** ($\mathbf{M_{\oplus}}$) &&& &&& &&& &&& &&&\
\
\
$\mathbf{0.1}$ & $21.1$ & $\pm$ & $1.6$ & $29.4$ & $\pm$ & $1.0$ &
$18.3$ & $\pm$ & $0.6$ & $47.8$ & $\pm$ & $0.8$ & $\mathbf{  25.9}$ &
$\mathbf{\pm}$ & $\mathbf{1.0}$\
$\mathbf{1}$ & $208$ & $\pm$ & $10$ & $232$ & $\pm$ & $6$ & $173$ &
$\pm$ & $4$ & $367$ & $\pm$ & $4$ & $\mathbf{   228}$ & $\mathbf{\pm}$ &
$\mathbf{  7}$\
$\mathbf{10}$ & $575$ & $\pm$ & $24$ & $793$ & $\pm$ & $14$ & $551$ &
$\pm$ & $9$ & $1030$ & $\pm$ & $10$ & $\mathbf{   690}$ & $\mathbf{\pm}$
& $\mathbf{ 12}$\
$\mathbf{100}$ & $470$ & $\pm$ & $14$ & $629$ & $\pm$ & $12$ & $439$ &
$\pm$ & $8$ & $726$ & $\pm$ & $15$ & $\mathbf{   522}$ & $\mathbf{\pm}$
& $\mathbf{ 25}$\
$\mathbf{1000}$ & $298$ & $\pm$ & $8$ & $367$ & $\pm$ & $6$ & $261$ &
$\pm$ & $4$ & $426$ & $\pm$ & $7$ & $\mathbf{   283}$ & $\mathbf{\pm}$ &
$\mathbf{  5}$\
$\mathbf{10^4}$ & $128$ & $\pm$ & $2$ & $160$ & $\pm$ & $2$ & $116$ &
$\pm$ & $1$ & $181$ & $\pm$ & $2$ & $\mathbf{   115}$ & $\mathbf{\pm}$ &
$\mathbf{  2}$\
\
**Total (0.1--**$\mathbf{10^4 M_{\oplus})}$ & & & & &\
:::

\
**Notes:** As
[\[cassan_table\]](#cassan_table){reference-type="ref+label"
reference="cassan_table"}, but using the event rate (${\sim}2.4$) and
detection efficiency compromise ($1.475$) scalings that were used in the
*WFIRST*-AFTA final report [@Spergel2015]. These yields should be
considered obsolete, and are only presented to aid comparison with the
previous *WFIRST* reports. []{#cassan_table_report
label="cassan_table_report"}
::::

[\[cassan_table\]](#cassan_table){reference-type="ref+label"
reference="cassan_table"} presents our fiducial estimate for the planet
yield of *WFIRST*. To compute these yields we multiply the raw yields
from [\[raw_table\]](#raw_table){reference-type="ref+label"
reference="raw_table"} by the following, fiducial, form of the planet
mass function, $$\begin{equation}
\frac{\mathrm{d}^2 N}{\mathrm{d}\log M_{\mathrm{p}}\mathrm{d}\log a} = \left\{\begin{array}{ll}
0.24\ \text{dex}^{-2} \left(\frac{M_{\mathrm{p}}}{95M_{\earth}}\right)^{-0.73} & \text{if} M_{\mathrm{p}}\ge 5.2M_{\earth},\\
2\ \text{dex}^{-2} & \text{if} M_{\mathrm{p}}< 5.2M_{\earth},
\end{array}\right.
\label{fiducialmf}
\end{equation}$$ which we will refer to hereafter as the fiducial mass
function. This mass function is based on the power-law bound planet mass
function measured by @Cassan2012 from microlensing observations, but
saturated at a value of 2 planets per star below a mass of
$5.2M_{\earth}$, which is roughly where @Cassan2012 lost sufficient
sensitivity to measure the mass function. For context, this saturation
value is comparable to the planet density of the inner solar system
between ${\sim}0.2$ and $2$ AU. We discuss the impact on our results of
more recent determinations of the mass ratio function in
[6](#discuss){reference-type="ref+label" reference="discuss"}. To
estimate the total number of planets *WFIRST* will detect we integrated
the resulting numbers using the trapezoidal rule; for the Cycle 7 design
this results in an expected total yield of ${\sim}1400$ planets, noting
that it does not include free-floating planets which would add a few
hundred to this figure [@Spergel2015]. This yield is smaller than
*Kepler*'s total yield, but of the same order of magnitude, suggesting
that a similar precision in demographics will be achievable.

![Number of detections as a function of planet mass for each
*WFIRST* design and for two different mass functions. Also shown is the
distribution of Kepler candidates assuming a mass-radius relation of
$(M/M_{\earth})=(R/R_{\earth})^{2.06}$ [@Lissauer2011]. Letters indicate
the masses of Solar System planets. The lower panel shows the yields of
the DRM designs relative to that of Cycle 7.](yieldplot.pdf){#yieldplot
width="\\columnwidth"}

[8](#yieldplot){reference-type="ref+label" reference="yieldplot"} shows
the simulation yields of
Tables [\[raw_table\]](#raw_table){reference-type="ref"
reference="raw_table"} and
[\[cassan_table\]](#cassan_table){reference-type="ref"
reference="cassan_table"} graphically, and compares them to *Kepler*. To
estimate the *Kepler* mass function we applied the simplistic
mass-radius $M_{\mathrm{p}}/M_{\earth}= (R_{\rm p}/R_{\earth})^{2.06}$
relation of @Lissauer2011 to the *Kepler* candidates with `koi_score`
$>0.5$.[^2] The first point to note is the large numbers of planets that
*WFIRST* is expected to detect, using any of the designs and across a
wide range of masses. As we discuss later, the cold planet mass function
below ${\sim}10M_{\earth}$ is almost completely unconstrained at
present, meaning that *WFIRST* will add at least two orders of magnitude
in mass sensitivity beyond current knowledge.

The lower panel of [8](#yieldplot){reference-type="ref+label"
reference="yieldplot"} compares the relative yields of the previous
*WFIRST* designs to the current Cycle 7 design as a function of planet
mass. Except for the highest mass planets, the Cycle 7 design
outperforms the IDRM and DRM2 designs in terms of planet detection
yield, though note that DRM2 had a significantly shorter total survey
duration. The DRM1 design has a ${\sim}10$ percent higher yield than the
current Cycle 7 design at low masses, but a larger difference at large
planet masses. The comparison of only the planet detection yields
between Cycle 7 and the ${\sim} 1$-m class designs is, however, unfair.
Cycle 7's 2.4-m mirror enables factor of ${\sim}2$ improvements in the
measurement of host and planet masses through lens flux, image
elongation and color-dependent centroid shifts [@Bennett2007], which the
planet detection yield alone does not account for. We will discuss these
measurements in [4.2](#properties){reference-type="ref+label"
reference="properties"}.

We have not shown the AFTA yields in
[8](#yieldplot){reference-type="ref+label" reference="yieldplot"}
because we consider them to be unrealistic. The significant drop in
yield from the AFTA design to Cycle 7 deserves some discussion, though.
While there were many changes between the designs, one change dominates
the reduction in yield. This was the adoption of more accurate estimates
of the slew and settle time of the spacecraft, and not a result of
descopes of mission hardware. For the AFTA designs, we had assumed
values for slew performance that were the same as for the smaller IDRM
and DRM designs, which was unrealistic given the larger mass and moment
of inertia associated with a larger mirror, secondary mirror support
structure, and spacecraft bus. Our AFTA results are further unrealistic,
because we applied the ${\sim}0.4\degr$ slew time to all slews between
fields, when some slews will be longer. These optimistic assumptions for
the previous designs, if corrected, would likely result in a less
optimal field layout and a reduction in yields, though perhaps
relatively smaller than the drop from AFTA to Cycle 7. If it were
possible to use attitude control systems that provide significantly
faster slew performance (e.g., control moment gyros instead of reaction
wheels), then significant gains in the yield of the
*WFIRST* microlensing survey could be realized.

## Sensitivity to moon-mass objects {#lowmass}

To trace out the approximate limits of the sensitivity of *WFIRST* to
low-mass planets, as well as wide and close separation planets, we ran
simulations on a grid in planet mass and semimajor axis over the ranges
$-2\le\log(M_{\mathrm{p}}/M_{\earth})<4$ and $-2\le\log(a/\text{AU})<2$.
We required that the events have impact parameters $|u_{\mathrm{0}}|<3$
and times of closest approach in the range
$0\le t_{\mathrm{0}}<2011$ days. The full details of the computations,
are described in [9](#curvecomp){reference-type="ref+label"
reference="curvecomp"}, including details of how false positive
detections due to numerical errors are accounted for. We note that the
simulations were conducted using the parameters of the AFTA design, but
we used the analytic estimate method described in
[5.1](#analytics){reference-type="ref+label" reference="analytics"} to
predict the yield of the Cycle 7 design from the AFTA design
simulations. Other than the change in field layout, there is only a
small change in exposure time for the analytic approximation to account
for, so we expect the uncertainty due to this conversion to be small.

![Comparison of the *WFIRST* Cycle 7 design sensitivity to that of
*Kepler* in the planet mass-semimajor axis plane. The red line shows an
approximation of the *Kepler* planet detection limit based on
@Burke2015. Blue shading shows the number of *WFIRST* planet detections
during the mission if there is one planet per star at a given mass and
semimajor axis point; this is directly proportional to the average
detection efficiency. The thick, dark blue line is an functional fit to
the 3-detection per mission contour, while the lighter blue line barely
visible beneath it is the actual contour. Red dots show Kepler candidate
and confirmed planets, black dots show all other known planets extracted
from the NASA exoplanet archive [accessed 28 Feb. 2018 @Akeson2013].
Blue dots show a simulated realization of the planets detected by the
*WFIRST* microlensing survey, assuming our fiducial planet mass function
([\[fiducialmf\]](#fiducialmf){reference-type="ref+label"
reference="fiducialmf"}), though note that in constructing this sample
of simulated detections we did not simulate planets smaller than
$0.03M_{\earth}$ or with semimajor axis less than $0.3$ AU. Solar system
bodies are shown by their images, including the satellites Ganymede,
Titan, and the Moon at the semimajor axis of their hosts. Images of the
solar system planets credit to NASA. The data and scripts used to make
this plot are available at
<https://github.com/mtpenny/wfirst-ml-figures>.](NRO_layout_7f_3_covfac_52_3_sensitivity.pdf){#sensitivity
width="\\textwidth"}

![Example lightcurve of a $0.025$-$M_{\earth}$ (Ganymede-mass) bound
planet detection from simulations of the AFTA design. Black and red data
points are in the $W149$ and $Z087$ filters, respectively. The blue
curve shows the underlying "true" lightcurve and the green line shows
the best fit single lens lightcurve.](ganymedemoon.pdf){#lightcurves
width="\\columnwidth"}

[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}
shows the results of the grid computation. The shading shows the planet
detection rate (in units of planets per full survey) at each
mass-semimajor axis point. *The blue sensitivity curve plots the
specific point in the mass-semimajor axis plane where 3 planet
detections can be expected in the course of the mission if there is one
such planet per star.* The sensitivity curve is also a line of constant
detection efficiency [e.g., @Peale1997]. We found that the sensitivity
curve is very well approximated by an analytic function
$$\begin{equation}
\log (M_{\mathrm{p}}/M_{\earth}) = \alpha + \beta\log (a/\text{AU}) + \gamma\sqrt{\delta^2+[\log (a/\text{AU})-\epsilon]^2},
\label{senscurve}
\end{equation}$$ where $a$ is the semimajor axis and the parameters take
the following values: $\alpha = -3.90$, $\beta = -1.15$, $\gamma=3.56$,
$\delta=0.783$, $\epsilon=0.356$. The analytic function (bright blue) is
plotted above the sensitivity curve data (pale blue) in the figure, but
the sensitivity data curve is almost invisible underneath the analytic
fit. It is interesting to note that seven of the eight Solar System
planets fall within the *WFIRST* sensitivity curve, with only Mercury
outside. However, in place of Mercury, when we place the Solar System's
moons on the diagram at the orbital separations of their host planets,
the Galilean moon Ganymede lies just within the sensitivity curve.
[10](#lightcurves){reference-type="ref+label" reference="lightcurves"}
shows an example lightcurve of such a Ganymede-mass exoplanet that
*WFIRST* could detect. If the Solar System moons were placed at the
minimum point of the analytic curve ($a=4.2$ AU, $M=0.021M_{\earth}$),
Ganymede ($0.025M_{\earth}$) and Titan ($0.023M_{\earth}$) would be
above the curve and Callisto ($0.018M_{\earth}$), Io ($0.015M_{\earth}$)
and the Moon ($0.012M_{\earth}$) would be below it; all other known
Solar System bodies have masses less than $0.01M_{\earth}$. At
$1M_{\earth}$, the sensitivity curve stretches from $0.5$ AU to $70$ AU.
Removing the constraint that the impact parameter of the host star's
microlensing event be $|u_{\mathrm{0}}|<3$ results in there being no
upper limit on the semimajor axis at which AFTA has sensitivity to
Earth-mass planets. However, most of these more distant planets would be
seen as free-floating planet candidates due to undetectable
magnification from the source star [see @Henderson2016-char for a
discussion of constraining the presence of host stars in free-floating
planet candidate events].

The shading in [9](#sensitivity){reference-type="ref+label"
reference="sensitivity"} does not accurately represent the distribution
of planets that we can expect to detect with *WFIRST*, only *WFIRST*'s
sensitivity to planets. *WFIRST* has a high-detection efficiency for
large-mass planets, but these have consistently been shown to be
rare [e.g.,
@Cumming2008; @Howard2010; @Cassan2012; @Fressin2013; @Shvartzvald2016; @Suzuki2016].
To give a better idea of the distribution of planet detections
*WFIRST* will detect, we simulated a survey with planets populated from
our fiducial mass function. A realization from this simulation is shown
as the blue dots in [9](#sensitivity){reference-type="ref+label"
reference="sensitivity"}. Note that the lower mass limit for this
simulation was $M_{\mathrm{p}}=0.03M_{\earth}$ and the smallest
semimajor axis was $0.3$ AU, so a small number of the most extreme
planets that could be detected will be missing from this realization. In
adding these simulated planets to the plot, we do not account for the
uncertainty in measurements of either $M_{\mathrm{p}}$ or $a$. We expect
the majority of *WFIRST*'s planets to have mass measurements from either
lens-detection measurements or parallax, so given the large range of
masses covered, uncertainties in $M_{\mathrm{p}}$ would not result in a
significant change of appearance, and features in the planet mass
function should be easily distinguishable. With a mass measurement also
comes a measurement of the physical Einstein radius, and so the physical
projected separation of the planet and star. This must be deprojected to
the actual semimajor axis, which will result in a substantial
uncertainty in the estimated value of $a$ relative to the range of $a$,
though for some planets orbital motion measurements can better constrain
$a$ [e.g., @Bennett2010; @Penny2011-om]. Our simulations do not include
an eccentricity distribution, so we can not estimate the uncertainty
associated with this deprojection.

<figure id="exlc">
<p><embed src="c62cassan_84_75_1226.pdf" style="width:49.0%" /> <embed
src="c62cassan_31_99_1606.pdf" style="width:49.0%" /><br />
<embed src="c62cassan_75_5_193.pdf" style="width:49.0%" /> <embed
src="c62cassan_54_33_566.pdf" style="width:49.0%" /><br />
<embed src="c62cassan_80_32_311.pdf" style="width:49.0%" /> <embed
src="c62cassan_16_72_192.pdf" style="width:49.0%" /></p>
<figcaption>Examples of simulated <em>WFIRST</em> lightcurves using the
Cycle 7 design parameters, chosen to display the some of the variety of
lightcurve features that <em>WFIRST</em> will detect, or challenges that
will impact the analysis of events. The examples demonstrate a
lightcurve with missing peak data due to <em>WFIRST</em>’s limited
observing seasons (<em>top left</em>), an Earth-mass planet orbiting a
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0.15</mn><msub><mi>M</mi><mo>⊙</mo></msub></mrow><annotation encoding="application/x-tex">0.15M_{\odot}</annotation></semantics></math>
star at
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics></math> AU
(<em>top right</em>), a wide orbit planet with a very low amplitude host
microlensing event (<em>middle left</em>), an event with a very faint
source and high blending (<em>middle right</em>), a high signal to noise
detection of a massive planet (<em>bottom left</em>), a low signal to
noise detection of a massive planet on a wide orbit (<em>bottom
right</em>).</figcaption>
</figure>

## Properties of the *WFIRST* microlensing events {#properties}

<figure id="sourcemag">
<p><embed src="cycle7_magdist.pdf" /> <embed
src="cycle7_fshist.pdf" /></p>
<figcaption><em>Top</em>: The distribution of source magnitudes for
different subsets of the simulated microlensing events. “All
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>μ</mi><annotation encoding="application/x-tex">\mu</annotation></semantics></math>L”
is the distribution of all simulated microlensing events, “Detected
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>μ</mi><annotation encoding="application/x-tex">\mu</annotation></semantics></math>L”
is the distribution of events with flux variation detected at
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">Δ</mi><msup><mi>χ</mi><mn>2</mn></msup><mo>&gt;</mo><mn>500</mn></mrow><annotation encoding="application/x-tex">\Delta\chi^2&gt;500</annotation></semantics></math>
above a flat baseline, and “Detected planets” is the distribution for
events with
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><msub><mi>M</mi><mi>♁</mi></msub></mrow><annotation encoding="application/x-tex">1M_{\earth}</annotation></semantics></math>
planet detections. Each distribution is on its own arbitrary scale.
<em>Bottom:</em> The distribution of the fraction of baseline flux
contributed by the source, <span class="math inline">$f_{\rm s}$</span>.
Again, each distribution has been arbitrarily scaled.</figcaption>
</figure>

The *WFIRST* microlensing survey will search for microlensing events
from fainter sources than are observed from the ground, and its
resolution will be sufficient to at least partially resolve lenses and
sources over the course of the 5 year mission, so it is important to
consider the properties of the sources, lenses and blending.
[12](#sourcemag){reference-type="ref+label" reference="sourcemag"} plots
the distribution of source magnitudes and blending of the microlensing
events that the Cycle 7 design will be able to observe. In both plots we
show the distribution for every microlensing event that occurs in the
*WFIRST* field on sources brighter than $H_{\mathrm{Vega}}=25$,
regardless of whether it will be detected or not (labeled all $\mu$L),
the events that cause a microlensing event that is detectable as a
$\Delta\chi^2>500$ deviation from a flat baseline (labeled detected
$\mu$L), and the events with detectable Earth-mass planets (labeled
detected planets).

While the number of all microlensing events per magnitude keeps rising
beyond a magnitude of $W149=25$, the number of detectable microlensing
events exhibits a broad peak between $W149=22$ and 24, before beginning
to fall. For planet detections, the source magnitude distribution peaks
between $W149\approx20$--$22$, but only begins to fall rapidly fainter
than $W149\approx 24$.

The lower panel of [12](#sourcemag){reference-type="ref+label"
reference="sourcemag"} shows the distribution of blending. The blending
parameter $f_{\mathrm{s}}$ is the ratio of source flux to total flux in
the photometric aperture when the source is unmagnified. We have
measured $f_{\mathrm{s}}$ in the same $3\times 3$ pixel aperture we have
used for photometry. Being as the input source magnitude distribution
continues to rise towards faint magnitudes, the majority of microlensing
events we simulated were significantly blended (i.e,
$f_{\mathrm{s}}<0.5$), despite *WFIRST*'s small PSF. This is also the
case for microlensing events that *WFIRST* will detect, though the
distribution $\mathrm{d}N/\mathrm{d}\log f_{\mathrm{s}}$ does peak above
$f_{\mathrm{s}}=0.5$. For events with planets detected, the distribution
of $f_{\mathrm{s}}$ is much more skewed towards small amounts of
blending $f_{\mathrm{s}}\sim 1$, but there remains a significant tail
with large amounts of blending.

![Cumulative distribution of the contribution of the lens flux to the
total blend flux in a $3\times3$ pixel aperture around events with
detected planets. The vertical line shows the point at which the lens
provides more than $50$% of the flux.](lens_over_blend.pdf){#lensblend
width="\\columnwidth"}

Figure [13](#lensblend){reference-type="ref" reference="lensblend"}
shows the relative contribution of the lens star to the total blend flux
for detected planets. In fewer than $20$% of events with planet
detections does the lens flux dominate the blended light. However, the
majority events will have a lens flux within a factor of 10 of the total
blend flux. Without knowing the nature of the blended light (i.e., is it
due to the PSF wings of bright stars, or nearby fainter stars), it is
difficult to say more about how this added confusion will affect host
mass measurements via lens detection [see, e.g.,
@Bennett2007; @Henderson2014-ao; @Bennett2015].

![Plot of the lens-source relative proper motion plotted against the
lens-source brightness contrast for the simulated planet sample from
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}.
Horizontal lines are spaced vertically by the proper motion required for
the separation to change by ${\sim}0.1\times$ the PSF FWHM in 4.5 years,
the spacing between the first and last microlensing season. Histograms
on each axis show the marginalized distributions. Note that
$\mu_{\mathrm{rel}}$ has not been corrected for the BGM1106's high
proper motion dispersions as discussed in
[6.2.2](#kinematics){reference-type="ref+label"
reference="kinematics"}.](contrast2.pdf){#contrast
width="\\columnwidth"}

[14](#contrast){reference-type="ref+label" reference="contrast"} shows
the joint distribution of the lens-source brightness contrast and the
lens-source relative proper motion for the simulated sample shown in
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}.
These are the two intrinsic properties of the event that have the
largest impact on whether *WFIRST* will be able to characterize the lens
through detection of lens flux and motion relative to the source. The
proper motions are not corrected in any way for the overly large proper
motion dispersions in the BGM1106's bulge stars, which cause
$\mu_{\mathrm{rel}}$ to be ${\sim}15$--$25$% too large (see
[6.2.2](#kinematics){reference-type="ref+label" reference="kinematics"}
for a detailed discussion). Regardless of this, it can be seen that the
majority of source-lens pairs will separate by ${\sim}10$ percent of the
FWHM of the PSF in the course of the mission, and few cases will
separate by more than half the PSF FWHM. By carefully modeling the PSF
and the motion of the source and lens, it will be possible to measure
lens fluxes and lens-source separations when the separation is
significantly smaller than the PSF [see, e.g.,
@Bennett2007; @Henderson2014-ao; @Bennett2015]. We leave it to future
work to simulate these measurements.

![Cumulative distribution of source diameter crossing times $2t_*$ for
events with $1M_{\earth}$ planet detections and high-magnification
events with $|u_{\mathrm{0}}|<0.05$. Vertical lines indicate multiples
of the 15-min observing cadence. Most events will have at least one
measurement per source diameter crossing time.](tstar.pdf){#sourcecross
width="\\columnwidth"}

The final property of *WFIRST* events we shall examine is the source
diameter crossing time $2t_*$, where $t_*$ is the time taken for the
source (relative to the lens) to traverse its radius. This is important
to consider, because, in addition to the requirement of sampling the
planetary perturbation, the cadence must be chosen to also sample any
finite source effects, which can be used to measure the angular Einstein
radius [e.g., @Nemiroff1994; @Yoo2004]. With *WFIRST* being sensitive to
fainter, and thus smaller, source stars than any previous microlensing
survey, there is a possibility that assumptions about the required
cadence overlooked this fact. It is especially important to consider as
@Chung2017 have identified a degeneracy in measuring $2t_*$ for some
single lens events when only a single measurement is affected by finite
source effects. [15](#sourcecross){reference-type="ref+label"
reference="sourcecross"} shows the cumulative distribution of $2t_*$ for
events with $1M_{\earth}$ planet detections, and for high magnification
events with $|u_{\mathrm{0}}|<0.05$, compared to the cadence of the
*WFIRST* microlensing survey observations. Over 80% of events with
planet detections will have at least two points per $2t_*$, and over 70%
will have three points per $2t_*$. This is likely an underestimate
because we expect $2t_*$ to be longer than simulated due to the
overestimated velocity dispersion of the BGM1106's bulge.
High-magnification events detected by *WFIRST* will tend to have shorter
$2t_*$ because they can be detected on fainter source stars on average.
Even so, ${\sim}60$% of events will be guaranteed two observations per
$2t_*$ and more than this can expect two measurements more often than
not in any given $2t_*$-long time interval. Free-floating planet events
will have brighter sources than high-magnification stellar microlensing
events on average, so we conclude that for most events $15$ min cadence
is sufficient to avoid the possible source radius measurement degeneracy
[identified by @Chung2017] when there are only a small number of
photometric measurements over the part of the lightcurve affected by
finite source effects.

# Evaluating the effect of changes to mission design on planet yields {#tradeoffs}

The design of any space mission must balance capabilities with cost.
*WFIRST* straddles the boundary between a targeted, single-goal mission
for which a focused set of hardware can be optimized within a relatively
constrained parameter space, and a general purpose observatory where the
breadth of capabilities should be optimized. Combined, *WFIRST*'s
primary missions present a relatively broad scope for optimization,
though the synergies between the observational requirements of each
survey and current economic considerations constrain this scope
considerably. In this section we consider the effect of changes in the
design of the spacecraft and the survey it carries out on the overall
planet yields. We begin by outlining how changes can be quickly
estimated analytically in [5.1](#analytics){reference-type="ref+label"
reference="analytics"}, present the results of two trade study
simulations that we use to test the analytic estimates in
Sections [5.2](#bandtrade){reference-type="ref" reference="bandtrade"}
and [5.3](#bgtrade){reference-type="ref" reference="bgtrade"}, and then
apply the analytic estimates to optimize the field choice for the
*WFIRST* Cycle 7 design in [5.4](#fieldopt){reference-type="ref+label"
reference="fieldopt"}.

## Analytic estimates of the change in yield {#analytics}

<figure id="nvdc2">
<embed src="cycle6_chi2dist.pdf" />
<p>. <span id="nvdc2" data-label="nvdc2"></span></p>
<figcaption>The cumulative distribution of
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">Δ</mi><msup><mi>χ</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">\Delta\chi^2</annotation></semantics></math>
for different planet masses (solid black lines) ranging from
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>0.1</mn><annotation encoding="application/x-tex">0.1</annotation></semantics></math>
to
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1000</mn><msub><mi>M</mi><mi>♁</mi></msub></mrow><annotation encoding="application/x-tex">1000M_{\earth}</annotation></semantics></math>
in factor-of-ten steps. Gray dashed lines show the power law fits to the
cumulative distributions over a factor of two above and below the
adopted
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">Δ</mi><msup><mi>χ</mi><mn>2</mn></msup><mo>=</mo><mn>160</mn></mrow><annotation encoding="application/x-tex">\Delta\chi^2=160</annotation></semantics></math>
threshold (as indicated by the vertical dashed lines). The slopes of the
fits are listed in <a href="#chi2alpha" data-reference-type="ref+label"
data-reference="chi2alpha">2</a></figcaption>
</figure>

+:-------------------+:-------:+:-------:+:-------:+:-------:+:-------:+
| Mass               | $\alpha$                                        |
| ($M_{\earth}$)     |                                                 |
+--------------------+---------+---------+---------+---------+---------+
|                    | IDRM    | DRM1    | DRM2    | AFTA    | Cycle 7 |
+--------------------+---------+---------+---------+---------+---------+
| $0.1$              | $0.674$ | $0.473$ | $0.520$ | $0.513$ | $0.534$ |
+--------------------+---------+---------+---------+---------+---------+
| $1$                | $0.420$ | $0.364$ | $0.355$ | $0.366$ | $0.399$ |
+--------------------+---------+---------+---------+---------+---------+
| $10$               | $0.324$ | $0.290$ | $0.296$ | $0.310$ | $0.313$ |
+--------------------+---------+---------+---------+---------+---------+
| $100$              | $0.315$ | $0.246$ | $0.241$ | $0.265$ | $0.245$ |
+--------------------+---------+---------+---------+---------+---------+
| $1000$             | $0.268$ | $0.212$ | $0.212$ | $0.223$ | $0.227$ |
+--------------------+---------+---------+---------+---------+---------+
| $10000$            | $0.201$ | $0.168$ | $0.151$ | $0.193$ | $0.204$ |
+--------------------+---------+---------+---------+---------+---------+

: Power law slopes fitted to the cumulative $\Delta\chi^2$ distributions
{#chi2alpha}

[]{#chi2alpha label="chi2alpha"}

It is possible to estimate the effect of a change in the design of
hardware or survey strategy on the total planet yield without performing
a full simulation. The only detection criteria we use for bound planets
is a cut on $\Delta\chi^2$. Therefore, the distribution of
$\Delta\chi^2$ combined with a model of how $\Delta\chi^2$ changes with
design can be used to estimate a change in yield. The cumulative
distribution of the number of planet detections with $\Delta\chi^2$
greater than a threshold $X$, $N(\Delta\chi^2>X)$, can be approximated
locally by a power law [e.g., @Bennett2002] $$\begin{equation}
N(\Delta\chi^2>X) \propto X^{-\alpha},
\label{dchi2plaw}
\end{equation}$$ as can be seen in
[16](#nvdc2){reference-type="ref+label" reference="nvdc2"}; the fitted
slopes are listed in [2](#chi2alpha){reference-type="ref+label"
reference="chi2alpha"}. The slope of the power law $\alpha$ is a
function of both the planet mass and semimajor axis of the planetary
companion. The range of validity of the approximation can extend by more
than an order of magnitudes in $\Delta\chi^2$ in some cases, though for
planets close to the edges of *WFIRST*'s parameter space it becomes
increasingly inaccurate. Finally, if one knows the ratio of the new
$\Delta\chi^2$ to the old $$\begin{equation}
\delta = \Delta\chi_{\mathrm{new}}^2/\Delta\chi_{\mathrm{old}}^2,
\end{equation}$$ then from
[\[dchi2plaw\]](#dchi2plaw){reference-type="ref+label"
reference="dchi2plaw"} the estimate of the yield for the new design
$N_{\rm new}$ is simply $$\begin{equation}
N_{\mathrm{new}} \approx N_{\mathrm{old}}\delta^{\alpha}.
\label{newyield}
\end{equation}$$ To increase the range of validity of the approximation
a higher order polynomial could be fit to the local cumulative
$\Delta\chi^2$ distribution in $\log$-$\log$ space, or the full
$\Delta\chi^2$ distribution could be used to directly evaluate the
change in yield that corresponds to a given change in $\Delta\chi^2$; we
assess these options in [5.4](#fieldopt){reference-type="ref+label"
reference="fieldopt"}.

We can calculate $\delta$ for two scenarios by computing the
signal-to-noise ratios ($SNR$) for each scenario, because if the signal
is constant $\Delta\chi^2\propto(SNR)^2$. The signal-to-noise ratio
$SNR$ of each photometric measurement is $$\begin{equation}
SNR = \frac{N_{\mathrm{s}}}{\sqrt{N_{\mathrm{s}}+N_{\mathrm{BG}}+\sigma_{\mathrm{det}}^2+\sigma_{\mathrm{sys}}^2}},
\label{snr}
\end{equation}$$ where $N_{\mathrm{s}}$ is the number of photons from
the source, $N_{\mathrm{BG}}$ is the number of detected photons from
blended stars and smooth backgrounds, $\sigma_{\mathrm{det}}$ is the
uncertainty on the total number of counts due to readout noise, dark
current, thermal photons from the spacecraft and other detector effects,
and $\sigma_{\mathrm{sys}}$ is a systematic error component, which in
this paper we assume is a small constant ($0.001$) multiplied by
$N_{\mathrm{s}}$. Each element of the $SNR$ will scale differently as
parameters of the telescope or survey change, and in general will be a
function of magnification that will be different for each microlensing
event. It will therefore be difficult to estimate the average ratio of
$\Delta\chi^2$s because $SNR$ will not be a simple function of the
changing parameters. However, each of the $N$ terms in the equation
scale linearly with the photon collection efficiacy of each scenario, so
if both of the $\sigma^2$ components are small and there is nothing to
change the ratio of source to background between the different
scenarios, the ratio of signal to noise will scale as the square root of
photon collection efficacy and so $\delta$ will scale linearly. This
will be the case if the only the exposure time were to change, but not
if the mirror diameter were changed, because in the latter case the
mirror diameter affects the resolution and hence the ratio of source to
background photons will change from event to event.

The concept can be illustrated by an example. We may be interested in
how the planet yield would be affected if the observation cadence was
halved, keeping all else fixed for this example. On average, halving the
number of data points will halve the $\Delta\chi^2$. However, halving
the cadence allows the exposure time to be increased by a factor of
$(2t_{\mathrm{exp}}+t_{\mathrm{ohead}})/t_{\mathrm{exp}}=2.73$ for
*AFTA*, which assuming that systematic errors and detector noise are
negligible, increases the per-exposure signal to noise by
$\sqrt{2.73}=1.65$. Overall then the $\Delta\chi^2$ will increase by a
factor of $\delta = 1.65^2/2=1.37$. Without worrying about the
normalization of the power law in
[\[dchi2plaw\]](#dchi2plaw){reference-type="ref+label"
reference="dchi2plaw"}, we can estimate that relative to the fiducial
case, halving the cadence will result in a yield that is a factor
$N_{\mathrm{cadence}/2}/N_{\mathrm{cadence}} \approx 1.37^{\alpha}$
times larger than the fiducial yield. So, for the examples shown in
[16](#nvdc2){reference-type="ref+label" reference="nvdc2"}, halving the
cadence would result in an increase in yields of
$100$%$\times (1.37^{\alpha}-1) \approx 9$% for $100M_{\earth}$-mass
planets where $\alpha=0.270$. For Earth-mass planets where
$\alpha=0.379$, the increase would be $13$%.

Note, however, that the above example also presents a cautionary tale.
In our pursuit of larger $\Delta\chi^2$, we have neglected the role of
sampling. In order for each planet detection to be useful for
demographic studies, we not only need to detect a deviation from a
single-lens microlensing lightcurve at a specified significance, we also
need to be able to fit the lightcurve with a unique planetary model and
be sure that the deviation is not caused by systematics in the data. By
halving the number of data points over a potentially short-lived
planetary deviation, we have significantly degraded our power to reject
systematic errors and to constrain our lightcurve model. These effects
could ultimately reduce the number of useful detections by a factor
larger than the increase in detections due to the improvement in the
average $\Delta\chi^2$. We must therefore take care to not over
interpret any of the results in this section. To properly assess the
impact of changes in design therefore requires even more detailed
simulations than we have conducted here, that assess not only the
detection significance but also the level to which events can be
characterized. However, with sensible restrictions on the survey design
in place to ensure that detected events will be well characterized (such
as restrictions on the minimum cadence), these simulations and analytic
estimates can provide useful insight into the effect of design
trade-offs.

## Testing Analytic Estimates: Bandpass {#bandtrade}

The filter bandpass primarily effects the amount of light that reaches
the detector, but also influences the width of the PSF. Therefore, the
actual effect of the bandpass on the photometric precision will change
from event to event due to the differing colors of the source, lens,
background and any blended stars, as well as differing amounts of
reddening.

*WFIRST*'s HgCdTe detectors can be designed to have a specified red
cutoff wavelength, with options in the range of $2.0$--$2.4$ microns
considered for *WFIRST*. Longer cutoff wavelengths allow for larger
total throughputs in the wide microlensing band, as well as a longer
wavelength baseline for its more standard filters [@Green2012]. However,
this added capability comes at the cost of additional spacecraft and
instrument cooling that is needed to reduce the thermal background
emitted by the mirrors and other components in the optical path.

To test the impact of bandpass on the planet yield of the
*WFIRST* microlensing survey, we ran simulations of DRM1 with $2.0$ and
$2.4$ $\mu$m cutoff detectors, using $W149$ and $W169$ filters,
respectively. This scenario is also ideal for quantitatively testing the
validity of our analytic relative yield estimates. It should be possible
to approximate the effect of the bandpass to zeroth order by just
considering the total photon throughput for a source with a spectrum
that is representative of sources that will be observed. To test this
assumption, we ran an additional simulation that used the $W169$ filter,
but the $W149$ zeropoint magnitude, which we will refer to as
$W169^{\prime}$.

  Simulation name   $W149$   $W169^{\prime}$   $W169$
  ----------------- -------- ----------------- --------
  Zeropoint (mag)   26.377   26.377            26.636
  Filter            $W149$   $W169$            $W169$
  Simulation        0.910    0.915             1
  Prediction        0.901    0.917             ---

  : Relative yield of $1M_{\earth}$ planets for DRM1 comparing $W149$
  and $W169$ bandpasses. {#bandpasssim}

**Notes**: Yields are given relative to the standard $W169$ simulation.
The $W169^{\prime}$ simulation uses the $W169$ filter, but a total
throughput (zeropoint) equal to the $W149$ simulation. The filter
determines the PSF, brightness of stars relative to the zeropoint
magnitude and the surface brightness of the zodiacal light.

The relevant parameters and relative yields of these simulations are
listed in [3](#bandpasssim){reference-type="ref+label"
reference="bandpasssim"}. All other parameters between the three
simulations are identical. We note that we should have reduced the
amount of thermal noise in the $W149$ simulation, but neglected to do
so. Fortunately, this mistake has essentially no effect on the result
because blended light and sky background dominate over the detector
noise for detector noise levels this low. The $W149$ bandpass results in
a drop in yield of $9.0$ percent relative to the $W169$ bandpass.
Because each simulation used the same set of simulated events, the
statistical uncertainty in the relative yields is significantly smaller
than the $1$ percent Poisson uncertainty on the total yield.

We predicted the relative yield using the analytic formalism from
[5.1](#analytics){reference-type="ref+label" reference="analytics"}. If
we ignore detector and systematic noise sources, and assume that both
blend stars and source stars have the same color, then the ratio of
$\Delta\chi^2$ between $W149$ and $W169$ will depend only on the
difference in zeropoints and the assumed $W149-W169$ color, which we
take to be $W149-W169=0.052$, which is the median of source colors for
the planets detected in the $W169$ simulation. Therefore,
$\log\delta=-0.4(0.259+0.052)=-0.12$, and the predicted reduction in
yield for $W149$ relative to $W169$ is $(\delta^{\alpha}-1)=9.9$ percent
for the $1$-$M_{\earth}$ DRM1 value of $\alpha=0.364$, which is in
reasonable agreement with the simulation's value of $9.0$ percent. This
estimate does not account for the reduced blending in $W149$ thanks to
the narrower PSF, which might explain why the analytic estimate predicts
a slightly larger drop in yield than the simulation produces. The same
calculation for the $W169^{\prime}$ simulation that only changes the
zeropoint of the $W169$ simulation, predicts a drop in yield of
$8.3$ percent compared to the actual simulation result of $8.5$ percent,
and is thus a much closer match. The $W169^{\prime}$ simulation shows
that the majority of the change in yields is due to the change in
zeropoint associated with a change in bandpass. However, because of the
relatively shallow slope of the $\Delta\chi^2$ distribution, even a
relatively significant change in bandpass (${\sim}40$ percent) results
in a significantly smaller change in planet yield (${\sim}10$ percent),
at least for Earth-mass planets. While we have only simulated the impact
for Earth-mass planets, having validated the analytic approximation of
the yield change, we can apply it to other planet masses. For example,
we predict that switching to a $2.0$ $\mu$m cutoff for DRM1 would reduce
$0.1$-$M_{\earth}$ yields by $13$ percent.

## Testing Analytic Estimates: Background light {#bgtrade}

![Relative yield of $1$-$M_{\earth}$ planets in the presence of elevated
smooth backgrounds. Data points are the results of our simulation and
the solid black line is our analytic prediction adopting values of the
average surface brightness of blend stars
$W149_{\rm blend}=19.2$ mag arcsec$^{-2}$ and the average source star
brightness $W149_{\rm s}=22$. Red and blue dashed and dotted lines show
the impact of changing the values of these parameters by
$\pm 1$ mag arcsec$^{-2}$ or $\pm 1$ mag,
respectively.](highbg.pdf){#highbg width="\\columnwidth"}

While there is nothing that one can do to control the amount of
astrophysical background light that enters the telescope from diffuse
backgrounds, it is nevertheless important to consider the effect that
varying levels of background have on the yield of the survey. To
investigate the impact of the zodiacal light -- the dominant smooth
background -- and its variations over the course of the *WFIRST* survey
we implemented a time- and position-dependent model of the zodiacal
light that is described in [8.2](#zodi){reference-type="ref+label"
reference="zodi"}. We found the impact of variations in the zodiacal
light over the course of *WFIRST*'s 72-day seasons to be negligible on
the overall yields. We also investigated the impact of adding additional
smooth backgrounds to the images. This can be used to estimate the
impact of observing when the moon lies near to the microlensing fields
(if *WFIRST* is in a geosynchronous Earth orbit, as was baselined for
early versions of the 2.4-m design).
[17](#highbg){reference-type="ref+label" reference="highbg"} shows the
yield of Earth-mass planets in $0.3$--$30$ AU orbits as a function of
the surface brightness of the added background relative to the case with
just zodiacal light (which is $W149 \approx 21.5$ mag arcsec$^2$). The
yield drops steadily as the background surface brightness increases, but
the drop is not severe unless the additional background is very bright.
In order to cut the yields in half, the additional background must
exceed the zodiacal light by a factor of ${\sim 80}$. This test is also
relevant to increased thermal noise backgrounds for differing telescope
and instrument operating temperatures, and the choice of whether to
include a cold pupil mask on the $W149$ filter.

To test the analytic estimate, we assumed that a typical source will
have a magnitude of $W149_{\rm s}=22$ (the peak of the detected
microlensing event source magnitude distribution, see
[12](#sourcemag){reference-type="ref+label" reference="sourcemag"}) and
that the influence of blended stars would be a smooth background of
$W149_{\rm blend}=19.2$ mag arcsec$^{-2}$, based on summing up the flux
of stars in BGM1106 with magnitudes $H_{\mathrm{Vega}}>15$ . Each
simulated scenario used the same set of microlensing events, meaning
that the uncertainty on the relative yield was significantly smaller
than the Poisson uncertainty on any of the individual simulations. To
compute the uncertainty on the relative yields, we split the simulated
sample into 10 parts and computed the variance in relative yield
measured for each of the subsamples.

There is good qualitative agreement between the analytic estimate and
the simulation results, but, moving from right to left in the plot, the
relative detection rate for analytic estimate falls off less quickly
than the simulations until providing a better match at backgrounds
brighter than $W149=18$ mag arcsec$^{-2}$. Additionally, our analytic
estimate depends on two model parameters (the typical source magnitude
and the effective surface brightness of unresolved and blended stars).
We appear to have chosen their values well, but the choices we made were
somewhat arbitrary, and other choices could have been justified. This
demonstrates that care needs to be taken when using analytic estimates
without simulations to anchor them.

## Applying analytic estimates: Optimizing Field Selection for Cycle 7 {#fieldopt}

More accurate models of the mass, inertia and reaction wheel complement
of the spacecraft led to significantly longer estimates of the slew and
settle time for the spacecraft in Cycle 7. This prompted us to perform a
more detailed accounting of the survey's overheads and a re-optimization
of the number and placement of the survey's fields. This process relied
on analytic yield change estimates to quickly assess the yield for a
large number of potential exposure times as described below. To simplify
the optimization process, we constrained the cadence to be fixed at 15
minutes, and optimized only for the yield of Earth-mass planets in a
broad range of orbits (i.e., with $a$ logarithmically distributed
between $0.3$ and $30$ AU).

![The fractional error of analytic yield estimates compared to actual
simulated yields for simulations with different exposure times, and all
else held fixed (including cadence). Analytic estimates of the yield
were computed based on the cumulative $\Delta\chi^2$ distributions of
simulations run using 52 s (open circles) and 130 s exposure times
(filled circles) for the main $W149$ survey observations. The
$\Delta\chi^2$ distribution was modeled by linear fits to the cumulative
$\Delta\chi^2$ distribution, quadratic fits to the distribution, and
direct evaluation of the distribution (indicated by point
color).](chi2dist_comp.pdf){#chi2test width="\\columnwidth"}

Before beginning the optimization process, we took heed of our above
warning to treat the analytic yield change estimates carefully. To test
the accuracy of the analytic yield estimates, we simulated identical
surveys using the Cycle 7 mission parameters at four different exposure
times spanning the expected range of values to be seriously considered
in the optimization exercise: $26, 52, 104$ and $130$ s. We used the
$\Delta\chi^2$ distributions of the $130$ s and $52$ s simulations to
predict the yield of each other simulation. We used both a linear (i.e.,
power law), and a quadratic fit to $\log N(\Delta\chi^2>X)$ vs
$\log \Delta\chi^2$, as well as a direct evaluation of the cumulative
$\Delta\chi^2$ distribution. The results are shown in
[18](#chi2test){reference-type="ref+label" reference="chi2test"}. No
particular method of estimating the change in yield showed consistently
better accuracy. The error in the approximation grew by ${\sim}5$% for
every factor of two change in exposure time, whether the $52$ s or
$130$ s simulations were used as the basis of the approximation. This
level of inaccuracy is a reasonable price to pay for the computational
cost savings the method provides.

Unlike with the previous designs, we evaluated the cumulative slew time
for a given set of fields using estimates of the cumulative slew, settle
and detector reset time as a function of slew angle provided by the
*WFIRST* project office. This calculation was done for a large number of
candidate field layouts with varying geometries and numbers of fields,
with the best path being selected by brute force solution of the
traveling salesman problem. The exposure time was divided evenly between
the number of fields from the remainder of 15 minute cadence minus the
total slew time. We constructed a map of the $1$-$M_{\earth}$ planet
detection rate per unit area for each candidate layout's exposure time
$t_{\rm exp}$ by direct evaluation of the $52$ s simulation's cumulative
$\Delta\chi^2$ distribution at $X=52 \text{s}/t_{\rm exp}$ individually
for each sight line in the map. The total number of detections for a
each layout was then evaluated using polygon clipping [@gpc] to estimate
the fraction of the area represented by each sight line that falls
within a given chip of each field.

<figure id="nfields">
<p><embed src="cycle6_nfields.pdf" /><br />
<embed src="cycle6_nfields_all.pdf" /><br />
</p>
<figcaption><em>Top</em>:
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>1</mn><annotation encoding="application/x-tex">1</annotation></semantics></math>-<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>M</mi><mi>♁</mi></msub><annotation encoding="application/x-tex">M_{\earth}</annotation></semantics></math>
planet yield as a function of the number of fields for simulations of
the Cycle 7 design, the Cycle 7 design with a failed reaction wheel, and
the overly-optimistic AFTA slew times. Several possible layouts are
considered for each number of fields. <em>Bottom</em>: The planet yield
relative to the adopted field layout (see <a href="#fieldplacement"
data-reference-type="ref+label" data-reference="fieldplacement">7</a>)
as a function of the number of fields for the nominal Cycle 7 slew times
and for
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>0.1</mn><annotation encoding="application/x-tex">0.1</annotation></semantics></math>-,
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>10</mn><annotation encoding="application/x-tex">10</annotation></semantics></math>-,
and
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mn>1000</mn><annotation encoding="application/x-tex">1000</annotation></semantics></math>-<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><msub><mi>M</mi><mi>♁</mi></msub><annotation encoding="application/x-tex">M_{\earth}</annotation></semantics></math>
planets. Different numbers of fields would maximize the yield for
different planet masses.</figcaption>
</figure>

The results of the optimization exercise are shown in the top panel of
[19](#nfields){reference-type="ref+label" reference="nfields"} for three
different slew time versus slew angle profiles: the first is a constant
slew, settle and reset time of $38$ s independent of slew distance (this
was assumed in the AFTA simulations), and the other two profiles are for
*WFIRST* Cycle 7 with all of its reaction wheels operational and with
one reaction wheel inoperable. For each number of fields, we consider
several possible layouts. For the AFTA slew times, the optimum number of
fields was 10 or larger (we did not consider layouts with more than 10
fields). For more realistic Cycle 7 slew times there is a broad optimum
of between 5 and 8 fields. We adopt a slightly sub-optimal field layout
of 7 fields (shown in [7](#fieldplacement){reference-type="ref+label"
reference="fieldplacement"}) to allow for some margin in yields. Note
that the relatively coarse resolution of our event rate map,
uncertainties in the yields for each sight line, and use of the analytic
yield estimates prevent accurate determination of the true optimum field
layout within the broad optimum we find. With one reaction wheel
in-operational the optimum number of fields would be fewer, at 5 or 6.
This optimum is somewhat sharper than the optimum for all wheels
operational. The factor of ${\sim}2.2$ reduction in estimated slew
performance between AFTA and Cycle 7 results in a large reduction in
planet yield of ${\sim} 50$%, which accounts for essentially all of the
difference between the AFTA and Cycle 7 yields that we find. The optimum
number of fields will depend on planet mass, as shown in the lower panel
of [19](#nfields){reference-type="ref+label" reference="nfields"} shows
the yield as a function of field number for $0.1$-, $10$-, and
$1000$-$M_{\earth}$ planets.

# Discussion {#discuss}

The statistical power of an exoplanet survey to infer demographics is
directly related to the expected yield of the survey assuming a given
exoplanet population. The ability to accurately estimate the survey
yields is therefore an important input into mission design.
Nevertheless, yield predictions have numerous potential sources of
uncertainty, and it is just as important to understand these. We
therefore devote this section to summarizing the sources of uncertainty
in our yield predictions and suggesting ways in which this uncertainty
can be reduced.

The sources of uncertainty in our results can be broken down into three
broad categories. The first is due to our ability to simulate how the
spacecraft collects data and how it will be processed. The second is due
to our ability to measure and model the astrophysical components that
produce microlensing events, i.e., the Galaxy and its stellar
populations. Finally, our assumptions of the planetary population
impacts the mission yields that we predict.

## Simulation Uncertainties

A principle concern when building a simulation is the balance between
realism and computational cost. One is invariably forced to make
compromises on the former in order to obtain a manageable run time. By
building simulated images of the *WFIRST* microlensing fields, combined
with a model of smooth backgrounds, our simulations should reasonably
capture all significant sources of photon noise. Our simulation of the
detectors is somewhat simplistic; we assume that *WFIRST*'s HAWAII-4RG
detectors behave like CCDs, which is probably reasonable given that
photon noise always dominates over read noise for the microlensing
fields and their exposure times. The most significant form of
uncertainty in the data collection and processing category is the
processing element. Our simulations perform a simple aperture photometry
noise calculation and limit its precision with a constant
1 millimagnitude term added in quadrature. Ultimately, the use of a
small, fixed, unweighted aperture should result in an underestimate of
the achievable photon-noise limited photometric precision, which helps
to offset our inability to simulate all of the imperfections between
photons entering the telescope and a photometric measurement. However,
there are a number of additional steps between measuring photometry and
declaring a planet detection that could be significantly affected by
sources of systematic noise (instrumental and/or astrophysical) that we
do not simulate. Estimating the impact of these sources of noise is
challenging, and would likely require a full end-to-end simulation.
Realistic noise simulations based on lab tests of H4RG detectors [e.g.,
@Rauscher2015] will help in this regard. We note that the impact of any
change in the simulation of photometry, insofar as it changes the
photometric precision by a uniform scaling factor, can be estimated by
changing the $\Delta\chi^2$ threshold for declaring a detection.

Another important uncertainty in the simulations is the ability to
convert a detection, i.e., a signal above the $\Delta\chi^2$ threshold,
into a bone fide planet with measured parameters. This process can be
affected by various discrete and continuous degeneracies [see @Gaudi2012
for a review] that can lead to ambiguity between planetary
interpretations and stellar binary lenses and sources as the cause of
the lightcurve anomaly. These ambiguous events can be dealt with by
Bayesian probability accounting, but naturally add uncertainty to any
inferences, especially if they constitute a significant fraction of the
potential planet sample. Reassuringly, @Suzuki2016 found only 1 out of
23 events in their systematically selected sample of planets had an
ambiguous binary lens interpretation, and 6 out of 23 events suffered a
close-wide degeneracy that impacted the measurement of the projected
separation $s$, but did not significantly affect the mass ratio $q$. The
improved photometry possible from space will likely resolve some
fraction of the degeneracies and ambiguities that are seen in
ground-based data, but the more subtle features detectable in
space-based data may introduce a higher fraction of ambiguous events;
e.g., in a simulation of a high-cadence microlensing survey with uniform
photometry @Zhu2014 found 55% of planets were detected without caustic
crossings. Additionally, in this work we have not simulated the
measurement of planet and host masses that observations from space
enable. For the MPF mission design, with pixels more than twice the size
of *WFIRST*'s Cycle 7 design, @Bennett2010 estimate that more than half
of the planetary events will have better than 10% mass measurements via
some form of direct detection of lens light. These estimates do not
account for the potential contamination of the measurement by either
bound stellar companions to the source or
lens [@Henderson2015-ao; @Koshimoto2017-950]

## Galactic model uncertainties

The microlensing event rate and the properties of the microlensing
events will depend on the distribution of stars in the Galaxy, their
kinematics and their masses. No model of the Galaxy will be able to
fully capture its complexities, and so our estimates will have some
degree of uncertainty due to any shortcomings of the model. In
[3.2](#ratecorr){reference-type="ref+label" reference="ratecorr"} we
estimated the corrections necessary to match the microlensing event rate
of the model. In this section we examine further the possible causes for
the BGM1106's under-prediction of event rates and the impact of any
model uncertainties or errors on the properties of the microlensing
events. We note that this discussion only applies specifically to
version 1106 of the Besançon  model that we have used in this paper.

### Bar angle

In BGM1106 the Galactic bulge is modeled as a triaxial bar with an angle
of $12.5\degr$ to the Sun-Galactic center line and a major axis scale
length of $1.63$ kpc. This is in contrast to modeling of the
distribution of red clump giants found in the OGLE and VVV surveys,
which find a bar angle ${\sim}30\degr$ and a major axis scale length of
${\sim}0.7$ kpc [@Stanek1994; @Rattenbury2007; @Wegg2013; @Cao2013].
With no distance information, both models can reproduce the 2-d
distribution of bulge stars on the sky (note that
$1.63$ kpc $\sin 12.5\degr \approx 0.7$ kpc $\sin 30\degr \approx 0.35$ kpc).
Red clump stars are standard candles [@Stanek1994], and so can trace out
the third dimension of the bulge density distribution. Along the line of
sight $(\ell,b)=(1.25,-2.65)$ the BGM1106 predicts a distance modulus
dispersion of $0.36$ mag for bulge stars, which is much larger than the
value of $0.20$ mag that @Nataf2013 measure from OGLE clump giants after
subtracting in quadrature an intrinsic magnitude dispersion of
$0.09$ mag and an extinction dispersion of ${\sim}0.11$ mag (the total
observed magnitude dispersion of the red clump is therefore $0.24$ mag).
@Simion2017, working with the Galaxia code that implements the 2003
Besançon  model [@Sharma2011], found that slightly smaller bar angles of
$20$--$25\degr$ provided the best fit to VVV red clump counts, but that
there was some degeneracy between the bar angle and the red clump
dispersion due to sources other than distance dispersion.

We found in [3.2.1](#starcounts){reference-type="ref+label"
reference="starcounts"} that the BGM1106 only slightly under-predicts
bulge star counts, so the principle impact of the bar angle is only to
spread bulge stars along the line of sight. This was confirmed by
comparing the red clump star counts of @Nataf2013 as a function of
$(\ell,b)$ to the total stellar mass of the BGM1106 bulge.

The line of sight distribution of lenses and sources affects the
distribution of microlensing event properties. The Einstein radius
depends on the relative distances of the source and lens as
$$\begin{equation}
r_{\mathrm{E}}= \sqrt{\frac{4G}{c^2}MD_{\mathrm{l}}(1-D_{\mathrm{l}}/D_{\mathrm{s}})},
\end{equation}$$ where $G$ and $c$ are the gravitational constant and
speed of light, respectively, and $D_{\mathrm{l}}$ and $D_{\mathrm{s}}$
are the lens and source distances, respectively. The larger line of
sight distance dispersion for the BGM1106 relative to that measured will
result in ${\sim}15$% larger Einstein radii for events with bulge lenses
and bulge sources (bulge-bulge lensing), and a smaller impact on events
with disk lenses and bulge sources (bulge-disk lensing). Event
timescales will be larger by the same degree, and the ratio of bulge to
disk lenses will also be increased. However, with only a maximum effect
of ${\sim}15$%, the impact will be relatively minor.

### Bulge kinematics {#kinematics}

In addition to the bar angle, the kinematics of the bulge stars are not
in agreement with measurements. We compared the predicted BGM1106 proper
motions to *Hubble* Space Telescope (HST) proper motion measurements in
the ${\sim}11$ arcmin$^2$ SWEEPS field [@Clarkson2008]. @Clarkson2008
separated bulge and disk populations by selecting stars above the bulge
main sequence turn off where the disk's main sequence stars were well
separated from the giant branch, which is dominated by bulge stars. For
this comparison, we combined the BGM1106 catalogs of the two sight lines
closest to the SWEEPS field at $(\ell,b)=(1\fdg1,-2\fdg7)$ and
$(1\fdg35,-2\fdg7)$ to improve the statistics for these bright stars. We
roughly mimicked the @Clarkson2008 selection in our BGM1106 catalogs by
selecting stars with $15.95<I_{\mathrm{AB}}<17.95$ and assigned those
with $(I-J)_{\mathrm{AB}}<0.5$ to the blue (disk proxy) population and
those with $(I-J)_{\mathrm{AB}}>0.58$ to the red (bulge proxy)
population. The two catalogs combined represent stars drawn from a solid
angle of $1.44$ arcmin$^2$, and there were a total of $37$ stars in the
blue disk proxy sample and $105$ stars in the red bulge proxy sample.

@Clarkson2008 measured their proper motions in an arbitrary reference
frame, so we can only compare the blue-red proper motion offsets and the
proper motion dispersions. They find an offset between the blue and red
population proper motions of
$(\Delta\mu_{\ell},\Delta\mu_b) = (3.24\pm 0.15,-0.81\pm 0.12)$ mas yr$^{-1}$,
where the $\Delta$ represents blue minus red. For the BGM1106 proper
motions we find
$(\Delta\mu_{\ell},\Delta\mu_b) = ( 3.53\pm 0.65,-0.12\pm 0.32)$, which
are largely consistent with each other.

@Clarkson2008 do not report the proper motion dispersions they measure,
but we are able to extract them from their Figure 21, finding
$(\sigma_{\ell},\sigma_b)=(2.2,1.3)$ mas yr$^{-1}$ for the blue (disk)
population and $(\sigma_{\ell},\sigma_b)=(3.0,2.8)$ mas yr$^{-1}$ for
the red (bulge) population. Individual proper motion uncertainties in
the HST data are likely below $0.3$ mas yr$^{-1}$ for each star, so have
a negligible impact on the measured dispersions, and the sample size is
larger than our comparison sample so the statistical uncertainty in the
estimates of the HST proper motion dispersions will be insignificant in
our comparison. For the blue BGM1106 population we find proper motion
dispersions of $(\sigma_{\ell},\sigma_b)=(2.47\pm 0.29,1.11\pm 0.13)$,
which is largely consistent with the HST measurements in both axes. For
the red BGM1106 population we find
$(\sigma_{\ell},\sigma_b)=(5.19 \pm  0.36,2.64 \pm  0.18)$; the
latitudinal dispersion is consistent with the HST measurements, but the
longitudinal dispersion is too large by a factor of $1.73 \pm 0.12$.

![Comparison of BGM1106 model proper motions with those measured using
*HST* by @Clarkson2008. *Top*: Proper motion vector point diagram. Small
points are all potential source stars ($H_{\rm Vega}<25$) from the
BGM1106 (light blue are disk stars, while light red are bulge stars).
Larger blue and red points are BGM1106 stars belonging to disk and bulge
proxy populations, respectively, with selections designed to replicate
those of @Clarkson2008. Light blue and red lines are the $1$-$\sigma$
proper motion dispersion contours measured by @Clarkson2008 for disk and
bulge proxy stars, respectively, while the darker lines are the same
$1$-$\sigma$ dispersion contours, but for the BGM1106 disk and bulge
proxy stars. *Bottom*: Distance versus $\ell$ proper motion for the same
BGM1106 stars as in the top panel. The CMD cuts do a good job of
isolating disk and bulge populations, though with some cross
contamination. The BGM1106 disk proper motions match the data well, but
the bulge proper motions have a dispersion that is too large the $\ell$
direction. The dotted line shows the distance of the Galactic center in
the model.](clarksoncomp.png){#clarksoncomp width="\\columnwidth"}

We can get an idea for the cause of the discrepancy between the BGM1106
and the data by looking at the proper-motion vector point diagram and
the longitudinal proper motion plotted against distance, both shown in
[20](#clarksoncomp){reference-type="ref+label"
reference="clarksoncomp"}. The first thing to notice is that the
color-magnitude selection does a good job separating near-side disk
stars from bulge stars, admittedly with a small degree of
cross-contamination between the disk and bulge populations. Also, the
selected stars do not appear to be a significantly biased subset of the
underlying population. This means that we cannot ascribe the discrepancy
to a difference in the selection of the stars for each population
between the observation and the model. The random velocity dispersions
in the BGM1106 bulge population are
$(\sigma_U,\sigma_V,\sigma_W)=(113,115,100)$ km s$^{-1}$, which
correspond to proper motions dispersions of the order of
$3$ mas yr$^{-1}$ at a distance of $8$ kpc, i.e., enough to account for
all of the measured HST value of $\sigma_{\ell}$. In addition to the
dispersion component, the BGM1106 bulge stars also have an additional
solid body rotation component, rotating at $40$ km s$^{-1}$ kpc$^{-1}$.
The combination of the longer bar and its small angle lead to a range of
solid body rotation velocities from ${\sim}-60$ km s$^{-1}$ on the near
end of the bar to ${\sim}+50$ km s$^{-1}$ as the sight line leaves the
far side. This results in a range of $-1.9$ to $+1.1$ mas yr$^{-1}$ in
proper motion, that would corresponds to an additional dispersion of
${\sim}0.87$ mas yr$^{-1}$ to be added in quadrature. Finally,
inspection of the BGM1106's $V$-component velocities (in a $UVW$ system)
as a function of distance suggests that in addition the solid body
rotation and the random dispersions there is an additional component
similar to the rotation curve of a stellar disk in a dark matter halo.
This results in a ${\sim}300$ km s$^{-1}$ offset between the mean
velocities of bulge stars that are ${\sim}1$ kpc from the Galactic
center on opposite sides. This causes a rapid change of
${\sim}8$ mas yr$^{-1}$ in the mean proper motion of stars as function
of distance at the distance of the Galactic center. This can be seen in
the lower panel of [20](#clarksoncomp){reference-type="ref+label"
reference="clarksoncomp"} as an offset in proper motions at a distance
of ${\sim}8$ kpc. This offset results in additional
${\sim}4$ mas yr$^{-1}$ to be added in quadrature to the proper motion
dispersion. Each of the three sources of dispersion combined in
quadrature result in a dispersion of $5.1$ mas yr$^{-1}$, which is
consistent with the value of $\sigma_{\ell}=5.19\pm0.36$ we measured
from the catalogs.

The addition of a potential quasi circular velocity component to the
bulge stars' velocities appears to be in error, because we expect the
bulge stellar population to be pressure supported with a sub-dominant
cylindrical rotational component to provide the pattern speed of the
bar. In the model, however, the quasi circular velocity component
together with the range of bulge star Galactocentric distances, leads to
this velocity component dominating the longitudinal proper motion
dispersion. The dichotomy in near-side bulge versus far-side bulge
velocities imposed by a large circular velocity also increases the event
rate of events with far bulge sources and near bulge lenses, which have
the largest Einstein radii, so will increase the mean Einstein radius of
bulge-bulge lenses somewhat. The increased longitudinal proper motion
dispersion of bulge stars will also increase the relative event rate of
bulge-disk lensing. In all cases, the BGM1106's event timescales will be
shorter than would be produced by more realistic kinematics.

### Bulge initial mass function {#bulgeimf}

As discussed already in [3.2.1](#starcounts){reference-type="ref+label"
reference="starcounts"}, the BGM1106's mass function in the bulge
differs from typically assumed mass functions [e.g., @Kroupa2001] in
both its shallow slope $\mathrm{d}N/\mathrm{d}M \propto M^{-1.0}$ and
its high lower mass cut off of $0.15M_{\odot}$. We found that replacing
the mass function with something more reasonable, such as from
@Sumi2011, a [@Kroupa2001] slope of $M^{-1.3}$ between $0.08$ and
$0.7M_{\odot}$ and a slope of $M^{-0.5}$ between $0.01$ and
$0.08M_{\odot}$, would improve the match of the shape of the BGM1106's
luminosity function to measurements from [@Calamida2015]. @Wegg2017 find
that a similar mass function, when combined with an $N$-body bulge model
fit to infrared star counts and radial velocity distributions, can
simultaneously fit both microlensing optical depths and timescale
distributions, though the slope of the brown-dwarf mass function in the
bulge remains uncertain ($-0.65\pm0.89$). We note that we have not
considered the effects of age or metallicity that can affect star
counts, especially for evolved stars, or in the case of metallicity,
M-dwarfs as well.

Adding stars and brown dwarfs below $0.15M_{\odot}$ to the BGM mass
function would increase the optical depth and event rate per star for
bulge-bulge lensing by factors of ${\sim}1.9$ and ${\sim}3.4$,
respectively. The disk's mass function in the BGM1106 has a more typical
slope, and extends down to $0.08M_{\odot}$ but adding brown dwarfs would
increase the optical depth and event rate for bulge-disk lensing, also,
but to a lesser degree than for bulge-bulge lensing. It is therefore
likely that the form of the mass function can explain a significant
amount of the factor of ${\sim}2.1$ under-prediction of the event rate
by the BGM1106, the factor of ${\sim}1.8$ under-prediction of the
optical depth, and its shallower slope of the luminosity function.
Adding low-mass stars to the mass function would also act to decrease
the mean event timescale [@Awiphan2016].

### Extinction

The BGM1106 uses the 3-d extinction model of @Marshall2006 to provide
extinction as a function of distance, and the @Cardelli1989 reddening
law with $R_V=3.1$ to convert extinctions in the $K_s$-band to other
wavelengths. @Schultheis2014 assessed the performance of various 2- and
3-d extinction maps and found that generally 3-d extinction maps were
accurate, but failed along certain site lines. Numerous studies have
shown that the reddening law towards the bulge differs from the
$R_V=3.1$, with $R_V{\sim}2.5$ more typical [e.g. @Nataf2013]. It is
even possible that the reddening law deviates from a power law in the
$1$--$2$ $\mu$m range [@Hosek2018].

Despite this uncertainty, it is likely that the impact of errors in the
extinction will only have a small impact on the predicted yields. This
is simply because the total extinction across our fields is only
$A_H{\sim}0.6$, though it does reach $A_H{\sim}1$ in small parts of the
fields closest to the plane. Therefore, even a large fractional error
corresponds to a relatively small absolute error. We can use the
analytic framework in [5.1](#analytics){reference-type="ref+label"
reference="analytics"} to estimate the impact. Errors in the extinction
will affect all stellar noise (source and blends) equally. A $33$%
under-estimate of the extinction, or $0.2$ mag, reduces flux and
$\Delta\chi^2$ by 17%. Using the slope of the $\Delta\chi^2$
distribution from [2](#chi2alpha){reference-type="ref+label"
reference="chi2alpha"}, $\alpha=-0.399$ for $1$-$M_{\earth}$ planets and
the Cycle 7 design, the under-prediction of extinction would results in
an over-prediction of the Earth-mass planet yield of ${\sim}7$%.
Averaged over the whole proposed fields, an error this large seems
unlikely. However, we note that the relatively coarse extinction map we
have used (resolution $0\fdg25\times0\fdg25$) may have impacted our
field optimization.

### Impact on *WFIRST*'s planet yield

In [3.2](#ratecorr){reference-type="ref+label" reference="ratecorr"} we
have adopted an event rate scaling to match measured microlensing event
rates per red clump source and the number of faint sources. This
correction factor will be valid to first order because the majority of
*WFIRST*'s sources will be in the bulge, like the red clump stars.
Therefore, the issues raised with the model in this section should not
affect our predictions for the number of microlensing events
*WFIRST* will detect. However, they will affect the properties of the
events, which may impact the detection efficiency.

The lack of low-mass stars and brown dwarfs means the mean lens mass is
too large, and at fixed planet mass the mass ratio will be too small.
This has the effect of reducing our detection efficiency per event
slightly at fixed planet mass. The BGM1106's bulge kinematics result in
timescales that are too short, which results in reduced planet detection
efficiency due to shorter planetary anomalies. The increase in Einstein
ring radii due to the elongated bulge will increase timescales slightly,
but not enough to counteract the effect from kinematics.

In addition to the average detection efficiency, the mass function and
bar angle issues cause the BGM1106 to overestimate average Einstein
radius. This means that its peak sensitivity to planets will be at
slightly smaller semimajor axis than indicated by
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}.

We have concluded that the BGM1106 probably under-predicts the number of
source stars because of its shallow mass function slope. However, we
corrected for the under-prediction by simply multiplying the event rate
for all source stars, which likely has the effect of over-correcting for
bright stars, brighter than $F814W_{\rm Vega}\sim 22$. Roughly two
thirds of $1M_{\earth}$ planet detections come from events with source
stars above this boundary, which would imply that the an over-correction
of bright source stars leads to an over estimate of ${\sim}14$% in
Earth-mass planet yield, and probably a larger overestimate for the most
difficult to detect planets. However, if we had estimated our event rate
scaling using the MOA all star event rates instead of the extended red
clump event rates (see [6](#gammacomp){reference-type="ref+label"
reference="gammacomp"}) and only used data in the range of Galactic
latitudes where *WFIRST* will probably observe, we would have derived a
larger correction.

In summary, the issues with the Galactic model after corrections act to
both increase and reduce the detection efficiency or number of events by
mostly small factors. To a certain degree then we can expect the effects
of different signs to cancel, and the associated uncertainties to grow
in quadrature. It is likely therefore that a single large uncertainty
will dominate over smaller uncertainties. The quantity with the largest
uncertainty is probably the microlensing event rate, due to the
relatively low signal to noise ratio when subdivided down to
square-degree scales, and the need to extrapolate closer to the Galactic
plane. We reiterate, however, that while there will remain significant
uncertainties in the absolute yield predictions, the relative yields
between designs simulated with the same methodology and common
parameters and assumptions will be much less uncertain.

## Planet Population Uncertainties

The uncertainty in our assumptions about the population of planets is
large, and some regions of the parameter space are completely
unconstrained. A major goal of the survey, after all, is to detect and
measure the occurrence rate of the cold planet population that can not
be conducted by any other method, or by microlensing observations from
Earth. Nevertheless there are measurements of planet abundances in the
regions of *WFIRST*'s sensitivity from microlensing
surveys [@Sumi2010; @Gould2010; @Cassan2012; @Shvartzvald2016; @Clanton2016; @Suzuki2016],
and near it from transits [e.g., @Burke2015], radial velocity [e.g.,
@Cumming2008; @Johnson2010; @Bonfils2013; @Montet2014] and direct
imaging [@Nielsen2010; @Chauvin2015; @Bowler2015]. These observational
constraints allow us to anchor extrapolations into the regions that are
unexplored.

Our fiducial joint mass-semimajor axis occurrence distribution (in many
places we have simply referred to this as our fiducial mass function)
assumes a broken power law in mass, and a log-uniform distribution in
semimajor axis. The high-mass end of the mass function was chosen to
match the estimate of the mass function from @Cassan2012 based on
microlensing searches. This measured mass function only extends down to
${\sim}5M_{\earth}$, so we chose to saturate the power law at a value of
$2$ planets per dex mass per dex semimajor axis per star at
$5.2M_{\earth}$ to prevent overly optimistic predictions of large
numbers of low mass planets. Since adopting this as our fiducial mass
function, several studies have advanced upon the @Cassan2012 result on
which it was based. While we have chosen to retain the fiducial mass
function for consistency and easy comparison with the past
*WFIRST* reports, it is worth examining what impact that adopting
another joint mass-semimajor axis function would have.

![Comparison of our fiducial mass function (solid gray line) to the
latest measurements based on microlensing data. Salmon and green points
with error bars show the planet occurrence as a function of mass ratio
converted into planet masses, assuming a $0.5M_{\odot}$ host star, from
@Suzuki2016 and @Shvartzvald2016, respectively, and the dotted gray line
shows a fit to microlensing, radial velocity trends, and direct imaging
data by @Clanton2016. Dark blue data points show the mass function
measurement precision of a mock survey by *WFIRST* (Cycle 7 design) in
0.5 dex mass bins assuming only half of the planet detections can be
used; filled points follow the fiducial mass function, while open points
follow a mass function that saturates at an occurrence rate a factor of
4 lower than the fiducial mass function.](massfn.pdf){#massfnplt
width="\\columnwidth"}

@Suzuki2016 analyzed a larger and more homogeneously selected [compared
to @Cassan2012] set of microlensing planet detections from the MOA
survey. @Shvartzvald2016 also studied the mass ratio function with a
smaller sample of events. Both mass ratio function measurements are
shown in [21](#massfnplt){reference-type="ref+label"
reference="massfnplt"} in comparison to our fiducial mass function. To
convert mass ratio to planet mass we assumed a host mass of
$0.5M_{\odot}$. @Suzuki2016 found evidence for a turnover in the planet
mass *ratio* function at $q\approx1.7\times10^{-4}$, which corresponds
to a planet mass of ${\sim}30M_{\earth}$ assuming a mean host mass of
$0.5M_{\odot}$. This turnover appears to be confirmed by an independent
analysis using very different methods [@Udalski2018], but the exact
shape of the turnover, and the steepness of the subsequent decline below
this mass, are very poorly constrained. In a bin centered at
$M_{\mathrm{p}}\approx 3M_{\earth}$ @Suzuki2016 place a $95$% upper
limit on the mass function of $0.5$ planets per dex$^2$, about a factor
of four below the value of our saturated fiducial mass function. At
${\sim}30$--$100M_{\earth}$ the fiducial mass function is a good match
to the @Suzuki2016 data, but at larger masses it again overestimates the
measurements, but to a lesser degree than at small masses. All together,
this suggests that our total yields will be overestimated somewhat, and
the yields at low masses could be overestimated significantly.

It is important to recognize that the planet yields assuming a fiducial
mass function that we estimate in this study are only a useful proxy for
the true value of the survey which is planet sensitivity, or its power
to measure the planet occurrence rate. This sensitivity is independent
of the assumed mass function, and, as can be seen from
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"},
the sensitivity will extend down to
${\sim}$few$\times10^{-2}M_{\earth}$. In this sense the sensitivity
range is the point at which no detections of planets of mass
$M_{\mathrm{p}}$ during the mission ceases to be an interesting
constraint on planet occurrence. In
[21](#massfnplt){reference-type="ref+label" reference="massfnplt"} we
show that even with a mass function saturation value a factor of $4$
lower than our fiducial mass function, *WFIRST* will detect a sufficient
number of planets to measure the mass function in $0.5$ dex bins to
below $1M_{\earth}$, and it would set interesting upper limits on the
planet occurrence at masses below this. In these estimates we assumed
that only half of *WFIRST*'s planets would be utilized in this mass
function measurement. Over its entire range it will provide measurements
of the mass function with far greater precision than is currently
possible from ground-based surveys. While not a direct comparison,
@Henderson2014-kmt predict that KMTNet, during its nominal 5 year
survey, would find a factor of ${\sim}16$ fewer 1-$M_{\earth}$ planets
than *WFIRST* will find in its nominal (Cycle 7) survey.

In addition to uncertainties in the planet mass function, there is even
greater uncertainty in the form of the planet occurrence as a function
of semimajor axis near to *WFIRST*'s peak sensitivity. @Clanton2014 have
shown that that there is at present very little overlap in the
sensitivity regions of current microlensing and radial velocity (RV)
surveys, but radial velocity surveys tend to show an increase in planet
occurrence with log semimajor axis or log period [e.g.,
@Cumming2008; @Bonfils2013] that appears to be consistent with
microlensing occurrence rates when extrapolated [see, e.g.,
@Gould2010; @Suzuki2016]. Results from *Kepler* show a similar rising
trend for large planets, but a shallow decline in occurrence beyond
$P{\sim}10$ d for planets smaller than Neptune [e.g. @Petigura2018];
whether these trends continue throughout *WFIRST*'s region of
sensitivity is unconstrained at present. At larger orbital separations,
@Clanton2016 find that a cut-off in planet occurrence at ${\sim}20$ AU
is required to remain consistent with microlensing, radial velocity
trends, and direct imaging results.

## Future Improvements

To make further progress on estimating the yields of the *WFIRST* survey
requires work on several fronts. The most critical need is
observational, due to the long lead time necessary to observe, analyze
and interpret new data. Advances in simulations are also needed to
better understand the relative importance of mass measurements in
optimizing *WFIRST*'s fields and observing strategy.

Observationally, the most important measurement to make is of the
microlensing event rate in the potential *WFIRST* fields, in the
infrared and to a depth as close as possible to that achievable by
*WFIRST*. Such a measurement will also test the ability of event rate
models based only on star counts [@Poleski2016] to predict event rates
closer to the Galactic plane. This requires an infrared microlensing
survey in order to penetrate the dust near the Galactic plane and reach
sources throughout the bulge and into the far side of the disk. Such a
survey is underway using the UK Infrared Telescope [UKIRT,
@Shvartzvald2017; @Shvartzvald2018], but VISTA, an infrared telescope
with a better location for bulge observations and a field of view that
is ${\sim}3$-times larger than UKIRT's, is not currently conducting
observations optimized for microlensing [though note that the Vista
Variables in the Via Lactea (VVV) survey has discovered a number of
microlensing events @Navarro2017]. In the time it takes the UKIRT survey
to build up enough events, progress can be made by analyzing the full
data sets of MOA and OGLE surveys. Currently the study measuring optical
depths and event rates with the largest number of events analyzes 474
MOA events from the 2007 and 2008 seasons (@Sumi2013, @Sumi2016;
@Wyrzykowski2015 only provides the timescale distribution of a larger
sample of 3718 events from the OGLE-III survey, and not optical depth
and event rate measurements). The current phase of the MOA survey has
now been operating for over a decade, and additionally, the OGLE-IV
survey has been discovering ${\sim}2000$ events a year since 2011.
Analysis of the full data sets of both these surveys would enable
measurements of the event rate at much higher spatial resolution than is
now possible.

In addition to the event rate, a better understanding is needed of the
source magnitude distribution in the infrared. Deep luminosity functions
in the $I$ band are available at latitudes of $b\approx -6, -4$ and
$-2.7$ [@Zoccali2000; @Holtzman1998; @Calamida2015], and in the $J$ band
at $b\approx-6$ [@Zoccali2000]. *WFIRST* will probably observe much
closer to the plane, and in addition to bulge stars, there will be a
significant contribution from stars in the near and far disk, which will
have very different event rates. Understanding the break down of
components will require new, deep, infrared magnitude distributions and
proper motion measurements from *Hubble* and/or the *James Webb Space
Telescope* (JWST), ideally for several sight lines in the potential
*WFIRST* fields. Images produced from special high-density mode scans
with *Gaia*[^3] can cover a much larger area than *HST* or *JWST*, but
so far have only been carried out in Baade's window, too far from the
expected *WFIRST* fields. Every high-resolution image taken in the
*WFIRST* fields before launch can will also provide a "precovery" data
set for lens mass measurements, extending the baseline over which PSF
elongation and color-dependent centroid shifts [e.g., @Bennett2007] can
be measured. A small sample of these could be used as ground truth for
the *WFIRST* measurements over the $4.5$ yr mission baseline. An
ambitious survey of the entire ${\sim}2$ deg$^2$ *WFIRST* microlensing
survey fields, in a similar manner to the Panchromatic Hubble Andromeda
Treasury (PHAT) survey [@Dalcanton2012], would require ${\sim}1500$
*HST* pointings, or ${\sim} 750$ *JWST* NIRCAM pointings, and would
provide immense legacy value for what will become one of the most
intensely observed patches of sky [@Yee2014b]. For example, optical
photometry from *HST* could provide photometric metallicity estimates
for every source and a large fraction of lens stars. *JWST* 3.6 and
$4.5$ $\mu$m imaging could be used to measure star-by star extinctions
using the Rayleigh-Jeans color excess [e.g., @Majewski2011]. Both *JWST*
and *HST* will have roughly twice the angular resolution of *WFIRST* and
so their imaging can assist in cases where local, random stellar over
densities hamper the interpretation of *WFIRST* images. The improved
resolution and increased time baseline would vastly improved
measurements of proper motions for all stars in the *WFIRST* field,
which would help in the measurement of parallaxes from *WFIRST*'s
microlensing data [@Gould2015]

There remains significant room for improvement in Galactic models. Fully
simulating a *WFIRST*-like survey requires all the features of a
population synthesis model, in order to understand not just the event
rates, but the properties of the lenses and sources. The Besançon  model
is presently the only publicly accessible population synthesis model
that incorporates kinematics. The latest version of the model[^4] has
some changes relative to the version we used here, but many of the
problems we have identified with it remain (e.g., the small bar angle,
too-fast kinematics). The publicly accessible Besançon  model also lacks
any flexibility to adjust model parameters, which is important for
maintaining a model in agreement with burgeoning data sets and for
understanding the propagation of model uncertainties to yields. The
TRILEGAL model [@Girardi2005; @Vanhollebeke2009] provides some
flexibility to adjust structural parameters, but the publicly available
version does not include kinematics.[^5] The publicly available Galaxia
code [@Sharma2011] implements a version of the Besançon  model and can
also accommodate $N$-body models, potentially providing the necessary
flexibility. New, more flexible versions of the Besançon  model are
under development, that improve the evolutionary tracks, add flexibility
of the IMF, star formation history, and bar angle [e.g.,
@Czekaj2014; @Lagarde2017]. GalMod is a another new population synthesis
model accessed via web forms with significant flexibility in its model
parameters [@Pasetto2018].

There is also significant work needed on microlensing simulations to
better understand the information that *WFIRST* will be able to measure
for each planet it finds. This is especially the case for host mass
measurements, which will be possible though one or more of the
techniques: detecting the host as it separates from the source and
measuring image elongation, color-dependent centroid shifts or directly
resolving the lens [e.g.,
@Bennett2007; @Henderson2015-ao; @Bhattacharya2017], measuring the
microlensing parallax with or without finite source measurements [e.g.,
@Yee2013; @Yee2015pieflux; @Bachelet2018], or even measuring astrometric
microlensing [@Gould2014apie]. The error budget of these measurements is
likely to be dominated by systematic errors, and so more detailed
end-to-end simulations of the stacking, photometry and astrometry
pipelines are likely necessary in order to fully understand *WFIRST*'s
capabilities. These simulations will then allow the optimization of
*WFIRST*'s survey for characterized planets and not just the total
number of detected planets. It will also be important to understand how
*WFIRST* performs for more exotic planetary systems (e.g., multiplanet
systems, @Zhu2014, circumbinary planets @Luhn2016, exomoons @Liebig2010,
etc.) and for rejecting possible false positive detections caused by,
for example, binary source stars [e.g., @Gaudi1998bs].

# Conclusion {#conclusions}

We have performed detailed simulations of several potential designs of
the *WFIRST* mission in order to estimate the planet detection yield of
its microlensing survey. We derived a correction factor to apply to
microlensing event rates computed using the Besançon  model in order to
normalize event rates to those measured by microlensing surveys. Having
done so, we estimate that the most recent *WFIRST* design (Cycle 7) will
be able to detect ${\sim} 180$ Earth-mass planets and ${\sim}1400$ cold
exoplanets in total. For Earth-mass planets, its sensitivity will extend
from ${\sim} 1$ AU outwards, and will have a wider range of sensitivity
at higher masses. The lower limit of *WFIRST*'s sensitivity for planets
in suitable orbits extends down to the mass regime of the solar system's
moons, e.g., Ganymede. The mission will fulfill the goals assigned to
its microlensing component by the 2010 decadal survey committee to
"determine how common Earth-like planets are over a wide range of
orbital parameters." However, significant observational, Galactic
modeling, and simulation work still needs to be done in order to
optimize and fully understand the yields of the survey.

This paper is dedicated to the memory of Neil Gehrels, who, as WFIRST
Project Scientist, gracefully sheparded this mission from its formal
initiation in 2016, until his untimely death. We miss him and his
leadership dearly. We would also like to thank members of the
*WFIRST* Microlensing Science Investigation Team, as well as Jeff Kruk,
Dave Content, Kevin Grady, and many others in the *WFIRST* program
office for their support. We would like to thank Chris Hirata and Jay
Anderson for their practical help and discussions. Finally, we would
like to single out David Bennett, who has been a constant source of
input and guidance as we have developed our models and worked on this
paper. We recognize that, without his tireless efforts, a microlensing
survey on WFIRST would not exist.

This work was performed in part under contract with the California
Institute of Technology (Caltech)/Jet Propulsion Laboratory (JPL) funded
by NASA through the Sagan Fellowship Program executed by the NASA
Exoplanet Science Institute. MTP and BSG were supported by NASA grants
NNX14AF63G and NNG16PJ32C, as well as the Thomas Jefferson Chair for
Discovery and Space Exploration. SM was supported by NSFC grants No.
11333003, 11390372, and 11761131004.

#  {#section .unnumbered}

# Improvements to  {#mabulsimprovements}

## Custom bandpasses {#customfilters}

*WFIRST* will perform its microlensing survey using a wide infrared
filter, covering the full range of detector sensitivity in order to
maximize photon count rates. The Besançon  model provides stellar
magnitudes in several standard photometric systems, computed from
stellar atmosphere models [@Robin2003], but it is not easy to compute
magnitudes in additional bands. We solved the problem of calculating
magnitudes in custom bandpasses by producing what amount to smoothed
spectral energy distributions (SEDs) by interpolating between the
different available pass bands, and then integrating the product of the
smoothed SED with the system throughput curve for each desired custom
filter.

The BGM only outputs a limited number of stellar magnitudes out of the
whole range available -- in the catalogs we were using $R, I, J$ and $H$
-- so we found it necessary to supplement these with synthesized $K$ and
$L$ magnitudes in order to completely cover and bracket the
*WFIRST* detector sensitivity range. The magnitudes in these bands were
synthesized by assuming that the star was emitting as a black body, and
that extinction followed the extinction law listed in the BGM1106 header
data, namely $A_K/A_V=0.118$ and $A_L/A_V=0.0$. The smoothed SEDs were
interpolated using radial basis functions (RBFs).

![The color-absolute magnitude diagram in the principle
*WFIRST* microlensing filters, $W149$ and $Z087$. Shown are stars from
three BGM1106 sightlines at $\ell=-0.4\degr$ and $b=-3.2, -1.95,$ and
$-0.7\degr$, combined, with disk stars plotted with black dots and bulge
stars with red dots. The evolutionary tracks and synthetic colors differ
between the disk and bulge stars as described by @Robin2003 and
references therein. The blue line shows a MIST version 0.3
[@Choi2013mist] isochrone for a 10 Gyr, \[Fe/H\]$=0.0$ population
computed using *WFIRST* filter profiles, shifted by
$\Delta(Z087-W149)=-0.05$, demonstrating that our scheme for computing
*WFIRST* colors and magnitudes works reasonably well. To aid conversion
to apparent magnitudes, the distance modulus to the bulge population is
approximately $14.5$, and the extinction and reddening will typically be
$A_{W149}{\sim}0.5$ and $E(Z087-W149){\sim}0.5$ in the expected
*WFIRST* microlensing fields.](wfirstcmd.png){#cmd
width="0.5\\columnwidth"}

To test of synthetic *WFIRST* magnitudes we combined catalogs from 3 BGM
sightlines ($\ell=-0.4\degr$ and $b=-3.2, -1.95,$ and $-0.7\degr$) and
mean extinctions to bulge stars of $A_V=2.35, 3.62,$ and $14.37$,
respectively. Colors and magnitudes were dereddened using values of
$A_{W149}/A_V=0.225$ and $E(Z087-W149)/A_V=0.208$ chosen to align the
red clump of each field. These values compare to $0.210$ and $0.295$,
respectively, computed at the central wavelength of the filters using
the @Cardelli1989 extinction law with $R_V=3.1$; we can expect some
difference due to the very wide bandpass of the W149 filter.
[22](#cmd){reference-type="ref+label" reference="cmd"} shows the
resulting color-absolute magnitude diagram. The dereddening does not
work perfectly, with the turnoff location of bulge stars differing by
${\sim}0.03$ mag in $Z087-W149$ for the different values of extinction.
We note that disk stars tend to be redder than the bulge stars, likely
due to the different stellar evolution and synthetic photometry models
used for each population as described by @Robin2003 and references
therein. We also compared the dereddened BGM stars to a MIST version 0.3
isochrone computed using *WFIRST* bandpasses [@Choi2013mist] for a 10
Gyr, solar metallicity population. Subtracting 0.05 mag from $Z087-W149$
MIST isochrone brings it into good alignment with the main sequence
BGM1106 stars, though the color of the turn-off and giant branch
disagree by ${\sim}0.05$ mag in opposite directions; it is possible that
differences in stellar evolution codes or the filter transmission curves
used for the MIST isochrones could cause these problems. Overall, it
appears that our scheme for computing magnitudes in the
*WFIRST* bandpasses is reasonable, and should not inject errors
significantly larger than the theoretical uncertainties associated with
the choice of isochrones.

## Zodiacal light model {#zodi}

Outside the Earth's atmosphere, in the near infrared, the brightest
diffuse background is caused by the Zodiacal light -- light from the Sun
scattered off interplanetary dust grains. In we assumed this was
constant, taking the mean value at the times that *Euclid* could
possibly conduct a putative bulge microlensing survey . However, the
level of the zodiacal background varies as a function of the elongation
of the target fields relative to the Sun, an effect that may become
important for long observing seasons. For this reason we incorporate a
full-sky model of the zodiacal light, removing the need for the  user to
calculate the average level of the zodiacal light in their required
bandpasses.

The zodiacal light brightness in a given bandpass is calculated by
integrating the RBF interpolated zodiacal light spectrum [as provided by
@Leinert1998 including solar elongation dependent color terms] over the
throughput curve of the bandpass. The spatial dependence of the zodiacal
light is calculated by RBF interpolation of the map provided by
@Leinert1998.

## Faster photometry routines {#photrout}

In we performed photometry on a pixel-by-pixel noise realization of each
image at each epoch. This was computationally expensive, and in certain
circumstances was the primary bottleneck of the computation. To speed up
the photometry we implemented a routine that takes as input a noiseless
realization of the baseline image, accounts for blending, and returns a
simple function to compute the photometric signal and uncertainty as a
function of magnification. With this, only a single realization of the
noise on the photometric data point is needed. The routine also solves
for the magnification at which saturation is reached in one of the
pixels of the aperture, allowing saturation to be identified accurately
without building a realization of an image.

## Improved observer-centric velocities/timescales {#obstE}

In order to include parallax effects in lightcurves we now compute
geocentric, or more accurately observer-centric, microlensing event
timescales. In , we used heliocentric velocities to compute event
timescales. Due to the observer's motion about the Sun (typically the
Earth's, which ranges from -30 to 30 km s$^{-1}$ projected onto the
sky), the relative source-lens velocity will change over the course of
the year. This compares to the ${\sim}200$--$1000$ km s$^{-1}$ projected
velocities of the source and lens [see, e.g., @CalchiNovati2015],
implying a typical modification of the timescales by
${\sim}3$--$15$ percent. However, for both *Euclid* and *WFIRST* 
microlensing observations will be made at or near quadrature, meaning
that the projected velocity of the Earth will be close to zero. The
effect on planet yields of using the improved timescales is therefore
likely to be very small. Some of the simulations presented here use the
improved timescales, while others were completed before the improved
timescale calculation was implemented. Full details are given by
@Penny2017.

# Computing the mass-semimajor axis sensitivity curve or "The making of Figure 9" {#curvecomp}

In order to compute the sensitivity curve shown in
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}
required computing the planet detection rate on a grid of planet mass
and semimajor axis, spaced by 0.25 and 0.125 dex, respectively.
Obtaining reasonably accurate results is computationally intensive, with
the required computation increasing as one over the square of the
detection efficiency in order to achieve equal Poisson statistical
uncertainties. With $t_{\mathrm{0}}$ drawn from any point in the 5 year
mission, and a ${\sim}24$% observing duty cycle, the detection
efficiency is ${\sim}10^{-5}$ at the 3-detection line. This implies that
a 10 percent statistical error would require ${\sim}100/10^{-5}=10^7$
lightcurves to be generated at each grid point near the sensitivity
curve, with most of these showing no detection. In order to make the
computation tractable we developed the CROIN
parametrization [@Penny2014], which is used to generate only lightcurves
where there is a reasonable probability of a planet detection. This
coordinate system is centered on the planetary caustic(s), and the
region around the caustic that contains a detectable planetary signature
is a circle of radius $r_{\rm c}(s,q)$, whose analytic functional
dependence on the projected separation relative to the Einstein radius
$s$ and mass ratio $q$ is derived empirically by @Penny2014. Only source
trajectories with impact parameters relative to the planetary caustic
$u_{\rm c}<r_{\rm c}$ are simulated. We used the CROIN parametrization
for planet masses $M\le 10M_{\earth}$ and for larger masses with
$\log (a/\text{AU}) \ge 1.125$, reducing the number of required
lightcurve computations by more than two orders of magnitude. When using
the CROIN parametrization we still require that the main-event impact
parameter and peak time obey $-3\leq u_{\mathrm{0}}<3$ and
$0\leq t_{\mathrm{0}}<2011$.

For the low-mass planets that *WFIRST* is sensitive to, computing the
lightcurve is not a trivial operation and is prone to numerical errors.
For its speed, we primarily relied on a contour integration
code [@Gould1997; @Dominik1998] written by S. Mao. This solves the
complex 5$^{\text{th}}$-order binary lens polynomial at many points
around the source circumference and then links the resulting solutions
into a number of potentially merging images. The coefficients of the
polynomial have additive terms of the order of 1, and various
combinations of powers of $q$ and $s$. For the lowest mass planets we
consider, $q\sim10^{-8}$, so we suspect that the numerical errors are a
result of catastrophic cancellations in parts of the calculation where
this is difficult if not impossible to avoid. The vast majority of
errors are caught by error handling routines, and when this occurs the
lightcurve is passed to a much slower but more robust inverse ray
shooting routine [e.g. @Kayser1986], but occasionally errors slip past
the error handing routines.

<figure id="badlc">
<p><embed src="badlc_highmag.pdf" style="width:49.0%" /> <embed
src="badlc_general.pdf" style="width:49.0%" /><br />
<embed src="badlc_dropout.pdf" style="width:49.0%" /> <embed
src="badlc_noncrit.pdf" style="width:49.0%" /></p>
<figcaption>Examples of lightcurves exhibiting numerical errors that
were not caught by error reporting routines. Each type of error is
discussed in the text. Data points with error bars show the predicted
magnitude and uncertainty of measurements without any noise, the blue
line shows the simulated event, including numerical errors, and the
green line shows the best fit single lens model. Parameters for each
event shown are listed above each plot;
<math display="inline" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mi>α</mi><annotation encoding="application/x-tex">\alpha</annotation></semantics></math>
is the angle subtended by the source trajectory relative to the binary
axis.</figcaption>
</figure>

In order to make sure that these numerical errors were not significantly
affecting results we visually inspected a large sample of the
lightcurves of the lowest mass exoplanet detections. We found examples
of errors that *did* cause false positive detections and *could* cause
false negative detections. As our simulations only output the
lightcurves of a sample of planet *detections*, we are not able to
assess the degree to which our predicted yields are reduced by false
negatives. As we correct for false positives (see below) and not for
false negatives our planet yield predictions at the lowest masses are
likely to be conservative. [23](#badlc){reference-type="ref+label"
reference="badlc"} shows four examples that represent the overwhelming
majority of the errors we found -- two are false positives, and two were
errors that did not affect the designation of the event as a detection,
but had the errors been more severe one of these would have resulted in
a false negative.

The first example (a) shows a type of false positive that only occurs in
high-magnification events where the source is resolved by the
magnification structure surrounding the host star. Most of these
examples had only a single discrepant data point. However, due to the
high photometric precision that high-magnification events enable, the
discrepant point causes a large $\Delta\chi^2$.

The second example of false positive (b) is one of a more general class
where a significantly discrepant data point (or several) occurs during a
planetary anomaly. They can be either positive or negative deviations,
and are typically sharp changes relative to the source crossing time.
The events with these numerical errors are only classified as false
positives if removal of the discrepant points would move the event below
the $\Delta\chi^2$ threshold.

A potential false negative non-detection (c), which we call a "finite
source drop-out," occurs for events with wide-separation planets that
show a small amplitude top-hat planetary signature due to extreme finite
source effects. They are caused when two images near the planet are both
incorrectly flagged as false solutions to the the lens equation, leaving
three valid solutions instead of five.[^6] In principle it is possible
for all the data points during a planetary anomaly to experience this
problem, in which case the event would not count as a planet detection
and the simulation would not output the lightcurve. It is therefore
impossible to estimate the number of these occurrences by our current
method of inspection. However, we can guess that the number is likely
small because most instances of drop-outs show only a small fraction of
the top hat dropping out.

The final example (d) of numerical errors is likely very similar to the
finite source drop-out but occurs for all separations. Again, the
magnification is artificially reduced, but usually by an insignificant
amount that does not affect the event's status as a detection or
non-detection.

![Fraction of false positive planet detections for points on the planet
mass-semimajor axis grid. In each cell the fraction is the number of
false positive lightcurves over the number of inspected lightcurves. The
number below that is the percentage of false positives, weighted by the
event rate as described in [3](#sims){reference-type="ref+label"
reference="sims"}. The shading is a linear scale that saturates to
yellow at 3 detections during the survey, before correction for the
false positive rate.](smapcontam.pdf){#fpgrid width="\\columnwidth"}

![Average rate-weighted false-positive fraction as a function of planet
mass. Filled black points show the rate-weighted false-positive fraction
as measured by inspecting lightcurves. The open red points show the same
data but showing the quantity $\log(1/\text{FPF}-1)$ plotted against the
axis on the right. The lines show the same best fit analytic
model.](fprate_red.pdf){#fpfit width="0.5\\columnwidth"}

The false positive fraction becomes significant as the planet mass
decreases, so it is important that we correct for it.
[24](#fpgrid){reference-type="ref+label" reference="fpgrid"} shows the
event-rate weighted (see [3](#sims){reference-type="ref+label"
reference="sims"}) false positive fraction for points on the planet
mass-semimajor axis grid, along with the number of events inspected and
the number of events that were false positives. The initial intention
was to correct each point on the grid individually by its own false
positive rate, but there were not enough lightcurves output by the
simulation for this to be accurate. Instead, being as the false positive
rate seemed to be relatively independent of semimajor axis (within the
large error bars), we took the rate weighted average of all semimajor
axes at each value of the mass. The false positive fractions can be
transformed to a form that is roughly a single power law in mass
$$\begin{equation}
\log\left(\frac{1}{\text{FPF}}-1\right) = \alpha\log(M/M_{\earth}) + \beta,
\label{fpeq}
\end{equation}$$ where $\text{FPF}$ is the false positive fraction and
$\alpha=1.25$ and $\beta=2.7$ are the best fit linear regression
parameters. This is shown in [25](#fpfit){reference-type="ref+label"
reference="fpfit"}.

![False-positive-corrected planet detection rates plotted as a function
of mass for each of the semimajor axis grid points. The detection rates
have been shifted vertically by an amount $10\log(a/\text{AU})$, and are
also color-coded by semimajor axis with black corresponding to
$a=0.01$ AU and yellow to $a=100$ AU. Curved lines are quadratic fits to
the points with detection rates within a factor of $30$ of the
$3$ detections per survey threshold that is plotted in
[9](#sensitivity){reference-type="ref+label" reference="sensitivity"}.
For each semimajor axis we plot the $3$-detection threshold as a
horizontal line and an open square point marking the position at which
the quadratic curve crosses the threshold.](fitmaplimit_30.pdf){#fitmap
width="0.5\\columnwidth"}

Returning to the problem of estimating *WFIRST*'s sensitivity in the
mass-semimajor axis planet, we correct the gridded planet detection
rates using [\[fpeq\]](#fpeq){reference-type="ref+label"
reference="fpeq"}. For a given semimajor axis, to find the mass at which
the planet detection rate crosses the 3 detection threshold we fit a
quadratic polynomial in $\log(M/M_{\earth})$ to the log of the planet
detection rates that are within a factor of 30 of the $3$ per survey
threshold, and then solve the resulting quadratic equation (taking care
to select the appropriate root). We repeat this process for each
semimajor axis grid point as is shown in
[26](#fitmap){reference-type="ref+label" reference="fitmap"}. We
excluded the points with $\log(a/\text{AU})=-2$ and $-1.875$ from the
analysis because our grid did not extend to high enough masses to
properly bracket the point at which 3 detections are expected.

[^1]: Note that in the software was called MaB$\mu$LS, but was renamed
    to disambiguate it from the MaB$\mu$LS online tool [@Awiphan2016].

[^2]: https://exoplanetarchive.ipac.caltech.edu/

[^3]: <https://www.esa.int/spaceinimages/Images/2017/08/Gaia_sky_mapper_image_near_the_Galactic_centre>

[^4]: <http://modele2016.obs-besancon.fr/>

[^5]: <http://stev.oapd.inaf.it/cgi-bin/trilegal>

[^6]: The binary lens equation will have either 3 or 5 solutions
    depending on whether the source is inside or outside a caustic, but
    the complex 5$^{\text{th}}$-order polynomial that can be formed by
    rearranging the lens equation always has 5 solutions. The validity
    of each solution is checked by inverse shooting a ray from each
    candidate solution and checking the proximity of the ray to the
    source position from which it should have originated.
