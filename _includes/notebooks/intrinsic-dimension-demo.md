<!-- Generated from notebooks/intrinsic-dimension-demo.ipynb by scripts/notebook_to_markdown.py. Do not edit by hand. -->


A quick, self-contained demo of the *two-nearest-neighbours* (TwoNN) estimator.
We generate points on a 2-dimensional surface embedded in a higher-dimensional
space and check that the estimator recovers a dimension near 2.

Run this top to bottom — no data files needed.

{% raw %}
```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
```
{% endraw %}

## 1. Make a 2D manifold living in 10D

We sample two latent coordinates, map them through a random linear embedding
into 10 dimensions, and optionally add noise.

{% raw %}
```python
def make_manifold(n=2000, latent_dim=2, ambient_dim=10, noise=0.0, rng=rng):
    """Sample `n` points from a `latent_dim` manifold embedded in `ambient_dim` space."""
    z = rng.uniform(-1, 1, size=(n, latent_dim))
    embedding = rng.normal(size=(latent_dim, ambient_dim))
    x = z @ embedding
    if noise:
        x = x + rng.normal(scale=noise, size=x.shape)
    return x


X = make_manifold()
X.shape
```
{% endraw %}

{% raw %}
```
(2000, 10)
```
{% endraw %}

## 2. The TwoNN estimator

For each point, take the distances to its two nearest neighbours, $r_1$ and $r_2$.
The ratio $\mu = r_2 / r_1$ follows a Pareto distribution whose shape parameter *is*
the intrinsic dimension $d$. Fitting a line to the empirical CDF gives $d$ directly.

Reference: Facco et al., *Scientific Reports* 7, 12140 (2017).

{% raw %}
```python
def twonn(X, discard_fraction=0.1):
    """Estimate intrinsic dimension via the two-nearest-neighbours ratio."""
    # Pairwise distances, then the two smallest nonzero ones per point.
    diff = X[:, None, :] - X[None, :, :]
    dists = np.sqrt((diff ** 2).sum(-1))
    np.fill_diagonal(dists, np.inf)
    nearest = np.sort(dists, axis=1)[:, :2]

    r1, r2 = nearest[:, 0], nearest[:, 1]
    mu = r2 / r1
    mu = np.sort(mu[np.isfinite(mu) & (mu > 1)])

    # Empirical CDF, dropping the noisy tail.
    n = len(mu)
    keep = int(n * (1 - discard_fraction))
    F = np.arange(1, n + 1) / n

    x = np.log(mu[:keep])
    y = -np.log(1 - F[:keep])

    # Line through the origin: slope is the dimension.
    return float((x @ y) / (x @ x))


print(f"estimated intrinsic dimension: {twonn(X):.2f}  (true value: 2)")
```
{% endraw %}

{% raw %}
```
estimated intrinsic dimension: 1.97  (true value: 2)
```
{% endraw %}

## 3. How does noise degrade the estimate?

Noise pushes points off the manifold, so the estimator starts to see the
ambient dimension instead of the latent one.

{% raw %}
```python
noise_levels = np.linspace(0, 0.5, 11)
estimates = [twonn(make_manifold(n=1000, noise=s)) for s in noise_levels]

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(noise_levels, estimates, "o-")
ax.axhline(2, ls="--", color="gray", label="true dimension")
ax.set_xlabel("noise standard deviation")
ax.set_ylabel("estimated intrinsic dimension")
ax.legend()
fig.tight_layout()
```
{% endraw %}

![](/images/notebooks/intrinsic-dimension-demo/output_1.png)

## Try it yourself

- Change `latent_dim` to 3 or 5 and see whether TwoNN keeps up.
- Raise `ambient_dim` while holding `latent_dim` fixed — the estimate should not move.
- Swap the linear embedding for a nonlinear one (e.g. a Swiss roll).
