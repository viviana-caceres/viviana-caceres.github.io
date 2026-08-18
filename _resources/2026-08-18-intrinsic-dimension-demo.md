---
title: "Estimating intrinsic dimension with TwoNN"
collection: resources
category: "Notebooks"
permalink: /resources/intrinsic-dimension-demo
date: 2026-08-18
excerpt: "A self-contained notebook that builds a 2D manifold inside a 10D space and recovers its dimension with the two-nearest-neighbours estimator."
notebook: notebooks/intrinsic-dimension-demo.ipynb
tags:
  - python
  - dimensionality reduction
---

This notebook walks through the two-nearest-neighbours (TwoNN) estimator from scratch —
no libraries beyond NumPy and Matplotlib, so you can see exactly where the dimension
estimate comes from.

## What it covers

1. **Building a test case.** Sampling points from a 2-dimensional manifold and embedding
   them linearly in 10 dimensions, so we know the right answer in advance.
2. **The estimator.** For every point, the ratio of the distances to its second and first
   nearest neighbours is Pareto-distributed with shape parameter equal to the intrinsic
   dimension. Fitting the empirical CDF recovers it in a few lines.
3. **Noise.** Sweeping the noise level to see how quickly the estimate drifts away from
   the true dimension once points sit off the manifold.

## Running it

The fastest option is **Run in Colab** above — nothing to install, and you can edit the
cells directly. **Download .ipynb** if you'd rather run it locally; it only needs
`numpy` and `matplotlib`.

## Reference

Facco, d'Errico, Rodriguez & Laio, *Estimating the intrinsic dimension of datasets by a
minimal neighborhood information*, [Scientific Reports 7, 12140 (2017)](https://www.nature.com/articles/s41598-017-11873-y).
