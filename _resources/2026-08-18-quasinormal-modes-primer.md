---
title: "A short primer on quasinormal modes"
collection: resources
category: "Tutorials"
permalink: /resources/quasinormal-modes-primer
date: 2026-08-18
excerpt: "What ringdown modes are, why their frequencies depend on only two numbers, and what that buys us as a test of general relativity."
tags:
  - black holes
  - gravitational waves
---

When two black holes merge, the remnant does not settle down quietly. It rings, and the
gravitational waves it emits during that ringdown can be written as a sum of damped
sinusoids called **quasinormal modes**.

## Why only two numbers matter

The no-hair theorem says an isolated, astrophysical black hole in general relativity is
fully described by its mass $M$ and spin $a$. Every quasinormal mode frequency
$\omega_{\ell m n}$ and damping time $\tau_{\ell m n}$ is then a fixed function of those
two parameters alone.

That is a strong statement, and it is testable. Measure several modes independently, and
they must all point back to the same $(M, a)$. If they don't, something in the picture is
wrong.

## The dimensional argument

Here is the framing I find most useful. Suppose you measure $N$ mode frequencies and
damping rates. Each measurement is a coordinate, so your data lives in a
$2N$-dimensional space. But if general relativity holds, every one of those points was
generated from just two underlying parameters — so the data must lie on a
**2-dimensional surface** inside that much larger space.

The dimension of that surface is measurable, without ever fitting a black hole model to
the data. If it comes out above 2, the extra directions correspond to degrees of freedom
the Kerr solution does not have.

## Where to go next

- The companion notebook, [Estimating intrinsic dimension with TwoNN](/resources/intrinsic-dimension-demo),
  shows how to measure the dimension of a dataset in practice.
- Berti, Cardoso & Starinets, [Quasinormal modes of black holes and black branes](https://arxiv.org/abs/0905.2975),
  is the standard review if you want the full derivation.
