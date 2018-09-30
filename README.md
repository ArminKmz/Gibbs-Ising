# Gibbs-Ising

This is simple python code for generating samples from Ising model using Gibbs sampling. 

## Useage
Call ```get_sample(W, u, n)``` to get ```n``` samples from Ising:<br></br>
<img src="https://latex.codecogs.com/svg.latex?P(x)=\frac{1}{z}exp(\sum_{i,j}W_{ij}x_ix_j+\sum_iu_ix_i)"/>
<br></br>
For thining and applying burn-in you can change ```gibbs_sampling``` function in ```sample_ising.py```.

## Example

For W as below, <img src="https://latex.codecogs.com/svg.latex?u=(0,0,0,0,0,0,0)"/> and ```n=10,000```, energy of samples plotted:
<br></br>
<img src="https://latex.codecogs.com/svg.latex?W=\begin{bmatrix}%200%20&%20-1%20&%200%20&%200%20&%200%20&%200%20&%200%20\\-1%20&%200%20&%201.5%20&%201%20&%200%20&%200%20&%200\\0%20&%201.5%20&%200%20&%200%20&%201.5%20&%202%20&%20-2\\0%20&%201%20&%200%20&%200%20&%200%20&%200%20&%200%20\\0%20&%200%20&%201.5%20&%200%20&%200%20&%200%20&%200%20\\0%20&%200%20&%202%20&%200%20&%200%20&%200%20&%200%20\\0%20&%200%20&%20-2%20&%200%20&%200%20&%200%20&%200%20\\%20\end{bmatrix}"/>
<br></br>
<p align="center">
<img width="576" alt="energy-samples" src="https://user-images.githubusercontent.com/7484808/46257495-7ed19300-c4c7-11e8-8f90-8473b4b8b946.png">
</p>

