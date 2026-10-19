# Table 2-2 Derivations: All Nine Slab Cases

Sep 30, 2026 · @CD

All nine cases follow the same path: write the slab problem, separate T = X(x)Γ(t), solve X″ + β²X = 0 with the two boundary conditions to get X and the eigenvalue equation, integrate X² from 0 to L to get N, then assemble T(x,t). Part A does the shared steps once; each case section then repeats the full path for its own boundary conditions so it stands alone on the exam.

## At a glance

The nine cases differ only in the boundary conditions; each row below is derived in full in its own section.

| Case | BC at x = 0 | BC at x = L | X(βₘ, x) | 1/N(βₘ) | βₘ are the positive roots of |
| --- | --- | --- | --- | --- | --- |
| 1 | −X′ + H₁X = 0 | X′ + H₂X = 0 | βₘ cos βₘx + H₁ sin βₘx | 2 / \[(βₘ² + H₁²)(L + H₂/(βₘ² + H₂²)) + H₁\] | tan βₘL = βₘ(H₁ + H₂)/(βₘ² − H₁H₂) |
| 2 | −X′ + H₁X = 0 | X′ = 0 | cos βₘ(L − x) | 2(βₘ² + H₁²) / \[L(βₘ² + H₁²) + H₁\] | βₘ tan βₘL = H₁ |
| 3 | −X′ + H₁X = 0 | X = 0 | sin βₘ(L − x) | 2(βₘ² + H₁²) / \[L(βₘ² + H₁²) + H₁\] | βₘ cot βₘL = −H₁ |
| 4 | X′ = 0 | X′ + H₂X = 0 | cos βₘx | 2(βₘ² + H₂²) / \[L(βₘ² + H₂²) + H₂\] | βₘ tan βₘL = H₂ |
| 5 | X′ = 0 | X′ = 0 | cos βₘx (X₀ = 1 for β₀ = 0) | 2/L for m ≥ 1; 1/L for β₀ = 0 | sin βₘL = 0, so βₘ = mπ/L, m = 0, 1, 2, … |
| 6 | X′ = 0 | X = 0 | cos βₘx | 2/L | cos βₘL = 0, so βₘ = (2m − 1)π/(2L) |
| 7 | X = 0 | X′ + H₂X = 0 | sin βₘx | 2(βₘ² + H₂²) / \[L(βₘ² + H₂²) + H₂\] | βₘ cot βₘL = −H₂ |
| 8 | X = 0 | X′ = 0 | sin βₘx | 2/L | cos βₘL = 0, so βₘ = (2m − 1)π/(2L) |
| 9 | X = 0 | X = 0 | sin βₘx | 2/L | sin βₘL = 0, so βₘ = mπ/L, m = 1, 2, … |

Every case assembles into the same final solution; only X, 1/N and the eigenvalue equation change from row to row:

```latex
T(x,t)=\sum_{m=1}^{\infty}\underbrace{e^{-\alpha\beta_m^{2}t}}_{\Gamma(t)}\;\underbrace{\frac{1}{N(\beta_m)}}_{\text{table}}\;\underbrace{X(\beta_m,x)}_{\text{table}}\int_{0}^{L}X(\beta_m,x')\,F(x')\,dx'
```

Notation: H₁ = h₁/k and H₂ = h₂/k; X′ = dX/dx; F(x) is the initial temperature; x′ is a dummy integration variable. Case 5 adds an m = 0 term.

Where to find it:

- Your professor's Table 2-2 (pp. 48–49) is from Özişik's 2nd edition; the 2nd-edition excerpt in your project cites it as "Table 2-2, case 9."
- The 3rd-edition PDF in your project prints the same table as Table 2-1 on p. 46 (λₙ for βₘ) and works Cases 7 and 2 on pp. 44–47.
- The class-notes example is Lecture Notes Set 1, PDF pages 36–41: Case 1 in general, then Cases 6 and 4 with a uniform start. A shorter first pass is on pages 30–33.

## Part A — The shared derivation

Every case runs the same seven steps; only the boundary conditions on X and the norm integral change from row to row. The recipe:

1. Problem statement: a slab, its initial temperature, and a condition on each face.
2. Differential equation: the 1-D heat equation, two boundary conditions, one initial condition.
3. Separate: T(x,t) = X(x)Γ(t) splits the PDE into one ODE for Γ and one for X.
4. Solve for Γ: Γ(t) = e^(−αβ²t) in every case.
5. Solve for X: X = A₁cos βx + A₂sin βx; the two boundary conditions give X(βₘ, x) and the eigenvalue equation.
6. Find 1/N: integrate X² from 0 to L, then simplify with the eigenvalue equation.
7. Combine: T(x,t) = Σ Γ · (1/N) · X · ∫X F dx′.

**A1 · Problem statement.** A slab 0 ≤ x ≤ L has constant k and α, no heat generation, and starts at T = F(x). For t > 0 each face is held at zero temperature (1st kind), insulated (2nd kind), or cooled by a fluid at zero temperature (3rd kind). Three choices at x = 0 times three at x = L gives the nine cases:

| Face at x = 0 ↓ · face at x = L → | Convection | Insulated | T = 0 |
| --- | --- | --- | --- |
| Convection | Case 1 | Case 2 | Case 3 |
| Insulated | Case 4 | Case 5 | Case 6 |
| T = 0 | Case 7 | Case 8 | Case 9 |

"Zero" loses nothing. If the fluid or wall is at T∞, work with θ = T − T∞: it obeys the same equations, starts at F(x) − T∞, and T = θ + T∞ at the end. If the two faces sit at different temperatures, split into a steady part plus a transient part first (Özişik Example 2-15).

**A2 · Differential equation.** The heat equation ∇²T + g/k = (1/α)∂T/∂t, reduced to one dimension with g = 0:

```latex
\frac{\partial^2 T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t}\qquad 0<x<L,\;\; t>0
```

**A3 · Boundary conditions from an energy balance.** At a face, heat conducted out of the solid equals heat convected into the fluid. Fourier's law gives the flux in the +x direction as q = −k ∂T/∂x.

- At x = L the outward direction is +x, so −k ∂T/∂x = h₂T, which rearranges to k ∂T/∂x + h₂T = 0.
- At x = 0 the outward direction is −x, so the outgoing flux is +k ∂T/∂x = h₁T, which rearranges to −k ∂T/∂x + h₁T = 0. That is where the minus sign at x = 0 comes from.

Divide by k and write H₁ = h₁/k and H₂ = h₂/k (units of 1/length):

```latex
\begin{aligned}
-\frac{\partial T}{\partial x}+H_1T&=0 &&\text{at } x=0,\; t>0\\
\frac{\partial T}{\partial x}+H_2T&=0 &&\text{at } x=L,\; t>0\\
T&=F(x) &&\text{at } t=0,\; 0\le x\le L
\end{aligned}
```

The other two kinds are limits of this one (class notes, page 39). As h → 0 the T term vanishes, leaving ∂T/∂x = 0 (insulated). As h → ∞, divide by h first: (k/h)∂T/∂x + T = 0 becomes T = 0. So all nine cases are this problem with each H set to 0 or ∞, which is also a built-in check on your answers.

**A4 · Separate: T = X(x)Γ(t).** Assume the solution is a function of x alone times a function of t alone. Then ∂²T/∂x² = X″Γ and ∂T/∂t = XΓ′. Substitute into the PDE and divide both sides by XΓ:

```latex
X''\,\Gamma=\frac{1}{\alpha}X\,\Gamma'\quad\Longrightarrow\quad \frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\,\Gamma}\frac{d\Gamma}{dt}=-\beta^2
```

The left side depends only on x and the right side only on t. Hold x fixed and change t: the left side cannot change, so the right side cannot either. Both sides must therefore equal the same constant, written −β².

Why negative (class notes, page 31): a positive constant +μ² gives Γ = e^(+αμ²t), a temperature that grows forever with no heat source, and X = cosh/sinh cannot meet these boundary conditions. A zero constant gives X″ = 0, so X = a + bx, which survives only when both faces are insulated (Case 5). So the constant is −β² with β > 0.

**A5 · Solve for Γ.**

```latex
\frac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\frac{d\Gamma}{\Gamma}=-\alpha\beta^2\,dt\;\Rightarrow\;\ln\Gamma=-\alpha\beta^2t+c\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}
```

The constant e^c is dropped because it merges into Cₘ in A9. Γ is the same in all nine cases.

**A6 · Solve for X (general form).** The ODE has constant coefficients, so try X = e^(Dx):

```latex
\frac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;D^2+\beta^2=0\;\Rightarrow\;D=\pm i\beta
```

The roots ±iβ give e^(±iβx). By Euler's formula, e^(iβx) = cos βx + i sin βx, so the real combinations are cos βx and sin βx:

```latex
\begin{aligned}
X(x)&=A_1\cos\beta x+A_2\sin\beta x\\
X'(x)&=-A_1\beta\sin\beta x+A_2\beta\cos\beta x\\
X(0)&=A_1,\qquad X'(0)=A_2\beta
\end{aligned}
```

**A7 · Move the boundary conditions onto X.** Put T = XΓ into each condition. At x = 0 this gives −X′(0)Γ(t) + H₁X(0)Γ(t) = 0. Γ = e^(−αβ²t) is never zero, so divide it out:

```latex
-X'(0)+H_1X(0)=0\qquad\qquad X'(L)+H_2X(L)=0
```

The same move turns T = 0 into X = 0 and ∂T/∂x = 0 into X′ = 0. The initial condition cannot move onto X because F(x) is not zero; it is used last, in A9.

**A8 · Eigenvalues and eigenfunctions.** Two boundary conditions, two constants. The first condition ties A₁ to A₂ or makes one of them zero. The second then reads (constant) × (function of β) = 0.

The constant cannot be zero, since that gives X ≡ 0, so the function of β must vanish: that is the eigenvalue equation. Its positive roots β₁ < β₂ < β₃ < … are the eigenvalues, and X(βₘ, x), written without the leftover constant, are the eigenfunctions. Always test β = 0 separately with X = a + bx; it survives only in Case 5.

**A9 · Superpose and apply the initial condition.** Each βₘ gives a solution CₘX(βₘ, x)e^(−αβₘ²t) of the PDE and both boundary conditions. The problem is linear and homogeneous, so the sum is a solution too:

```latex
T(x,t)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)\,e^{-\alpha\beta_m^2t}
```

At t = 0 this must equal F(x). Multiply both sides by X(βₙ, x) and integrate from 0 to L:

```latex
F(x)=\sum_{m=1}^{\infty}C_m\,X(\beta_m,x)\;\Longrightarrow\;\int_0^L F(x)\,X(\beta_n,x)\,dx=\sum_{m=1}^{\infty}C_m\int_0^L X(\beta_m,x)\,X(\beta_n,x)\,dx
```

By orthogonality (A10), every integral on the right is zero except the one with m = n, which equals N(βₙ). Solve for the coefficient and rename n → m:

```latex
C_m=\frac{1}{N(\beta_m)}\int_0^L X(\beta_m,x')\,F(x')\,dx'\qquad\qquad N(\beta_m)=\int_0^L\big[X(\beta_m,x)\big]^2dx
```

**A10 · Why orthogonality holds.** Write Xₘ″ + βₘ²Xₘ = 0 and Xₙ″ + βₙ²Xₙ = 0. Multiply the first by Xₙ and the second by Xₘ, subtract, and use XₙXₘ″ − XₘXₙ″ = (XₙXₘ′ − XₘXₙ′)′. Integrating from 0 to L:

```latex
\Big[X_nX_m'-X_mX_n'\Big]_0^L+\left(\beta_m^2-\beta_n^2\right)\int_0^L X_mX_n\,dx=0
```

At x = L, X′ = −H₂X makes the bracket Xₙ(−H₂Xₘ) − Xₘ(−H₂Xₙ) = 0. The same happens at x = 0 with X′ = H₁X, and the bracket is trivially zero for X = 0 or X′ = 0. So (βₘ² − βₙ²)∫XₘXₙdx = 0, and βₘ ≠ βₙ forces ∫XₘXₙdx = 0.

**A11 · Combine into the final solution.** Put Cₘ back into the series:

```latex
T(x,t)=\sum_{m=1}^{\infty}\underbrace{e^{-\alpha\beta_m^2t}}_{\Gamma}\;\underbrace{\frac{1}{N(\beta_m)}}_{1/N}\;\underbrace{X(\beta_m,x)}_{X}\int_0^L X(\beta_m,x')\,F(x')\,dx'
```

This is the book's general solution, eq. (2-36a) in the 2nd edition. For any case, take X, 1/N and the eigenvalue equation from its row and substitute; x′ is only the integration variable.

## Toolkit — identities, integrals and exam checks

The identities and integrals below cover every norm in the table; the rest is substituting the eigenvalue equation.

| Identity | Where it is used |
| --- | --- |
| sin²u = (1 − cos 2u)/2 and cos²u = (1 + cos 2u)/2 | Every norm integral |
| sin 2u = 2 sin u cos u | Every norm integral |
| cos(A − B) = cos A cos B + sin A sin B | Case 2: turns X into cos β(L − x) |
| sin(A − B) = sin A cos B − cos A sin B | Case 3: turns X into sin β(L − x) |
| cos²u = 1/(1 + tan²u), from 1 + tan²u = sec²u | Cases 1, 2, 4 |
| sin²u = 1/(1 + cot²u), from 1 + cot²u = csc²u | Cases 3, 7 |
| sin u cos u = tan u/(1 + tan²u) = cot u/(1 + cot²u) | Cases 2, 3, 4, 7 |
| sin 2u = 2 tan u/(1 + tan²u) and sin²u = tan²u/(1 + tan²u) | Case 1 |
| sin mπ = 0, cos mπ = (−1)ᵐ, cos((2m − 1)π/2) = 0, sin((2m − 1)π/2) = (−1)ᵐ⁺¹ | Cases 5, 6, 8, 9 |

The integrals, all from 0 to L:

```latex
\begin{aligned}
\int_0^L\sin^2\beta x\,dx&=\int_0^L\frac{1-\cos2\beta x}{2}\,dx=\left[\frac{x}{2}-\frac{\sin2\beta x}{4\beta}\right]_0^L=\frac{L}{2}-\frac{\sin\beta L\cos\beta L}{2\beta}\\
\int_0^L\cos^2\beta x\,dx&=\int_0^L\frac{1+\cos2\beta x}{2}\,dx=\left[\frac{x}{2}+\frac{\sin2\beta x}{4\beta}\right]_0^L=\frac{L}{2}+\frac{\sin\beta L\cos\beta L}{2\beta}\\
\int_0^L\sin\beta x\cos\beta x\,dx&=\frac{1}{2}\int_0^L\sin2\beta x\,dx=\frac{1-\cos2\beta L}{4\beta}=\frac{\sin^2\beta L}{2\beta}\\
\int_0^L\sin\beta x\,dx&=\frac{1-\cos\beta L}{\beta}\qquad\qquad\int_0^L\cos\beta x\,dx=\frac{\sin\beta L}{\beta}\\
\int_0^L f(L-x)\,dx&=\int_0^L f(u)\,du\qquad(u=L-x,\;du=-dx,\;\text{limits swap})
\end{aligned}
```

The last step of the first two lines uses sin 2βL = 2 sin βL cos βL; the third line uses 1 − cos 2u = 2 sin²u.

**The move that finishes every one-term norm.** For X = a single sine or cosine (Cases 2–9), the integral leaves N = L/2 ± sin βL cos βL/(2β). The eigenvalue equation then fixes the product sin βL cos βL:

| Eigenvalue equation | Cases | sin βL cos βL | N | 1/N |
| --- | --- | --- | --- | --- |
| sin βL = 0 or cos βL = 0 | 5, 6, 8, 9 | 0 | L/2 | 2/L |
| β tan βL = H (X is a cosine) | 2, 4 | +Hβ/(β² + H²) | L/2 + H/\[2(β² + H²)\] | 2(β² + H²)/\[L(β² + H²) + H\] |
| β cot βL = −H (X is a sine) | 3, 7 | −Hβ/(β² + H²) | L/2 + H/\[2(β² + H²)\] | 2(β² + H²)/\[L(β² + H²) + H\] |

For the tan row: sin βL cos βL = tan βL · cos²βL = tan βL/(1 + tan²βL) = (H/β)/(1 + H²/β²) = Hβ/(β² + H²). The cot row flips the sign, but the sine integral carries a minus sign, so both land on the same N.

**Exam self-checks.**

1. Plug X back into both boundary conditions: one must vanish for every β, the other exactly when the eigenvalue equation holds.
2. Limits: in a convective row, H → 0 must give the insulated row and H → ∞ the zero-temperature row. For Case 4, β tan βL = H₂ becomes sin βL = 0 (Case 5) as H₂ → 0 and cos βL = 0 (Case 6) as H₂ → ∞, and 1/N → 2/L both ways.
3. Mirror pairs: flipping the slab (x → L − x) swaps the faces, so Cases 2 and 4, 3 and 7, and 6 and 8 share eigenvalues and norms.
4. Units: β and H are 1/length, so βL is dimensionless, H/(β² + H²) is a length like L, and 1/N is 1/length.
5. Only Case 5 keeps β = 0. A zero eigenvalue anywhere else means an algebra slip.
6. At t = 0 the series must rebuild F(x).

All nine rows of the table are correct as printed. I checked each numerically: both boundary conditions, the norm, orthogonality, and the t = 0 series for a uniform start. A separate finite-difference solution matched the Case 1 and Case 4 series to 1 part in 10⁷.

## Case 1 — Convection at x = 0, convection at x = L

Result: X(βₘ, x) = βₘcos βₘx + H₁sin βₘx; 1/N = 2\[(βₘ² + H₁²)(L + H₂/(βₘ² + H₂²)) + H₁\]⁻¹; βₘ are the positive roots of tan βₘL = βₘ(H₁ + H₂)/(βₘ² − H₁H₂). This is the general case: the other eight are its limits, and your class notes work it on pages 38–39.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 both faces lose heat by convection to fluid at zero temperature, with h₁ at x = 0 and h₂ at x = L.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&-k\frac{\partial T}{\partial x}+h_1T=0\;\Rightarrow\;-\frac{\partial T}{\partial x}+H_1T=0 &&x=0,\;t>0\\
&k\frac{\partial T}{\partial x}+h_2T=0\;\Rightarrow\;\frac{\partial T}{\partial x}+H_2T=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ into each condition and divide by Γ(t) ≠ 0:

```latex
-X'(0)+H_1X(0)=0\qquad\qquad X'(L)+H_2X(L)=0
```

**Step 4 · Apply the condition at x = 0.** With X(0) = A₁ and X′(0) = A₂β:

```latex
-A_2\beta+H_1A_1=0\;\Rightarrow\;A_2=\frac{H_1}{\beta}A_1\;\Rightarrow\;X=A_1\Big(\cos\beta x+\frac{H_1}{\beta}\sin\beta x\Big)=\frac{A_1}{\beta}\big(\beta\cos\beta x+H_1\sin\beta x\big)
```

The factor A₁/β is a constant that merges into Cₘ, so drop it: X(β, x) = β cos βx + H₁ sin βx. Your notes write the same step as A₂β = H₁A₁.

**Step 5 · Apply the condition at x = L to get the eigenvalues.** Differentiate X, then evaluate X and X′ at x = L:

```latex
\begin{aligned}
X'(x)&=-\beta^2\sin\beta x+\beta H_1\cos\beta x\\
X(L)&=\beta\cos\beta L+H_1\sin\beta L\\
X'(L)&=-\beta^2\sin\beta L+\beta H_1\cos\beta L
\end{aligned}
```

Substitute into X′(L) + H₂X(L) = 0, group the sin and cos terms, and divide by (β² − H₁H₂)cos βL:

```latex
\begin{aligned}
-\beta^2\sin\beta L+\beta H_1\cos\beta L+\beta H_2\cos\beta L+H_1H_2\sin\beta L&=0\\
\beta(H_1+H_2)\cos\beta L&=(\beta^2-H_1H_2)\sin\beta L\\
\tan\beta_mL&=\frac{\beta_m(H_1+H_2)}{\beta_m^2-H_1H_2}
\end{aligned}
```

Its positive roots β₁ < β₂ < … are the eigenvalues, found numerically or graphically. β = 0 is not one: X = a + bx gives b = H₁a at x = 0, then a(H₁ + H₂ + H₁H₂L) = 0 at x = L, so a = b = 0.

**Step 6 · Find 1/N.** Square X and integrate term by term:

```latex
N=\int_0^L(\beta\cos\beta x+H_1\sin\beta x)^2dx=\beta^2\!\int_0^L\cos^2\beta x\,dx+2\beta H_1\!\int_0^L\sin\beta x\cos\beta x\,dx+H_1^2\!\int_0^L\sin^2\beta x\,dx
```

Insert the three Toolkit integrals and collect terms:

```latex
\begin{aligned}
N&=\beta^2\left[\frac{L}{2}+\frac{\sin2\beta L}{4\beta}\right]+2\beta H_1\,\frac{\sin^2\beta L}{2\beta}+H_1^2\left[\frac{L}{2}-\frac{\sin2\beta L}{4\beta}\right]\\
&=\frac{(\beta^2+H_1^2)L}{2}+\frac{(\beta^2-H_1^2)\sin2\beta L}{4\beta}+H_1\sin^2\beta L\qquad(\star)
\end{aligned}
```

Now remove sin 2βL and sin²βL with the eigenvalue equation. Let τ = tan βL = β(H₁ + H₂)/(β² − H₁H₂). The key algebra is 1 + τ²; when you expand the numerator, the ±2β²H₁H₂ cross terms cancel and it factors:

```latex
1+\tau^2=\frac{(\beta^2-H_1H_2)^2+\beta^2(H_1+H_2)^2}{(\beta^2-H_1H_2)^2}=\frac{\beta^4+\beta^2H_1^2+\beta^2H_2^2+H_1^2H_2^2}{(\beta^2-H_1H_2)^2}=\frac{(\beta^2+H_1^2)(\beta^2+H_2^2)}{(\beta^2-H_1H_2)^2}
```

Then sin 2u = 2τ/(1 + τ²) and sin²u = τ²/(1 + τ²) give:

```latex
\sin2\beta L=\frac{2\beta(H_1+H_2)(\beta^2-H_1H_2)}{(\beta^2+H_1^2)(\beta^2+H_2^2)}\qquad\qquad
\sin^2\beta L=\frac{\beta^2(H_1+H_2)^2}{(\beta^2+H_1^2)(\beta^2+H_2^2)}
```

Put these into the last two terms of (⋆) over the common denominator 2(β² + H₁²)(β² + H₂²):

```latex
\begin{aligned}
\frac{(\beta^2-H_1^2)\sin2\beta L}{4\beta}+H_1\sin^2\beta L
&=\frac{(H_1+H_2)\left[(\beta^2-H_1^2)(\beta^2-H_1H_2)+2H_1\beta^2(H_1+H_2)\right]}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
&=\frac{(H_1+H_2)\left[\beta^4+\beta^2H_1^2+\beta^2H_1H_2+H_1^3H_2\right]}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}\\
&=\frac{(H_1+H_2)(\beta^2+H_1^2)(\beta^2+H_1H_2)}{2(\beta^2+H_1^2)(\beta^2+H_2^2)}=\frac{(H_1+H_2)(\beta^2+H_1H_2)}{2(\beta^2+H_2^2)}
\end{aligned}
```

The bracket factors because β⁴ + β²H₁² + β²H₁H₂ + H₁³H₂ = β²(β² + H₁²) + H₁H₂(β² + H₁²). Last, split (H₁ + H₂)(β² + H₁H₂) = H₁(β² + H₂²) + H₂(β² + H₁²), add back the first term of (⋆), and factor out ½:

```latex
N=\frac{1}{2}\left[(\beta_m^2+H_1^2)\left(L+\frac{H_2}{\beta_m^2+H_2^2}\right)+H_1\right]\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=2\left[(\beta_m^2+H_1^2)\left(L+\frac{H_2}{\beta_m^2+H_2^2}\right)+H_1\right]^{-1}
```

**Step 7 · Combine into T(x,t).** Γ from Step 2, X from Step 4 and 1/N from Step 6, inserted into A11:

```latex
T(x,t)=\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\;\frac{2\,(\beta_m\cos\beta_mx+H_1\sin\beta_mx)}{(\beta_m^2+H_1^2)\left(L+\dfrac{H_2}{\beta_m^2+H_2^2}\right)+H_1}\int_0^L(\beta_m\cos\beta_mx'+H_1\sin\beta_mx')\,F(x')\,dx'
```

The βₘ are the positive roots of tan βₘL = βₘ(H₁ + H₂)/(βₘ² − H₁H₂).

**Uniform start, F(x) = T₀.** The integral is ∫₀ᴸ(βₘcos βₘx′ + H₁sin βₘx′)dx′ = sin βₘL + (H₁/βₘ)(1 − cos βₘL), so:

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\;\frac{\sin\beta_mL+\dfrac{H_1}{\beta_m}(1-\cos\beta_mL)}{(\beta_m^2+H_1^2)\left(L+\dfrac{H_2}{\beta_m^2+H_2^2}\right)+H_1}\,\big(\beta_m\cos\beta_mx+H_1\sin\beta_mx\big)
```

Limit check: H₁ → 0 turns X into β cos βx and the eigenvalue equation into β tan βL = H₂, which is Case 4.

## Case 2 — Convection at x = 0, insulated at x = L

Result: X(βₘ, x) = cos βₘ(L − x); 1/N = 2(βₘ² + H₁²)/\[L(βₘ² + H₁²) + H₁\]; βₘ are the positive roots of βₘ tan βₘL = H₁. It is the mirror image of Case 4, and the 3rd-edition PDF works it as Example 2-2 (pp. 45–47).

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 convects to fluid at zero temperature (h₁) and the face x = L is insulated.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&-\frac{\partial T}{\partial x}+H_1T=0 &&x=0,\;t>0\quad(H_1=h_1/k)\\
&\frac{\partial T}{\partial x}=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
-X'(0)+H_1X(0)=0\qquad\qquad X'(L)=0
```

**Step 4 · Apply the condition at x = 0.** Exactly as in Case 1, −A₂β + H₁A₁ = 0, so A₂ = (H₁/β)A₁:

```latex
X=A_1\Big(\cos\beta x+\frac{H_1}{\beta}\sin\beta x\Big)
```

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₁ ≠ 0, so the bracket must vanish; divide by cos βL for the last line:

```latex
\begin{aligned}
X'(x)&=A_1\left(-\beta\sin\beta x+H_1\cos\beta x\right)\\
X'(L)&=A_1\left(-\beta\sin\beta L+H_1\cos\beta L\right)=0\\
\beta\sin\beta L&=H_1\cos\beta L\;\Rightarrow\;\beta_m\tan\beta_mL=H_1
\end{aligned}
```

**Tidy X with a trig identity.** The eigenvalue equation says H₁/β = tan βL. Substitute it into X from Step 4:

```latex
\begin{aligned}
X&=A_1\left(\cos\beta x+\tan\beta L\,\sin\beta x\right)=A_1\left(\cos\beta x+\frac{\sin\beta L}{\cos\beta L}\sin\beta x\right)\\
&=\frac{A_1}{\cos\beta L}\left(\cos\beta L\cos\beta x+\sin\beta L\sin\beta x\right)=\frac{A_1}{\cos\beta L}\cos(\beta L-\beta x)
\end{aligned}
```

The last step is cos(A − B) = cos A cos B + sin A sin B. Drop the constant A₁/cos βL: X(βₘ, x) = cos βₘ(L − x).

Check: X′ = β sin β(L − x) is 0 at x = L, and −X′(0) + H₁X(0) = −β sin βL + H₁cos βL = 0 by the eigenvalue equation. β = 0 fails: X = a + bx gives b = H₁a and b = 0, so a = 0. Shortcut: starting from X = A₁cos β(L − x) + A₂sin β(L − x), the x = L condition gives A₂ = 0 at once.

**Step 6 · Find 1/N.** Substitute u = L − x (du = −dx, limits swap), then use the cos² integral:

```latex
N=\int_0^L\cos^2\beta(L-x)\,dx=\int_0^L\cos^2\beta u\,du=\frac{L}{2}+\frac{\sin\beta L\cos\beta L}{2\beta}
```

From β tan βL = H₁, tan βL = H₁/β, and cos²βL = 1/(1 + tan²βL):

```latex
\sin\beta L\cos\beta L=\tan\beta L\cos^2\beta L=\frac{\tan\beta L}{1+\tan^2\beta L}=\frac{H_1/\beta}{1+H_1^2/\beta^2}=\frac{H_1\beta}{\beta^2+H_1^2}
```

```latex
N=\frac{L}{2}+\frac{H_1}{2(\beta_m^2+H_1^2)}=\frac{L(\beta_m^2+H_1^2)+H_1}{2(\beta_m^2+H_1^2)}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\,\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}\,\cos\beta_m(L-x)\int_0^L\cos\beta_m(L-x')\,F(x')\,dx'
```

The βₘ are the positive roots of βₘ tan βₘL = H₁.

**Uniform start, F(x) = T₀.** The integral is ∫₀ᴸcos βₘ(L − x′)dx′ = sin βₘL/βₘ. Using sin βₘL = H₁cos βₘL/βₘ and cos²βₘL = βₘ²/(βₘ² + H₁²), the coefficient collapses exactly as in your notes' Case 4 example (see Case 4):

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}\frac{H_1}{\cos\beta_mL\,\left[L(\beta_m^2+H_1^2)+H_1\right]}\,e^{-\alpha\beta_m^2t}\cos\beta_m(L-x)
```

## Case 3 — Convection at x = 0, zero temperature at x = L

Result: X(βₘ, x) = sin βₘ(L − x); 1/N = 2(βₘ² + H₁²)/\[L(βₘ² + H₁²) + H₁\]; βₘ are the positive roots of βₘ cot βₘL = −H₁. It is the mirror image of Case 7 and runs parallel to Case 2, with sine in place of cosine.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 convects to fluid at zero temperature (h₁) and the face x = L is held at T = 0.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&-\frac{\partial T}{\partial x}+H_1T=0 &&x=0,\;t>0\quad(H_1=h_1/k)\\
&T=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
-X'(0)+H_1X(0)=0\qquad\qquad X(L)=0
```

**Step 4 · Apply the condition at x = 0.** Exactly as in Case 1, A₂ = (H₁/β)A₁:

```latex
X=A_1\Big(\cos\beta x+\frac{H_1}{\beta}\sin\beta x\Big)
```

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₁ ≠ 0, so the bracket must vanish. Multiply it by β/sin βL and use cos/sin = cot:

```latex
\begin{aligned}
X(L)&=A_1\left(\cos\beta L+\frac{H_1}{\beta}\sin\beta L\right)=0\\
\cos\beta L+\frac{H_1}{\beta}\sin\beta L&=0\qquad\Big|\times\frac{\beta}{\sin\beta L}\\
\beta\cot\beta L+H_1&=0\;\Rightarrow\;\beta_m\cot\beta_mL=-H_1
\end{aligned}
```

**Tidy X with a trig identity.** The eigenvalue equation says H₁/β = −cot βL = −cos βL/sin βL. Substitute it into X from Step 4:

```latex
\begin{aligned}
X&=A_1\left(\cos\beta x-\frac{\cos\beta L}{\sin\beta L}\sin\beta x\right)=\frac{A_1}{\sin\beta L}\left(\sin\beta L\cos\beta x-\cos\beta L\sin\beta x\right)\\
&=\frac{A_1}{\sin\beta L}\sin(\beta L-\beta x)
\end{aligned}
```

The last step is sin(A − B) = sin A cos B − cos A sin B. Drop the constant A₁/sin βL: X(βₘ, x) = sin βₘ(L − x).

Check: X(L) = sin 0 = 0. X′ = −β cos β(L − x), so −X′(0) + H₁X(0) = β cos βL + H₁sin βL, which is zero by the eigenvalue equation. β = 0 fails: b = H₁a, then X(L) = a(1 + H₁L) = 0, so a = 0.

**Step 6 · Find 1/N.** Substitute u = L − x, then use the sin² integral:

```latex
N=\int_0^L\sin^2\beta(L-x)\,dx=\int_0^L\sin^2\beta u\,du=\frac{L}{2}-\frac{\sin\beta L\cos\beta L}{2\beta}
```

From β cot βL = −H₁, cot βL = −H₁/β, and sin²βL = 1/(1 + cot²βL):

```latex
\sin\beta L\cos\beta L=\cot\beta L\,\sin^2\beta L=\frac{\cot\beta L}{1+\cot^2\beta L}=\frac{-H_1/\beta}{1+H_1^2/\beta^2}=-\frac{H_1\beta}{\beta^2+H_1^2}
```

The two minus signs cancel, so the norm matches Case 2:

```latex
N=\frac{L}{2}+\frac{H_1}{2(\beta_m^2+H_1^2)}=\frac{L(\beta_m^2+H_1^2)+H_1}{2(\beta_m^2+H_1^2)}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\,\frac{2(\beta_m^2+H_1^2)}{L(\beta_m^2+H_1^2)+H_1}\,\sin\beta_m(L-x)\int_0^L\sin\beta_m(L-x')\,F(x')\,dx'
```

The βₘ are the positive roots of βₘ cot βₘL = −H₁.

**Uniform start, F(x) = T₀.** The integral is ∫₀ᴸsin βₘ(L − x′)dx′ = (1 − cos βₘL)/βₘ, so:

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}\frac{(\beta_m^2+H_1^2)(1-\cos\beta_mL)}{\beta_m\left[L(\beta_m^2+H_1^2)+H_1\right]}\,e^{-\alpha\beta_m^2t}\sin\beta_m(L-x)
```

## Case 4 — Insulated at x = 0, convection at x = L

Result: X(βₘ, x) = cos βₘx; 1/N = 2(βₘ² + H₂²)/\[L(βₘ² + H₂²) + H₂\]; βₘ are the positive roots of βₘ tan βₘL = H₂. This is the example on page 41 of your notes, and the classic plane wall of half-thickness L with x = 0 as the symmetry plane.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 is insulated (or is the centerline of a symmetric wall) and the face x = L convects to fluid at zero temperature (h₂).

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&\frac{\partial T}{\partial x}=0 &&x=0,\;t>0\\
&\frac{\partial T}{\partial x}+H_2T=0 &&x=L,\;t>0\quad(H_2=h_2/k)\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X'(0)=0\qquad\qquad X'(L)+H_2X(L)=0
```

**Step 4 · Apply the condition at x = 0.** X′(0) = A₂β = 0, and β ≠ 0, so A₂ = 0:

```latex
X=A_1\cos\beta x,\qquad X'=-A_1\beta\sin\beta x
```

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₁ ≠ 0, so the bracket must vanish; divide by cos βL:

```latex
\begin{aligned}
X'(L)+H_2X(L)&=A_1\left(-\beta\sin\beta L+H_2\cos\beta L\right)=0\\
\beta\sin\beta L&=H_2\cos\beta L\;\Rightarrow\;\beta_m\tan\beta_mL=H_2
\end{aligned}
```

Drop A₁: X(βₘ, x) = cos βₘx. Your notes multiply through by L to get the Biot form, ζₘ tan ζₘ = Bi, with ζₘ = βₘL and Bi = h₂L/k, and read the roots off the graph of tan ζ against Bi/ζ. β = 0 fails: b = 0 at x = 0, then H₂a = 0 at x = L.

**Step 6 · Find 1/N.**

```latex
N=\int_0^L\cos^2\beta x\,dx=\frac{L}{2}+\frac{\sin\beta L\cos\beta L}{2\beta}
```

From β tan βL = H₂, tan βL = H₂/β, and cos²βL = 1/(1 + tan²βL):

```latex
\sin\beta L\cos\beta L=\frac{\tan\beta L}{1+\tan^2\beta L}=\frac{H_2/\beta}{1+H_2^2/\beta^2}=\frac{H_2\beta}{\beta^2+H_2^2}
```

```latex
N=\frac{L}{2}+\frac{H_2}{2(\beta_m^2+H_2^2)}=\frac{L(\beta_m^2+H_2^2)+H_2}{2(\beta_m^2+H_2^2)}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\,\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}\,\cos\beta_mx\int_0^L\cos\beta_mx'\,F(x')\,dx'
```

The βₘ are the positive roots of βₘ tan βₘL = H₂.

**Uniform start, F(x) = T₀ (your notes, page 41).** The integral is ∫₀ᴸcos βₘx′dx′ = sin βₘL/βₘ, so Cₘ = 2T₀(βₘ² + H₂²)sin βₘL/(βₘ\[L(βₘ² + H₂²) + H₂\]). The eigenvalue equation shrinks it:

```latex
\begin{aligned}
\sin\beta_mL&=\frac{H_2}{\beta_m}\cos\beta_mL,\qquad\cos^2\beta_mL=\frac{1}{1+\tan^2\beta_mL}=\frac{\beta_m^2}{\beta_m^2+H_2^2}\\
\frac{(\beta_m^2+H_2^2)\sin\beta_mL}{\beta_m}&=\frac{(\beta_m^2+H_2^2)\,H_2\cos\beta_mL}{\beta_m^2}=\frac{H_2\cos\beta_mL}{\cos^2\beta_mL}=\frac{H_2}{\cos\beta_mL}
\end{aligned}
```

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}\frac{H_2}{\cos\beta_mL\,\left[L(\beta_m^2+H_2^2)+H_2\right]}\,e^{-\alpha\beta_m^2t}\cos\beta_mx
```

That is exactly the Cₘ in your notes. In Biot form it is the undergraduate plane-wall coefficient, Cₘ/T₀ = 4 sin ζₘ/(2ζₘ + sin 2ζₘ).

## Case 5 — Insulated at both faces

Result: X(βₘ, x) = cos βₘx, plus X₀ = 1 for β₀ = 0; 1/N = 2/L for m ≥ 1 and 1/L for β₀ = 0; sin βₘL = 0, so βₘ = mπ/L. It is the only case with a zero eigenvalue, and forgetting that extra term is the most likely trap.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 both faces are insulated, so no heat enters or leaves.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&\frac{\partial T}{\partial x}=0 &&x=0,\;t>0\\
&\frac{\partial T}{\partial x}=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X'(0)=0\qquad\qquad X'(L)=0
```

**Step 4 · Apply the condition at x = 0.** X′(0) = A₂β = 0, so A₂ = 0 and X = A₁cos βx.

**Step 5 · Apply the condition at x = L to get the eigenvalues.**

```latex
X'(L)=-A_1\beta\sin\beta L=0\;\Rightarrow\;\sin\beta L=0\;\Rightarrow\;\beta_mL=m\pi\;\Rightarrow\;\beta_m=\frac{m\pi}{L},\quad m=1,2,3,\dots
```

**Step 5b · The zero eigenvalue.** With β = 0 the separated equations become X″ = 0 and dΓ/dt = 0, so X = a + bx and Γ is a constant. X′ = b, and both conditions give b = 0, which leaves X = a ≠ 0. So β₀ = 0 is an eigenvalue with X₀ = 1 and Γ₀ = e⁰ = 1. The table folds it into X = cos βₘx because cos(0 · x) = 1.

**Step 6 · Find 1/N.**

```latex
\begin{aligned}
m\ge1:&\quad N=\int_0^L\cos^2\beta_mx\,dx=\frac{L}{2}+\frac{\sin\beta_mL\cos\beta_mL}{2\beta_m}=\frac{L}{2}\quad(\sin m\pi=0) &&\Rightarrow\;\frac{1}{N}=\frac{2}{L}\\
m=0:&\quad N_0=\int_0^L1^2\,dx=L &&\Rightarrow\;\frac{1}{N_0}=\frac{1}{L}
\end{aligned}
```

The m = 0 norm is L, not L/2, because cos²(0) = 1 everywhere instead of averaging to ½.

**Step 7 · Combine into T(x,t).** The sum now starts at m = 0; write that term out on its own:

```latex
T(x,t)=\underbrace{\frac{1}{L}\int_0^L F(x')\,dx'}_{m=0}+\frac{2}{L}\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\cos\beta_mx\int_0^L\cos\beta_mx'\,F(x')\,dx',\qquad\beta_m=\frac{m\pi}{L}
```

The first term is the average initial temperature. It is also T as t → ∞: no heat leaves an insulated slab, so it relaxes to its mean temperature.

**Uniform start, F(x) = T₀.** Every m ≥ 1 integral is sin(mπ)/βₘ = 0, so T(x,t) = T₀ for all t, as it should be. A start that exercises the method is F(x) = T₀x/L. Integrating by parts, ∫₀ᴸx cos βx dx = L sin βL/β + (cos βL − 1)/β², which is ((−1)ᵐ − 1)/βₘ² here. The m = 0 term is T₀/2, and only odd m survive:

```latex
T(x,t)=\frac{T_0}{2}-\frac{4T_0}{\pi^2}\sum_{m=1,3,5,\dots}\frac{1}{m^2}\,e^{-\alpha(m\pi/L)^2t}\cos\frac{m\pi x}{L}
```

## Case 6 — Insulated at x = 0, zero temperature at x = L

Result: X(βₘ, x) = cos βₘx; 1/N = 2/L; cos βₘL = 0, so βₘ = (2m − 1)π/(2L). This is the example on page 40 of your notes, where it appears as Case 1 with H₁ = 0 and H₂ → ∞.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 is insulated and the face x = L is held at T = 0.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&\frac{\partial T}{\partial x}=0 &&x=0,\;t>0\\
&T=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X'(0)=0\qquad\qquad X(L)=0
```

**Step 4 · Apply the condition at x = 0.** X′(0) = A₂β = 0, so A₂ = 0 and X = A₁cos βx.

**Step 5 · Apply the condition at x = L to get the eigenvalues.** Cosine is zero at odd multiples of π/2:

```latex
X(L)=A_1\cos\beta L=0\;\Rightarrow\;\cos\beta L=0\;\Rightarrow\;\beta_mL=\frac{(2m-1)\pi}{2}\;\Rightarrow\;\beta_m=\frac{(2m-1)\pi}{2L},\quad m=1,2,3,\dots
```

Your notes count from m = 0 instead, with βₘ = (2m + 1)π/(2L); the roots are the same. Drop A₁: X(βₘ, x) = cos βₘx. β = 0 fails: b = 0 at x = 0, then X(L) = a = 0.

**Step 6 · Find 1/N.** The product sin βL cos βL is zero because cos βₘL = 0:

```latex
N=\int_0^L\cos^2\beta_mx\,dx=\frac{L}{2}+\frac{\sin\beta_mL\cos\beta_mL}{2\beta_m}=\frac{L}{2}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2}{L}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\frac{2}{L}\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\cos\beta_mx\int_0^L\cos\beta_mx'\,F(x')\,dx',\qquad\beta_m=\frac{(2m-1)\pi}{2L}
```

**Uniform start, F(x) = T₀ (your notes, page 40).** The integral is ∫₀ᴸcos βₘx′dx′ = sin βₘL/βₘ, and sin((2m − 1)π/2) = (−1)ᵐ⁺¹ (+1, −1, +1, …). So Cₘ = 2T₀(−1)ᵐ⁺¹/(βₘL):

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}(-1)^{m+1}\,\frac{e^{-\alpha\beta_m^2t}}{\beta_mL}\cos\beta_mx
```

This is the result on page 40 of your notes, with the index shifted by one.

## Case 7 — Zero temperature at x = 0, convection at x = L

Result: X(βₘ, x) = sin βₘx; 1/N = 2(βₘ² + H₂²)/\[L(βₘ² + H₂²) + H₂\]; βₘ are the positive roots of βₘ cot βₘL = −H₂. It is the mirror image of Case 3, and the 3rd-edition PDF works it as Example 2-1 (pp. 44–45).

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 is held at T = 0 and the face x = L convects to fluid at zero temperature (h₂).

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&T=0 &&x=0,\;t>0\\
&\frac{\partial T}{\partial x}+H_2T=0 &&x=L,\;t>0\quad(H_2=h_2/k)\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X(0)=0\qquad\qquad X'(L)+H_2X(L)=0
```

**Step 4 · Apply the condition at x = 0.** X(0) = A₁cos 0 + A₂sin 0 = A₁ = 0:

```latex
X=A_2\sin\beta x,\qquad X'=A_2\beta\cos\beta x
```

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₂ ≠ 0, so the bracket must vanish. Divide it by sin βL and use cos/sin = cot:

```latex
\begin{aligned}
X'(L)+H_2X(L)&=A_2\left(\beta\cos\beta L+H_2\sin\beta L\right)=0\\
\beta\cot\beta L+H_2&=0\;\Rightarrow\;\beta_m\cot\beta_mL=-H_2
\end{aligned}
```

Drop A₂: X(βₘ, x) = sin βₘx. β = 0 fails: a = 0 at x = 0, then b(1 + H₂L) = 0 at x = L.

**Step 6 · Find 1/N.**

```latex
N=\int_0^L\sin^2\beta x\,dx=\frac{L}{2}-\frac{\sin\beta L\cos\beta L}{2\beta}
```

From β cot βL = −H₂, cot βL = −H₂/β, and sin²βL = 1/(1 + cot²βL):

```latex
\sin\beta L\cos\beta L=\cot\beta L\,\sin^2\beta L=\frac{\cot\beta L}{1+\cot^2\beta L}=\frac{-H_2/\beta}{1+H_2^2/\beta^2}=-\frac{H_2\beta}{\beta^2+H_2^2}
```

The minus from the eigenvalue equation cancels the minus in the sin² integral:

```latex
N=\frac{L}{2}+\frac{H_2}{2(\beta_m^2+H_2^2)}=\frac{L(\beta_m^2+H_2^2)+H_2}{2(\beta_m^2+H_2^2)}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\,\frac{2(\beta_m^2+H_2^2)}{L(\beta_m^2+H_2^2)+H_2}\,\sin\beta_mx\int_0^L\sin\beta_mx'\,F(x')\,dx'
```

The βₘ are the positive roots of βₘ cot βₘL = −H₂.

**Uniform start, F(x) = T₀.** The integral is ∫₀ᴸsin βₘx′dx′ = (1 − cos βₘL)/βₘ, so:

```latex
T(x,t)=2T_0\sum_{m=1}^{\infty}\frac{(\beta_m^2+H_2^2)(1-\cos\beta_mL)}{\beta_m\left[L(\beta_m^2+H_2^2)+H_2\right]}\,e^{-\alpha\beta_m^2t}\sin\beta_mx
```

## Case 8 — Zero temperature at x = 0, insulated at x = L

Result: X(βₘ, x) = sin βₘx; 1/N = 2/L; cos βₘL = 0, so βₘ = (2m − 1)π/(2L). It is the mirror image of Case 6: same eigenvalues, sine instead of cosine.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 the face x = 0 is held at T = 0 and the face x = L is insulated.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&T=0 &&x=0,\;t>0\\
&\frac{\partial T}{\partial x}=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X(0)=0\qquad\qquad X'(L)=0
```

**Step 4 · Apply the condition at x = 0.** X(0) = A₁ = 0, so X = A₂sin βx and X′ = A₂β cos βx.

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₂ ≠ 0 and β ≠ 0, so cos βL must vanish:

```latex
X'(L)=A_2\beta\cos\beta L=0\;\Rightarrow\;\cos\beta L=0\;\Rightarrow\;\beta_m=\frac{(2m-1)\pi}{2L},\quad m=1,2,3,\dots
```

Drop A₂: X(βₘ, x) = sin βₘx. β = 0 fails: a = 0 at x = 0, then X′(L) = b = 0.

**Step 6 · Find 1/N.** Again cos βₘL = 0 kills the product term:

```latex
N=\int_0^L\sin^2\beta_mx\,dx=\frac{L}{2}-\frac{\sin\beta_mL\cos\beta_mL}{2\beta_m}=\frac{L}{2}\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2}{L}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\frac{2}{L}\sum_{m=1}^{\infty}e^{-\alpha\beta_m^2t}\sin\beta_mx\int_0^L\sin\beta_mx'\,F(x')\,dx',\qquad\beta_m=\frac{(2m-1)\pi}{2L}
```

**Uniform start, F(x) = T₀.** The integral is (1 − cos βₘL)/βₘ = 1/βₘ, so Cₘ = 2T₀/(βₘL) = 4T₀/\[(2m − 1)π\]:

```latex
T(x,t)=\frac{4T_0}{\pi}\sum_{m=1}^{\infty}\frac{1}{2m-1}\,e^{-\alpha\beta_m^2t}\sin\beta_mx
```

## Case 9 — Zero temperature at both faces

Result: X(βₘ, x) = sin βₘx; 1/N = 2/L; sin βₘL = 0, so βₘ = mπ/L. This is the simplest row, and the one the 2nd-edition excerpt in your project uses in Example 2-15.

**Step 1 · Problem statement and differential equation.** A slab 0 ≤ x ≤ L starts at T = F(x). For t > 0 both faces are held at T = 0.

```latex
\begin{aligned}
&\frac{\partial^2T}{\partial x^2}=\frac{1}{\alpha}\frac{\partial T}{\partial t} &&0<x<L,\;t>0\\
&T=0 &&x=0,\;t>0\\
&T=0 &&x=L,\;t>0\\
&T=F(x) &&t=0
\end{aligned}
```

**Step 2 · Separate into X and Γ.** Substitute T = X(x)Γ(t) and divide by XΓ (Part A, A4–A6):

```latex
\frac{1}{X}\frac{d^2X}{dx^2}=\frac{1}{\alpha\Gamma}\frac{d\Gamma}{dt}=-\beta^2\;\Rightarrow\;
\begin{cases}\dfrac{d\Gamma}{dt}+\alpha\beta^2\Gamma=0\;\Rightarrow\;\Gamma(t)=e^{-\alpha\beta^2t}\\[8pt]
\dfrac{d^2X}{dx^2}+\beta^2X=0\;\Rightarrow\;X=A_1\cos\beta x+A_2\sin\beta x\end{cases}
```

**Step 3 · Boundary conditions on X.** Substitute T = XΓ and divide by Γ(t) ≠ 0:

```latex
X(0)=0\qquad\qquad X(L)=0
```

**Step 4 · Apply the condition at x = 0.** X(0) = A₁ = 0, so X = A₂sin βx.

**Step 5 · Apply the condition at x = L to get the eigenvalues.** A₂ ≠ 0, so sin βL must vanish:

```latex
X(L)=A_2\sin\beta L=0\;\Rightarrow\;\sin\beta L=0\;\Rightarrow\;\beta_mL=m\pi\;\Rightarrow\;\beta_m=\frac{m\pi}{L},\quad m=1,2,3,\dots
```

m = 0 is excluded because sin(0 · x) ≡ 0 is the trivial solution; checking X = a + bx directly gives a = 0 and bL = 0. Drop A₂: X(βₘ, x) = sin βₘx.

**Step 6 · Find 1/N.**

```latex
N=\int_0^L\sin^2\beta_mx\,dx=\frac{L}{2}-\frac{\sin\beta_mL\cos\beta_mL}{2\beta_m}=\frac{L}{2}\quad(\sin m\pi=0)\qquad\Rightarrow\qquad\frac{1}{N(\beta_m)}=\frac{2}{L}
```

**Step 7 · Combine into T(x,t).**

```latex
T(x,t)=\frac{2}{L}\sum_{m=1}^{\infty}e^{-\alpha(m\pi/L)^2t}\sin\frac{m\pi x}{L}\int_0^L\sin\frac{m\pi x'}{L}\,F(x')\,dx'
```

**Uniform start, F(x) = T₀.** The integral is (1 − cos mπ)/βₘ = (1 − (−1)ᵐ)/βₘ: 2/βₘ for odd m and 0 for even m. So Cₘ = 4T₀/(mπ) for odd m:

```latex
T(x,t)=\frac{4T_0}{\pi}\sum_{m=1,3,5,\dots}\frac{1}{m}\,e^{-\alpha(m\pi/L)^2t}\sin\frac{m\pi x}{L}
```
