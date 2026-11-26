"""Local search filter applied to every downloaded title + abstract (search v1, 2026-11-23).

A record is kept for screening when it passes any of:
  F1 energy route:      neural PDE solver AND computational energy/power/carbon term
  F2 break-even route:  neural PDE solver AND break-even/amortization term
  F3 parametric route:  physics-informed AND classical-solver term AND cost term AND parametric/many-query term
Text is lower-cased and hyphens, slashes and underscores become spaces before matching.
"""
import re


def _rx(*parts):
    return re.compile("|".join(parts))


A1 = _rx(r"physics (informed|constrained|guided|embedded) (neural|deep|machine|network|operator|deeponet|kan|learning|graph)",
         r"\bpinns?\b", r"\bvpinns?\b", r"\bxpinns?\b", r"\bcpinns?\b", r"\bpino\b", r"\bpikans?\b",
         r"deep (ritz|galerkin)")
A2 = _rx(r"neural operators?", r"\bfno\b", r"deeponets?", r"operator learning", r"neural (pde|partial differential equation) solvers?",
         r"learned (pde )?solvers?", r"neural (network )?surrogates?",
         r"(machine learning|deep learning|neural network|graph neural network|\bgnn|convolutional|\bcnn) (based )?(surrogate|emulator)s?",
         r"neural emulators?", r"(machine learning|deep learning|data driven|neural|\bai\b) (based )?(weather|climate) (prediction|forecasting|model|emulat)")
NN = _rx(r"neural networks?", r"deep learning", r"machine learning")
PDE = _rx(r"partial differential equations?", r"\bpdes?\b", r"navier stokes", r"poisson", r"heat (equation|conduction|transfer)",
          r"diffusion equation", r"darcy", r"elasticity", r"helmholtz", r"burgers", r"advection", r"wave equation",
          r"schr[oö]dinger", r"allen cahn", r"reaction diffusion", r"\bcfd\b", r"computational fluid dynamics",
          r"finite (element|difference|volume)", r"numerical weather", r"weather (prediction|forecast)", r"climate model",
          r"(fluid|shear|turbulent|incompressible|compressible|multiphase|porous media) flows?", r"turbulen", r"fluid dynamics",
          r"flow fields?", r"maxwell", r"electromagnetic", r"structural mechanics", r"solid mechanics")
CL = _rx(r"finite (element|difference|volume)s?", r"spectral (method|element|solver)s?", r"numerical (solver|method|solution|simulation|scheme|model)s?",
         r"(traditional|classical|conventional|standard|high fidelity|full order) (numerical )?(pde )?(solver|method|simulation|model|approach)s?",
         r"\bsolvers?\b", r"\bfem\b", r"\bfdm\b", r"\bfvm\b", r"\bbem\b", r"multigrid", r"conjugate gradient", r"krylov",
         r"lattice boltzmann", r"reduced (basis|order)", r"comsol", r"openfoam", r"ansys", r"abaqus", r"fluent", r"petsc", r"fenics",
         r"\bcfd\b", r"numerical weather prediction", r"\bnwp\b")
CO = _rx(r"computational(ly)? (cost|time|efficien|speed|performance|burden|expense|expensive|effort|resource|advantage|saving)",
         r"comput(ation|ing) (cost|time)", r"(solution|solve|solving|simulation|training|inference|prediction|evaluation) (time|cost|speed)s?",
         r"(cpu|gpu) (time|hour)s?", r"\brun ?times?\b", r"wall ?clock", r"speed ?ups?", r"(faster|slower|cheaper) than",
         r"times faster", r"orders? of magnitude (faster|speed|cheaper|reduction|less|lower|fewer)", r"\bflops?\b",
         r"performance benchmark", r"exceedingly long time")
EN = _rx(r"energy (consumption|efficien|usage|cost|footprint|use|saving|budget|measurement|aware|requirement|demand|reduction|per)s?",
         r"(less|lower|reduced|total|operating|computational|electrical|electricity) energy", r"electricity",
         r"power (consumption|draw|usage|budget|measurement)s?", r"carbon (footprint|emission|cost|intensity|impact)s?",
         r"\bco2\b", r"\bco 2\b", r"greenhouse", r"\bjoules?\b", r"\bkwh\b", r"\bwatts?\b", r"green (ai|computing|machine learning|deep learning)",
         r"sustainab", r"\brapl\b", r"\bnvml\b", r"codecarbon", r"carbontracker", r"energy efficient")
BE = _rx(r"break ?even", r"amorti[sz]", r"many query", r"multi query", r"multiple queries", r"\bqueries\b",
         r"number of (queries|evaluations|simulations|solves|forward solves)", r"offline (cost|phase|stage|training|computation)",
         r"online (cost|phase|stage)", r"offline online", r"cost (accuracy|benefit)", r"accuracy cost", r"total (computational )?cost",
         r"training cost", r"pays? off", r"payback")
PA = _rx(r"parametri", r"parameteri[sz]", r"parameter (space|range|family|varying|dependent|sweep)s?", r"family of",
         r"surrogates?", r"real time", r"design optimi[sz]", r"optimi[sz]ation loop", r"uncertainty quantification", r"\buq\b",
         r"inverse design", r"many query", r"multi query", r"repeated(ly)? (solv|evaluat|simul|quer)", r"amorti[sz]",
         r"(unseen|new|different|varying|various) (parameter|condition|geometr|boundary|initial|coefficient|source|instance)s?")


def norm(text):
    t = (text or "").lower()
    t = re.sub(r"[-_/‐‑–—]", " ", t)
    return re.sub(r"\s+", " ", t)


def routes(title, abstract):
    t = norm(f"{title} . {abstract}")
    a1, a2 = bool(A1.search(t)), bool(A2.search(t))
    ns = a1 or a2 or (bool(NN.search(t)) and bool(PDE.search(t)))
    out = []
    if ns and EN.search(t):
        out.append("F1")
    if ns and BE.search(t):
        out.append("F2")
    if a1 and CL.search(t) and CO.search(t) and PA.search(t):
        out.append("F3")
    return out


def title_keep(title):
    """Route T for records with no abstract anywhere: the title names a neural PDE solver and a cost, energy or parametric cue."""
    t = norm(title)
    ns = A1.search(t) or A2.search(t) or (NN.search(t) and PDE.search(t))
    return bool(ns and (EN.search(t) or BE.search(t) or CO.search(t) or PA.search(t)))


def chase_keep(title, abstract):
    """Looser filter for citation-chasing records: neural PDE solver plus any energy, break-even or cost term."""
    t = norm(f"{title} . {abstract}")
    ns = A1.search(t) or A2.search(t) or (NN.search(t) and PDE.search(t))
    return bool(ns and (EN.search(t) or BE.search(t) or CO.search(t)))
