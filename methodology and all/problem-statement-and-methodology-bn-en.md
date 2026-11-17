# Class task: problem statement, solution approach, and brief methodology

**Purpose:** a study note for the Green Computing class task. It collects our problem definition, solution approach, and brief methodology in simple English and Bangla, in one place, for speaking and revision. Section ৬ is a glossary of the technical words used above; section ৭ explains every formula in plain words.

**Status:** the proposal is submitted. Solver implementation and experiments have not started. Nothing here is a measured result. The equation and parameter values shown are working candidates; the pilot freezes them.

**Sources:** the submitted proposal PDF, `docs/research-plan.md`, `docs/problem-definition.md`, `docs/model-equations.md`, `docs/reference-solution.md`, `Break-Even Methodology.md`, and the flowchart PDF in this folder.

**Note:** AI-assisted draft; team review pending.

---

## ১. Quick answer (say this first)

**English**

> We compare a physics-informed neural network (PINN) with a classical finite-difference solver on one fixed family of 2D steady-diffusion problems. The PINN trains once and then answers new parameter settings cheaply; the classical solver pays a full solve for every query. At the same accuracy, we ask how many new parameter queries the PINN needs before its total measured electricity, and separately its total runtime, catches up with the classical solver's. That query count is the break-even point N*. A crossover may not exist, or may sit too far away to be useful; either is a valid result.

**বাংলা**

> আমরা একটা নির্দিষ্ট 2D steady-diffusion সমস্যার family-তে PINN (physics-informed neural network) আর classical finite-difference solver-কে তুলনা করি। PINN একবার train হয়, তারপর নতুন parameter-এ সস্তায় উত্তর দেয়; classical solver-কে প্রতি query-তে পুরো solve-টা নতুন করে করতে হয়। সমান accuracy-তে আমাদের প্রশ্ন: কত নতুন query-র পর PINN-এর মোট মাপা বিদ্যুৎ (এবং আলাদাভাবে মোট সময়) classical solver-এর খরচের সমান হয়? সেই query-সংখ্যাটাই break-even পয়েন্ট N*। Crossover নাও থাকতে পারে, বা থাকলেও ব্যবহারের অযোগ্য দূরে থাকতে পারে; দুটোই বৈধ ফল।

---

## ২. Problem statement

### English

Many physics and engineering problems are written as partial differential equations (PDEs). In practice we often solve the same PDE many times, with only a parameter changed, for example the conductivity of a material. This is called a parametric family of problems.

There are two ways to answer such a family:

- **Classical solver (here, finite differences).** No training. Every new parameter query needs a full numerical solve, so every query costs energy and time again.
- **Parametric PINN.** A small neural network is trained once across the whole parameter family. Training costs a lot of energy and time upfront, but after training each query is one fast pass through the network.

The usual claim is that the PINN becomes cheap after training, so the upfront cost pays itself back over many queries. But within the literature we checked, nobody has measured this in electricity: earlier comparisons report runtime for single solves or cost in modeled units, not metered joules across a parameter family at matched accuracy.

**Our question:** for a fixed family of 2D steady-diffusion problems, how many new parameter queries N* does the parametric PINN need before its cumulative electricity equals that of a tuned finite-difference solver that is re-solved for every query? The same question is asked separately for cumulative runtime.

**The workload (working candidate, frozen at the pilot):** steady diffusion on the unit square,

```text
−∇ · (k ∇u) = 1        inside (0, 1)²
u = 0                  on the boundary
k = 1 + μ₁x + μ₂y      conductivity
−1/4 ≤ μ₁ ≤ 1/4,  −1/4 ≤ μ₂ ≤ 1/4
```

**Fairness rules:** both methods answer the same unseen (held-out) parameter settings, on the same fixed output grid, at the same accuracy targets: relative L2 error of 1% (10⁻²) and 0.1% (10⁻³); 0.01% is an optional stretch target. The comparison runs on one controlled machine, inside one declared measurement boundary that names which components (CPU, memory, GPU) are metered.

**Important condition:** a crossover may not exist, or may be too far away to be useful. Either outcome is a valid result. We do not assume the PINN wins.

### বাংলা

পদার্থবিজ্ঞান আর প্রকৌশলের অনেক সমস্যা PDE (partial differential equation) দিয়ে লেখা হয়। বাস্তবে একই PDE অনেকবার সমাধান করতে হয়, শুধু একটা parameter বদলায়, যেমন কোনো মাধ্যমের conductivity। এটাকে বলে parametric family।

এই ধরনের সমস্যার উত্তর দেওয়ার দুইটা পথ:

- **Classical solver (এখানে finite differences)।** কোনো training নেই। প্রতিটা নতুন parameter query-তে পুরো সংখ্যাগত সমাধান নতুন করে করতে হয়, তাই প্রতি query-তে বিদ্যুৎ আর সময় বারবার খরচ হয়।
- **Parametric PINN।** একটা ছোট নিউরাল নেটওয়ার্ককে পুরো parameter family নিয়ে একবার train করা হয়। Training-এ শুরুতেই অনেক বিদ্যুৎ আর সময় খরচ হয়, কিন্তু train হয়ে গেলে প্রতি query মানে network-এর ভেতর দিয়ে একবার যাওয়া, দ্রুত।

সবার ধারণা: train হয়ে গেলে PINN সস্তা, তাই শুরুর training-খরচ অনেকগুলো query-তে ফেরত আসে। কিন্তু আমাদের দেখা সাহিত্যে কেউ এটা বিদ্যুতে মেপে দেখায়নি: আগের তুলনাগুলোতে আছে একবারের solve-এর সময় বা মডেল করা খরচের একক; সমান accuracy-তে, পুরো parameter family জুড়ে, মিটারে মাপা জুল কেউ দেয়নি।

**আমাদের প্রশ্ন:** ঠিক করা একটা 2D steady-diffusion সমস্যার family-তে, parametric PINN-কে কত নতুন parameter query করতে হবে যাতে তার মোট বিদ্যুৎ-খরচ এমন এক tuned finite-difference solver-এর মোট খরচের সমান হয়, যেটা প্রতি query-তে নতুন করে solve করে? সেই সংখ্যাটাই N*। একই প্রশ্ন আলাদাভাবে মোট সময়ের (runtime) জন্যও করা হয়।

**কাজের সমস্যাটা (working candidate, pilot-এ চূড়ান্ত হবে):** একক বর্গক্ষেত্রে steady diffusion,

```text
−∇ · (k ∇u) = 1        ভেতরে (0, 1)²
u = 0                  ধারে (boundary)
k = 1 + μ₁x + μ₂y      conductivity
−1/4 ≤ μ₁ ≤ 1/4,  −1/4 ≤ μ₂ ≤ 1/4
```

**ন্যায্যতার নিয়ম:** দুই পদ্ধতিই একই unseen (held-out) parameter-গুলোর উত্তর দেবে, একই নির্দিষ্ট output grid-এ, একই accuracy লক্ষ্যে: relative L2 error 1% (10⁻²) আর 0.1% (10⁻³); 0.01% হলো optional stretch লক্ষ্য। তুলনাটা চলবে এক নিয়ন্ত্রিত মেশিনে, একটা ঘোষিত measurement boundary-র ভেতরে, যেটা স্পষ্ট বলে দেয় কোন কোন অংশ (CPU, memory, GPU) মাপা হচ্ছে।

**জরুরি শর্ত:** crossover নাও থাকতে পারে, বা থাকলেও ব্যবহারের অযোগ্য দূরে থাকতে পারে। দুটোই বৈধ ফল। আমরা ধরে নিই না যে PINN জিতবে।

---

## ৩. Solution approach

The strategy in one line: compare the two methods as cumulative cost curves over the number of queries, at matched accuracy, with measured energy and honest reuse for both sides, and read the crossing point off the curves.

### English

1. **Define the problem.** Fix the PDE family above, split the parameter box into training, validation, and held-out sets, fix the shared output grid, and set the error targets (1% and 0.1%).
2. **Pilot and freeze.** Check the energy meters (CPU, memory, GPU) and their noise floor. Validate both methods on a 1D heat problem with a known solution. Size the query blocks, repeats, and compute budget. Then freeze the equations, bounds, network, seeds, and budget, and tag the protocol in Git.
3. **Build both solvers.**
   - **Classical:** five-point finite differences with k taken at cell faces. The matrix is split into three fixed parts, A(μ) = A₀ + μ₁A₁ + μ₂A₂, built once; each query combines the parts and solves the linear system. A finer-grid solution with a Richardson check gives the reference answer used only for accuracy checks.
   - **PINN:** one network (x, y, μ₁, μ₂) → û. The zero boundary condition is built into the output, so training needs only the PDE residual. Train across the parameter family with at least three seeds. Failed runs are kept and enter the training-cost estimate under a declared retry policy.
4. **Pass the accuracy gate.** Both methods answer the held-out parameters on the shared grid. A target goes forward to energy trials only when both methods pass it. A miss is recorded as a result and kept out of the cost comparison.
5. **Measure energy and runtime.** Inside one declared boundary (CPU + memory + GPU, read for both methods): warm-up first, then repeated blocks of queries, with synchronized timing. Record setup cost S and per-query cost e, in joules and seconds, for each phase.
6. **Estimate the break-even points.** Fit cumulative cost E(N) = S + N·e for each method and check the slope is stable. The candidate crossing is N* = (S_P − S_C) / (e_C − e_P). Energy and runtime give two separate answers, each with an uncertainty range from seeds and repeats. Classify the outcome: no crossing, one method cheaper throughout, an uncertain crossing, or an extrapolated crossing.
7. **Report.** A comparison table per accuracy target, crossover plots with uncertainty bands, and answers to four questions (Q1 to Q4 below). The electricity used by the whole study is reported separately from the deployment cost model.

### বাংলা

মূল কৌশল এক লাইনে: দুই পদ্ধতিকে query-সংখ্যার সাথে মোট খরচের রেখা হিসেবে তুলনা করা, সমান accuracy-তে, দুই পক্ষের জন্যই মাপা বিদ্যুৎ আর সৎ (honest) reuse নিয়ে, আর রেখা দুটোর ছেদবিন্দু থেকে উত্তর পড়া।

1. **সমস্যা ঠিক করা।** উপরের PDE family স্থির করা; parameter-গুলো training, validation আর held-out ভাগে ভাগ করা; দুই পদ্ধতির জন্য এক output grid স্থির করা; error লক্ষ্য (1% আর 0.1%) ঠিক করা।
2. **Pilot আর protocol freeze।** মিটারগুলো (CPU, memory, GPU) কাজ করে কি না আর তাদের noise কেমন চেক করা। জানা উত্তরের একটা 1D heat সমস্যায় দুই পদ্ধতিকে যাচাই করা। Query block-এর আকার, repeat-সংখ্যা আর compute budget ঠিক করা। তারপর সমীকরণ, bound, network, seed আর budget জমিয়ে protocol Git-এ tag করা।
3. **দুই solver বানানো।**
   - **Classical:** পাঁচ-পয়েন্ট finite differences, k নেওয়া হয় cell face-এ। Matrix-কে তিনটা স্থির অংশে ভাগ করা হয়, A(μ) = A₀ + μ₁A₁ + μ₂A₂, একবারই বানানো হয়; প্রতি query-তে অংশগুলো জোড়া দিয়ে linear system solve করা হয়। আরও ঘন জালের (finer grid) সমাধান, Richardson check-সহ, শুধু accuracy যাচাইয়ের reference দেয়।
   - **PINN:** একটা network, ইনপুট (x, y, μ₁, μ₂), আউটপুট û। শূন্য boundary শর্ত আউটপুটের ভেতরেই বানানো থাকে, তাই training-এ শুধু PDE residual লাগে। পুরো parameter family জুড়ে train করা হয়, অন্তত তিনটা seed দিয়ে। ব্যর্থ run-গুলো হারানো হয় না; ঘোষিত retry policy অনুযায়ী সেগুলো training-খরচের হিসাবে ঢোকে।
4. **Accuracy gate পার হওয়া।** দুই পদ্ধতিই held-out parameter-এ, এক grid-এ উত্তর দেয়। দুজনেই লক্ষ্য পূরণ করলে তবেই সেই লক্ষ্যের energy trial-এ যাওয়া হয়। মিস করলে সেটা ফল হিসেবে জমা থাকে, খরচ-তুলনায় ঢোকে না।
5. **Energy ও runtime মাপা।** একটা ঘোষিত boundary-র ভেতরে (CPU + memory + GPU, দুই পদ্ধতির জন্যই পড়া হয়): আগে warm-up, তারপর query-র ব্লক বারবার, সময় synchronize করে। প্রতি ধাপে setup খরচ S আর প্রতি-query খরচ e জুল আর সেকেন্ডে জমা হয়।
6. **Break-even বের করা।** প্রতি পদ্ধতির জন্য মোট খরচ E(N) = S + N·e ফিট করা হয়, আর দেখা হয় slope স্থির কি না। ছেদবিন্দুর প্রার্থী N* = (S_P − S_C) / (e_C − e_P)। Energy আর runtime দুটো আলাদা উত্তর দেয়, প্রতিটার সাথে seed ও repeat থেকে আসা uncertainty থাকে। ফল শ্রেণিবদ্ধ হয়: কোনো ছেদ নেই, এক পদ্ধতি সব জায়গায় সস্তা, অনিশ্চিত ছেদ, বা extrapolate করা ছেদ।
7. **রিপোর্ট।** প্রতি accuracy লক্ষ্যে তুলনা-টেবিল, uncertainty band-সহ crossover plot, আর চারটা প্রশ্নের উত্তর (নিচে Q1–Q4)। পুরো স্টাডির নিজের খরচা বিদ্যুৎ deployment cost model থেকে আলাদা করে রিপোর্ট হয়।

---

## ৪. Brief methodology (short version for a quick answer)

The flowchart PDF in this folder shows the same steps as numbered boxes; the phases below match it.

### English

1. Freeze the problem: one 2D steady-diffusion family, two conductivity parameters, training and test parameters separate, one shared output grid, error targets 1% and 0.1%.
2. Pilot on a 1D heat problem with a known answer; check the meters; freeze the protocol.
3. Build a finite-difference solver with matrix reuse, and one parametric PINN trained across the family (three seeds).
4. Accuracy gate: both methods must reach the target error on unseen parameters on the shared grid; misses are reported, not compared.
5. Energy trials: meter setup, training, and repeated query blocks (CPU + memory + GPU) with synchronized timing.
6. Fit E(N) = S + N·e for each method; compute N* separately for energy and runtime, with uncertainty.
7. Report per target, including the case of no crossover; log the study's own electricity separately.

### বাংলা

এই ফোল্ডারের flowchart PDF-এ একই ধাপগুলো নম্বর দেওয়া বাক্সে আছে; নিচের ধাপগুলো সেটার সাথে মেলে।

1. সমস্যা জমানো: একটা 2D steady-diffusion family, দুইটা conductivity parameter, training আর test parameter আলাদা, এক output grid, error লক্ষ্য 1% আর 0.1%।
2. জানা উত্তরের 1D heat সমস্যায় pilot; মিটার চেক; protocol জমানো।
3. Matrix reuse-সহ finite-difference solver বানানো, আর পুরো family জুড়ে train করা একটা parametric PINN বানানো (তিনটা seed)।
4. Accuracy gate: unseen parameter-এ, এক grid-এ দুই পদ্ধতিকেই লক্ষ্যের error-এ পৌঁছাতে হবে; মিস রিপোর্ট হয়, তুলনায় ঢোকে না।
5. Energy trial: setup, training আর বারবার চালানো query block মাপা (CPU + memory + GPU), সময় synchronize করে।
6. প্রতি পদ্ধতির জন্য E(N) = S + N·e ফিট করা; energy আর runtime-এর জন্য আলাদা N*, uncertainty-সহ।
7. প্রতি লক্ষ্যে রিপোর্ট, যেখানে "crossover নেই" কথাটাও থাকে; স্টাডির নিজের বিদ্যুৎ আলাদা লগে।

---

## ৫. Key facts to remember

**Cost model (same form for runtime):**

```text
PINN:       E_P(N) = S_P + N · e_P
Classical:  E_C(N) = S_C + N · e_C
```

| Symbol | Meaning |
|---|---|
| S_P, S_C | Setup cost; for the PINN this includes training energy (joules or seconds) |
| e_P, e_C | Mean cost per complete query (one new parameter setting on the full grid) |
| N | Number of new parameter queries |

**Break-even (candidate crossing):**

```text
N* = (S_P − S_C) / (e_C − e_P)
```

A finite crossover needs S_P > S_C and e_P < e_C. If the slopes are equal or statistically indistinguishable, there is no reliable crossover.

**Fixed choices:**

- Error targets: relative L2 error 1% (10⁻²) and 0.1% (10⁻³); 0.01% (10⁻⁴) optional within the training budget.
- At least three training seeds; seed-to-seed spread enters the uncertainty.
- One controlled machine; declared boundary: CPU package + DRAM + GPU board.
- Candidate problem: −∇·(k∇u) = 1 on (0, 1)², k = 1 + μ₁x + μ₂y, μ₁, μ₂ ∈ [−¼, ¼], u = 0 on the boundary. Values frozen at the pilot.

**The four research questions:**

| # | Question |
|---|---|
| Q1 | Does an energy crossover N* exist within a usable query count? |
| Q2 | Do the energy and runtime crossovers land at the same N, or differ? |
| Q3 | How does N* move when the accuracy target tightens from 1% to 0.1%? |
| Q4 | How wide is the seed-to-seed uncertainty on N*, and does a crossover claim survive it? |

**Valid outcomes:** a finite crossover, one method cheaper throughout, an uncertain crossing, an extrapolated crossing, or no reliable crossover. All are reportable results.

---

## ৬. Technical words, in simple words (glossary)

The words are grouped by where they appear above. Each row gives the plain English meaning and the plain Bangla meaning.

### ক. The physics problem

| Term | English | বাংলা |
|---|---|---|
| PDE (partial differential equation) | The physics law written as an equation: it links a field's value to how it changes across space. | পদার্থের সূত্র সমীকরণের রূপে: কোনো রাশির মান আর জায়গা বরাবর তার পরিবর্তনের সম্পর্ক। |
| 2D steady diffusion | A spreading process, like heat spreading in a plate, that no longer changes with time (steady). 2D means the space has two coordinates, x and y. This is not an AI "diffusion model" that generates images. | ছড়িয়ে পড়ার প্রক্রিয়া, যেমন তাপের ছড়ানো, যা সময়ের সাথে আর বদলায় না (steady)। 2D মানে জায়গায় দুইটা মাত্রা, x আর y। এটা AI-র image-বানানো diffusion model না। |
| Unit square (0, 1)² | The problem's domain: a square where x and y both run from 0 to 1. | সমস্যার জায়গা (domain): বর্গক্ষেত্র, যার x আর y দুটোই 0 থেকে 1। |
| Conductivity k | How easily the material passes heat (or whatever spreads) at each point. Here it changes from place to place. | মাধ্যমটা প্রতি বিন্দুতে কত সহজে তাপ পার করায় (তাপ পরিবহন ক্ষমতা)। এখানে সেটা জায়গা বরাবর বদলায়। |
| Parameter μ₁, μ₂ | Two numbers that select one member of the problem family; each pair fixes one conductivity pattern. | দুইটা সংখ্যা, যেগুলো সমস্যা-পরিবারের একজন সদস্য বাছে; এক জোড়া মানে এক conductivity প্যাটার্ন। |
| Parametric family | All the problems made by varying μ₁, μ₂. Geometry, source, and boundary stay fixed; only k's shape changes. | μ₁, μ₂ বদলে যত সমস্যা তৈরি হয়, সব মিলে সেটা। জ্যামিতি, source, boundary এক থাকে; শুধু k-র আকার বদলায়। |
| Boundary condition (u = 0) | The rule on the domain's edges. Here the edges are pinned at zero, so nothing flows out. The formal name is a Dirichlet condition. | Domain-এর ধারের নিয়ম। এখানে ধার শূন্যে বাঁধা, তাই বাইরে কিছু বইতে পারে না। এর প্রকৃত নাম Dirichlet শর্ত। |
| Reference solution u_ref | A trusted near-true answer used only to grade the two methods; neither method under test produces it. | একটা নির্ভরযোগ্য প্রায়-সত্য উত্তর, শুধু দুই পদ্ধতির নম্বর দেওয়ার কাজে; পরীক্ষিত দুই পদ্ধতির কেউ এটা বানায় না। |

### খ. The two solvers

| Term | English | বাংলা |
|---|---|---|
| Classical solver | The traditional route: turn the PDE into equations on a grid and solve them numerically. No training. | চেনা পথ: PDE-কে জালের সমীকরণে ফেলে সংখ্যাগত সমাধান। কোনো training নেই। |
| Finite differences | Replace each derivative with differences between neighbouring grid points, which turns the PDE into a linear system. | প্রতিটা derivative-কে প্রতিবেশী বিন্দুর পার্থক্য দিয়ে বদলানো; PDE তখন linear system হয়ে যায়। |
| Five-point stencil | Each grid point's equation uses itself plus its four neighbours: up, down, left, right. | প্রতিটা বিন্দুর সমীকরণে সে নিজে আর চার প্রতিবেশী: উপর, নিচ, বাঁ, ডান। |
| Sparse matrix | The system's matrix is mostly zeros, since each row touches only a few neighbours; special solvers use that to save memory and time. | Matrix-এর বেশিরভাগ ঘর শূন্য, কারণ প্রতি row-এ অল্প কয়েকজন প্রতিবেশী; বিশেষ solver সেটা কাজে লাগিয়ে সময় ও জায়গা বাঁচায়। |
| Cell face | The shared edge of two neighbouring grid cells; k is averaged there so a varying material is handled correctly. | দুই পাশের ঘরের ভাগ হওয়া ধার; k সেখানে গড় করে নেওয়া হয়, যাতে বদলায়মান মাধ্যম ঠিকভাবে হিসাব হয়। |
| Matrix split, A(μ) = A₀ + μ₁A₁ + μ₂A₂ | The parameters enter the matrix only by scaling three fixed parts, so the parts are built once and each query just rescales, adds, and solves. | Parameter matrix-এ ঢোকে শুধু তিনটা স্থির অংশ গুণ করে; তাই অংশগুলো একবার বানানো হয়, প্রতি query-তে গুণে-যোগে জুড়ে solve। |
| Finer grid, Richardson check | Solve again on a much denser grid; the dense answer is the reference, and comparing the two grids sizes the coarse answer's error. | অনেক ঘন জালে আবার solve; ঘন জালের উত্তরই reference, আর দুই জাল মিলিয়ে মোটা জালের ভুলের মাপ বের হয়। |
| PINN | Physics-informed neural network: a network trained to satisfy the PDE itself, not only to copy example answers. | Physics-informed neural network: এমন network যাকে নমুনা উত্তর নকল করতে না, PDE-র সূত্র মানতে শেখানো হয়। |
| Parametric PINN | One network whose inputs include the parameters, so a single training covers the whole family. | এক network, ইনপুটে parameter-ও আছে; তাই এক training-ই পুরো family কভার করে। |
| MLP, tanh | A plain multi-layer network (multi-layer perceptron) with the smooth tanh function between layers; small here, per the budget. | সাধারণ বহু-স্তরের network (multi-layer perceptron), স্তরের মাঝে smooth tanh ফাংশন; এখানে ছোট, budget অনুযায়ী। |
| Automatic differentiation (autodiff) | The library computes the network's derivatives exactly by the chain rule; the residual needs them. | Library চেইন রুল মেনে network-এর derivative হুবহু বের করে দেয়; residual-এর জন্য এগুলো লাগে। |
| PDE residual r | How far the prediction is from satisfying the equation at one point; training pushes r toward 0. | এক বিন্দুতে prediction সমীকরণ কতটা ভাঙছে; training r-কে শূন্যের দিকে ঠেলে। |
| Hard boundary enforcement | The boundary value is baked into the output formula, so the prediction obeys it exactly and the loss needs no boundary term. The other option, soft enforcement, adds a boundary penalty to the loss. | Boundary মান আউটপুটের সূত্রেই বানানো, তাই prediction ধারে হুবহু শর্ত মানে আর loss-এ boundary-শাস্তি লাগে না। অন্য পথ, soft enforcement, loss-এ boundary-ভুলের শাস্তি যোগ করে। |
| Adam, L-BFGS | Two optimizers: Adam moves fast early, L-BFGS gives a careful final polish. | দুই optimizer: Adam শুরুতে দ্রুত এগোয়, L-BFGS শেষে যত্নের ফিনিশিং দেয়। |
| Training seed | The random number that starts each training run (initial weights, sampling). Different seeds give different results, so at least three are used. | এলোমেলো শুরুর সংখ্যা, যা প্রতিটা training চালের ভিত্তি (প্রাথমিক weight, sampling)। ভিন্ন seed ভিন্ন ফল দেয়, তাই অন্তত তিনটা নেওয়া হয়। |
| Failed runs, retry policy | Attempts that diverge or miss the target are logged with their cost and counted under a declared policy; nothing is hidden. | যে চাল ভেঙে পড়ে বা লক্ষ্য মিস করে, খরচসহ রেকর্ড হয় আর ঘোষিত নিয়মে হিসাবে পড়ে; কিছুই লুকানো হয় না। |

### গ. Fair comparison words

| Term | English | বাংলা |
|---|---|---|
| Query | One full task: take one new parameter pair and return the whole solution on the shared grid. | এক পূর্ণ কাজ: এক নতুন parameter জোড়া নিয়ে ভাগ করা grid-এ পুরো solution জমা দেওয়া। |
| Held-out (unseen) parameters | Parameter values kept outside all training and tuning, touched only at the final test. | যে parameter training বা tuning-এ কোনোভাবে ব্যবহার হয়নি; শুধু শেষ পরীক্ষায় আসে। |
| Training / validation / held-out split | Training parameters teach the network, validation parameters guide choices, held-out parameters grade the final answers. | Training parameter network-কে শেখায়, validation parameter সিদ্ধান্তে সাহায্য করে, held-out parameter শেষ উত্তর মাপে। |
| Output grid | The fixed point set where both methods must report answers, so the answers can be compared point by point. | নির্দিষ্ট বিন্দুসেট, যেখানে দুই পদ্ধতিকেই উত্তর জমা দিতে হয়; ফলে বিন্দু-বিন্দু তুলনা চলে। |
| Relative L2 error | The mistake's size over the whole grid, divided by the true answer's size. 1% means the mistake is one hundredth of the answer. | পুরো grid-এ ভুলের আকার ÷ সত্য উত্তরের আকার। 1% মানে ভুল উত্তরের এক-শতাংশ। |
| Matched accuracy | Both methods must reach the same error target before any cost comparison; a rough answer versus a fine one is not a fair race. | খরচ তুলনার আগে দুজনকেই এক error লক্ষ্যে পৌঁছাতে হবে; মোটা উত্তর বনাম ঝকঝকে উত্তর সমান প্রতিযোগিতা না। |
| Accuracy gate | The checkpoint before energy trials: a target is measured only when both methods pass it on held-out parameters. | Energy trial-এর আগের দ্বার: দুই পদ্ধতি held-out parameter-এ লক্ষ্য পার করলে তবেই সেই লক্ষ্য মাপা হয়। |
| Tuned baseline | The classical solver is configured carefully, with every valid reuse allowed; an under-tuned opponent would invent a false crossover. | Classical solver-কে যত্ন করে কনফিগার করা হয়, সব বৈধ reuse দিয়ে; দুর্বল করে রাখলে মিথ্যা crossover আঁটানো যেত। |

### ঘ. Measurement words

| Term | English | বাংলা |
|---|---|---|
| Controlled machine | Every run on one fixed computer, so hardware differences cannot explain any gap. | সব run এক নির্দিষ্ট কম্পিউটারে, তাই হার্ডওয়্যারের তফাত কোনো ফারাকের ব্যাখ্যা হতে পারে না। |
| Measurement boundary | The exact list of components whose electricity is counted (here CPU + memory + GPU), stated with every number. | কোন কোন অংশের বিদ্যুৎ গোনা হচ্ছে তার স্পষ্ট তালিকা (এখানে CPU + memory + GPU), প্রতিটা সংখ্যার সাথে ঘোষণা। |
| CPU package, DRAM, GPU board | The processor chip, the memory, and the graphics card; each has its own meter. | প্রসেসর চিপ, মেমরি, আর গ্রাফিক্স কার্ড; প্রতিটার নিজের মিটার। |
| Watt, joule | Power is the instant rate (watts); energy is power accumulated over time (joules = watts × seconds). | Power মুহূর্তের হার (watt); energy সময় জুড়ে জমা হার (joule = watt × second)। |
| Metered vs modeled | Metered values come from hardware counters; modeled values come from formulas or tools and must always be labeled as estimates. | Metered মান হার্ডওয়্যার কাউন্টার থেকে; modeled মান সূত্র বা টুলের অনুমান, সবসময় estimate লেবেল লাগবে। |
| Warm-up | Untimed practice queries before the measured blocks, so caches and clocks settle first. | মাপা ব্লকের আগে মাপা-বাইরের অভ্যাস-কোয়েরি, যাতে cache আর clock আগে গুছিয়ে নেয়। |
| Query block (K × R) | K queries in a row form one block, and the block repeats R times; blocks are long enough that their energy rises above meter noise. | Kটা query পরপর এক ব্লক, ব্লক রিপিট হয় R বার; ব্লক এত বড় যে বিদ্যুৎ-পাঠ মিটারের noise-এর উপরে ওঠে। |
| Synchronized timing | For GPU work, the clock stops only after the device reports that all its work is done, so no work escapes the timer. | GPU-র কাজে ঘড়ি থামে শুধু ডিভাইস সব কাজ শেষ বলার পরে, তাই কোনো কাজ টাইমার এড়িয়ে যায় না। |
| Setup cost S | The one-time cost before queries: training energy for the PINN, grid and matrix preparation for the classical solver. | Query শুরুর আগের এককালীন খরচ: PINN-এ training-বিদ্যুৎ, classical solver-এ grid ও matrix তৈরি। |
| Per-query cost e | The average cost of one complete query, read from the measured blocks. | এক পূর্ণ query-র গড় খরচ, মাপা ব্লক থেকে। |
| Runtime (wall-clock time) | Elapsed seconds on a normal clock; in this project it is the computational cost, separate from energy. | সাধারণ ঘড়ির সেকেন্ড; এই প্রজেক্টে এটাই computational cost, energy থেকে আলাদা। |
| Noise floor | The meters' own small random jitter; measured blocks must be long enough to rise above it. | মিটারের নিজের ছোট এলোমেলো কাঁপন; মাপা ব্লক এর উপরে ওঠার মতো বড় হতে হবে। |

### ঙ. Process and break-even words

| Term | English | বাংলা |
|---|---|---|
| Pilot | A small rehearsal on a simpler 1D problem before the main study: it tests the meters, both codes, and the budget. | মূল স্টাডির আগে সহজ 1D সমস্যায় ছোট মহড়া: মিটার, দুই code আর budget পরীক্ষা হয়। |
| Protocol freeze, Git tag | After the pilot, every choice (equations, bounds, network, budget, blocks) is fixed and recorded with a Git tag, so nothing shifts mid-study. | Pilot-এর পর সব সিদ্ধান্ত (সমীকরণ, bound, network, budget, block) স্থির করে Git tag-এ জমা, যাতে কাজের মাঝে কিছু সরে না। |
| Energy trial | The measured campaign for one accuracy target: setup, training, and repeated query blocks inside the declared boundary. | এক accuracy লক্ষ্যের মাপা অভিযান: ঘোষিত boundary-র ভেতরে setup, training আর বারবার চালানো query block। |
| Deployment cost vs study electricity | The model of running one trained method in use is reported separately from the total electricity the research itself burned, including failures and tuning. | Train হওয়া এক পদ্ধতি কাজে চলার খরচ-মডেল আর গবেষণা নিজের মোট খরচা (ব্যর্থতা ও tuning-সহ) আলাদা করে রিপোর্ট হয়। |
| Cumulative cost curve | Total cost drawn against the query count N; each method's curve is a straight line with its own start and slope. | Query-সংখ্যা N-এর বিপরীতে মোট খরচের রেখা; প্রতি পদ্ধতির রেখা সরল, নিজের শুরু ও ঢাল (slope) নিয়ে। |
| Break-even point, crossover N* | The query count where the two lines meet; from there on, the cheaper-per-query method stays ahead. | দুই রেখা যে query-সংখ্যায় মেলে; সেখান থেকে প্রতি-query-সস্তা পদ্ধতি এগিয়ে থাকে। |
| Linear model, slope stability | The model treats every query as costing about the same; the measured slope is checked for drift, and a drifting slope voids the crossover claim. | মডেল ধরে প্রতি query-র খরচ মোটামুটি এক; মাপা slope সরে কি না দেখা হয়, slope সরলে crossover-দাবি বাতিল। |
| Uncertainty interval, bootstrap | A range built by resampling the repeated measurements and seeds many times; it shows how far N* could move. | বারবার মাপা মান ও seed বারবার নমুনা করে বানানো পাল্লা; দেখায় N* কতটা এদিক-ওদিক হতে পারে। |
| Outcome classes | No crossing within the measured range; one method already cheaper everywhere; an uncertain crossing inside measurement noise; or an extrapolated crossing beyond the measured range. | মাপা রেজে ছেদ নেই; এক পদ্ধতি সব জায়গায় সস্তা; ছেদ অনিশ্চয়তার ভেতরে ঢাকা; বা ছেদ মাপার রেজের বাইরে গিয়ে অনুমান করা। |

---

## ৭. The formulas, in simple words

### ৭.১ The PDE (the physics)

```text
−∇ · (k ∇u) = 1        inside the unit square
u = 0                  on the boundary
k = 1 + μ₁x + μ₂y
−1/4 ≤ μ₁ ≤ 1/4,  −1/4 ≤ μ₂ ≤ 1/4
```

| Symbol | English | বাংলা |
|---|---|---|
| u | The unknown answer at each point, like a temperature field | প্রতি বিন্দুতে অজানা উত্তর, যেমন তাপের মান |
| k | Conductivity; changes from place to place, steered by μ₁, μ₂ | পরিবহন ক্ষমতা; জায়গা বরাবর বদলায়, μ₁, μ₂ এটা নিয়ন্ত্রণ করে |
| ∇u | How fast u changes as you move (two parts, uₓ and uᵧ) | সরার সাথে সাথে u কত দ্রুত বদলায় (দুই অংশ, uₓ আর uᵧ) |
| ∇·( ) | The net flow entering or leaving a point; k∇u is the flow itself | এক বিন্দুতে প্রবাহ ঢুকছে না বেরোচ্ছে, সেই নিট হার; k∇u হলো প্রবাহটা |
| − sign | Flow runs from more to less | প্রবাহ বেশি থেকে কমের দিকে বইতে চায় |
| = 1 | A constant source, the same at every point | সমান উৎস, প্রতি বিন্দুতে একই পরিমাণ |

**English:** one square plate, a material that conducts differently at each point, edges pinned at zero, and the same source everywhere inside. Find the steady field u.

**বাংলা:** একটা বর্গ পাতা, যার মাধ্যম প্রতি বিন্দুতে ভিন্নভাবে পরিবহন করে, ধার শূন্যে বাঁধা, ভেতরে সব জায়গায় সমান উৎস। স্থির অবস্থার রাশি u বের করতে হবে।

Because k changes with position, the equation opens up as:

```text
−[k(uₓₓ + uᵧᵧ) + kₓuₓ + kᵧuᵧ] = 1
```

The kₓuₓ and kᵧuᵧ pieces exist only because k varies with place; a uniform material would drop them. **English:** the varying material adds two extra terms. **বাংলা:** মাধ্যম যেহেতু জায়গা বরাবর বদলায়, তাই দুইটা বাড়তি পদ আসে।

The bounds keep k between 1/2 and 3/2, never zero or negative. **English:** a positive conductivity keeps the problem solvable for every allowed parameter pair. **বাংলা:** conductivity ধনাত্মক থাকায় অনুমোদিত সব parameter জোড়ায় সমস্যাটা সমাধানযোগ্য থাকে।

### ৭.২ Relative L2 error (the grade)

```text
ε = ‖û − u_ref‖₂ / ‖u_ref‖₂
‖q‖₂ = √(q₁² + q₂² + … + q_M²)
```

- û is a method's answer, u_ref the reference; both are lists of M grid values.
- The top is the mistake's overall size; the bottom is the true answer's overall size.
- Targets: ε ≤ 0.01 (1%) and ε ≤ 0.001 (0.1%).

**English:** the mistake counted as a share of the answer itself, over the whole grid.

**বাংলা:** পুরো grid জুড়ে ভুলটা উত্তরের কত ভাগ, সেই অনুপাত।

### ৭.৩ Matrix split (the classical solver's trick)

```text
A(μ) = A₀ + μ₁A₁ + μ₂A₂
```

- A(μ) is the linear system's matrix for one parameter pair.
- A₀, A₁, A₂ are three fixed matrices built once.
- Each query: scale A₁ by μ₁, scale A₂ by μ₂, add A₀, then solve.

**English:** the parameters enter only through simple scaling, so the expensive building happens once and each query just rescales and solves.

**বাংলা:** parameter ঢোকে শুধু সরল গুণ (scaling) হয়ে, তাই মূল নির্মাণ একবারই; প্রতি query-তে গুণে-যোগে জুড়ে solve।

### ৭.৪ The PINN output with the boundary built in

```text
û(x, y; μ) = x(1−x) · y(1−y) × v(x, y, μ₁, μ₂; w)
```

- v is the network's raw output and w its learned weights.
- The multiplier x(1−x)y(1−y) is exactly 0 on all four edges, so û = 0 there automatically.

**English:** the boundary rule is baked into the output, so training only fits the inside physics.

**বাংলা:** boundary নিয়মটা আউটপুটের সূত্রেই বানানো, তাই training শুধু ভেতরের পদার্থ মেলায়।

### ৭.৫ PDE residual and training loss

```text
r = −∇ · (k ∇û) − 1
L = average of r² over sampled points
```

- r is the equation error at one sampled point; a perfect answer gives r = 0.
- Autodiff supplies û's derivatives; the optimizer lowers the mean of r².

**English:** training punishes the network wherever its answer breaks the equation.

**বাংলা:** যেখানে নেটওয়ার্কের উত্তর সমীকরণ ভাঙে, training সেখানে শাস্তি দেয়।

### ৭.৬ Energy from the meter

```text
E = ∫ P(t) dt        watts × seconds = joules
```

- P(t) is the combined power of the metered components at time t.
- Energy is summed over the whole measured window; one instant reading is not energy.

**English:** energy is power accumulated over the run, not one glance at the meter.

**বাংলা:** energy মানে পুরো run জুড়ে জমা হওয়া power, মিটারে একবার তাকানো না।

### ৭.৭ Cost model and break-even

```text
PINN:       E_P(N) = S_P + N · e_P
Classical:  E_C(N) = S_C + N · e_C
N* = (S_P − S_C) / (e_C − e_P)
```

- Each line is one-time setup S plus a fixed price e per query.
- The two lines meet where the totals are equal; solving E_P(N) = E_C(N) gives N*.
- A finite, meaningful N* needs S_P > S_C (the PINN starts ahead in cost) and e_P < e_C (but each PINN query is cheaper).
- The same form gives the runtime crossover: replace energy with seconds. The two crossovers need not land at the same N.

**English:** two straight lines over N. The PINN's line starts higher (training) but climbs slower (cheap queries); N* is the query count where it catches up.

**বাংলা:** N-এর সাথে দুইটা সরলরেখা। PINN-এর রেখা উপর থেকে শুরু করে (training-খরচ) কিন্তু ধীরে ওঠে (সস্তা query); N* হলো সেই query-সংখ্যা যেখানে সে ধরে ফেলে।

If the slopes are equal, or their difference is smaller than the measurement uncertainty, there is no reliable crossover.
