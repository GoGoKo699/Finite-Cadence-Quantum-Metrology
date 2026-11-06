# Inline mathematical glyph calibration

This temporary diagnostic page compares the same mathematical expressions with zero-width layout guards. It is held on the verification branch only.

| Expression | Original | Strut | Tall phantom |
|---|---|---|---|
| `T` | $`T`$ | $`\strut T`$ | $`\vphantom{X^{2}_{2}}T`$ |
| `Z/2` | $`Z/2`$ | $`\strut Z/2`$ | $`\vphantom{X^{2}_{2}}Z/2`$ |
| `-cZ/2` | $`-cZ/2`$ | $`\strut -cZ/2`$ | $`\vphantom{X^{2}_{2}}-cZ/2`$ |
| `F_j` | $`F_j`$ | $`\strut F_j`$ | $`\vphantom{X^{2}_{2}}F_j`$ |
| `\tau` | $`\tau`$ | $`\strut \tau`$ | $`\vphantom{X^{2}_{2}}\tau`$ |
| `Q_+` | $`Q_+`$ | $`\strut Q_+`$ | $`\vphantom{X^{2}_{2}}Q_+`$ |
| `T^{-1}` | $`T^{-1}`$ | $`\strut T^{-1}`$ | $`\vphantom{X^{2}_{2}}T^{-1}`$ |
| `T_K\le T` | $`T_K\le T`$ | $`\strut T_K\le T`$ | $`\vphantom{X^{2}_{2}}T_K\le T`$ |
| `\mathcal R` | $`\mathcal R`$ | $`\strut \mathcal R`$ | $`\vphantom{X^{2}_{2}}\mathcal R`$ |
| `\gamma` | $`\gamma`$ | $`\strut \gamma`$ | $`\vphantom{X^{2}_{2}}\gamma`$ |
| `T/\tau` | $`T/\tau`$ | $`\strut T/\tau`$ | $`\vphantom{X^{2}_{2}}T/\tau`$ |
| `0\lt\Delta\le W` | $`0\lt\Delta\le W`$ | $`\strut 0\lt\Delta\le W`$ | $`\vphantom{X^{2}_{2}}0\lt\Delta\le W`$ |

Running text: original $`T`$ and guarded $`\strut T`$; original $`Z/2`$ and guarded $`\strut Z/2`$; original $`\tau`$ and guarded $`\strut\tau`$.
