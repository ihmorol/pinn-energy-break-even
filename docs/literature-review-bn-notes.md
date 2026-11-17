# সামারি নোট (বাংলা): আমার ভাগের পাঁচটা পেপার

**প্রজেক্ট:** Reaching the energy and computational break-even point between PINNs, and classical solvers.
**তৈরির তারিখ:** 2026-11-14
**নোট:** রিভিশনের জন্য ছোট সারাংশ। বিস্তারিত ভার্সন: [docs/literature-review-bn.md](literature-review-bn.md)। টিম নোট (`references/`) আর পুরো PDF পড়ার তথ্য মিলিয়ে তৈরি, AI-assisted। সংখ্যাগুলো preprint-এর; উপমাগুলো শুধু বোঝার জন্য।

---

## ১. Raissi, Perdikaris, Karniadakis — PINN-এর ভিত্তি পেপার (2017 preprint / 2019 JCP)

**পেপারে কাজ কী:**
- পদ্ধতিটার জন্মদান: নিউরাল নেটওয়ার্ককে PDE-র সমাধান শেখানো, যেখানে physics ট্রেনিং loss-এর ভেতরে ঢোকানো।
- Loss দুই অংশে: জানা পয়েন্টে (শুরু + ধার) উত্তরের ভুল `MSE_u`, আর অনেক collocation point-এ সূত্র ভাঙার ভুল `MSE_f`। Derivative আসে autodiff দিয়ে।
- Burgers, Schrödinger, Allen-Cahn-এ সামান্য data দিয়ে relative L2 ভুল 10⁻³ থেকে 10⁻⁴ মাপে নেমে আসে।
- মনে রাখো: আমাদের `raissi-2019-pinn.pdf` ফাইলটা আসলে 2017-এর Part I preprint, published পেপার না; method cite হবে JCP 2019 থেকে।

**আমাদের জন্য প্রাসঙ্গিকতা:**
- আমাদের PINN-এর residual loss `L_PDE = mean(r²)` সরাসরি এর `MSE_f`-এর অনুবাদ; autodiff আর relative L2 মূল্যায়নের রীতিও এখান থেকে।
- লেখকেরা নিজেরাই বলেন পদ্ধতিটা classical-এর বিকল্প না; এই স্বীকারোক্তিই আমাদের তুলনার প্রশ্নের ভিত্তি।
- এই পেপারে খরচ, সময় তুলনা বা energy কিছুই মাপা নেই, আর (μ₁, μ₂) মতো parameter ইনপুটও নেই; সেটা আমাদের এক্সটেনশন।

---

## ২. Grossmann et al. 2024 — PINN বনাম FEM সরাসরি তুলনা

**পেপারে কাজ কী:**
- ৬টা সমস্যায় (Poisson 1D/2D/3D, Allen-Cahn, Schrödinger 1D/2D) একই accuracy-তে head-to-head রেস: একই mesh-এ relative L2, 10 চালের গড় সময়।
- ফল: প্রায় সব জায়গায় FEM জেতে, solution time-এ 1 থেকে 6 orders (দশগুণ থেকে লাখ গুণ) আগে।
- একমাত্র ব্যতিক্রম: 3D Poisson-এর evaluation, সেখানে ট্রেন হওয়া PINN 2-3 orders দ্রুত।
- এরা শুধু wall-clock time মেপেছে; energy না, parametric PDE না, offline training খরচের হিসাবও না।

**আমাদের জন্য প্রাসঙ্গিকতা:**
- এটাই আমাদের সরাসরি পূর্বসূরি; ওই তিনটা ফাঁক (energy, parametric, training খরচ) পূরণ করাই আমাদের অবদান।
- এদের ফলটা আমাদের সৎ পূর্বানুমান: single-solve-এ classical সম্ভাব্য এগিয়ে; তবে প্রতি-কোয়েরি সাশ্রয় থাকলে training খরচ কত কোয়েরিতে উসুল হয়, সেটাই আমাদের N* মাপবে।
- শিক্ষা: এদের FEM CPU-তে, PINN GPU-তে চলেছে; আমরা device placement ঘোষণা করব যাতে তুলনা অসম না হয়।

---

## ৩. de Hoop, Huang, Qian, Stuart 2022 — cost-accuracy কাঠামো

**পেপারে কাজ কী:**
- Operator learning (একটা ফাংশন দিলে আরেকটা ফাংশন বলা শেখা) বিচারের কাঠামো: আসল প্রশ্ন "কত খরচে কত accuracy"।
- চার architecture (PCA-Net, DeepONet, PARA-Net, FNO), চার সমস্যায় মাপা; training cost = data volume, evaluation cost = FLOPs।
- ফল: বিজয়ী সমস্যা-ভেদে বদলায়; লেখকেরা নিজেরাই বলেন কোনো নিশ্চিত সিদ্ধান্ত নেই, ফল সমস্যার ওপর নির্ভরশীল।
- মূল বাক্য: শেখার খরচ উসুল হবে কি না নির্ভর করছে নতুন প্রশ্নেও ভালো উত্তর দিতে পারে কি নার ওপর।

**আমাদের জন্য প্রাসঙ্গিকতা:**
- কেন আমরা fixed accuracy-তে (1%, 0.1%) খরচ তুলনা করি, শুধু "কে ভালো" না: এই পেপারই সেই মাপদণ্ডের ভিত্তি।
- এদের training বনাম evaluation ভাগ আমাদের S (শুরুর খরচ) বনাম e (প্রতি-কোয়েরি) ভাগের পূর্বসূরি।
- সতর্কতা: এরা FLOPs মাপে, বিদ্যুৎ বা wall-clock না; এই পেপারে Darcy example নেই, আর surrogate গুলো PINN না (সব data-driven supervised)।

---

## ৪. Huang et al. 2026 — decision framework ও amortization সূত্র

**পেপারে কাজ কী:**
- বড় review: কখন classical, কখন learned, কখন hybrid solver ন্যায্য; query volume, data, certification দেখে সিদ্ধান্ত ছক।
- Amortization সূত্র: `N* = (γ·N_tr + τ)/(1 − 1/S)`, শর্ত S > 1; S ≤ 1 হলে surrogate কখনো break-even করে না।
- প্রমাণের সিঁড়ি P0-P4 (training loss থেকে বাস্তব deployment প্রমাণ); নিচু ধাপের প্রমাণ উঁচু ধাপের দাবি করে না।
- নিজেদের মাপা Darcy পরীক্ষায়: 1% এর নিচে accuracy-তে কোনো FNO 3.1×10⁴ কোয়েরির আগে break-even করে না; 512² resolution-এ সংখ্যাটা 9.2×10⁵। আরেকটা প্রমাণ: 76টা ML পেপারের 79% দুর্বল baseline হারিয়ে জয় দাবি করেছে; FNO-র 440× speedup end-to-end মাত্র ~1.5×।

**আমাদের জন্য প্রাসঙ্গিকতা:**
- এদের সূত্র আর আমাদের `N* = (S_P − S_C)/(e_C − e_P)` একই কঙ্কাল: শুরুর বাড়তি খরচ ÷ প্রতি-কোয়েরি সাশ্রয়।
- পার্থক্য: আমরা energy মাপি, এরা শুধু compute time; আমাদের PINN solver-generated data খায় না, তাই data-জেনারেশন অংশ আমাদের ক্ষেত্রে নেই, break-even মূলত training খরচের হাতে।
- আমাদের তুলনা তাদের সিঁড়ির P3 ধাপে: একই accuracy, মাপা খরচ, ধারালো classical প্রতিপক্ষ। এদের 3-seed নিয়মও আমাদের নিয়মের সমর্থন।
- সতর্কতা: unrefereed preprint; মাপা মান শুধু সময়, energy না; surrogate হলো FNO, PINN না (তারা নিজেরাই PINN-এর efficiency প্রমাণকে Weak বলেছে; আমাদের মাপা সেই ফাঁক ভরাট করে)।

---

## ৫. Henderson et al. 2020 — বিদ্যুৎ মাপার প্রোটোকল

**পেপারে কাজ কী:**
- ML-এর বিদ্যুৎ ও কার্বন মাপা ও রিপোর্ট করার পদ্ধতি: RAPL/powercap (CPU+DRAM), nvidia-smi (GPU), psutil (প্রতি-প্রসেস ভাগ)।
- Attribution সূত্র: `e_total = PUE × Σ(p_dram·e_dram + p_cpu·e_cpu + p_gpu·e_gpu)`; প্রসেস যত ভাগ সম্পদ খায়, তত ভাগ খরচ তার খাতায়।
- দেখায়: FLOPs বিদ্যুতের প্রায় সম্পর্কহীন proxy (R² = 0.083); আনুমানিক হিসাব বড় ভুল করায়; grid region কার্বন 30 গুণ পর্যন্ত বদলায় (Quebec বনাম Estonia)।
- Carbon Impact Statement দেয়: নিজের পেপারের মোট kWh, kg CO2eq ঘোষণা করা; এটা সচেতনতার জন্য, শাস্তির জন্য না।

**আমাদের জন্য প্রাসঙ্গিকতা:**
- আমাদের মাপার নকশা এখান থেকে: টুল-স্ট্যাক, measurement boundary ঘোষণা (আমরা শুধু CPU/GPU/DRAM দেখি, তাই রিডিংকে "পুরো মেশিনের বিদ্যুৎ" বলা যাবে না)।
- Unit রীতি: energy kWh/J, power W; মাপা মান আর অনুমিত মান আলাদা লেবেলে; FLOPs-ভিত্তিক দাবি না।
- আমাদের "study electricity" আলাদা লগ = এদের Carbon Impact Statement-এর অনুবাদ।
- সতর্কতা: GPU power reading ±5 W ভুল করতে পারে, ছোট কাজে outlier ঝুঁকি; তাই বহু চাল, warm-up, আর গড়ের ভুল রিপোর্ট করা হবে।

---

## সব মিলিয়ে (২-৩ লাইনে)

কোনো পেপারই আমাদের প্রশ্নের সরাসরি উত্তর দেয় না: Raissi খরচ মাপে না, Grossmann শুধু সময় মাপে, de Hoop FLOPs মাপে, Huang শুধু সময় ও FNO-র জন্য মাপে, Henderson বিদ্যুৎ মাপে কিন্তু PDE-র জন্য না। আমাদের জায়গা: parametric PDE-তে, একই accuracy-তে, একই মেশিনে, মাপা energy ও runtime দিয়ে break-even কোয়েরি সংখ্যা বের করা। Crossover না থাকাও বৈধ ফলাফল; কাউকে আগে থেকে জেতার দরকার নেই।
