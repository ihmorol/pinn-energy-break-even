# সামারি নোট: আমার ভাগের পাঁচটা পেপার (বাংলা)

**প্রজেক্ট:** Reaching the energy and computational break-even point between PINNs, and classical solvers.
**তারিখ:** 2026-11-14
**রিভিশনের ছোট নোট।** বিস্তারিত ব্যাখ্যা ও উপমা: [literature-review-bn.md](literature-review-bn.md)। টিমের চেক করা নোট: `references/` ফোল্ডার।
মনে রাখার গল্প এক লাইনে: Raissi পদ্ধতি দেয় → Grossmann তুলনা দেখায় → de Hoop মাপদণ্ড দেয় → Huang সূত্র দেয় → Henderson মাপার নিয়ম দেয়।

## ১. Raissi, Perdikaris, Karniadakis — PINN-এর ভিত্তি পেপার

**পেপারটা কী কাজ করেছে:**
- নিউরাল নেটওয়ার্ক দিয়ে PDE সমাধানের মূল পদ্ধতি (PINN) চালু করে: নেটওয়ার্ককে শুধু উত্তর মিলাতে শেখানো হয় না, সূত্রও মানতে শেখানো হয়।
- Loss দুই অংশের: যেখানে উত্তর জানা (শুরুর মান, ধার) সেখানে ভুল মেলানো (MSE_u), আর অনেক collocation point-এ সূত্র কতটা ভাঙছে সেই residual-এর গড় বর্গ (MSE_f)। Derivative আসে autodiff দিয়ে।
- সামান্য data দিয়ে ভালো accuracy: Burgers-এ relative L2 ভুল 6.7×10⁻⁴ (~60 সেকেন্ড, Titan X GPU); Schrödinger (1.97×10⁻³) আর Allen-Cahn-এর উদাহরণও আছে।
- লেখকেরা নিজেরাই বলেন: এটা classical numerical পদ্ধতির বিকল্প না।
- ফাইল নোট: আমাদের PDF আসলে 2017-এর Part I preprint (arXiv:1711.10561), published পেপার না; method cite করতে হবে JCP 2019।

**আমাদের প্রজেক্টে প্রাসঙ্গিকতা:**
- আমাদের PINN-এর ট্রেনিং loss `L_PDE = mean(r²)` সরাসরি এর MSE_f থেকে; boundary penalty এর MSE_b ধারা থেকে।
- Relative L2 error দিয়ে accuracy মাপার রীতি এখান থেকে; আমাদের held-out টার্গেট (1%, 0.1%) সেই মাপেই।
- এই পেপারে খরচ, সময়ের তুলনা বা বিদ্যুতের মাপ কিছুই নেই; তাই এটা শুধু method-এর cite, খরচের দাবিতে ব্যবহার করা যাবে না।

## ২. Grossmann et al. 2024 — PINN বনাম FEM-এর সরাসরি রেস

**পেপারটা কী কাজ করেছে:**
- ৬টা সমস্যায় (Poisson 1D/2D/3D, Allen-Cahn, Schrödinger) vanilla PINN (JAX, GPU) বনাম FEM (FEniCS, CPU) একই মাঠে তুলনা: solution time, evaluation time, আর relative L2 error; প্রতিটা চাল 10 বারের গড়।
- ফল: প্রায় সব জায়গায় FEM জেতে, 2 থেকে 6 orders আগে পৌঁছায়; Allen-Cahn-এ PINN কিছু সেটিংয়ে পুরো ব্যর্থ।
- ব্যতিক্রম: 3D Poisson-এ evaluation-এ PINN 2-3 orders জেতে (FEM-এর interpolation এমনকি তার নিজের solve-এর চেয়েও ধীর ছিল সেখানে)।
- এরা মাপে শুধু wall-clock সময়; energy বা বিদ্যুৎ কিছুই মাপে না।

**আমাদের প্রজেক্টে প্রাসঙ্গিকতা:**
- এটা আমাদের সরাসরি predecessor। এরা parametric PDE (এক সমস্যার অনেক parameter) চেক করেনি আর energy মাপেনি; এই দুই ফাঁকই আমাদের প্রজেক্টের অবদান।
- তাদের evaluation জয় দেখায় "ট্রেন হওয়া নেটওয়ার্কের প্রতি-কোয়েরি দাম কম" এমন পরিস্থিতি আস্তে; আমাদের N* ফর্মুলা ঠিক সেটাকে সংখ্যায় মাপে।
- দুইটা শিক্ষা আমাদের প্রোটোকলে আছে: device placement ঘোষণা করা (তাদের GPU বনাম CPU confound), আর classical query-র ধাপগুলো (assemble, solve, grid evaluation) আলাদা মাপা (তাদের interpolation anomaly)।

## ৩. de Hoop, Huang, Qian, Stuart 2022 — cost-accuracy কাঠামো

**পেপারটা কী কাজ করেছে:**
- Operator learning (পুরো ইনপুট-মানচিত্র দিলে পুরো সমাধান-মানচিত্র শেখা) বিচারের কাঠামো দেয়; মূল প্রশ্ন: যে accuracy পেল, তার জন্য evaluation খরচ কত, আর খরচ accuracy-র সাথে কীভাবে বদলায়।
- চারটা supervised architecture (PCA-Net, DeepONet, PARA-Net, FNO) আর চারটা সমস্যায় মাপা: training cost = কত truth-solver চালানো (data volume), evaluation cost = FLOPs।
- ফল: smooth সমস্যায় data বাড়ালে ভুল O(N^(−1/2)) হারে কমে; FNO smooth সমস্যায় ভালো কিন্তু dimension বাড়লে খরচ খারাপ; বিজয়ী সমস্যা-ভেদে বদলায়, কোনো সার্বজনীন জেতা নেই।
- মনে রাখার জিনিস: এখানে Darcy উদাহরণ নেই (প্রচলিত ভুল); আর এরা PINN পড়ে না, সব surrogate supervised operator learner।

**আমাদের প্রজেক্টে প্রাসঙ্গিকতা:**
- কেন আমরা fixed accuracy-তে (1%, 0.1%) খরচ তুলনা করি, শুধু "কে ভালো" না: সেই ন্যায্যতার ভিত্তি-সাইটেশন এই পেপার।
- এদের training cost বনাম online evaluation cost ভাগ আমাদের S (শুরুর খরচ) বনাম e (প্রতি কোয়েরি) ভাগের পূর্বসূরি; আমাদের N* ফর্মুলা এই দুই ভাগকেই জুড়ে দেয়।
- এরা মাপে FLOPs আর data volume; বিদ্যুৎ বা wall-clock না। আমরা সেই খানায় সরাসরি মাপা খরচ যোগ করি।

## ৪. Huang et al. 2026 — decision framework ও break-even-এর সূত্র

**পেপারটা কী কাজ করেছে:**
- বড় review: কখন classical, কখন machine learning, কখন hybrid solver ন্যায্য, তার decision framework (query volume, data availability, certification) আর প্রমাণের সিঁড়ি P0 থেকে P4।
- Amortization সূত্র (Sec 4.5, Eq 1): `N* = (N_tr·c_gen + C_train)/(c_cl − c_nn) = (γ·N_tr + τ)/(1 − 1/S)`, S > 1; S ≤ 1 হলে surrogate কখনো break-even করে না।
- নিজেরা Darcy-তে মেপেছে (FNO on GPU বনাম finite volume + AMG-CG on single-core CPU, 3 seed): 1% এর নিচে accuracy-তে কোনো FNO 3.1×10⁴ কোয়েরির আগে break-even করে না; 512² resolution-এ 9.2×10⁵; offline খরচের ~97% training।
- সতর্কবার্তা: 76টা ML পেপারের প্রায় 79% দুর্বল baseline হারিয়ে দাবি করেছে; FNO-র 440× per-query speedup end-to-end নামে ~1.5×।

**আমাদের প্রজেক্টে প্রাসঙ্গিকতা:**
- আমাদের `N* = (S_P − S_C)/(e_C − e_P)` এই সূত্রের গঠনই অনুসরণ করে। দুই পার্থক্য: আমরা বিদ্যুৎ মাপি (এরা শুধু সময়), আর আমাদের PINN solver-generated data খায় না, তাই আমাদের N* মূলত training খরচের হাতে।
- আমাদের তুলনা এদের P3 রাং-এ: একই accuracy-তে, মাপা খরচে, ধারালো classical প্রতিপক্ষের সাথে।
- 79% সতর্কবার্তা আমাদের মনে করায়: আমাদের FD baseline ধারালো হতে হবে (tolerance, preconditioner, grid convergence), নইলে আমাদের দাবিও ওই কাতারে বসবে।
- তাদের Darcy সংখ্যা আমাদের N*-এর quantitative prior, পূর্বানুমান না: আমাদের ছোট সমস্যায় N* অনেক ছোট বা বিশাল দুটোই হতে পারে।
- ফাইল নোট: preprint v1, peer review হয়নি; cite-এ preprint লিখতে হবে।

## ৫. Henderson et al. 2020 — বিদ্যুৎ ও কার্বন মাপার নিয়ম

**পেপারটা কী কাজ করেছে:**
- ML-এর বিদ্যুৎ আর কার্বন খরচ মাপা ও রিপোর্ট করার টুল ও প্রোটোকল: RAPL/powercap বা PowerGadget (CPU+DRAM), nvidia-smi (GPU), psutil (প্রতি-প্রসেস utilization)।
- প্রতি-প্রসেস attribution সূত্র (Sec 4.3.1, Eq 1): `e_total = PUE × Σ(p_dram·e_dram + p_cpu·e_cpu + p_gpu·e_gpu)`; শেয়ার্ড মেশিনে ভাগ না করলে ডাবল হিসাব হয়।
- মূল ফল: FLOPs বিদ্যুতের প্রায় সম্পর্কহীন proxy (R² = 0.083); আনুমানিক হিসাব বড় ভুল করায়; grid region বদলালে কার্বন 30× পর্যন্ত বদলায়।
- Carbon Impact Statement চালু করে: পেপারের নিজের সব এক্সপেরিমেন্টের খরচ ঘোষণা (তাদের নিজের: 24.344 kWh, 8.021 kg CO2eq)।

**আমাদের প্রজেক্টে প্রাসঙ্গিকতা:**
- আমাদের মাপার টুল-স্ট্যাক আর measurement boundary এখান থেকে: আমরা CPU/GPU/DRAM দেখি, তাই রিডিংকে "পুরো মেশিনের বিদ্যুৎ" বলা যাবে না।
- প্রতি-প্রসেস attribution এক মেশিনে PINN আর classical-এর খরচ আলাদা করে দেখাবে।
- R² = 0.083 আমাদের "FLOPs গুনে না, সরাসরি মিটার দিয়ে মাপব" সিদ্ধান্তের সাইটেশন।
- আমাদের study-electricity লগ (তালিম, tuning, ব্যর্থ চালসহ পুরো স্টাডির বিদ্যুৎ) এদের Carbon Impact Statement-এর অনুবাদ।
- বোনাস সতর্কতা: GPU-র power reading ±5 W ভুল করতে পারে, তাই বহু চাল + standard error; এক মেশিনে সব চালানো তাদের footnote 19-এর সমর্থন।

## রিভিশনের শেষ মনে-রাখা তিন জিনিস

1. আমাদের সূত্র: `E_P(N) = S_P + N·e_P`, `E_C(N) = S_C + N·e_C`, `N* = (S_P − S_C)/(e_C − e_P)`; energy আর runtime আলাদা মাপা হবে।
2. কোনো পেপারই আমাদের প্রশ্নের সরাসরি উত্তর দেয় না (কেউ energy মাপে না parametric PDE-তে); তাই ফলাফল কী হবে আগে থেকে বলা যায় না, crossover না থাকাও বৈধ।
3. তিনটা identity নোট: Raissi-র PDF = preprint (cite JCP 2019); de Hoop-এ Darcy নেই; Huang = unrefereed preprint।
