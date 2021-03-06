# Ising model report


Tung D. Nguyen - Department of Physics, Wabash College, IN. 
 
Professor James Brown - Department of Physics, Wabash College, IN.


# Abstract: 
The topic of ferromagnetism has received great attentions for research and developments in science due to its exotic 
properties and many applications for generators, transformers, telephones, loudspeakers, and magnetic recording devices. 
Among those research topics, the most fundamentally pioneering model came from the work of the Ising model by 
Wilhelm Lenz. As the model covered undegraduate concepts of electrodynamics and thermal physics, it has 
been widely taught and researched by undergraduate faculties and students interested in such courses. 
One framework of interest we chose for this report comes from the book ”Thermal Physics” by 
Daniel V. Schroeder. Specifically, we follow the theoretical development of this book to code, simulate, and visualize the ferromagnetism behavior of the Ising Model. As a result, our codes effetively shows great consistency with the theoretical Ising model. Here we shortly describe our implementation of this model on Python3, and additional information is attached inside the folder "report".


# 1 Procedures for the Ising model on 2D:
# 1.1 Metropolis algorithm:

The Metropolis Algorithm is summarized as the following from [3]:

• Set up a lattice size N and the desired temperature T under consideration
• Set the spins inside the lattice to be one-half up and one-half down under random number 0.5.
• Start with a random state (i,j) in the lattice.

• Define the function <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;U(i,j)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;U(i,j)" title="\Delta U(i,j)" /></a> to calculate the temperature difference when changing the direction of the spin at position (i,j).

• Make an iteration loop with the duration <a href="https://www.codecogs.com/eqnedit.php?latex=100*\textrm{size}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?100*\textrm{size}^2" title="100*\textrm{size}^2" /></a> and choose an arbitrary i and j to calculate the temperature difference. 

If <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;U&space;<&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;U&space;<&space;0" title="\Delta U < 0" /></a> we change the direction of the spin (sign of s[i,j]). If <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;U&space;\geq&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;U&space;\geq&space;0" title="\Delta U \geq 0" /></a>, we only change the direction of the spin under the probability <a href="https://www.codecogs.com/eqnedit.php?latex=p&space;=&space;e^{-\frac{\Delta&space;U}{T}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p&space;=&space;e^{-\frac{\Delta&space;U}{T}}" title="p = e^{-\frac{\Delta U}{T}}" /></a>.

• Assign two different colors to both the up-spin and down-spin in the lattice.

From the demonstration in [3] about the algorithm, the probability of having diffrent energy values is non-negative and effectively 
maintains the ratio of Boltzmann factor of the two changing states. This means that for any two states 1 and 2, being different 
by only the spinning direction, the ratios of changing from 1 to 2 and back from 2 to 1 are balanced together and maintain the 
Boltzmann probabilities. The algorithm for these phenomena is in the file ”First_code_on_the_Ising_model.py”


# 1.2 The correlation function:

The correlation function over a distance r is calculated by the formula: <a href="https://www.codecogs.com/eqnedit.php?latex=c(r)&space;=&space;\bar{s_i}\bar{s_j}&space;-&space;\bar{s_j}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c(r)&space;=&space;\bar{s_i}\bar{s_j}&space;-&space;\bar{s_j}^2" title="c(r) = \bar{s_i}\bar{s_j} - \bar{s_j}^2" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=s_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i" title="s_i" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=s_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_j" title="s_j" /></a> is randomly chosen across the lattice's grids, and r is the shortest over 9 distances between <a href="https://www.codecogs.com/eqnedit.php?latex=s_i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i" title="s_i" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=s_j" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_j" title="s_j" /></a> by the periodic boundary conditions. To set up the algorithm, we use the random distribution library Random to set up two arbitrary pairs of grids. After we iterate among <a href="https://www.codecogs.com/eqnedit.php?latex=100*\textrm{size}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?100*\textrm{size}^2" title="100*\textrm{size}^2" /></a>

then we calculate the shortest distances, with the formulas are given
in the file ”isingmodelgrahics.py”. Then, for each j, the part <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{s_i}\bar{s_j}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{s_i}\bar{s_j}" title="\bar{s_i}\bar{s_j}" /></a> of
the function and the part <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{s_j}^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{s_j}^2" title="\bar{s_j}^2" /></a> are added over each iteration and then averaged altogether. Finally, we represent the indexes by setting up the command colors in the libraries matplotlib.pyplot and matplotlib.

# 1.3 The correlation and temperature graph:

From the Metropolis algorithm and the correlation function, we use those two packages to find out the correlation length of the corresponding temperature. We incorporate those characteristics into coding the file ”isingmodelgraphics.py” and extract 3 functions from the new file ”correlation length - temperature.py.” Direcly calculating all temperature ranges results in being the most extensive piece of computation of this projecr, as the iteration requires a lot of steps that could take a couple of days to produce the results from a Macbook with Processor 2.9 GHz - Intel Core i7 and Memory of 12 GB - 1600 MHz - DDR3. So, the processing are divided from 3 different temperature ranges, one from 0.5 to 1.5, from 1.5 to 2.5, and from 2.5 to 3.5, with the ranging step is 0.05, and the resulting data are combined in a text file name ”list 0.5 - 3.5.txt.” In each temperature, we calculate the quadratic difference of the correlation distance function over each pair of spins of the lattice. For each time, we track down the data in the correlation function to obtain the closest lower bond of 1/e. The final closest number was averaged over 10 times the size.


# References
[1] Thomas Ising, Reinhard Folk, Ralph Kenna, Bertrand Berche, Yurij Holo- vatch. The Fate of Ernst Ising and the Fate of his 
Model. arXiv:1706.01764 [physics.hist-ph], 2017.

[2] David J. Griffith. Introduction to electrodynamics. Cambridge University Press, 2017.

[3] Daniel V. Schroeder. An Introduction to Thermal Physics. Pearson, 1st edition, 1999.

[4] Mark Newman. Computational Physics in Python. CreateSpace Independent Publishing Platform (November 7, 2012).

[5] Wei Cai. ME346A - Introduction to Statistical Mechanics - Handout 12. Ising Model. Stanford University, winter 
2011 CreateSpace Independent Publishing Platform. http://micro.stanford.edu/~caiwei/me334/Chap12_Ising_Model_v04.pdf.

[6] Tom Kennedy. University of Arizona, 2008. The Ising model. https://www.math.arizona.edu/tgk/541/chap1.pdf
