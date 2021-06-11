# Unearthing Other Worlds

<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/Screen%20Shot%202021-06-10%20at%202.53.05%20PM.png" width ="1000" height=500>



## Background
Exoplanets are planets outside of our solar system.  The first exoplanet discovery was in 1989 and since the community has discovered many more within our galaxy as more robust detection methods are established and applied.

## Exoplanet Data
The data are available on the NASA Exoplanet Archive, both through an <a href="https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html">API</a> and an <a href="https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars">interactive format</a>.  The data used for this exploration is included in the data directory, however, the get_data script in the src directory can be used to retrieve and save the data explored by this code.

The dataset contains 4401 confirmed exoplanets from a variety of detection sources.  The discoveries span 1989 - 2021 and contain numerous parameters about the planets, including but not limited to:

<li>Planet Name</li>
<li>Discovery Method</li>
<li>Discovery Facility</li>
<li>Planet Radius</li>
<li>Distance to Planet's Solar System</li>
<li>Orbital Period</li>
<li>Equilibrium Temperature</li>

## Exploratory Data Analysis

### Data Cleaning
The dataset retrieved from the exoplanet archive for this exploration was largely clean.  For some parameters, like planet radius and equilibrium temperature, there were records with no entry, so the only cleaning that needed to occur was to omit these entries when plotting or calculating means.  The features with missing values are noted in the EDA notebook.

### Visualizations

#### Detection Methods
The first element of this dataset that I explored was the breakdown of discovery methods across the confirmed exoplanets.  The bar chart, below, shows that the clear leader in terms of number of detections is the transit method.
<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/detection_bar_chart.png">

Diving a little deeper, I was curious to investigate applications of the detection methods over time.  As can be seen in the previous plot, there are a number of detection methods but only a handful of them surpass 50 detections.  The next plot features the four methods that exceed this threshold, illustrating their contributions to exoplanet detections over time.

<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/detections_per_year_by_method.png">

A number of interesting points can be gleaned from this plot:
<li> The first exoplanet detection was in 1989.  It was identified with the radial transit method</li>
<li> Not only is the transit method the leading method, but in recent years (particularly 2014 and 2016), it has yielded the largest contributions to exoplanet detections.</li>
<li> Imaging and microlensing are more recent methods that have come on to the scene.</li>

#### Planetary Characteristics

To get a sense of some planetary characteristics, the next series of plots show the galactic position of the exoplanets as well as the relative size (in terms of planet radius relative to Earth's).
<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/galactic_plot.png">

From this plot we can see that the detections largely span the different directions of the galaxy relative to Earth.  We can also see that the size of the planets ranges from ones as small as the size of the Moon to ones almost as large as our Sun.  Centered near approximately 12 degrees latitude, and 70 degrees longitude, there is a very dense cluster of exoplanet detections.  The next figure zooms in on this region.

<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/curious_cluster_zoom.png">

It turns out that the overwhelming majority of the detections in this cluster were identified by the Kepler space telescope.  In fact, in contains all of the detections from the first Kepler mission.  This mission kept the telescoped fixed on the same area of the galaxy for several years.  It was imperative to maintain the same field of view from the telescope for a long duration of time in order to observe any fleeting dips in brightness from host stars as planets transited betweeen the star and the telescope.  Due to this fixed pointing of the telescope, you can even observe a distinct hashtag or grid pattern between the detections.  This pattern matches the gridded focal plane array used for the Kepler space telescope, pictured in the next image.

<p align="center">
<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/286257main_07-3348d1-kepler-4x3_226-170.jpeg">
</p>

Next, I wanted to get a better sense of how the planet size and position in the galaxy varied over time.  The next three plots illustrate these parameters for detections across (roughly) 3 decades.

<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/galactic_by_decade_2.png">

Progressing from left to right, from the first decade of detections to the last, it can be observed that the first 2 decades consisted of exoplanet detections that were much larger than Earth.  Roughly, these planets are mostly on the order of magnitude of Jupiter-sized planets.  However, in the last decade, we can see that many more planets in the realm of Earth's size (and even smaller) were detected.

Finally, I explored a few additional paramters:  the number of stars in the planet's solar system, as well as the total number of planets.

<img src="https://github.com/jstodd867/unearthing-other-worlds/blob/main/images/solar_system_features.png">

Surprisingly, you can see that most of the planets are the only ones in their solar system, while systems like ours with 8 planets are the minority.

## Hypothesis Testing

### Hypothesis Test 1:  Is the mean planet radius detected from 1989 - 2010 greater than that over the period 2011 - 2021?
<p align="center">
H<sub>0</sub>:   &mu;<sub>1989-2010</sub> = &mu;<sub>2011-2021</sub><br>
H<sub>A</sub>:   &mu;<sub>1989-2010</sub> > &mu;<sub>2011-2021</sub><br>
&alpha; = 0.05
</p>

The results of the Welsh's t-test produced a p-value of approximately 0, which indicates that we can reject the null hypothesis in favor of the alternate hypothesis that the mean planet radius over the more recent time period is lower.
## Conclusions
<li>The Transit method has emerged as the largest contributor to exoplanet detections</li>
<li>Ability to detect smaller planets has improved over time</li>
