Broadly follows the convention laid out by Luhn et al 2016:

- Origin at center of mass of the binary star system. More massive star to the left of the origin and binary axis along the X axis.
- Microlensing parameters scaled to the Einstein ring of the binary stars.
- $s_b \equiv$ Projected separation between the binary stars; $q_b \equiv M_1/M_2$ 
- $s_p \equiv$ Projected distance of planet from origin; $q_p \equiv m_P/(M_1 + M_2)$
- $\alpha$ measured wrt binary axis in a counter-clockwise direction. Source moves from left to right when $\alpha = 0\degree$ 
- $\psi \equiv$ Position angle of the planet wrt the binary axis, measured in the same sense as $\alpha$.
- $u_0$ is the smallest distance of the source trajectory from the origin.

This parametrization ensures that parameters don't have to be rescaled or shifted when moving from a system with just the binary stars to one with a planet orbiting a star with the combined mass of the two stars at the origin.

**Note:** VBMicrolensing scales all parameters to the Einstein ring for unitary mass for multiple lenses. To implement our conventions with VBM when generating triple lens light curves, we need to set the total mass of the binary to 1. This convention is used when MultiMa0 or MultiMag2 functions are called.
For binary lenses, VBM defines the origin at the barycenter of the system and defines all parameters in terms of the Einstein ring for the total mass of the binary lens system. This convention is used when BinaryMag0 or BinaryMag2 functions are called.