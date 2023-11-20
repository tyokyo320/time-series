$$
\begin{align}
    e_i(t) = |\bar{X}(t+1) - X(t+1)|
\end{align}
$$

$$
\begin{align}
    \text{TAE} = \sum_{t=1}^{T} e_i(t)
\end{align}
$$

$$
\begin{align}
    \bar{\text{TAE}} = \frac{1}{n} \sum_{i=1}^{n} \text{TAE}
\end{align}
$$

- - -

$$
\begin{align}
    e_i(t) = |\bar{X}(t+1) - X(t+1)|
\end{align}
$$

$$
\begin{align}
    \text{MAE} = \frac{1}{T} \sum_{t=1}^{T} e_i(t)
\end{align}
$$

$$
\begin{align}
    \bar{\text{MAE}} = \frac{1}{n} \sum_{i=1}^{n} \text{MAE}
\end{align}
$$

- - -

index
predict: 0 - 414914 -> total 414915
error  : 414916 -> 829830 -> total 414915

$$
\begin{align}
    \mathbf{X}' = \argmax_{x \in \mathbf{X}} \sum^{|\mathbf{d}|}_{j=1} d_jx_j
\end{align}
$$

- - -

$$
\begin{align}
    \overline{\mathbf{x}} = \text{median}(\mathbf{X}')
\end{align}
$$

- - -

$x_i (i = 0, 1, 2, \cdots, n)$

$$
\begin{align}
    x_i = \begin{cases}
        1, \quad \text{if} \ h(X(t)) \leq i < h(X(t)) + \delta
        \\
        0, \quad \text{otherwise}
    \end{cases}
\end{align}
$$

$h(X(t)) = \text{round}( \frac{(X(t) - X^{min}) \cdot (n - \delta)}{X^{max} - X^{min}} )$

$h(X(t))$

- - -

- [x] case1: 真値
  - [x] sin_wave_nonoise
  - [x] trend_sin_nonoise
  - [x] change_sin_nonoise
  - [x] change2_sin_nonoise
- [x] case2: 5倍
  - [x] sin_wave_nonoise
  - [x] trend_sin_nonoise
  - [x] change_sin_nonoise
  - [x] change2_sin_nonoise
- [x] case3: 丸める
  - [x] sin_wave_nonoise
  - [x] trend_sin_nonoise
  - [x] change_sin_nonoise
  - [x] change2_sin_nonoise
- [x] case4: proposed (range 201)
  - [x] sin_wave_nonoise
  - [x] trend_sin_nonoise
  - [x] change_sin_nonoise
  - [x] change2_sin_nonoise

- - -

old -> backup

- [x] case4: proposed (range 401)
  - [x] sin_wave_nonoise
  - [x] trend_sin_nonoise
  - [x] change_sin_nonoise
  - [x] change2_sin_nonoise

new -> case5: proposed (range 201) -> case4: proposed