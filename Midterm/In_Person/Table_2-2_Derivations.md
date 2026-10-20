# Table 2-2 Derivations: All Nine Slab Cases

Oct 19, 2026 · @CD

On Wednesday you get one problem and six graded parts in 75 minutes, with no notes or calculator: a 1D transient slab or, possibly, a 2D steady-state plate. Each problem type has its own shared method, and both use the same nine Table 2-2 case solves for the eigenfunction and the normalization factor. Every answer must match Table 2-2, and the normalization factor comes in just three patterns.

## Study plan: Monday 10/19 to Wednesday 10/21

Learn the two methods, drill the cases by pattern, then practice under exam conditions: blank paper, no notes, no calculator, 50 minutes per case. Three timed mock exams and a full night of sleep will do more than rereading.

Your whole memorization list: Steps 1, 2, 3 and 5 of both methods, Table 2-2 through the four rebuild rules (rule 4 gives the six Y functions), the four trig identities (1, 2, 4 and 7) and the hyperbolic derivatives. Everything else you work out on the page.

The drill for every block: read the section once, close the doc, write it on blank paper, then check it against the doc and log each mistake in the error log below. The patterns are: Pattern A = no convective face (Cases 5, 6, 8, 9), Pattern B = one convective face (Cases 2, 3, 4, 7), Pattern C = two convective faces (Case 1).

Short on time? Keep the order and cut the reading, not the blank-paper practice.

### Monday evening (about 3 hours, from 7:30 PM)

- [ ] 7:30–8:30 PM · Read this guide front to back once, starting with the exam flow. Don't try to memorize yet.
- [ ] 8:30–9:00 PM · Method 1 (1D transient): write Steps 1, 2, 3 and 5 from memory, check, and repeat once. Target: 12 minutes with no errors.
- [ ] 9:00–9:20 PM · Memorize the four identities (1, 2, 4 and 7) and the hyperbolic derivatives. Then derive the cos² and sin² integrals and rebuild identity 4 once.
- [ ] 9:20–9:30 PM · Break.
- [ ] 9:30–10:15 PM · Pattern A: Cases 9, 8, 6, 5. Read each once, then write Steps 4 to 6 from memory and check them against Table 2-2. Do not skip the β = 0 check in Case 5.
- [ ] 10:15–10:30 PM · Write Table 2-2 from memory using rules 1 to 3. Log every mistake.

### Tuesday evening (about 4 hours)

- [ ] 6:00–6:20 PM · Warm-up from memory: Method 1 Steps 1, 2, 3 and 5, the four identities, Table 2-2.
- [ ] 6:20–7:20 PM · Pattern B: Cases 4, 7, 2, 3 (Case 4 is your class-notes example). Read each once, then write Steps 4 to 6 from memory. Focus on the sin 2u step and the common-denominator flip to 1/N.
- [ ] 7:20–7:30 PM · Break.
- [ ] 7:30–8:10 PM · Case 1 (Pattern C): write the eigenvalue equation twice, then the phase-trick normalization twice, from memory.
- [ ] 8:10–8:55 PM · Method 2 (2D steady state): read it once. Then write Steps 1, 2, 3 and 5 from memory, derive all six Y functions, and do the flip once on paper.
- [ ] 8:55–9:50 PM · Mock exam 1 (1D transient): draw a case at random (write 1 to 9 on scraps). Closed book, 50 minutes, all six steps, then grade it against this guide.
- [ ] 9:50–10:00 PM · Update the error log and reread only the steps you missed.
- [ ] Sleep 7 to 8 hours. Sleep is when the day's memorizing sets; skip the all-nighter.

### Wednesday, exam day (study until 2:15 PM)

- [ ] 8:30–9:00 AM · Warm-up from memory: Steps 1, 2, 3 and 5 of both methods, the four identities, the six Y functions, Table 2-2.
- [ ] 9:00–10:00 AM · Mock exam 2 (2D steady state): draw the x-faces as a random case (1 to 9), then draw the homogeneous y-face (zero temperature, insulated or convection, at y = 0 or y = b). 50 minutes, then grade.
- [ ] 10:00–10:15 AM · Break away from the desk.
- [ ] 10:15–11:00 AM · Fix: redo every step in the error log, then redo the Case 1 normalization once.
- [ ] 11:00 AM–12:00 PM · Mock exam 3 (1D transient): a convective case you have not mocked yet (1, 2, 3, 4 or 7), then grade.
- [ ] 12:00–12:45 PM · Lunch, away from the material.
- [ ] 12:45–1:45 PM · Speed drill: all nine cases, Steps 4 and 6 only, about 5 minutes each. Then the six Y functions and the Cₘ rule once.
- [ ] 1:45–2:15 PM · Last pass: Table 2-2 from memory twice, the exam flow once, then read the error log.
- [ ] 2:15–3:30 PM · Stop studying. Eat a real meal, since the exam runs through dinner (5:00–6:15 PM). Pack two pens or pencils, an eraser and water.
- [ ] 3:45 PM · Leave.

### Error log

| Case | Step | What went wrong | Fix |
| --- | --- | --- | --- |
| Example: 3 | 6 | Used the cos² integral for a sine eigenfunction | Sine X takes the sin² integral, with a minus sign before sin 2βL/(4β) |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Exam flow: from problem statement to boxed answers

Do these steps in order. Steps 1 to 5 take about 3 minutes and tell you which method, which case and which Y to use. Step 6 is the six graded parts.

1. **Sketch and label.** Draw the slab or plate and write each face's condition on the sketch.
2. **Pick the method.**
   - T depends on x and t: 1D transient, so use Method 1.
   - T depends on x and y, with no t: 2D steady state, so use Method 2.
3. **Classify every face.** Each face is zero temperature, insulated, convection (note its H), or nonhomogeneous (a given f, or a fluid or wall temperature that is not zero).
   - A nonzero fluid temperature: shift θ = T − T∞ when that leaves only one nonhomogeneous condition (Method 1, Step 2).
   - Method 2 with more than one nonhomogeneous face: split the problem by superposition (Notes p. 59).
4. **Find the eigenfunction direction.**
   - Method 1: always x.
   - Method 2: the direction whose two faces are both homogeneous. If that is y, use the flip at the end of Method 2.
5. **Name the case and write your targets in a corner.**
   - The two faces of the eigenfunction direction give the case (Table 2-2 targets). Copy its row: X, eigenvalue equation, 1/N. In Method 2, write a in place of L.
   - Method 2 only: also write the Y function for the remaining homogeneous face (rule 4) and its value at the f(x) face.
6. **Work the six graded parts in order**, labeling each with your professor's wording:
   - Step 1 · Governing equation: from your method section.
   - Step 2 · Boundary conditions: the case's Step 2 for the eigenfunction faces, plus the initial condition (Method 1) or the two y-faces (Method 2).
   - Step 3 · Separation: your method's Step 3, then move each homogeneous condition onto X (and Y).
   - Step 4 · Eigenfunction: the case's Step 4, with L → a in Method 2. Method 2 adds the Y derivation.
   - Step 5 · Cₘ: your method's Step 5. Keep 1/N(βₘ) as a symbol until Step 6 (trick 12).
   - Step 6 · Normalization factor: the case's Step 6.
7. **Assemble the final answer.** Put 1/N into Cₘ and box T in the table's form.
8. **Check.** Plug X (and Y) into each homogeneous condition, run the H → 0 and H → ∞ limits, and compare with your corner targets.

### In the exam room (75 minutes)

| Minutes | Do this |
| --- | --- |
| 0–3 | Exam flow steps 1 to 5: sketch, pick the method, classify the faces, find the case, and write its Table 2-2 row in a corner (plus Y in Method 2). |
| 3–15 | Step 1 (formulate) and Step 2 (boundary conditions, plus the initial condition or the f(x) face). |
| 15–23 | Step 3 (separation down to the Table 2-2 ODE, plus Γ or Y). |
| 23–36 | Step 4 (eigenfunction, eigenvalue equation, β = 0 check, and Y in Method 2). |
| 36–46 | Step 5 (Cₘ). |
| 46–62 | Step 6 (normalization factor). |
| 62–75 | Check: plug X (and Y) into each boundary condition, run the H → 0 or H → ∞ limit, and box each answer in table form. |

Label each part with your professor's wording and box every final answer in the table's form. If you get stuck, write the definition (for example N = ∫X²dx) and the target, then show every step you can: each part is graded on its own.

## The exam at a glance

The exam is one problem and six graded parts, and this guide numbers them Step 1 to Step 6 in your professor's order. Your method fixes Steps 1, 3 and 5. The case fixes Steps 2, 4 and 6, and the case solves are the same for both methods.

| Step (exam part) | Method 1: 1D transient | Method 2: 2D steady state |
| --- | --- | --- |
| 1 · Formulate the governing equation | ∂²T/∂x² = (1/α) ∂T/∂t | ∂²T/∂x² + ∂²T/∂y² = 0 |
| 2 · Apply the boundary conditions | The two x-faces, plus T = F(x) at t = 0 | The two x-faces, one homogeneous y-face, plus T = f(x) on the other y-face |
| 3 · Solve by separation of variables | T = X(x)Γ(t): d²X/dx² + β²X = 0 and Γ(t) = e^(−αβ²t) | T = X(x)Y(y): d²X/dx² + β²X = 0 and d²Y/dy² − β²Y = 0 |
| 4 · Find the eigenfunction | X(βₘ, x) and the eigenvalue equation, from the case | The same with L → a, plus one of the six Y functions |
| 5 · Find Cₘ | Cₘ = (1/N(βₘ)) ∫₀ᴸ X F dx | Cₘ = (1/(N(βₘ) Y(βₘ, y\_f))) ∫₀ᵃ X f dx |
| 6 · Find the normalization factor | 1/N(βₘ) from the case | The same, with L → a |

Cₘ contains N(βₘ). On the exam, either do Step 6 before Step 5, or write Cₘ in terms of N(βₘ) first and fill it in after Step 6.

Table 2-2 was built for the 1D transient slab, but each row is just the X eigenvalue problem: d²X/dx² + β²X = 0 with two homogeneous faces. That is why the same rows serve 2D steady state, with L replaced by the plate width a. In Method 2, y\_f is the y-face that carries T = f(x).

**Solution map (Method 1).** Every case follows this path; only Steps 2, 4 and 6 change with the boundary conditions.

1. **Step 1 · Formulate the governing equation.** Heat equation, three assumptions, then ∂²T/∂x² = (1/α) ∂T/∂t. Same in every case.
2. **Step 2 · Apply the boundary conditions.** The math form of each face, plus T = F(x) at t = 0. Changes with the case.
3. **Step 3 · Separate variables, T(x,t) = X(x)Γ(t).** The PDE splits into two parts:
    - Time part: dΓ/dt + αβ²Γ = 0, so Γ(t) = e^(−αβ²t). Same in every case.
    - Space part: the Table 2-2 ODE, d²X/dx² + β²X = 0, plus the boundary conditions on X.
4. **Step 4 · Find the eigenfunction.** X(βₘ, x) and the eigenvalue equation for βₘ. Changes with the case.
5. **Step 5 · Find Cₘ.** Superpose, set t = 0, use orthogonality. Same formula in every case.
6. **Step 6 · Find the normalization factor.** N(βₘ) = ∫₀ᴸ X² dx, then flip to 1/N(βₘ). Changes with the case.
7. **Final answer.** T(x,t) = Σ Cₘ X(βₘ, x) e^(−αβₘ²t), with an extra m = 0 term in Case 5.

The map shows Method 1. Method 2 follows the same path with Y(y) in place of Γ(t) and one extra factor in Cₘ. For each method, memorize Steps 1, 3 and 5 once; for each case, only Steps 2, 4 and 6 change.

### Table 2-2 targets

These nine rows are what every answer must match exactly. In Method 2 they are the X rows, with L replaced by the plate width a. H₁ = h₁/k and H₂ = h₂/k.

| Case | BC at x = 0 | BC at x = L | X(βₘ, x) | 1/N(βₘ) | βₘ are the positive roots of |
| --- | --- | --- | --- | --- | --- |
| 1 | −dX/dx + H₁X = 0 | dX/dx + H₂X = 0 | βₘ cos βₘx + H₁ sin βₘx | 2[(βₘ² + H₁²)(L + H₂/(βₘ² + H₂²)) + H₁]⁻¹ | tan βₘL = βₘ(H₁ + H₂)/(βₘ² − H₁H₂) |
| 2 | −dX/dx + H₁X = 0 | dX/dx = 0 | cos βₘ(L − x) | 2(βₘ² + H₁²)/[L(βₘ² + H₁²) + H₁] | βₘ tan βₘL = H₁ |
| 3 | −dX/dx + H₁X = 0 | X = 0 | sin βₘ(L − x) | 2(βₘ² + H₁²)/[L(βₘ² + H₁²) + H₁] | βₘ cot βₘL = −H₁ |
| 4 | dX/dx = 0 | dX/dx + H₂X = 0 | cos βₘx | 2(βₘ² + H₂²)/[L(βₘ² + H₂²) + H₂] | βₘ tan βₘL = H₂ |
| 5 | dX/dx = 0 | dX/dx = 0 | cos βₘx, plus X₀ = 1 for β₀ = 0 | 2/L for βₘ ≠ 0; 1/L for β₀ = 0 | sin βₘL = 0, so βₘ = mπ/L, m = 0, 1, 2, … |
| 6 | dX/dx = 0 | X = 0 | cos βₘx | 2/L | cos βₘL = 0, so βₘ = (2m − 1)π/(2L) |
| 7 | X = 0 | dX/dx + H₂X = 0 | sin βₘx | 2(βₘ² + H₂²)/[L(βₘ² + H₂²) + H₂] | βₘ cot βₘL = −H₂ |
| 8 | X = 0 | dX/dx = 0 | sin βₘx | 2/L | cos βₘL = 0, so βₘ = (2m − 1)π/(2L) |
| 9 | X = 0 | X = 0 | sin βₘx | 2/L | sin βₘL = 0, so βₘ = mπ/L, m = 1, 2, … |

### Rebuild the table and Y from four rules

1. Eigenfunction rule. Anchor X on a face that is not convective: an insulated face gets a cosine (zero slope there), and a zero-temperature face gets a sine (zero value there). Use x = 0 when it is not convective: Cases 4 to 9 give cos βₘx (insulated) or sin βₘx (zero temperature). When x = 0 is convective, anchor at x = L with (L − x): Case 2 gives cos βₘ(L − x) and Case 3 gives sin βₘ(L − x). Both faces convective (Case 1): βₘ cos βₘx + H₁ sin βₘx.
2. Eigenvalue rule. No convective face: sin βₘL = 0 when both faces are the same kind (Cases 5, 9), and cos βₘL = 0 when they differ (Cases 6, 8). One convective face with coefficient H: βₘ tan βₘL = H when the other face is insulated (Cases 2, 4), and βₘ cot βₘL = −H when the other face is at zero temperature (Cases 3, 7). Both convective: Case 1's row.
3. Normalization rule. No convective face: 1/N = 2/L, and Case 5 adds 1/L for β₀ = 0. One convective face: 1/N = 2(βₘ² + H²)/[L(βₘ² + H²) + H], using that face's H. Both convective: Case 1's row.
4. Y rule (Method 2 only). Anchor Y on its homogeneous y-face the way rule 1 anchors X, but with hyperbolic functions: a zero-temperature face gets sinh, an insulated face gets cosh, and a convective face gets βₘ cosh + H₃ sinh. Measure from that face: use y when it is y = 0 and (b − y) when it is y = b. The six results are in Method 2, Step 4.

### Names and notation

- Cₘ is the Fourier coefficient (also called the expansion coefficient): the weight of the m-th eigenfunction in the series that rebuilds the initial temperature F(x).
- N(βₘ) is the norm, or normalization integral, ∫₀ᴸ X² dx. The table lists 1/N(βₘ), the normalization factor.
- X(βₘ, x) is the eigenfunction and βₘ are the eigenvalues. The equation that fixes βₘ is the eigenvalue (characteristic) equation. Γ(t) is the time function.
- Y(βₘ, y) is the y-function in Method 2. It is not an eigenfunction: it plays the role Γ(t) plays in Method 1, and it uses the eigenvalues βₘ that X sets.
- a is the plate width in the eigenfunction direction (it replaces L), b is the plate height, and y\_f is the y-face that carries T = f(x). H₃ = h₃/k belongs to a convective y-face.
- β or λ: your professor's Table 2-2 and notes write βₘ and Cₘ, while the 3rd-edition PDF writes λₙ and Cₙ (its header reads d²X/dx² + λ²X = 0). It is the same table. Use your professor's symbols and never mix the two.
- H₁ = h₁/k and H₂ = h₂/k, in 1/length. Your notes write k₁ and k₂; for one slab, k₁ = k₂ = k.
- Derivatives: d/dx and d/dt for X(x) and Γ(t), which are ordinary; ∂/∂x and ∂/∂t for T(x,t), which is partial.

### Sources cited in this guide

- "Notes p. N" = ME5130 Lecture Notes Set 1 Heat Conduction, PDF page N.
- "Özişik p. N, eq. (…)" = the Heat Conduction 3rd edition PDF in the project, printed page number.
- Your professor's Table 2-2 = Özişik 2nd edition, pp. 48–49 (his page numbers). It has the same nine rows as Table 2-1 on Özişik p. 46. The 2nd-edition excerpt in the project cites it as "Table 2-2, case 9" on p. 87 and uses its general solution, eq. (2-36a), on p. 86.

## Method 1 · 1D transient: shared Steps 1 to 6

Use this method when T depends on x and t. Every case repeats it with its own two boundary conditions, so each case section below shows all six steps but explains only what is new.

### Step 1 · Formulate the governing equation

Start from the general heat conduction equation (Notes p. 5; Özişik p. 10, eq. 1-24):

$$
\rho c_p\frac{\partial T}{\partial t}=\nabla\cdot(k\nabla T)+g
$$

State three assumptions, then apply them one at a time.

Assumption 1, constant k (homogeneous, isotropic slab). k comes out of the divergence:

$$
\nabla\cdot(k\nabla T)=k\,\nabla^2T
$$

Assumption 2, no heat generation:

$$
g=0
$$

Assumption 3, one-dimensional: T changes only with x and t, so the y and z terms of the Cartesian Laplacian are zero (Notes p. 6; Özişik p. 10, eq. 1-25):

$$
\nabla^2T=\frac{\partial^2T}{\partial x^2}+\frac{\partial^2T}{\partial y^2}+\frac{\partial^2T}{\partial z^2}=\frac{\partial^2T}{\partial x^2}
$$

Substitute all three into the heat equation:

$$
\rho c_p\frac{\partial T}{\partial t}=k\,\frac{\partial^2T}{\partial x^2}
$$

Divide both sides by k and use the thermal diffusivity α = k/(ρcₚ) (Notes p. 6; Özişik p. 10, eq. 1-26):

$$
\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t}\qquad 0<x<L,\;\;t>0
$$

This governing equation is the same for all nine cases.

### Step 2 · Apply the boundary conditions

One rule produces every convection condition, with no sign guessing (Notes pp. 8–9; Özişik pp. 19–20, eqs. 1-52 and 1-57a):

$$
-k\,\frac{\partial T}{\partial n}=h\,(T-T_\infty)\qquad\text{at the surface}
$$

Here n is the outward normal: the direction pointing out of the solid (Özişik p. 20). The only thing to decide at each face is which way is out, and that is fixed by the geometry, since the slab fills 0 < x < L:

| Face | Outward normal | ∂T/∂n becomes |
| --- | --- | --- |
| x = 0 | points toward −x | −∂T/∂x |
| x = L | points toward +x | +∂T/∂x |

Convection at x = 0 (substitute ∂T/∂n = −∂T/∂x into the rule):

$$
\begin{aligned}
-k\left(-\frac{\partial T}{\partial x}\right)&=h_1\,(T-T_\infty) &&\text{substitute}\\
k\,\frac{\partial T}{\partial x}&=h_1\,(T-T_\infty) &&\text{the two minus signs cancel}\\
-k\,\frac{\partial T}{\partial x}+h_1\,(T-T_\infty)&=0 &&\text{move everything to one side}
\end{aligned}
$$

Convection at x = L (substitute ∂T/∂n = +∂T/∂x into the rule):

$$
\begin{aligned}
-k\,\frac{\partial T}{\partial x}&=h_2\,(T-T_\infty) &&\text{substitute}\\
k\,\frac{\partial T}{\partial x}+h_2\,(T-T_\infty)&=0 &&\text{move everything to one side}
\end{aligned}
$$

The other two kinds need no sign: an insulated face has ∂T/∂n = 0, which is ∂T/∂x = 0 (Özişik p. 20, eq. 1-56). A face held at temperature Tₛ has T = Tₛ (Özişik p. 19, eq. 1-53a).

Make the conditions homogeneous. Separation of variables needs every boundary condition to equal zero (Notes p. 17; Özişik p. 81, eq. 3-30). Shift the temperature by the fluid (or wall) temperature:

$$
\theta(x,t)=T(x,t)-T_\infty
$$

θ obeys the same PDE, because T∞ is a constant and its derivatives are zero. Divide each convection condition by k and write H = h/k. The result, for every kind of face:

| Physical statement | At x = 0 | At x = L |
| --- | --- | --- |
| Held at zero temperature (or at Tₛ, with θ = T − Tₛ) | θ = 0 | θ = 0 |
| Insulated, adiabatic, or a symmetry plane | ∂θ/∂x = 0 | ∂θ/∂x = 0 |
| Convection to fluid at T∞ (θ = T − T∞) | −∂θ/∂x + H₁θ = 0 | ∂θ/∂x + H₂θ = 0 |

The initial condition is the starting temperature, shifted the same way:

$$
\theta(x,0)=F(x)=T_i(x)-T_\infty
$$

The table's cases assume this shift is already done, so the rest of this guide writes T for θ. One shift only works when every non-insulated face sees the same temperature. If two faces see different temperatures, split into a steady part plus a transient part first (Özişik 2nd ed. Example 2-15, p. 86).

The three kinds are linked by limits (Notes p. 39). As H → 0 the Hθ term vanishes, leaving the insulated condition. As H → ∞, divide by H first: (1/H)∂θ/∂x + θ = 0 becomes θ = 0. So every case is the convection problem with each H set to 0 or ∞, which gives you a built-in check.

### Step 3 · Solve by separation of variables (down to the Table 2-2 ODE)

This step turns the PDE into the ODE at the top of Table 2-2 (Notes pp. 31 and 36; Özişik pp. 81–82, eqs. 3-33 to 3-36).

3a. Assume T is a function of x alone times a function of t alone:

$$
T(x,t)=X(x)\,\Gamma(t)
$$

3b. Differentiate. X does not depend on t, and Γ does not depend on x:

$$
\begin{aligned}
\frac{\partial T}{\partial t}&=X\,\frac{d\Gamma}{dt}\\
\frac{\partial^2T}{\partial x^2}&=\Gamma\,\frac{d^2X}{dx^2}
\end{aligned}
$$

3c. Substitute both into the governing equation from Step 1:

$$
\Gamma\,\frac{d^2X}{dx^2}=\frac{1}{\alpha}\,X\,\frac{d\Gamma}{dt}
$$

3d. Divide both sides by XΓ:

$$
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\,\Gamma}\frac{d\Gamma}{dt}
$$

3e. The left side depends only on x, and the right side only on t. Hold x fixed and let t change: the left side cannot change, so the right side cannot either. Both sides therefore equal one constant, named −β²:

$$
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\,\Gamma}\frac{d\Gamma}{dt}=-\beta^2
$$

3f. The space equation. Take the left equality, multiply by X, and move the term to the left side:

$$
\begin{aligned}
\frac{d^2X}{dx^2}&=-\beta^2X &&\text{multiply by }X\\
\frac{d^2X}{dx^2}+\beta^2X&=0\qquad 0<x<L &&\text{move to the left side}
\end{aligned}
$$

This is the ODE at the top of Table 2-2. The 3rd-edition table writes λ in place of β (Özişik p. 46).

3g. The time equation. Take the right equality and solve it (Notes p. 31; Özişik p. 83, eq. 3-42):

$$
\begin{aligned}
\frac{d\Gamma}{dt}&=-\alpha\beta^2\,\Gamma &&\text{multiply by }\alpha\Gamma\\
\frac{d\Gamma}{\Gamma}&=-\alpha\beta^2\,dt &&\text{separate }\Gamma\text{ and }t\\
\ln\Gamma&=-\alpha\beta^2t+c &&\text{integrate both sides}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{exponentiate; }e^{c}\text{ joins }C_m\text{ later}
\end{aligned}
$$

3h. Why the constant is −β². Check all three possibilities instead of relying on intuition:

| Separation constant | Time solution | Space solution | Result |
| --- | --- | --- | --- |
| −β² (negative) | Γ = e^(−αβ²t), decays | X = A₁cos βx + A₂sin βx | Meets both BCs at discrete βₘ: this is Table 2-2 |
| +μ² (positive) | Γ = e^(+αμ²t), grows forever | X = A cosh μx + B sinh μx | Only X = 0 meets the BCs, so no solution |
| 0 | Γ = constant | X = a + bx | Nonzero only when both faces are insulated (Case 5) |

3i. Move the boundary conditions onto X. Substitute T = XΓ into each condition and divide by Γ(t), which is never zero:

$$
\begin{aligned}
-\frac{\partial T}{\partial x}+H_1T=0\;&\Rightarrow\;-\frac{dX}{dx}+H_1X=0 &&\text{at }x=0\\
\frac{\partial T}{\partial x}+H_2T=0\;&\Rightarrow\;\frac{dX}{dx}+H_2X=0 &&\text{at }x=L\\
T=0\;&\Rightarrow\;X=0 &&\text{at that face}\\
\frac{\partial T}{\partial x}=0\;&\Rightarrow\;\frac{dX}{dx}=0 &&\text{at that face}
\end{aligned}
$$

The initial condition does not move onto X, because F(x) is not zero; it is used in Step 5. The result of Step 3 is the eigenvalue problem that Table 2-2 solves: d²X/dx² + β²X = 0 on 0 < x < L, with one homogeneous condition at each face.

### Step 4 · Find the eigenfunction

4a. General solution of d²X/dx² + β²X = 0 (Notes p. 38; Özişik p. 43, eq. 2-12). Try X = e^(Dx):

$$
\begin{aligned}
D^2+\beta^2&=0 &&\text{characteristic equation}\\
D&=\pm i\beta &&\text{two imaginary roots}\\
X(x)&=A_1\cos\beta x+A_2\sin\beta x &&\text{real form of }e^{\pm i\beta x}\\
\frac{dX}{dx}&=-A_1\beta\sin\beta x+A_2\beta\cos\beta x &&\text{differentiate}
\end{aligned}
$$

At x = 0, cos 0 = 1 and sin 0 = 0, so:

$$
X(0)=A_1\qquad\qquad\left.\frac{dX}{dx}\right|_{x=0}=A_2\beta
$$

4b. Apply the condition at x = 0. It fixes one constant:

| Face at x = 0 | Condition | Result |
| --- | --- | --- |
| Zero temperature | X(0) = A₁ = 0 | X = A₂ sin βx |
| Insulated | dX/dx at x = 0 equals A₂β = 0, so A₂ = 0 | X = A₁ cos βx |
| Convection | −A₂β + H₁A₁ = 0, so A₂ = (H₁/β)A₁ | X = A₁[cos βx + (H₁/β) sin βx] |

4c. Apply the condition at x = L. It always reads (constant) × (function of β) = 0. The constant cannot be zero, because then X = 0 everywhere. So the function of β must be zero: that is the eigenvalue equation, and its positive roots β₁ < β₂ < β₃ < … are the eigenvalues βₘ (Notes pp. 31–32; Özişik p. 43). This table gives all nine at once:

| X after the x = 0 condition | Face at x = L | Condition at x = L | Eigenvalue equation | Case |
| --- | --- | --- | --- | --- |
| A₂ sin βx | Zero temperature | A₂ sin βL = 0 | sin βₘL = 0 | 9 |
| A₂ sin βx | Insulated | A₂β cos βL = 0 | cos βₘL = 0 | 8 |
| A₂ sin βx | Convection | A₂(β cos βL + H₂ sin βL) = 0 | βₘ cot βₘL = −H₂ | 7 |
| A₁ cos βx | Zero temperature | A₁ cos βL = 0 | cos βₘL = 0 | 6 |
| A₁ cos βx | Insulated | −A₁β sin βL = 0 | sin βₘL = 0 | 5 |
| A₁ cos βx | Convection | A₁(−β sin βL + H₂ cos βL) = 0 | βₘ tan βₘL = H₂ | 4 |
| A₁[cos βx + (H₁/β) sin βx] | Zero temperature | cos βL + (H₁/β) sin βL = 0 | βₘ cot βₘL = −H₁ | 3 |
| A₁[cos βx + (H₁/β) sin βx] | Insulated | −β sin βL + H₁ cos βL = 0 | βₘ tan βₘL = H₁ | 2 |
| A₁[cos βx + (H₁/β) sin βx] | Convection | (H₁H₂ − β²) sin βL + β(H₁ + H₂) cos βL = 0 | tan βₘL = βₘ(H₁ + H₂)/(βₘ² − H₁H₂) | 1 |

4d. Write X in the table's form. Drop the leftover constant, because it joins Cₘ in Step 5. Cases 2 and 3 also use a trig identity to reach the table's form.

4e. Check β = 0 separately (Notes p. 32). With β = 0 the ODE is d²X/dx² = 0, so X = a + bx. Only Case 5 keeps a nonzero X.

The simplest example, Case 9 (Özişik pp. 43–44, eqs. 2-13 to 2-17):

$$
\begin{aligned}
X(0)&=A_1=0 &&\text{BC at }x=0\\
X&=A_2\sin\beta x &&\text{what is left}\\
X(L)&=A_2\sin\beta L=0 &&\text{BC at }x=L\\
\sin\beta_mL&=0 &&A_2\neq0\\
\beta_m&=\frac{m\pi}{L},\quad m=1,2,3,\dots &&\text{zeros of sine}\\
X(\beta_m,x)&=\sin\beta_mx &&\text{drop }A_2
\end{aligned}
$$

### Step 5 · Find Cₘ (the Fourier coefficient)

5a. Superpose. Each βₘ gives a solution of the PDE and both boundary conditions. The problem is linear and homogeneous, so their sum is also a solution (Notes pp. 32 and 37; Özişik p. 83, eq. 3-44):

$$
T(x,t)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)\,e^{-\alpha\beta_m^2t}
$$

5b. Apply the initial condition. At t = 0 every exponential equals 1:

$$
F(x)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)
$$

5c. Multiply both sides by X(βₙ, x) and integrate from 0 to L:

$$
\int_0^L F(x)\,X(\beta_n,x)\,dx=\sum_{m=1}^{\infty}C_m\int_0^L X(\beta_m,x)\,X(\beta_n,x)\,dx
$$

5d. Use orthogonality (Notes p. 32; Özişik p. 42, eq. 2-8). Every integral on the right is zero except the one with m = n:

$$
\int_0^L X(\beta_m,x)\,X(\beta_n,x)\,dx=\begin{cases}0 & m\neq n\\ N(\beta_m) & m=n\end{cases}
$$

5e. Solve for the coefficient and rename n as m (Notes pp. 33 and 37; Özişik p. 83, eq. 3-46):

$$
C_m=\frac{1}{N(\beta_m)}\int_0^L X(\beta_m,x')\,F(x')\,dx'
$$

The prime on x′ only marks the integration variable. Table 2-2 leaves F(x) as a symbol, so Cₘ stays in this form. Appendix B shows what happens for a specific F(x), such as the uniform start in your notes (pp. 40–41).

5f. Why orthogonality holds, in case you are asked. Write the ODE for two eigenvalues:

$$
\begin{aligned}
\frac{d^2X_m}{dx^2}+\beta_m^2X_m&=0\\
\frac{d^2X_n}{dx^2}+\beta_n^2X_n&=0
\end{aligned}
$$

Multiply the first by Xₙ and the second by Xₘ, subtract, and notice that the derivative terms form one derivative:

$$
\frac{d}{dx}\left(X_n\frac{dX_m}{dx}-X_m\frac{dX_n}{dx}\right)+\left(\beta_m^2-\beta_n^2\right)X_mX_n=0
$$

Integrate from 0 to L:

$$
\left[X_n\frac{dX_m}{dx}-X_m\frac{dX_n}{dx}\right]_0^L+\left(\beta_m^2-\beta_n^2\right)\int_0^L X_mX_n\,dx=0
$$

The bracket is zero at each face for all three kinds. For example, at x = L with dX/dx = −H₂X, it becomes Xₙ(−H₂Xₘ) − Xₘ(−H₂Xₙ) = 0. So when βₘ ≠ βₙ, the integral must be zero.

### Step 6 · Find the normalization factor

6a. Definition (Notes p. 32; Özişik p. 42, eq. 2-9):

$$
N(\beta_m)=\int_0^L\big[X(\beta_m,x)\big]^2\,dx
$$

The table lists 1/N(βₘ). Every norm in the table follows one of three patterns, set by how many faces have convection:

| Pattern | Cases | After integrating | Then use the eigenvalue equation to | Result 1/N(βₘ) |
| --- | --- | --- | --- | --- |
| A: no convective face | 5, 6, 8, 9 | N = L/2 ± sin 2βL/(4β) | make sin 2βL = 2 sin βL cos βL = 0 | 2/L (Case 5 also has 1/L for β₀ = 0) |
| B: one convective face (coefficient H) | 2, 3, 4, 7 | N = L/2 ± sin 2βL/(4β) | replace sin 2βL by ±2βH/(β² + H²) | 2(βₘ² + H²)/[L(βₘ² + H²) + H] |
| C: two convective faces | 1 | N = (β² + H₁²)[L/2 + (sin 2φ + sin 2ψ)/(4β)] | replace sin 2φ and sin 2ψ | Case 1's row |

The plus sign goes with a cosine eigenfunction (the cos² integral), and the minus sign with a sine eigenfunction (the sin² integral).

6b. Pattern B step by step, using Case 4 (X = cos βx, eigenvalue equation β tan βL = H₂). First integrate:

$$
\begin{aligned}
N&=\int_0^L\cos^2\beta x\,dx &&\text{definition}\\
&=\int_0^L\frac{1+\cos2\beta x}{2}\,dx &&\text{power reduction}\\
&=\left[\frac{x}{2}+\frac{\sin2\beta x}{4\beta}\right]_0^L &&\text{integrate}\\
&=\frac{L}{2}+\frac{\sin2\beta L}{4\beta} &&\text{limits; }\sin0=0
\end{aligned}
$$

Then replace sin 2βL with the eigenvalue equation, written as tan βL = H₂/β:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\tan\beta L}{1+\tan^2\beta L} &&\text{identity}\\
&=\frac{2H_2/\beta}{1+H_2^2/\beta^2} &&\text{substitute }\tan\beta L=H_2/\beta\\
&=\frac{2\beta H_2}{\beta^2+H_2^2} &&\text{multiply top and bottom by }\beta^2
\end{aligned}
$$

Substitute, put over one denominator, and flip:

$$
\begin{aligned}
N&=\frac{L}{2}+\frac{1}{4\beta}\cdot\frac{2\beta H_2}{\beta^2+H_2^2} &&\text{substitute}\\
&=\frac{L}{2}+\frac{H_2}{2(\beta^2+H_2^2)} &&\text{cancel }2\beta\\
&=\frac{L(\beta^2+H_2^2)+H_2}{2(\beta^2+H_2^2)} &&\text{common denominator}\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

A sine eigenfunction (Cases 3 and 7) has −sin 2βL/(4β) from the sin² integral, and its cot-form eigenvalue equation gives sin 2βL = −2βH/(β² + H²). The two minus signs cancel, so the result is the same.

6c. Pattern C (Case 1) rewrites X as a single cosine, then uses the same identity twice. The full steps are in Case 1.

6d. A check rule for all nine norms (use it to check, not as the derivation):

$$
N=A^2\left[\frac{L}{2}+\sum_{\text{convective faces}}\frac{H}{2(\beta^2+H^2)}\right]
$$

A² = β² + H₁² in Case 1, whose X has amplitude √(β² + H₁²), and A² = 1 in every other case. An insulated or zero-temperature face adds nothing.

### Final answer · Combine

Put Cₘ into the series (Notes p. 37; Özişik p. 84, eq. 3-48; 2nd ed. eq. 2-36a):

$$
T(x,t)=\sum_{m=1}^{\infty}\underbrace{e^{-\alpha\beta_m^2t}}_{\Gamma}\;\underbrace{\frac{1}{N(\beta_m)}}_{\text{Step 6}}\;\underbrace{X(\beta_m,x)}_{\text{Step 4}}\int_0^L X(\beta_m,x')\,F(x')\,dx'
$$

If you shifted with θ = T − T∞, add T∞ back at the end (Özişik p. 84, eq. 3-47). Case 5 adds an m = 0 term.

## Method 2 · 2D steady state: shared Steps 1 to 6

Use this method when T depends on x and y but not on t. The X work is the same as in Method 1 and comes from the nine cases. What is new is Laplace's equation, a Y function in place of Γ(t), and one extra factor in Cₘ (Notes pp. 59–61).

**The setup.** A rectangular plate, 0 < x < a and 0 < y < b, in steady state, with no heat generation and constant k.

- The two x-faces, x = 0 and x = a, are homogeneous: zero temperature, insulated, or convection to a fluid at zero temperature. Together they pick one of the nine cases.
- One y-face is homogeneous, with one of the same three types.
- The other y-face, y = y\_f, has the one nonhomogeneous condition, T = f(x).

### Step 1 · Formulate the governing equation

**1a.** Start from the general heat equation:

$$
\rho c_p\frac{\partial T}{\partial t}=\nabla\cdot\left(k\nabla T\right)+g
$$

**1b.** Steady state means nothing changes with time:

$$
\frac{\partial T}{\partial t}=0
$$

**1c.** No heat generation:

$$
g=0
$$

**1d.** Constant k comes out of the divergence:

$$
\nabla\cdot\left(k\nabla T\right)=k\,\nabla^2T
$$

**1e.** Put 1b to 1d into 1a and divide by k:

$$
\nabla^2T=0
$$

**1f.** In two dimensions, ∇²T has two terms. This is Laplace's equation:

$$
\frac{\partial^2T}{\partial x^2}+\frac{\partial^2T}{\partial y^2}=0\qquad 0<x<a,\quad 0<y<b
$$

### Step 2 · Apply the boundary conditions

**2a.** Every convective face uses the outward-normal rule, with the fluid at zero temperature:

$$
-k\frac{\partial T}{\partial n}=h\,\left(T-T_\infty\right),\qquad T_\infty=0
$$

**2b.** The outward normal points away from the plate: −x at x = 0, +x at x = a, −y at y = 0 and +y at y = b. At y = 0, ∂/∂n = −∂/∂y, so:

$$
-k\left(-\frac{\partial T}{\partial y}\right)=h_3T\quad\Rightarrow\quad -\frac{\partial T}{\partial y}+H_3T=0\qquad\text{at }y=0
$$

**2c.** At y = b, ∂/∂n = +∂/∂y, so:

$$
-k\,\frac{\partial T}{\partial y}=h_3T\quad\Rightarrow\quad \frac{\partial T}{\partial y}+H_3T=0\qquad\text{at }y=b
$$

**2d.** Every homogeneous option, written the same way. H₁ and H₂ are as in Table 2-2, and H₃ = h₃/k is for a convective y-face:

| Face | Zero temperature | Insulated | Convection |
| --- | --- | --- | --- |
| x = 0 | T = 0 | ∂T/∂x = 0 | −∂T/∂x + H₁T = 0 |
| x = a | T = 0 | ∂T/∂x = 0 | ∂T/∂x + H₂T = 0 |
| y = 0 | T = 0 | ∂T/∂y = 0 | −∂T/∂y + H₃T = 0 |
| y = b | T = 0 | ∂T/∂y = 0 | ∂T/∂y + H₃T = 0 |

**2e.** The nonhomogeneous face:

$$
T(x,y_f)=f(x)
$$

**2f.** A condition is homogeneous when every term contains T or a derivative of T and the other side is 0. Separation of variables needs exactly one nonhomogeneous condition (Notes p. 59; Özişik p. 75).

With more than one, split the problem by superposition: each sub-problem keeps one nonhomogeneous face, sets the others to their homogeneous form, and the solutions add (Notes p. 59). If a fluid temperature is not zero, shift θ = T − T∞ when that leaves only one nonhomogeneous face (Özişik Example 3-2, p. 90).

### Step 3 · Solve by separation of variables

**3a.** Assume a product:

$$
T(x,y)=X(x)\,Y(y)
$$

**3b.** Differentiate twice in x. Y(y) doesn't depend on x, so it acts like a constant:

$$
\frac{\partial^2T}{\partial x^2}=Y\,\frac{d^2X}{dx^2}
$$

**3c.** Differentiate twice in y. X(x) acts like a constant:

$$
\frac{\partial^2T}{\partial y^2}=X\,\frac{d^2Y}{dy^2}
$$

**3d.** Substitute into Laplace's equation:

$$
Y\,\frac{d^2X}{dx^2}+X\,\frac{d^2Y}{dy^2}=0
$$

**3e.** Divide every term by XY:

$$
\frac{1}{X}\frac{d^2X}{dx^2}+\frac{1}{Y}\frac{d^2Y}{dy^2}=0
$$

**3f.** Move the y term to the right side:

$$
\frac{1}{X}\frac{d^2X}{dx^2}=-\frac{1}{Y}\frac{d^2Y}{dy^2}
$$

**3g.** The left side depends only on x and the right side only on y. Changing y with x held fixed can't change the left side, so the right side can't change either. Both sides equal the same constant, −β²:

$$
\frac{1}{X}\frac{d^2X}{dx^2}=-\frac{1}{Y}\frac{d^2Y}{dy^2}=-\beta^2
$$

**3h.** Set the left side equal to −β² and multiply by X. This is the Table 2-2 equation:

$$
\frac{d^2X}{dx^2}+\beta^2X=0\qquad 0<x<a
$$

**3i.** Set the right side equal to −β² and multiply by −Y. This replaces the Γ equation of Method 1:

$$
\frac{d^2Y}{dy^2}-\beta^2Y=0\qquad 0<y<b
$$

**3j.** Why −β² and not +β²: x is the direction with two homogeneous faces, and only sin and cos can satisfy two homogeneous conditions without being zero. To show it on the exam, try +β² with your two x-faces. For example, with an insulated face at x = 0 and convection at x = a:

$$
X=A\cosh\beta x+B\sinh\beta x\qquad\text{(the solution with }+\beta^2\text{)}
$$

The insulated face gives Bβ = 0, so B = 0. The convective face then gives:

$$
A\left(\beta\sinh\beta a+H_2\cosh\beta a\right)=0
$$

The bracket is always positive, so A = 0 and X = 0. With β = 0, X = c₁ + c₂x, and the two faces force c₁ = c₂ = 0 as well. The one exception is two insulated x-faces (Case 5), where β₀ = 0 keeps X₀ = 1; see "Both x-faces insulated" below.

**3k.** Move each homogeneous condition onto X or Y. Substitute T = XY, factor, and cancel the factor that can't be zero. It can't be zero everywhere, because then T would be zero everywhere and could never equal f(x).

Zero temperature at x = 0:

$$
T(0,y)=X(0)\,Y(y)=0\quad\Rightarrow\quad X(0)=0
$$

Insulated at x = 0:

$$
\left.\frac{\partial T}{\partial x}\right|_{x=0}=Y(y)\left.\frac{dX}{dx}\right|_{x=0}=0\quad\Rightarrow\quad \left.\frac{dX}{dx}\right|_{x=0}=0
$$

Convection at x = 0. Factor out Y(y):

$$
Y(y)\left[-\frac{dX}{dx}+H_1X\right]_{x=0}=0\quad\Rightarrow\quad \left[-\frac{dX}{dx}+H_1X\right]_{x=0}=0
$$

The x = a face works the same way with +dX/dx and H₂. The homogeneous y-face works the same way too, except that the factor you cancel is X(x). Each condition keeps its form:

| Condition on T | Condition on X or Y |
| --- | --- |
| T = 0 | X = 0 (x-face) or Y = 0 (y-face) |
| ∂T/∂x = 0 | dX/dx = 0 |
| −∂T/∂x + H₁T = 0 at x = 0 | −dX/dx + H₁X = 0 |
| ∂T/∂x + H₂T = 0 at x = a | dX/dx + H₂X = 0 |
| ∂T/∂y = 0 | dY/dy = 0 |
| −∂T/∂y + H₃T = 0 at y = 0 | −dY/dy + H₃Y = 0 |
| ∂T/∂y + H₃T = 0 at y = b | dY/dy + H₃Y = 0 |

**3l.** The face T = f(x) can't be split, because its right side is f(x), not 0:

$$
X(x)\,Y(y_f)=f(x)
$$

A single product can't equal a general f(x); only the sum of all the products can. Save this condition for Step 5.

### Step 4 · Find the eigenfunction and the Y function

**The X part.** Go to the case for your two x-faces and do its Step 4 exactly, with L replaced by a. You get that case's X(βₘ, x) and eigenvalue equation from Table 2-2, with L → a. Drop the leftover constant; 4h below shows why that is allowed.

**The Y part.**

**4a.** Y needs functions whose second derivative is +β² times themselves. These are the hyperbolic functions:

$$
\cosh u=\frac{e^{u}+e^{-u}}{2},\qquad \sinh u=\frac{e^{u}-e^{-u}}{2}
$$

Their derivatives and their values at zero:

$$
\frac{d}{du}\cosh u=\sinh u,\qquad \frac{d}{du}\sinh u=\cosh u
$$

$$
\cosh 0=1,\qquad \sinh 0=0
$$

**4b.** Check them in the Y equation. Differentiating twice gives +β² times the function:

$$
\frac{d^2}{dy^2}\cosh\beta y=\beta^2\cosh\beta y,\qquad \frac{d^2}{dy^2}\sinh\beta y=\beta^2\sinh\beta y
$$

**4c.** So the general solution is:

$$
Y=B_1\cosh\beta y+B_2\sinh\beta y
$$

and its derivative is:

$$
\frac{dY}{dy}=B_1\beta\sinh\beta y+B_2\beta\cosh\beta y
$$

At y = 0 these give Y(0) = B₁ and dY/dy = B₂β, which makes the y = 0 faces quick.

**4d. The six Y functions.** Apply the one homogeneous y-face condition to 4c. Each derivation ends by dropping the leftover constant (4h).

**Y1 · Zero temperature at y = 0** (f(x) on y = b). Set Y(0) = 0:

$$
Y(0)=B_1=0\quad\Rightarrow\quad Y=\sinh\beta y
$$

**Y2 · Insulated at y = 0** (f(x) on y = b). Set dY/dy = 0 at y = 0:

$$
\left.\frac{dY}{dy}\right|_{y=0}=B_2\beta=0\quad\Rightarrow\quad B_2=0\quad\Rightarrow\quad Y=\cosh\beta y
$$

**Y3 · Convection at y = 0** (f(x) on y = b). The condition is −dY/dy + H₃Y = 0 at y = 0. Use Y(0) = B₁ and dY/dy = B₂β:

$$
-B_2\beta+H_3B_1=0\quad\Rightarrow\quad B_2=\frac{H_3}{\beta}\,B_1
$$

Substitute B₂ and factor out B₁/β:

$$
Y=B_1\cosh\beta y+\frac{H_3}{\beta}B_1\sinh\beta y=\frac{B_1}{\beta}\left(\beta\cosh\beta y+H_3\sinh\beta y\right)
$$

Drop the constant:

$$
Y=\beta\cosh\beta y+H_3\sinh\beta y
$$

The y = b faces need two hyperbolic identities. They match identities 7 and 8, except that cosh(A − B) has a minus sign:

$$
\cosh(A-B)=\cosh A\cosh B-\sinh A\sinh B
$$

$$
\sinh(A-B)=\sinh A\cosh B-\cosh A\sinh B
$$

**Y4 · Zero temperature at y = b** (f(x) on y = 0). Set Y(b) = 0 and solve for B₂. You can divide by sinh βb because it is not zero for β > 0:

$$
B_1\cosh\beta b+B_2\sinh\beta b=0\quad\Rightarrow\quad B_2=-B_1\,\frac{\cosh\beta b}{\sinh\beta b}
$$

Substitute B₂ and factor out B₁/sinh βb:

$$
Y=\frac{B_1}{\sinh\beta b}\Big(\sinh\beta b\,\cosh\beta y-\cosh\beta b\,\sinh\beta y\Big)
$$

The bracket is sinh(βb − βy). Drop the constant:

$$
Y=\sinh\beta(b-y)
$$

**Y5 · Insulated at y = b** (f(x) on y = 0). Set dY/dy = 0 at y = b, divide by β, and solve for B₂. cosh is never zero:

$$
B_1\sinh\beta b+B_2\cosh\beta b=0\quad\Rightarrow\quad B_2=-B_1\,\frac{\sinh\beta b}{\cosh\beta b}
$$

Substitute B₂ and factor out B₁/cosh βb:

$$
Y=\frac{B_1}{\cosh\beta b}\Big(\cosh\beta b\,\cosh\beta y-\sinh\beta b\,\sinh\beta y\Big)
$$

The bracket is cosh(βb − βy). Drop the constant:

$$
Y=\cosh\beta(b-y)
$$

**Y6 · Convection at y = b** (f(x) on y = 0). The condition is dY/dy + H₃Y = 0 at y = b. Substitute 4c and group the B₁ terms and the B₂ terms:

$$
B_1\left(\beta\sinh\beta b+H_3\cosh\beta b\right)+B_2\left(\beta\cosh\beta b+H_3\sinh\beta b\right)=0
$$

Call the second bracket D. It is always positive, so you can divide by it:

$$
B_2=-B_1\,\frac{\beta\sinh\beta b+H_3\cosh\beta b}{D},\qquad D=\beta\cosh\beta b+H_3\sinh\beta b
$$

Substitute B₂, factor out B₁/D, and group the β terms and the H₃ terms:

$$
\begin{aligned}
Y&=\frac{B_1}{D}\Big[\beta\left(\cosh\beta b\cosh\beta y-\sinh\beta b\sinh\beta y\right)\\[10pt]
&\qquad+H_3\left(\sinh\beta b\cosh\beta y-\cosh\beta b\sinh\beta y\right)\Big]
\end{aligned}
$$

The two brackets are cosh β(b − y) and sinh β(b − y). Drop the constant:

$$
Y=\beta\cosh\beta(b-y)+H_3\sinh\beta(b-y)
$$

**4e. Summary of the six Y functions.** Y is measured from its homogeneous face. The last column is the value you need in Cₘ (Step 5).

| Y | Homogeneous y-face | Condition on Y | Y(βₘ, y) | Y at the f(x) face |
| --- | --- | --- | --- | --- |
| Y1 | Zero temperature at y = 0 | Y = 0 at y = 0 | sinh βₘy | sinh βₘb |
| Y2 | Insulated at y = 0 | dY/dy = 0 at y = 0 | cosh βₘy | cosh βₘb |
| Y3 | Convection at y = 0 | −dY/dy + H₃Y = 0 at y = 0 | βₘ cosh βₘy + H₃ sinh βₘy | βₘ cosh βₘb + H₃ sinh βₘb |
| Y4 | Zero temperature at y = b | Y = 0 at y = b | sinh βₘ(b − y) | sinh βₘb |
| Y5 | Insulated at y = b | dY/dy = 0 at y = b | cosh βₘ(b − y) | cosh βₘb |
| Y6 | Convection at y = b | dY/dy + H₃Y = 0 at y = b | βₘ cosh βₘ(b − y) + H₃ sinh βₘ(b − y) | βₘ cosh βₘb + H₃ sinh βₘb |

**4f.** A quick check: each y = b function is the y = 0 function with y replaced by (b − y). That works because d/dy of (b − y) is −1, so the second derivative picks up (−1)² = 1 and the Y equation does not change. Your professor's example (Notes p. 60) is Y5.

**4g.** The Y functions are not eigenfunctions. They set no eigenvalues and are not orthogonal; each one uses the βₘ that X sets.

**4h. Why the constants can be dropped.** Multiply X and Y for one βₘ. The unknown constants multiply into one unknown number:

$$
T_m=\big(A\,X(\beta_m,x)\big)\big(B\,Y(\beta_m,y)\big)=\underbrace{A\,B}_{C_m}\,X(\beta_m,x)\,Y(\beta_m,y)
$$

You never need A or B separately, because Step 5 finds Cₘ from f(x). So X and Y are written with no constant, as in Table 2-2.

**4i.** The governing equation and the three homogeneous conditions are linear and homogeneous, so the sum of the product solutions is also a solution:

$$
T(x,y)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)\,Y(\beta_m,y)
$$

### Step 5 · Find Cₘ (the Cₘ rule)

**5a.** Use the last condition, T = f(x) at y = y\_f. Set y = y\_f in the sum:

$$
f(x)=\sum_{m=1}^{\infty}C_m\,Y(\beta_m,y_f)\,X(\beta_m,x)
$$

**5b.** The goal is to pull one Cₘ out of the infinite sum. The tool is orthogonality of the eigenfunctions X on 0 ≤ x ≤ a (Method 1, Step 5f):

$$
\int_0^a X(\beta_m,x)\,X(\beta_n,x)\,dx=\begin{cases}0 & m\neq n\\[6pt] N(\beta_n) & m=n\end{cases}
$$

You integrate over x from 0 to a because that is where the X functions are orthogonal. Y has no such property.

**5c.** Pick one eigenfunction, X(βₙ, x), where n is any fixed number (1, 2, 3, …). Multiply both sides of 5a by it:

$$
f(x)\,X(\beta_n,x)=\sum_{m=1}^{\infty}C_m\,Y(\beta_m,y_f)\,X(\beta_m,x)\,X(\beta_n,x)
$$

**5d.** Integrate both sides from x = 0 to x = a. Each Cₘ Y(βₘ, y\_f) is a constant, so it comes out of its integral:

$$
\int_0^a f(x)\,X(\beta_n,x)\,dx=\sum_{m=1}^{\infty}C_m\,Y(\beta_m,y_f)\int_0^a X(\beta_m,x)\,X(\beta_n,x)\,dx
$$

**5e.** Write out the first few terms to see orthogonality work. Take n = 2 as an example:

$$
\begin{aligned}
\int_0^a f(x)\,X(\beta_2,x)\,dx
&=C_1Y(\beta_1,y_f)\underbrace{\int_0^a X(\beta_1,x)X(\beta_2,x)\,dx}_{=\,0}\\[12pt]
&\quad+C_2Y(\beta_2,y_f)\underbrace{\int_0^a X(\beta_2,x)^2\,dx}_{=\,N(\beta_2)}\\[12pt]
&\quad+C_3Y(\beta_3,y_f)\underbrace{\int_0^a X(\beta_3,x)X(\beta_2,x)\,dx}_{=\,0}+\cdots
\end{aligned}
$$

**5f.** Every term is zero except the one where m = n:

$$
\int_0^a f(x)\,X(\beta_n,x)\,dx=C_n\,Y(\beta_n,y_f)\,N(\beta_n)
$$

**5g.** Solve for Cₙ, then rename n as m (it's just a label). This is the Cₘ rule:

$$
C_m=\frac{1}{N(\beta_m)\,Y(\beta_m,y_f)}\int_0^a X(\beta_m,x)\,f(x)\,dx
$$

In words, it is the Method 1 Cₘ divided by Y at the f(x) face. Method 1 has the same factor, but there it is Γ(0) = e⁰ = 1, so you never see it. Y(βₘ, y\_f) is always sinh βₘb, cosh βₘb or βₘ cosh βₘb + H₃ sinh βₘb (last column of 4e). Keep 1/N(βₘ) as a symbol until Step 6.

### Step 6 · Find the normalization factor

**6a.** The norm involves only X, so this step is the case's Step 6 with L replaced by a:

$$
N(\beta_m)=\int_0^a\big[X(\beta_m,x)\big]^2\,dx
$$

The result is the case's 1/N(βₘ) from Table 2-2, with L → a.

### Final answer (general form)

The temperature:

$$
T(x,y)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)\,Y(\beta_m,y)
$$

The coefficients:

$$
C_m=\frac{1}{N(\beta_m)}\cdot\frac{1}{Y(\beta_m,y_f)}\int_0^a X(\beta_m,x)\,f(x)\,dx
$$

X(βₘ, x), the eigenvalue equation and 1/N(βₘ) come from the case, with L → a. Y(βₘ, y) and Y(βₘ, y\_f) come from 4e.

**Checks.** Plug Y into its homogeneous y-face condition. At y = y\_f, the Y(βₘ, y\_f) in Cₘ cancels the one in T, and the sum rebuilds f(x).

### Both x-faces insulated (Case 5): the β₀ = 0 term

Case 5 keeps β₀ = 0 with X₀ = 1. For that term the Y equation becomes d²Y/dy² = 0, so Y₀ is a straight line chosen to meet the homogeneous y-face:

| Homogeneous y-face | Y₀(y) |
| --- | --- |
| Zero temperature at y = 0 | y |
| Zero temperature at y = b | b − y |
| Insulated at y = 0 or y = b | 1 |
| Convection at y = 0 | 1 + H₃y |
| Convection at y = b | 1 + H₃(b − y) |

The series gets one extra term. The C₀ formula is the Cₘ rule with X₀ = 1 and N₀ = a:

$$
T(x,y)=C_0\,Y_0(y)+\sum_{m=1}^{\infty}C_m\cos\beta_mx\,Y(\beta_m,y)
$$

$$
C_0=\frac{1}{a\,Y_0(y_f)}\int_0^a f(x)\,dx
$$

### When the two homogeneous faces are in y (the flip)

Sometimes one x-face carries the nonhomogeneous condition, T = g(y), and both y-faces are homogeneous. Then y is the eigenfunction direction, and everything above holds with x and y swapped.

**F1.** The separation constant changes sign, so that Y gets the Table 2-2 equation:

$$
\frac{1}{X}\frac{d^2X}{dx^2}=-\frac{1}{Y}\frac{d^2Y}{dy^2}=+\beta^2
$$

$$
\frac{d^2X}{dx^2}-\beta^2X=0,\qquad \frac{d^2Y}{dy^2}+\beta^2Y=0
$$

**F2.** Y is now the eigenfunction. Use the case for the two y-faces, and read its Table 2-2 row with y in place of x and b in place of L: y = 0 plays x = 0 (with H₁) and y = b plays x = L (with H₂).

**F3.** X is now the hyperbolic function. Use the 4e table with y → x and b → a, anchored on the homogeneous x-face.

**F4.** Cₘ integrates over y and divides by X at the face x = x\_f that carries g(y):

$$
C_m=\frac{1}{N(\beta_m)\,X(\beta_m,x_f)}\int_0^b Y(\beta_m,y)\,g(y)\,dy
$$

The norm is now taken over y:

$$
N(\beta_m)=\int_0^b\big[Y(\beta_m,y)\big]^2\,dy
$$

After the flip the steps are identical; only the letters change.

Sources: Notes pp. 59–61; Özişik p. 75 (one nonhomogeneous condition), Example 3-2 on p. 90, and p. 98 (the norms come from the same table, which the PDF calls Table 2-1).

## Trig identities: memorize only four

You only need to memorize four identities: 1, 2, 4 and 7. The others you already know or can rebuild in one line, and Method 2 adds the hyperbolic facts at the end of this section. "Step" means the exam part: Step 4 = eigenfunction, Step 5 = Cₘ, Step 6 = normalization factor.

**Memorize these four.** Identity 4 is the one that makes the normalization factors come out.

| # | Identity | Where it is used |
| --- | --- | --- |
| 1 | cos²u = (1 + cos 2u)/2 | Step 6 of Cases 2, 4, 5, 6 (the cos² integral) and Case 1 (the cos²(βx − φ) integral) |
| 2 | sin²u = (1 − cos 2u)/2 | Step 6 of Cases 3, 7, 8, 9 (the sin² integral) |
| 4 | sin 2u = 2 tan u/(1 + tan²u). It also holds with cot in place of tan (identity 5). | Step 6 of Cases 1, 2, 4 (tan form) and Cases 3, 7 (cot form) |
| 7 | cos(A − B) = cos A cos B + sin A sin B | Step 6 of Case 1 (X becomes R cos(βx − φ)); Step 4 of Case 2, unless you use trick 7 |

**Skip memorizing the rest.** You already know them, or they rebuild in one line.

| # | Identity | Where it is used | Why you can skip it |
| --- | --- | --- | --- |
| 3 | sin 2u = 2 sin u cos u | Step 6 of Cases 5, 6, 8, 9 (shows sin 2βL = 0) and Case 1 (gives sin 2φ) | You already know it |
| 5 | sin 2u = 2 cot u/(1 + cot²u) | Step 6 of Cases 3 and 7 | Identity 4 with cot in place of tan |
| 6 | cos²u = 1/(1 + tan²u) and sin²u = 1/(1 + cot²u) | Rebuilding identity 4 | One line from sin²u + cos²u = 1 (below) |
| 8 | sin(A − B) = sin A cos B − cos A sin B | Step 4 of Case 3 (X becomes sin β(L − x)) | The partner of identity 7; trick 7 avoids it |
| 9 | tan u = sin u/cos u and cot u = cos u/sin u | Step 4: tan form (Cases 1, 2, 4) or cot form (Cases 3, 7) | You already know it |
| 10 | sin mπ = 0 | Steps 4 and 6 of Cases 5 and 9 | Read it off the unit circle |
| 11 | cos((2m − 1)π/2) = 0 | Steps 4 and 6 of Cases 6 and 8 | Read it off the unit circle |
| 12 | sin 0 = 0, cos 0 = 1, cos(−u) = cos u, sin(−u) = −sin u | Step 4 of every case; Step 6 of Case 1 (the lower limit) | You already know it |
| 13 | e^(iu) = cos u + i sin u (Euler) | Step 4a: why X is built from cos βx and sin βx | You never write it on the exam |
| Check | tan(A + B) = (tan A + tan B)/(1 − tan A tan B) | Optional check of Case 1's eigenvalue equation | Optional |

If you forget identity 6, rebuild it from sin²u + cos²u = 1:

$$
\begin{aligned}
\sin^2u+\cos^2u&=1 &&\text{start}\\
\tan^2u+1&=\frac{1}{\cos^2u} &&\text{divide by }\cos^2u\\
\cos^2u&=\frac{1}{1+\tan^2u} &&\text{flip both sides}
\end{aligned}
$$

If you forget identity 4, rebuild it from identities 3 and 6:

$$
\begin{aligned}
\sin2u&=2\sin u\cos u &&\text{identity 3}\\
&=2\,\frac{\sin u}{\cos u}\,\cos^2u &&\text{multiply and divide by }\cos u\\
&=2\tan u\cos^2u &&\text{identity 9}\\
&=\frac{2\tan u}{1+\tan^2u} &&\text{identity 6}
\end{aligned}
$$

Identity 5 is the same move with sine: sin 2u = 2 cot u sin²u = 2 cot u/(1 + cot²u).

### Hyperbolic facts for Method 2

Method 2's Y functions use cosh and sinh. Memorize the derivatives and the values at zero; they work like sin and cos, but with no minus signs.

$$
\cosh u=\frac{e^{u}+e^{-u}}{2},\qquad \sinh u=\frac{e^{u}-e^{-u}}{2}
$$

$$
\frac{d}{du}\cosh u=\sinh u,\qquad \frac{d}{du}\sinh u=\cosh u
$$

$$
\cosh 0=1,\qquad \sinh 0=0,\qquad \cosh u\geq1\ \text{for every }u
$$

Only Y4 to Y6 use the two difference identities, and the check in Method 2, Step 4f gives the same results without them:

$$
\cosh(A-B)=\cosh A\cosh B-\sinh A\sinh B
$$

$$
\sinh(A-B)=\sinh A\cosh B-\cosh A\sinh B
$$

## Integrals: derive, don't memorize

Every integral runs from 0 to L, and none needs memorizing. Integrals 1, 2 and 3 come from identities 1 and 2 in three lines, worked below. The rest are basic calculus or part of the shared Step 5; integrals 5 to 8, used only for a specific F(x), are in Appendix B.

| # | Integral, from 0 to L | Where it is used | How you get it |
| --- | --- | --- | --- |
| 1 | ∫cos²βx dx = L/2 + sin 2βL/(4β) | Step 6 of Cases 4, 5, 6; Case 2 after u = L − x | Identity 1, then integrate (below) |
| 2 | ∫sin²βx dx = L/2 − sin 2βL/(4β) | Step 6 of Cases 7, 8, 9; Case 3 after u = L − x | Identity 2, then integrate (below) |
| 3 | ∫cos²(βx − φ) dx = L/2 + [sin 2(βL − φ) + sin 2φ]/(4β) | Step 6 of Case 1 (the phase method) | Integral 1 with βx − φ in place of βx (below) |
| 4 | ∫f(L − x) dx = ∫f(u) du, with u = L − x | Step 6 of Cases 2 and 3 | A substitution (below) |
| 9 | ∫1² dx = L | Step 6 of Case 5, for β₀ = 0 | Basic |
| 10 | ∫X(βₘ, x) X(βₙ, x) dx = 0 if m ≠ n, and N(βₘ) if m = n | Step 5 of every case (orthogonality) | Part of the shared Step 5, not a separate fact |
| 11 | ∫dΓ/Γ = ln Γ + c | Step 3 of every case (the time function) | Basic |
| 12 | ∫sin βx cos βx dx = sin²βL/(2β) | Only Appendix A (Case 1 by direct expansion) | Skip unless you use Appendix A |

Practice deriving integrals 1 and 2; each takes three lines:

$$
\begin{aligned}
\int_0^L\cos^2\beta x\,dx&=\int_0^L\frac{1+\cos2\beta x}{2}\,dx &&\text{identity 1}\\
&=\left[\frac{x}{2}+\frac{\sin2\beta x}{4\beta}\right]_0^L &&\text{integrate}\\
&=\frac{L}{2}+\frac{\sin2\beta L}{4\beta} &&\text{upper minus lower; }\sin0=0
\end{aligned}
$$

$$
\begin{aligned}
\int_0^L\sin^2\beta x\,dx&=\int_0^L\frac{1-\cos2\beta x}{2}\,dx &&\text{identity 2}\\
&=\left[\frac{x}{2}-\frac{\sin2\beta x}{4\beta}\right]_0^L &&\text{integrate}\\
&=\frac{L}{2}-\frac{\sin2\beta L}{4\beta} &&\text{upper minus lower; }\sin0=0
\end{aligned}
$$

Integral 3 is the same move with a shifted angle. The lower limit gives sin(−2φ), and subtracting it adds sin 2φ:

$$
\begin{aligned}
\int_0^L\cos^2(\beta x-\varphi)\,dx&=\left[\frac{x}{2}+\frac{\sin(2\beta x-2\varphi)}{4\beta}\right]_0^L &&\text{identity 1}\\
&=\frac{L}{2}+\frac{\sin(2\beta L-2\varphi)-\sin(-2\varphi)}{4\beta} &&\text{limits}\\
&=\frac{L}{2}+\frac{\sin2(\beta L-\varphi)+\sin2\varphi}{4\beta} &&\sin(-u)=-\sin u
\end{aligned}
$$

Integral 4, the reflection. The minus sign from du swaps the limits back:

$$
\begin{aligned}
\int_0^L f(L-x)\,dx&=\int_L^0 f(u)\,(-du) &&u=L-x,\;du=-dx,\;\text{limits }L\text{ to }0\\
&=\int_0^L f(u)\,du &&\text{swap limits, drop the minus}
\end{aligned}
$$

## Tricks and simplifications

These are the moves that save time or prevent sign errors, grouped by step. Don't memorize this list: each trick is already written into the case steps. Know these cold: 1 (boundary-condition signs), 9 (tan or cot form) and 15 to 18 (normalization factor).

| # | Step | Trick | Where it is used |
| --- | --- | --- | --- |
| 1 | 2 | Outward-normal rule: write −k ∂T/∂n = h(T − T∞), then set ∂/∂n = −∂/∂x at x = 0 and +∂/∂x at x = L. The signs come from substitution, not intuition. | Step 2 of Cases 1, 2, 3 (x = 0) and Cases 1, 4, 7 (x = L) |
| 2 | 2 | Temperature shift: θ = T − T∞ (or T − Tₛ) turns the T∞ terms into zero. Add T∞ back in the final answer. | Step 2 of any case whose fluid or wall is not at zero |
| 3 | 2 | Limits link the face kinds: H → 0 gives insulated, and H → ∞ gives zero temperature. | Step 2 of every case; also a check on Steps 4 and 6 |
| 4 | 3 | The separation constant is −β²: the only choice that decays in time and gives a nonzero X (see Step 3h). | Step 3 of every case |
| 5 | 3 | Divide each boundary condition by Γ(t), which is never zero, to move it from T onto X. | Step 3 of every case |
| 6 | 4 | Start at the simple face: X = 0 or dX/dx = 0 removes a constant immediately. | Step 4 of Cases 4 to 9 (x = 0 is simple) |
| 7 | 4 | Shifted general solution: X = A cos β(L − x) + B sin β(L − x). The condition at x = L removes one constant at once. | Step 4 of Cases 2 and 3 (a shortcut; the book's route uses identities 7 and 8) |
| 8 | 4 | Drop leftover constants (A₁/β, A₁/cos βL, A₁/sin βL). They join Cₘ, and the table writes X without them. | Step 4 of Cases 1, 2, 3 |
| 9 | 4 | Tan form or cot form: divide by cos βL for tan, by sin βL for cot. Hook: other face insulated gives β tan βL = H; other face at zero temperature gives β cot βL = −H. | Step 4 of Cases 1, 2, 4 (tan) and 3, 7 (cot) |
| 10 | 4 | Test β = 0 with X = a + bx. Only Case 5 keeps it, with X₀ = 1. | Step 4 of every case |
| 11 | 4 | Index conventions: (2m − 1)π/(2L) for m = 1, 2, … lists the same roots as (2m + 1)π/(2L) for m = 0, 1, … (your notes p. 40 use the second). | Step 4 of Cases 6 and 8 |
| 12 | 5 | Write Cₘ with 1/N(βₘ) as a symbol first, then fill it in after Step 6. | Step 5 of every case |
| 15 | 6 | No sin βL or cos βL may stay in the final 1/N; the table has none. Always replace them with the eigenvalue equation. | Step 6 of every case |
| 16 | 6 | One identity for every convective face: tan u = H/β gives sin 2u = 2βH/(β² + H²), and cot u = −H/β gives sin 2u = −2βH/(β² + H²). | Step 6 of Cases 1, 2, 3, 4, 7 |
| 17 | 6 | Common-denominator flip: L/2 + H/(2(β² + H²)) = [L(β² + H²) + H]/[2(β² + H²)], then invert. | Step 6 of Cases 2, 3, 4, 7 |
| 18 | 6 | Phase trick for a two-term X: β cos βx + H₁ sin βx = √(β² + H₁²) cos(βx − φ), with tan φ = H₁/β. | Step 6 of Case 1 |
| 19 | 6 | Universal check: N = A²[L/2 + sum of H/(2(β² + H²)) over the convective faces], with A² = β² + H₁² in Case 1 and 1 otherwise. | Checking Step 6 of every case |
| 20 | 4, 6 | Mirror pairs: flipping the slab (x → L − x) swaps the faces, so Cases 2 and 4, 3 and 7, and 6 and 8 share eigenvalues and norms. | Checking Steps 4 and 6 |
| 21 | All | Write the target row first, label each part with your professor's wording, and box every answer in table form. If stuck, write the definition and the target, and show what you can. | The whole exam |

Tricks 13 and 14 are only for a specific F(x), so they are in Appendix B.

**Method 2 tricks.**

| # | Step | Trick | Where it is used |
| --- | --- | --- | --- |
| 22 | 3 | Give −β² to the direction with two homogeneous faces. That direction gets sin and cos; the other gets cosh and sinh. | Step 3 of Method 2, and the flip |
| 23 | 4 | Y rule: anchor Y on its homogeneous face. Zero temperature gives sinh, insulated gives cosh, and convection gives βₘ cosh + H₃ sinh; use (b − y) when that face is y = b. | Step 4 of Method 2 |
| 24 | 5 | Cₘ rule: the Method 2 Cₘ is the Method 1 Cₘ divided by Y at the f(x) face. | Step 5 of Method 2 |

## The nine cases, shared by both methods

Each case below is written out for Method 1. For a 2D steady problem, use it like this:

- **Method 1 (1D transient):** use the whole case section.
- **Method 2 (2D steady state):** take the case's Step 2 for the x-faces, Step 4 for X and the eigenvalue equation, and Step 6 for 1/N, each with L replaced by a. Take Steps 1, 3 and 5, the Y function and the final answer from Method 2.
- **Case 5 in Method 2:** also add the β₀ = 0 term (Method 2, "Both x-faces insulated").

## Case 1 — Convection at both faces

Pattern C. What is new: the condition at x = 0 only links A₁ and A₂, and the normalization factor needs the phase trick. Your notes work this case on pp. 38–39. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\beta_m\cos\beta_mx+H_1\sin\beta_mx\\
\tan\beta_mL&=\frac{\beta_m(H_1+H_2)}{\beta_m^2-H_1H_2}\\
\frac{1}{N(\beta_m)}&=2\left[(\beta_m^2+H_1^2)\left(L+\frac{H_2}{\beta_m^2+H_2^2}\right)+H_1\right]^{-1}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** Both faces convect to fluid at zero temperature. Use −k ∂T/∂n = hT with ∂/∂n = −∂/∂x at x = 0 and +∂/∂x at x = L:

$$
\begin{aligned}
k\,\frac{\partial T}{\partial x}&=h_1T &&x=0:\ \partial T/\partial n=-\partial T/\partial x\\
-\frac{\partial T}{\partial x}+H_1T&=0 &&\text{divide by }k;\ H_1=h_1/k\\
-k\,\frac{\partial T}{\partial x}&=h_2T &&x=L:\ \partial T/\partial n=+\partial T/\partial x\\
\frac{\partial T}{\partial x}+H_2T&=0 &&\text{divide by }k;\ H_2=h_2/k\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
-\frac{dX}{dx}+H_1X&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}+H_2X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply the condition at x = 0, using X(0) = A₁ and dX/dx = A₂β at x = 0:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
-A_2\beta+H_1A_1&=0 &&\text{BC at }x=0\\
A_2&=\frac{H_1}{\beta}A_1 &&\text{solve for }A_2\\
X&=\frac{A_1}{\beta}\left(\beta\cos\beta x+H_1\sin\beta x\right) &&\text{substitute, factor out }A_1/\beta\\
X&=\beta\cos\beta x+H_1\sin\beta x &&\text{drop the constant (trick 8)}
\end{aligned}
$$

Apply the condition at x = L:

$$
\begin{aligned}
\frac{dX}{dx}&=-\beta^2\sin\beta x+\beta H_1\cos\beta x &&\text{differentiate}\\
0&=\left.\frac{dX}{dx}\right|_{x=L}+H_2X(L) &&\text{BC at }x=L\\
0&=-\beta^2\sin\beta L+\beta H_1\cos\beta L+H_2\beta\cos\beta L+H_1H_2\sin\beta L &&\text{substitute}\\
0&=(H_1H_2-\beta^2)\sin\beta L+\beta(H_1+H_2)\cos\beta L &&\text{group}
\end{aligned}
$$

Move the sin term to the other side, then divide both sides by (β² − H₁H₂) cos βL:

$$
\begin{aligned}
\beta(H_1+H_2)\cos\beta L&=(\beta^2-H_1H_2)\sin\beta L\\
\tan\beta_mL&=\frac{\beta_m(H_1+H_2)}{\beta_m^2-H_1H_2}
\end{aligned}
$$

So X(βₘ, x) = βₘ cos βₘx + H₁ sin βₘx, with βₘ the positive roots. β = 0 fails: X = a + bx gives b = H₁a at x = 0, then a(H₁ + H₂ + H₁H₂L) = 0 at x = L, so a = b = 0.

**Step 5 · Find Cₘ.** Superpose and set t = 0:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\left(\beta_m\cos\beta_mx+H_1\sin\beta_mx\right)e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\left(\beta_m\cos\beta_mx+H_1\sin\beta_mx\right) &&t=0
\end{aligned}
$$

Multiply by X(βₙ, x), integrate from 0 to L, and use orthogonality (shared Step 5):

$$
C_m=\frac{1}{N(\beta_m)}\int_0^L\left(\beta_m\cos\beta_mx'+H_1\sin\beta_mx'\right)F(x')\,dx'
$$

**Step 6 · Find the normalization factor (phase method).**

6a. Rewrite X as one cosine. Let R = √(β² + H₁²) and pick the angle φ with cos φ = β/R and sin φ = H₁/R, so tan φ = H₁/β:

$$
\begin{aligned}
X&=\beta\cos\beta x+H_1\sin\beta x &&\text{eigenfunction}\\
&=R\left(\cos\varphi\cos\beta x+\sin\varphi\sin\beta x\right) &&\beta=R\cos\varphi,\;H_1=R\sin\varphi\\
&=R\cos(\beta x-\varphi) &&\text{identity 7}
\end{aligned}
$$

6b. Write the condition at x = L in this form. Let ψ = βL − φ:

$$
\begin{aligned}
\frac{dX}{dx}&=-R\beta\sin(\beta x-\varphi) &&\text{differentiate}\\
-R\beta\sin\psi+H_2R\cos\psi&=0 &&\text{BC at }x=L\\
\tan\psi&=\frac{H_2}{\beta} &&\text{divide by }R\beta\cos\psi
\end{aligned}
$$

6c. Integrate with integral 3:

$$
\begin{aligned}
N&=\int_0^L R^2\cos^2(\beta x-\varphi)\,dx &&\text{definition}\\
&=R^2\left[\frac{L}{2}+\frac{\sin2\psi+\sin2\varphi}{4\beta}\right] &&\text{integral 3, with }\psi=\beta L-\varphi
\end{aligned}
$$

6d. Evaluate the two sines:

$$
\begin{aligned}
\sin2\varphi&=2\sin\varphi\cos\varphi &&\text{identity 3}\\
&=2\cdot\frac{H_1}{R}\cdot\frac{\beta}{R}=\frac{2\beta H_1}{\beta^2+H_1^2} &&R^2=\beta^2+H_1^2\\
\sin2\psi&=\frac{2\tan\psi}{1+\tan^2\psi} &&\text{identity 4}\\
&=\frac{2H_2/\beta}{1+H_2^2/\beta^2}=\frac{2\beta H_2}{\beta^2+H_2^2} &&\tan\psi=H_2/\beta
\end{aligned}
$$

6e. Substitute. Each sine divided by 4β leaves H/[2(β² + H²)]:

$$
\begin{aligned}
N&=(\beta^2+H_1^2)\left[\frac{L}{2}+\frac{H_1}{2(\beta^2+H_1^2)}+\frac{H_2}{2(\beta^2+H_2^2)}\right] &&\text{substitute}\\
&=\frac{(\beta^2+H_1^2)L}{2}+\frac{H_1}{2}+\frac{(\beta^2+H_1^2)H_2}{2(\beta^2+H_2^2)} &&\text{expand}\\
&=\frac{1}{2}\left[(\beta^2+H_1^2)\left(L+\frac{H_2}{\beta^2+H_2^2}\right)+H_1\right] &&\text{factor}\\
\frac{1}{N(\beta_m)}&=2\left[(\beta_m^2+H_1^2)\left(L+\frac{H_2}{\beta_m^2+H_2^2}\right)+H_1\right]^{-1} &&\text{flip}
\end{aligned}
$$

The last line matches Table 2-2.

Optional check of Step 4: φ + ψ = βL, so the tangent addition formula rebuilds the eigenvalue equation:

$$
\tan\beta L=\frac{\tan\varphi+\tan\psi}{1-\tan\varphi\tan\psi}=\frac{H_1/\beta+H_2/\beta}{1-H_1H_2/\beta^2}=\frac{\beta(H_1+H_2)}{\beta^2-H_1H_2}
$$

If you forget the phase trick, Appendix A reaches the same N by expanding X² directly.

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\left(\beta_m\cos\beta_mx+H_1\sin\beta_mx\right)e^{-\alpha\beta_m^2t}\\
C_m&=\frac{2\displaystyle\int_0^L\left(\beta_m\cos\beta_mx'+H_1\sin\beta_mx'\right)F(x')\,dx'}{(\beta_m^2+H_1^2)\left(L+\dfrac{H_2}{\beta_m^2+H_2^2}\right)+H_1}
\end{aligned}
$$

Sources: Notes pp. 38–39 for this case and pp. 31–37 for the method; Özişik pp. 81–84 for the method and p. 46 for the table row.

## Case 2 — Convection at x = 0, insulated at x = L

Pattern B, cosine. What is new: the simple face is x = L, so after the x = 0 condition you tidy X with identity 7 into cos βₘ(L − x). The 3rd-edition PDF works this case as Example 2-2 (Özişik pp. 45–47, eqs. 2-25 to 2-34). It is the mirror image of Case 4. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\cos\beta_m(L-x)\\
\beta_m\tan\beta_mL&=H_1\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 convects to fluid at zero temperature; the face x = L is insulated:

$$
\begin{aligned}
k\,\frac{\partial T}{\partial x}&=h_1T &&x=0:\ \partial T/\partial n=-\partial T/\partial x\\
-\frac{\partial T}{\partial x}+H_1T&=0 &&\text{divide by }k;\ H_1=h_1/k\\
\frac{\partial T}{\partial x}&=0 &&x=L:\ \text{insulated}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
-\frac{dX}{dx}+H_1X&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
0&=-A_2\beta+H_1A_1 &&\text{BC at }x=0\\
X&=A_1\left(\cos\beta x+\frac{H_1}{\beta}\sin\beta x\right) &&A_2=(H_1/\beta)A_1\\
\frac{dX}{dx}&=A_1\left(-\beta\sin\beta x+H_1\cos\beta x\right) &&\text{differentiate}\\
0&=A_1\left(-\beta\sin\beta L+H_1\cos\beta L\right) &&\text{BC at }x=L\\
\beta\sin\beta L&=H_1\cos\beta L &&A_1\neq0\\
\beta_m\tan\beta_mL&=H_1 &&\text{divide by }\cos\beta L
\end{aligned}
$$

Tidy X into the table's form (Özişik p. 47, eqs. 2-30 to 2-33). The eigenvalue equation says H₁/β = tan βL:

$$
\begin{aligned}
X&=A_1\left(\cos\beta x+\frac{\sin\beta L}{\cos\beta L}\sin\beta x\right) &&H_1/\beta=\tan\beta L\\
&=\frac{A_1}{\cos\beta L}\left(\cos\beta L\cos\beta x+\sin\beta L\sin\beta x\right) &&\text{factor out }1/\cos\beta L\\
&=\frac{A_1}{\cos\beta L}\cos(\beta L-\beta x) &&\text{identity 7}\\
X(\beta_m,x)&=\cos\beta_m(L-x) &&\text{drop the constant}
\end{aligned}
$$

Check: dX/dx = β sin β(L − x) is zero at x = L, and −dX/dx + H₁X at x = 0 equals −β sin βL + H₁ cos βL, which is zero by the eigenvalue equation. β = 0 fails: X = a + bx gives b = H₁a and b = 0, so a = 0. Shortcut (trick 7): start from X = A cos β(L − x) + B sin β(L − x), and dX/dx = 0 at x = L gives B = 0 at once.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_m(L-x)\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\cos\beta_m(L-x) &&t=0\\
C_m&=\frac{1}{N(\beta_m)}\int_0^L\cos\beta_m(L-x')\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** Reflect, then integrate:

$$
\begin{aligned}
N&=\int_0^L\cos^2\beta(L-x)\,dx &&\text{definition}\\
&=\int_0^L\cos^2\beta u\,du &&u=L-x\text{ (integral 4)}\\
&=\frac{L}{2}+\frac{\sin2\beta L}{4\beta} &&\text{integral 1}
\end{aligned}
$$

Replace sin 2βL with the eigenvalue equation, tan βL = H₁/β:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\tan\beta L}{1+\tan^2\beta L} &&\text{identity 4}\\
&=\frac{2H_1/\beta}{1+H_1^2/\beta^2} &&\tan\beta L=H_1/\beta\\
&=\frac{2\beta H_1}{\beta^2+H_1^2} &&\text{multiply top and bottom by }\beta^2
\end{aligned}
$$

Substitute, use one denominator, and flip:

$$
\begin{aligned}
N&=\frac{L}{2}+\frac{1}{4\beta}\cdot\frac{2\beta H_1}{\beta^2+H_1^2} &&\text{substitute}\\
&=\frac{L}{2}+\frac{H_1}{2(\beta^2+H_1^2)} &&\text{cancel }2\beta\\
&=\frac{L(\beta^2+H_1^2)+H_1}{2(\beta^2+H_1^2)} &&\text{common denominator}\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_m(L-x)\,e^{-\alpha\beta_m^2t}\\
C_m&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}\int_0^L\cos\beta_m(L-x')\,F(x')\,dx'
\end{aligned}
$$

Sources: Özişik pp. 45–47 (Example 2-2) for this case; Notes pp. 31–37 for the method.

## Case 3 — Convection at x = 0, zero temperature at x = L

Pattern B, sine. What is new: you tidy X with identity 8 into sin βₘ(L − x), the eigenvalue equation comes out in cot form, and the normalization factor uses the sin² integral. It is the mirror image of Case 7, and Özişik problem 2-3 (p. 74) asks for exactly this case. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\sin\beta_m(L-x)\\
\beta_m\cot\beta_mL&=-H_1\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 convects to fluid at zero temperature; the face x = L is held at zero temperature:

$$
\begin{aligned}
k\,\frac{\partial T}{\partial x}&=h_1T &&x=0:\ \partial T/\partial n=-\partial T/\partial x\\
-\frac{\partial T}{\partial x}+H_1T&=0 &&\text{divide by }k;\ H_1=h_1/k\\
T&=0 &&x=L:\ \text{zero temperature}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
-\frac{dX}{dx}+H_1X&=0 &&\text{BC on }X\text{ at }x=0\\
X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
0&=-A_2\beta+H_1A_1 &&\text{BC at }x=0\\
X&=A_1\left(\cos\beta x+\frac{H_1}{\beta}\sin\beta x\right) &&A_2=(H_1/\beta)A_1\\
0&=A_1\left(\cos\beta L+\frac{H_1}{\beta}\sin\beta L\right) &&\text{BC at }x=L:\ X=0\\
0&=\cos\beta L+\frac{H_1}{\beta}\sin\beta L &&A_1\neq0\\
0&=\beta\cot\beta L+H_1 &&\times\,\beta/\sin\beta L\\
\beta_m\cot\beta_mL&=-H_1 &&\text{eigenvalue equation}
\end{aligned}
$$

Tidy X into the table's form. The eigenvalue equation says H₁/β = −cot βL = −cos βL/sin βL:

$$
\begin{aligned}
X&=A_1\left(\cos\beta x-\frac{\cos\beta L}{\sin\beta L}\sin\beta x\right) &&H_1/\beta=-\cot\beta L\\
&=\frac{A_1}{\sin\beta L}\left(\sin\beta L\cos\beta x-\cos\beta L\sin\beta x\right) &&\text{factor out }1/\sin\beta L\\
&=\frac{A_1}{\sin\beta L}\sin(\beta L-\beta x) &&\text{identity 8}\\
X(\beta_m,x)&=\sin\beta_m(L-x) &&\text{drop the constant}
\end{aligned}
$$

Check: X(L) = sin 0 = 0. Also dX/dx = −β cos β(L − x), so −dX/dx + H₁X at x = 0 equals β cos βL + H₁ sin βL, which is the eigenvalue equation times sin βL, so it is zero. β = 0 fails: b = H₁a, then X(L) = a(1 + H₁L) = 0, so a = 0. Shortcut (trick 7): start from X = A cos β(L − x) + B sin β(L − x), and X(L) = 0 gives A = 0 at once.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_m(L-x)\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\sin\beta_m(L-x) &&t=0\\
C_m&=\frac{1}{N(\beta_m)}\int_0^L\sin\beta_m(L-x')\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** Reflect, then integrate:

$$
\begin{aligned}
N&=\int_0^L\sin^2\beta(L-x)\,dx &&\text{definition}\\
&=\int_0^L\sin^2\beta u\,du &&u=L-x\text{ (integral 4)}\\
&=\frac{L}{2}-\frac{\sin2\beta L}{4\beta} &&\text{integral 2}
\end{aligned}
$$

Replace sin 2βL with the eigenvalue equation, cot βL = −H₁/β:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\cot\beta L}{1+\cot^2\beta L} &&\text{identity 5}\\
&=\frac{-2H_1/\beta}{1+H_1^2/\beta^2} &&\cot\beta L=-H_1/\beta\\
&=-\frac{2\beta H_1}{\beta^2+H_1^2} &&\text{multiply top and bottom by }\beta^2
\end{aligned}
$$

Substitute, use one denominator, and flip:

$$
\begin{aligned}
N&=\frac{L}{2}-\frac{1}{4\beta}\left(-\frac{2\beta H_1}{\beta^2+H_1^2}\right) &&\text{substitute}\\
&=\frac{L}{2}+\frac{H_1}{2(\beta^2+H_1^2)} &&\text{the two minus signs cancel}\\
&=\frac{L(\beta^2+H_1^2)+H_1}{2(\beta^2+H_1^2)} &&\text{common denominator}\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_m(L-x)\,e^{-\alpha\beta_m^2t}\\
C_m&=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}\int_0^L\sin\beta_m(L-x')\,F(x')\,dx'
\end{aligned}
$$

Sources: Notes pp. 31–37 for the method; Özişik p. 46 for the row, pp. 45–47 for the parallel Example 2-2, and p. 74 (problem 2-3).

## Case 4 — Insulated at x = 0, convection at x = L

Pattern B, cosine. What is new: the insulated face at x = 0 removes A₂ at once. This is your class-notes example (Notes p. 41), the textbook's worked transient slab (Özişik pp. 80–84, eqs. 3-28 to 3-48), and Özişik problem 2-4 (p. 74). It is also the classic plane wall of half-thickness L, with x = 0 as the symmetry plane. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\cos\beta_mx\\
\beta_m\tan\beta_mL&=H_2\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 is insulated; the face x = L convects to fluid at T∞. The textbook states this case with T∞ (Özişik p. 81, eqs. 3-29 to 3-32), so it shows the temperature shift:

$$
\begin{aligned}
\frac{\partial T}{\partial x}&=0 &&x=0:\ \text{insulated}\\
-k\,\frac{\partial T}{\partial x}&=h_2\,(T-T_\infty) &&x=L:\ \partial T/\partial n=+\partial T/\partial x\\
\theta&=T-T_\infty &&\text{shift (eq. 3-30)}\\
\frac{\partial\theta}{\partial x}&=0 &&x=0\\
\frac{\partial\theta}{\partial x}+H_2\theta&=0 &&x=L;\ \text{divide by }k,\ H_2=h_2/k\\
\theta&=F(x)=T_i-T_\infty &&\text{at }t=0
\end{aligned}
$$

From here on T stands for θ, matching the table.

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}+H_2X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
0&=A_2\beta &&\text{BC at }x=0:\ dX/dx=0\\
X&=A_1\cos\beta x &&A_2=0\ (\beta\neq0)\\
\frac{dX}{dx}&=-A_1\beta\sin\beta x &&\text{differentiate}\\
0&=A_1\left(-\beta\sin\beta L+H_2\cos\beta L\right) &&\text{BC at }x=L\\
\beta\sin\beta L&=H_2\cos\beta L &&A_1\neq0\\
\beta_m\tan\beta_mL&=H_2 &&\text{divide by }\cos\beta L\\
X(\beta_m,x)&=\cos\beta_mx &&\text{drop }A_1
\end{aligned}
$$

Your notes multiply the eigenvalue equation by L to get the Biot form, ζₘ tan ζₘ = Bi, with ζₘ = βₘL and Bi = h₂L/k. They read the roots off a graph of tan ζ against Bi/ζ (Notes p. 41; Özişik p. 82, eq. 3-41). β = 0 fails: b = 0 at x = 0, then H₂a = 0 at x = L.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx &&t=0\\
C_m&=\frac{1}{N(\beta_m)}\int_0^L\cos\beta_mx'\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** Integrate:

$$
\begin{aligned}
N&=\int_0^L\cos^2\beta x\,dx &&\text{definition}\\
&=\frac{L}{2}+\frac{\sin2\beta L}{4\beta} &&\text{integral 1}
\end{aligned}
$$

Replace sin 2βL with the eigenvalue equation, tan βL = H₂/β:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\tan\beta L}{1+\tan^2\beta L} &&\text{identity 4}\\
&=\frac{2H_2/\beta}{1+H_2^2/\beta^2} &&\tan\beta L=H_2/\beta\\
&=\frac{2\beta H_2}{\beta^2+H_2^2} &&\text{multiply top and bottom by }\beta^2
\end{aligned}
$$

Substitute, use one denominator, and flip:

$$
\begin{aligned}
N&=\frac{L}{2}+\frac{1}{4\beta}\cdot\frac{2\beta H_2}{\beta^2+H_2^2} &&\text{substitute}\\
&=\frac{L}{2}+\frac{H_2}{2(\beta^2+H_2^2)} &&\text{cancel }2\beta\\
&=\frac{L(\beta^2+H_2^2)+H_2}{2(\beta^2+H_2^2)} &&\text{common denominator}\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.** If you shifted with θ = T − T∞, add T∞ back at the end (Özişik p. 84, eq. 3-47):

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t}\\
C_m&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}\int_0^L\cos\beta_mx'\,F(x')\,dx'
\end{aligned}
$$

Sources: Notes p. 41 for this case and pp. 31–37 for the method; Özişik pp. 80–84 and p. 74 (problem 2-4).

## Case 5 — Insulated at both faces

Pattern A, plus a zero eigenvalue. What is new: β₀ = 0 is an eigenvalue with X₀ = 1 and 1/N₀ = 1/L, so the series gets an extra m = 0 term. Forgetting that term is the most likely trap. Özişik problem 2-5 (p. 74) asks for exactly this case. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\cos\beta_mx,\quad\text{plus }X_0=1\text{ for }\beta_0=0\\
\sin\beta_mL&=0,\quad\text{so }\beta_m=\frac{m\pi}{L},\ m=0,1,2,\dots\\
\frac{1}{N(\beta_m)}&=\frac{2}{L}\text{ for }\beta_m\neq0,\qquad\frac{1}{N(\beta_0)}=\frac{1}{L}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** Both faces are insulated, so no heat enters or leaves, and no temperature shift is needed:

$$
\begin{aligned}
\frac{\partial T}{\partial x}&=0 &&x=0:\ \text{insulated}\\
\frac{\partial T}{\partial x}&=0 &&x=L:\ \text{insulated}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
A_2\beta&=0 &&\text{BC at }x=0:\ dX/dx=0\\
X&=A_1\cos\beta x &&A_2=0\text{ for }\beta\neq0\\
-A_1\beta\sin\beta L&=0 &&\text{BC at }x=L:\ dX/dx=0\\
\sin\beta_mL&=0 &&A_1\neq0,\ \beta\neq0\\
\beta_m&=\frac{m\pi}{L},\quad m=1,2,3,\dots &&\text{zeros of sine (identity 10)}\\
X(\beta_m,x)&=\cos\beta_mx &&\text{drop }A_1
\end{aligned}
$$

Now check β = 0 (Step 4e). It survives here:

$$
\begin{aligned}
\frac{d^2X}{dx^2}&=0 &&\text{space equation with }\beta=0\\
X&=a+bx &&\text{integrate twice}\\
\frac{dX}{dx}&=b=0 &&\text{both BCs}\\
X_0&=1 &&\text{any nonzero constant; choose }1\\
\Gamma_0&=1 &&\text{time equation with }\beta=0:\ d\Gamma/dt=0
\end{aligned}
$$

So β₀ = 0 is an eigenvalue. The table folds it into cos βₘx, because cos(0 · x) = 1.

**Step 5 · Find Cₘ.** Superpose with the m = 0 term written out, set t = 0, then use orthogonality:

$$
\begin{aligned}
T(x,t)&=C_0+\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=C_0+\sum_{m=1}^{\infty}C_m\cos\beta_mx &&t=0\\
C_0&=\frac{1}{L}\int_0^L F(x')\,dx' &&X_0=1,\ N_0=L\\
C_m&=\frac{2}{L}\int_0^L\cos\beta_mx'\,F(x')\,dx' &&m\geq1
\end{aligned}
$$

C₀ is the average initial temperature. It is also the final temperature, because an insulated slab keeps its energy and relaxes to its mean.

**Step 6 · Find the normalization factor.** For m ≥ 1:

$$
\begin{aligned}
N(\beta_m)&=\int_0^L\cos^2\beta_mx\,dx &&\text{definition}\\
&=\frac{L}{2}+\frac{\sin2\beta_mL}{4\beta_m} &&\text{integral 1}\\
&=\frac{L}{2}+\frac{2\sin\beta_mL\cos\beta_mL}{4\beta_m}=\frac{L}{2} &&\text{identity 3; }\sin\beta_mL=0\\
\frac{1}{N(\beta_m)}&=\frac{2}{L} &&\text{flip}
\end{aligned}
$$

For m = 0:

$$
\begin{aligned}
N_0&=\int_0^L1^2\,dx=L &&\text{integral 9}\\
\frac{1}{N_0}&=\frac{1}{L} &&\text{flip; matches the table footnote}
\end{aligned}
$$

The m = 0 norm is L, not L/2, because cos²(0) = 1 everywhere instead of averaging to ½.

**Final answer.**

$$
\begin{aligned}
T(x,t)&=C_0+\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t},\qquad\beta_m=\frac{m\pi}{L}\\
C_0&=\frac{1}{L}\int_0^L F(x')\,dx'\\
C_m&=\frac{2}{L}\int_0^L\cos\beta_mx'\,F(x')\,dx'
\end{aligned}
$$

Sources: Özişik p. 46 (the row and its footnote) and p. 74 (problem 2-5); Notes pp. 31–37 for the method.

## Case 6 — Insulated at x = 0, zero temperature at x = L

Pattern A. What is new: cos βL = 0 gives odd multiples of π/2. This is the example on p. 40 of your notes, where it appears as Case 1 with H₁ = 0 and H₂ → ∞. It is also Özişik problem 2-6 (p. 74), and the 2nd-edition excerpt uses it in Example 2-16 (pp. 87–89). Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\cos\beta_mx\\
\cos\beta_mL&=0,\quad\text{so }\beta_m=\frac{(2m-1)\pi}{2L}\\
\frac{1}{N(\beta_m)}&=\frac{2}{L}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 is insulated; the face x = L is held at zero temperature (if it is held at Tₛ, shift with θ = T − Tₛ first):

$$
\begin{aligned}
\frac{\partial T}{\partial x}&=0 &&x=0:\ \text{insulated}\\
T&=0 &&x=L:\ \text{zero temperature}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=0\\
X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
A_2\beta&=0 &&\text{BC at }x=0:\ dX/dx=0\\
X&=A_1\cos\beta x &&A_2=0\text{ because }\beta\neq0\\
A_1\cos\beta L&=0 &&\text{BC at }x=L:\ X=0\\
\cos\beta_mL&=0 &&A_1\neq0\\
\beta_mL&=\frac{(2m-1)\pi}{2},\quad m=1,2,3,\dots &&\text{zeros of cosine (identity 11)}\\
\beta_m&=\frac{(2m-1)\pi}{2L} &&\text{divide by }L\\
X(\beta_m,x)&=\cos\beta_mx &&\text{drop }A_1
\end{aligned}
$$

Your notes count from m = 0 instead, with βₘ = (2m + 1)π/(2L); the roots are the same (trick 11). β = 0 fails: b = 0 at x = 0, then X(L) = a = 0.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality with 1/N = 2/L from Step 6:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx &&t=0\\
C_m&=\frac{2}{L}\int_0^L\cos\beta_mx'\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** The eigenvalue equation makes the sin 2βL term vanish:

$$
\begin{aligned}
N&=\int_0^L\cos^2\beta_mx\,dx &&\text{definition}\\
&=\frac{L}{2}+\frac{\sin2\beta_mL}{4\beta_m} &&\text{integral 1}\\
&=\frac{L}{2}+\frac{2\sin\beta_mL\cos\beta_mL}{4\beta_m}=\frac{L}{2} &&\text{identity 3; }\cos\beta_mL=0\\
\frac{1}{N(\beta_m)}&=\frac{2}{L} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\cos\beta_mx\,e^{-\alpha\beta_m^2t},\qquad\beta_m=\frac{(2m-1)\pi}{2L}\\
C_m&=\frac{2}{L}\int_0^L\cos\beta_mx'\,F(x')\,dx'
\end{aligned}
$$

Sources: Notes p. 40 for this case and pp. 31–37 for the method; Özişik p. 46 and p. 74 (problem 2-6).

## Case 7 — Zero temperature at x = 0, convection at x = L

Pattern B, sine. What is new: the zero-temperature face at x = 0 removes A₁ at once, the eigenvalue equation comes out in cot form, and the normalization factor uses the sin² integral. The 3rd-edition PDF works this case as Example 2-1 (Özişik pp. 44–45, eqs. 2-20 to 2-24). It is the mirror image of Case 3. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\sin\beta_mx\\
\beta_m\cot\beta_mL&=-H_2\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 is held at zero temperature; the face x = L convects to fluid at zero temperature:

$$
\begin{aligned}
T&=0 &&x=0:\ \text{zero temperature}\\
-k\,\frac{\partial T}{\partial x}&=h_2T &&x=L:\ \partial T/\partial n=+\partial T/\partial x\\
\frac{\partial T}{\partial x}+H_2T&=0 &&\text{divide by }k;\ H_2=h_2/k\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
X&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}+H_2X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
X(0)&=A_1=0 &&\text{BC at }x=0\\
X&=A_2\sin\beta x &&\text{what is left}\\
\frac{dX}{dx}&=A_2\beta\cos\beta x &&\text{differentiate}\\
A_2\left(\beta\cos\beta L+H_2\sin\beta L\right)&=0 &&\text{BC at }x=L\\
\beta\cos\beta L+H_2\sin\beta L&=0 &&A_2\neq0\\
\beta\cot\beta L+H_2&=0 &&\text{divide by }\sin\beta L\\
\beta_m\cot\beta_mL&=-H_2 &&\text{eigenvalue equation}\\
X(\beta_m,x)&=\sin\beta_mx &&\text{drop }A_2
\end{aligned}
$$

β = 0 fails: X = a + bx gives a = 0 at x = 0, then b(1 + H₂L) = 0 at x = L, so b = 0.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx &&t=0\\
C_m&=\frac{1}{N(\beta_m)}\int_0^L\sin\beta_mx'\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** Integrate:

$$
\begin{aligned}
N&=\int_0^L\sin^2\beta x\,dx &&\text{definition}\\
&=\frac{L}{2}-\frac{\sin2\beta L}{4\beta} &&\text{integral 2}
\end{aligned}
$$

Replace sin 2βL with the eigenvalue equation, cot βL = −H₂/β:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\cot\beta L}{1+\cot^2\beta L} &&\text{identity 5}\\
&=\frac{-2H_2/\beta}{1+H_2^2/\beta^2} &&\cot\beta L=-H_2/\beta\\
&=-\frac{2\beta H_2}{\beta^2+H_2^2} &&\text{multiply top and bottom by }\beta^2
\end{aligned}
$$

Substitute, use one denominator, and flip:

$$
\begin{aligned}
N&=\frac{L}{2}-\frac{1}{4\beta}\left(-\frac{2\beta H_2}{\beta^2+H_2^2}\right) &&\text{substitute}\\
&=\frac{L}{2}+\frac{H_2}{2(\beta^2+H_2^2)} &&\text{the two minus signs cancel}\\
&=\frac{L(\beta^2+H_2^2)+H_2}{2(\beta^2+H_2^2)} &&\text{common denominator}\\
\frac{1}{N(\beta_m)}&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx\,e^{-\alpha\beta_m^2t}\\
C_m&=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}\int_0^L\sin\beta_mx'\,F(x')\,dx'
\end{aligned}
$$

Sources: Özişik pp. 44–45 (Example 2-1) for this case; Notes pp. 31–37 for the method.

## Case 8 — Zero temperature at x = 0, insulated at x = L

Pattern A. What is new: nothing beyond Case 6, mirrored. The eigenvalues are the same as Case 6, with a sine instead of a cosine. Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\sin\beta_mx\\
\cos\beta_mL&=0,\quad\text{so }\beta_m=\frac{(2m-1)\pi}{2L}\\
\frac{1}{N(\beta_m)}&=\frac{2}{L}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** The face x = 0 is held at zero temperature; the face x = L is insulated:

$$
\begin{aligned}
T&=0 &&x=0:\ \text{zero temperature}\\
\frac{\partial T}{\partial x}&=0 &&x=L:\ \text{insulated}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
X&=0 &&\text{BC on }X\text{ at }x=0\\
\frac{dX}{dx}&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
X(0)&=A_1=0 &&\text{BC at }x=0\\
X&=A_2\sin\beta x &&\text{what is left}\\
\frac{dX}{dx}&=A_2\beta\cos\beta x &&\text{differentiate}\\
A_2\beta\cos\beta L&=0 &&\text{BC at }x=L:\ dX/dx=0\\
\cos\beta_mL&=0 &&A_2\neq0,\ \beta\neq0\\
\beta_m&=\frac{(2m-1)\pi}{2L},\quad m=1,2,3,\dots &&\text{zeros of cosine (identity 11)}\\
X(\beta_m,x)&=\sin\beta_mx &&\text{drop }A_2
\end{aligned}
$$

β = 0 fails: X = a + bx gives a = 0 at x = 0, then dX/dx = b = 0 at x = L.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality with 1/N = 2/L from Step 6:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx &&t=0\\
C_m&=\frac{2}{L}\int_0^L\sin\beta_mx'\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** The eigenvalue equation makes the sin 2βL term vanish:

$$
\begin{aligned}
N&=\int_0^L\sin^2\beta_mx\,dx &&\text{definition}\\
&=\frac{L}{2}-\frac{\sin2\beta_mL}{4\beta_m} &&\text{integral 2}\\
&=\frac{L}{2}-\frac{2\sin\beta_mL\cos\beta_mL}{4\beta_m}=\frac{L}{2} &&\text{identity 3; }\cos\beta_mL=0\\
\frac{1}{N(\beta_m)}&=\frac{2}{L} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx\,e^{-\alpha\beta_m^2t},\qquad\beta_m=\frac{(2m-1)\pi}{2L}\\
C_m&=\frac{2}{L}\int_0^L\sin\beta_mx'\,F(x')\,dx'
\end{aligned}
$$

Sources: Özişik p. 46 for the row; Notes pp. 31–37 for the method.

## Case 9 — Zero temperature at both faces

Pattern A, and the simplest row. The textbook works it first (Özişik pp. 43–44, eqs. 2-13 to 2-19), and the 2nd-edition excerpt uses it in Example 2-15 (pp. 85–87). Targets from Table 2-2:

$$
\begin{aligned}
X(\beta_m,x)&=\sin\beta_mx\\
\sin\beta_mL&=0,\quad\text{so }\beta_m=\frac{m\pi}{L},\ m=1,2,3,\dots\\
\frac{1}{N(\beta_m)}&=\frac{2}{L}
\end{aligned}
$$

**Step 1 · Formulate the governing equation.** Same as the shared Step 1:

$$
\begin{aligned}
\rho c_p\frac{\partial T}{\partial t}&=\nabla\cdot(k\nabla T)+g &&\text{heat equation}\\
\frac{\partial^2T}{\partial x^2}&=\frac{1}{\alpha}\frac{\partial T}{\partial t},\quad 0<x<L,\;t>0 &&k\text{ constant},\;g=0,\;\text{1-D}
\end{aligned}
$$

**Step 2 · Apply the boundary conditions.** Both faces are held at zero temperature. If both are held at the same Tₛ, shift with θ = T − Tₛ first; if they differ, split into steady plus transient as in Example 2-15:

$$
\begin{aligned}
T&=0 &&x=0:\ \text{zero temperature}\\
T&=0 &&x=L:\ \text{zero temperature}\\
T&=F(x) &&\text{at }t=0
\end{aligned}
$$

**Step 3 · Solve by separation of variables.** Set T = X(x)Γ(t) as in the shared Step 3:

$$
\begin{aligned}
\frac{1}{X}\frac{d^2X}{dx^2}&=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2 &&\text{separate}\\
\frac{d^2X}{dx^2}+\beta^2X&=0 &&\text{Table 2-2 ODE}\\
\Gamma(t)&=e^{-\alpha\beta^2t} &&\text{time function}\\
X&=0 &&\text{BC on }X\text{ at }x=0\\
X&=0 &&\text{BC on }X\text{ at }x=L
\end{aligned}
$$

**Step 4 · Find the eigenfunction.** Apply both conditions:

$$
\begin{aligned}
X&=A_1\cos\beta x+A_2\sin\beta x &&\text{general solution}\\
X(0)&=A_1=0 &&\text{BC at }x=0\\
X&=A_2\sin\beta x &&\text{what is left}\\
A_2\sin\beta L&=0 &&\text{BC at }x=L:\ X=0\\
\sin\beta_mL&=0 &&A_2\neq0\\
\beta_m&=\frac{m\pi}{L},\quad m=1,2,3,\dots &&\text{zeros of sine (identity 10)}\\
X(\beta_m,x)&=\sin\beta_mx &&\text{drop }A_2
\end{aligned}
$$

m = 0 is excluded, because sin(0 · x) = 0 is the trivial solution. Checking X = a + bx directly gives a = 0 and bL = 0.

**Step 5 · Find Cₘ.** Superpose, set t = 0, then use orthogonality with 1/N = 2/L from Step 6:

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx\,e^{-\alpha\beta_m^2t} &&\text{superpose}\\
F(x)&=\sum_{m=1}^{\infty}C_m\sin\beta_mx &&t=0\\
C_m&=\frac{2}{L}\int_0^L\sin\beta_mx'\,F(x')\,dx' &&\text{orthogonality}
\end{aligned}
$$

**Step 6 · Find the normalization factor.** The eigenvalue equation makes the sin 2βL term vanish:

$$
\begin{aligned}
N&=\int_0^L\sin^2\beta_mx\,dx &&\text{definition}\\
&=\frac{L}{2}-\frac{\sin2\beta_mL}{4\beta_m} &&\text{integral 2}\\
&=\frac{L}{2}-\frac{2\sin\beta_mL\cos\beta_mL}{4\beta_m}=\frac{L}{2} &&\text{identity 3; }\sin\beta_mL=0\\
\frac{1}{N(\beta_m)}&=\frac{2}{L} &&\text{flip; matches Table 2-2}
\end{aligned}
$$

**Final answer.**

$$
\begin{aligned}
T(x,t)&=\sum_{m=1}^{\infty}C_m\sin\frac{m\pi x}{L}\,e^{-\alpha(m\pi/L)^2t}\\
C_m&=\frac{2}{L}\int_0^L\sin\frac{m\pi x'}{L}\,F(x')\,dx'
\end{aligned}
$$

Sources: Özişik pp. 43–44 for this case; the 2nd-edition excerpt's Example 2-15 (pp. 85–87); Notes pp. 31–37 for the method.

## Appendix A — Case 1 normalization factor by direct expansion

Use this only if you forget the phase trick. It reaches the same N with more algebra.

A1. Square X, integrate term by term with integrals 1, 12 and 2, and collect terms:

$$
\begin{aligned}
N&=\int_0^L\left(\beta\cos\beta x+H_1\sin\beta x\right)^2dx &&\text{definition}\\
&=\beta^2\!\int_0^L\cos^2\beta x\,dx+2\beta H_1\!\int_0^L\sin\beta x\cos\beta x\,dx\\
&\quad+H_1^2\!\int_0^L\sin^2\beta x\,dx &&\text{expand}\\
&=\beta^2\left[\frac{L}{2}+\frac{\sin2\beta L}{4\beta}\right]+2\beta H_1\,\frac{\sin^2\beta L}{2\beta}\\
&\quad+H_1^2\left[\frac{L}{2}-\frac{\sin2\beta L}{4\beta}\right] &&\text{int. 1, 12, 2}\\
&=\frac{(\beta^2+H_1^2)L}{2}+\frac{(\beta^2-H_1^2)\sin2\beta L}{4\beta}+H_1\sin^2\beta L &&(\star)
\end{aligned}
$$

A2. Let τ = tan βL = β(H₁ + H₂)/(β² − H₁H₂), from the eigenvalue equation. The key algebra is 1 + τ²: when you expand the numerator, the ±2β²H₁H₂ cross terms cancel and it factors:

$$
\begin{aligned}
1+\tau^2&=\frac{(\beta^2-H_1H_2)^2+\beta^2(H_1+H_2)^2}{(\beta^2-H_1H_2)^2} &&\text{common denominator}\\
&=\frac{\beta^4+\beta^2H_1^2+\beta^2H_2^2+H_1^2H_2^2}{(\beta^2-H_1H_2)^2} &&\text{expand; cross terms cancel}\\
&=\frac{(\beta^2+H_1^2)(\beta^2+H_2^2)}{(\beta^2-H_1H_2)^2} &&\text{factor}
\end{aligned}
$$

A3. Use identity 4 for sin 2βL, and sin²u = tan²u cos²u = τ²/(1 + τ²) for sin²βL:

$$
\begin{aligned}
\sin2\beta L&=\frac{2\tau}{1+\tau^2}=\frac{2\beta(H_1+H_2)(\beta^2-H_1H_2)}{(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
\sin^2\beta L&=\frac{\tau^2}{1+\tau^2}=\frac{\beta^2(H_1+H_2)^2}{(\beta^2+H_1^2)(\beta^2+H_2^2)}
\end{aligned}
$$

A4. Call the last two terms of (⋆) S, then put the A3 results into S over the common denominator 2(β² + H₁²)(β² + H₂²), expand the bracket, factor it, and cancel:

$$
\begin{aligned}
S&=\frac{(\beta^2-H_1^2)\sin2\beta L}{4\beta}+H_1\sin^2\beta L\\
&=\frac{(H_1+H_2)\left[(\beta^2-H_1^2)(\beta^2-H_1H_2)+2H_1\beta^2(H_1+H_2)\right]}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
&=\frac{(H_1+H_2)\left[\beta^4+\beta^2H_1^2+\beta^2H_1H_2+H_1^3H_2\right]}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
&=\frac{(H_1+H_2)(\beta^2+H_1^2)(\beta^2+H_1H_2)}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
&=\frac{(H_1+H_2)(\beta^2+H_1H_2)}{2(\beta^2+H_2^2)}
\end{aligned}
$$

The bracket factors because β⁴ + β²H₁² + β²H₁H₂ + H₁³H₂ = β²(β² + H₁²) + H₁H₂(β² + H₁²).

A5. Split (H₁ + H₂)(β² + H₁H₂) = H₁(β² + H₂²) + H₂(β² + H₁²), add back the first term of (⋆), and factor out ½:

$$
\begin{aligned}
N&=\frac{(\beta^2+H_1^2)L}{2}+\frac{H_1}{2}+\frac{H_2(\beta^2+H_1^2)}{2(\beta^2+H_2^2)} &&\text{split}\\
&=\frac{1}{2}\left[(\beta^2+H_1^2)\left(L+\frac{H_2}{\beta^2+H_2^2}\right)+H_1\right] &&\text{factor out }\tfrac12\\
\frac{1}{N(\beta_m)}&=2\left[(\beta_m^2+H_1^2)\left(L+\frac{H_2}{\beta_m^2+H_2^2}\right)+H_1\right]^{-1} &&\text{flip}
\end{aligned}
$$

This is the same result as the phase method in Case 1.

## Appendix B — Specific starting temperatures

Table 2-2 and its general solution keep F(x) as a symbol, so you do not need this appendix to derive the table. It shows how Cₘ simplifies for a specific F(x), mostly a uniform start F = T₀, as your notes do for Cases 6 and 4 on pp. 40–41. Each part below continues Step 5 of its case, and the last part is your notes' 2D steady example (p. 61).

### Facts used only for a specific F(x)

Each item keeps its number from the main lists, and every integral runs from 0 to L.

| Item | Fact | Where it is used |
| --- | --- | --- |
| Identity 10, second half | cos mπ = (−1)ᵐ | Case 9 uniform start; Case 5 linear start |
| Identity 11, second half | sin((2m − 1)π/2) = (−1)ᵐ⁺¹ | Case 6 uniform start |
| Integral 5 | ∫cos βx dx = sin βL/β | Uniform start: Cases 1, 4, 5, 6; Case 2 after u = L − x |
| Integral 6 | ∫sin βx dx = (1 − cos βL)/β | Uniform start: Cases 1, 7, 8, 9; Case 3 after u = L − x |
| Integral 7 | ∫x cos βx dx = L sin βL/β + (cos βL − 1)/β² | Linear start with a cosine X (the Case 5 example) |
| Integral 8 | ∫x sin βx dx = sin βL/β² − L cos βL/β | Linear start with a sine X |
| Trick 13 | If β tan βL = H, then (β² + H²) sin βL/β = H/cos βL. This shrinks the uniform-start Cₘ. | Cases 2 and 4 (your notes p. 41) |
| Trick 14 | Odd and even m: 1 − (−1)ᵐ is 2 for odd m and 0 for even m, so only odd terms survive. | Case 9 uniform start; Case 5 linear start |

Integrals 7 and 8 by parts, needed only if F(x) is not constant:

$$
\begin{aligned}
\int_0^L x\cos\beta x\,dx&=\left[\frac{x\sin\beta x}{\beta}\right]_0^L-\int_0^L\frac{\sin\beta x}{\beta}\,dx &&u=x,\;dv=\cos\beta x\,dx\\
&=\frac{L\sin\beta L}{\beta}+\frac{\cos\beta L-1}{\beta^2} &&\text{integrate, limits}
\end{aligned}
$$

$$
\begin{aligned}
\int_0^L x\sin\beta x\,dx&=\left[-\frac{x\cos\beta x}{\beta}\right]_0^L+\int_0^L\frac{\cos\beta x}{\beta}\,dx &&u=x,\;dv=\sin\beta x\,dx\\
&=\frac{\sin\beta L}{\beta^2}-\frac{L\cos\beta L}{\beta} &&\text{integrate, limits}
\end{aligned}
$$

### Case 1 with a uniform start

Uniform start, F = T₀. Integrals 5 and 6 give the integral; 1/N comes from Step 6:

$$
\int_0^L\left(\beta_m\cos\beta_mx'+H_1\sin\beta_mx'\right)dx'=\sin\beta_mL+\frac{H_1}{\beta_m}\left(1-\cos\beta_mL\right)
$$

Multiply by T₀/N, with 1/N from Step 6:

$$
C_m=\frac{2T_0\left[\sin\beta_mL+\dfrac{H_1}{\beta_m}(1-\cos\beta_mL)\right]}{(\beta_m^2+H_1^2)\left(L+\dfrac{H_2}{\beta_m^2+H_2^2}\right)+H_1}
$$

### Case 2 with a uniform start

Uniform start, F = T₀. The integral comes from integrals 4 and 5:

$$
\begin{aligned}
\int_0^L\cos\beta_m(L-x')\,dx'&=\int_0^L\cos\beta_mu\,du=\frac{\sin\beta_mL}{\beta_m} &&\text{integrals 4 and 5}\\
C_m&=\frac{2T_0(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}\cdot\frac{\sin\beta_mL}{\beta_m} &&\text{times }T_0/N
\end{aligned}
$$

Shrink it with trick 13. The eigenvalue equation gives sin βₘL = (H₁/βₘ)cos βₘL, and identity 6 gives (βₘ² + H₁²)/βₘ² = 1/cos²βₘL:

$$
\begin{aligned}
\frac{(\beta_m^2+H_1^2)\sin\beta_mL}{\beta_m}&=\frac{(\beta_m^2+H_1^2)H_1\cos\beta_mL}{\beta_m^2} &&\text{substitute }\sin\beta_mL\\
&=\frac{H_1\cos\beta_mL}{\cos^2\beta_mL}=\frac{H_1}{\cos\beta_mL} &&\text{identity 6}\\
C_m&=\frac{2T_0H_1}{\cos\beta_mL\left[L(\beta_m^2+H_1^2)+H_1\right]} &&\text{uniform-start result}
\end{aligned}
$$

### Case 3 with a uniform start

Uniform start, F = T₀:

$$
\begin{aligned}
\int_0^L\sin\beta_m(L-x')\,dx'&=\int_0^L\sin\beta_mu\,du=\frac{1-\cos\beta_mL}{\beta_m} &&\text{integrals 4 and 6}\\
C_m&=\frac{2T_0(\beta_m^2+H_1^2)(1-\cos\beta_mL)}{\beta_m\left[L(\beta_m^2+H_1^2)+H_1\right]} &&\text{times }T_0/N
\end{aligned}
$$

### Case 4 with a uniform start

Uniform start, F = T₀, as in your notes (p. 41):

$$
\begin{aligned}
\int_0^L\cos\beta_mx'\,dx'&=\frac{\sin\beta_mL}{\beta_m} &&\text{integral 5}\\
C_m&=\frac{2T_0(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}\cdot\frac{\sin\beta_mL}{\beta_m} &&\text{times }T_0/N
\end{aligned}
$$

Shrink it with trick 13. The eigenvalue equation gives sin βₘL = (H₂/βₘ)cos βₘL, and identity 6 gives (βₘ² + H₂²)/βₘ² = 1/cos²βₘL:

$$
\begin{aligned}
\frac{(\beta_m^2+H_2^2)\sin\beta_mL}{\beta_m}&=\frac{(\beta_m^2+H_2^2)H_2\cos\beta_mL}{\beta_m^2} &&\text{substitute}\\
&=\frac{H_2\cos\beta_mL}{\cos^2\beta_mL}=\frac{H_2}{\cos\beta_mL} &&\text{identity 6}\\
C_m&=\frac{2T_0H_2}{\cos\beta_mL\left[L(\beta_m^2+H_2^2)+H_2\right]} &&\text{notes p. 41}
\end{aligned}
$$

In Biot form this is the undergraduate plane-wall coefficient, Cₘ/T₀ = 4 sin ζₘ/(2ζₘ + sin 2ζₘ).

### Case 5 with uniform and linear starts

Uniform start, F = T₀: every m ≥ 1 integral is sin(mπ)/βₘ = 0, so T = T₀ for all time, as it must. A start that exercises the method is F(x) = T₀x/L. Use integral 7 with sin βₘL = 0 and cos βₘL = (−1)ᵐ:

$$
\begin{aligned}
C_0&=\frac{1}{L}\int_0^L\frac{T_0x'}{L}\,dx'=\frac{T_0}{2} &&\text{ramp average}\\
\int_0^L x'\cos\beta_mx'\,dx'&=\frac{(-1)^m-1}{\beta_m^2} &&\text{integral 7}\\
C_m&=\frac{2}{L}\cdot\frac{T_0}{L}\cdot\frac{(-1)^m-1}{\beta_m^2} &&\text{Step 5}\\
&=\frac{2T_0\left[(-1)^m-1\right]}{m^2\pi^2} &&\beta_m=m\pi/L\\
&=-\frac{4T_0}{m^2\pi^2}\text{ (odd }m),\quad0\text{ (even }m) &&\text{trick 14}
\end{aligned}
$$

$$
T(x,t)=\frac{T_0}{2}-\frac{4T_0}{\pi^2}\sum_{m=1,3,5,\dots}\frac{1}{m^2}\,e^{-\alpha(m\pi/L)^2t}\cos\frac{m\pi x}{L}
$$

### Case 6 with a uniform start

Uniform start, F = T₀, as in your notes (p. 40). Here sin βₘL = sin((2m − 1)π/2) = (−1)ᵐ⁺¹, which runs +1, −1, +1, …:

$$
\begin{aligned}
\int_0^L\cos\beta_mx'\,dx'&=\frac{\sin\beta_mL}{\beta_m}=\frac{(-1)^{m+1}}{\beta_m} &&\text{integral 5, identity 11}\\
C_m&=\frac{2T_0(-1)^{m+1}}{\beta_mL} &&\text{times }2T_0/L
\end{aligned}
$$

$$
T(x,t)=2T_0\sum_{m=1}^{\infty}(-1)^{m+1}\,\frac{e^{-\alpha\beta_m^2t}}{\beta_mL}\cos\beta_mx
$$

This is the result on p. 40 of your notes, with the index shifted by one.

### Case 7 with a uniform start

Uniform start, F = T₀:

$$
\begin{aligned}
\int_0^L\sin\beta_mx'\,dx'&=\frac{1-\cos\beta_mL}{\beta_m} &&\text{integral 6}\\
C_m&=\frac{2T_0(\beta_m^2+H_2^2)(1-\cos\beta_mL)}{\beta_m\left[L(\beta_m^2+H_2^2)+H_2\right]} &&\text{times }T_0/N
\end{aligned}
$$

### Case 8 with a uniform start

Uniform start, F = T₀. Since cos βₘL = 0, the integral simplifies:

$$
\begin{aligned}
\int_0^L\sin\beta_mx'\,dx'&=\frac{1-\cos\beta_mL}{\beta_m}=\frac{1}{\beta_m} &&\cos\beta_mL=0\\
C_m&=\frac{2}{L}\cdot\frac{T_0}{\beta_m}=\frac{2T_0}{\beta_mL} &&1/N=2/L\\
&=\frac{4T_0}{(2m-1)\pi} &&\beta_mL=\tfrac{(2m-1)\pi}{2}
\end{aligned}
$$

$$
T(x,t)=\frac{4T_0}{\pi}\sum_{m=1}^{\infty}\frac{1}{2m-1}\,e^{-\alpha\beta_m^2t}\sin\beta_mx
$$

### Case 9 with a uniform start

Uniform start, F = T₀. Here cos βₘL = cos mπ = (−1)ᵐ:

$$
\begin{aligned}
\int_0^L\sin\beta_mx'\,dx'&=\frac{1-(-1)^m}{\beta_m} &&\text{integral 6}\\
C_m&=\frac{2}{L}\cdot\frac{T_0\left[1-(-1)^m\right]}{\beta_m} &&1/N=2/L\\
&=\frac{2T_0\left[1-(-1)^m\right]}{m\pi} &&\beta_mL=m\pi\\
&=\frac{4T_0}{m\pi}\text{ (odd }m),\quad0\text{ (even }m) &&\text{trick 14}
\end{aligned}
$$

$$
T(x,t)=\frac{4T_0}{\pi}\sum_{m=1,3,5,\dots}\frac{1}{m}\,e^{-\alpha(m\pi/L)^2t}\sin\frac{m\pi x}{L}
$$

### 2D steady state with a uniform edge temperature (Notes p. 61)

Your notes end with this Method 2 example: T = 0 on x = 0, x = a and y = 0, and T = 1 on y = b. The x-faces are Case 9 with L → a, and the zero-temperature face at y = 0 gives Y1:

$$
X(\beta_m,x)=\sin\beta_mx,\qquad \beta_m=\frac{m\pi}{a},\qquad \frac{1}{N(\beta_m)}=\frac{2}{a}
$$

$$
Y(\beta_m,y)=\sinh\beta_my,\qquad Y(\beta_m,b)=\sinh\beta_mb
$$

Apply the Cₘ rule with f(x) = 1. The integral is integral 6 with L → a, and cos mπ = (−1)ᵐ:

$$
C_m=\frac{2}{a}\cdot\frac{1}{\sinh\beta_mb}\int_0^a\sin\beta_mx\,dx=\frac{2}{a}\cdot\frac{1}{\sinh\beta_mb}\cdot\frac{1-(-1)^m}{\beta_m}
$$

Use βₘ = mπ/a, so (2/a)(1/βₘ) = 2/(mπ):

$$
C_m=\frac{2\left[1-(-1)^m\right]}{m\pi\,\sinh(m\pi b/a)}
$$

$$
T(x,y)=\sum_{m=1}^{\infty}\frac{2\left[1-(-1)^m\right]}{m\pi\,\sinh(m\pi b/a)}\,\sin\frac{m\pi x}{a}\,\sinh\frac{m\pi y}{a}
$$

Only odd m survive (trick 14). This matches Notes p. 61, which writes the bracket as (−1)ᵐ⁺¹ + 1.
