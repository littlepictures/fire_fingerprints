# CLIP - Fire Fingerprints <img style="float: right;" src="https://raw.githubusercontent.com/trevalabs/.github/main/logos/trevelabs_logo.png" width="180">
<hr>

## TrevaLabs
 
[TrevaLabs](https://www.TrevaLabs.com) is a collective of climate data visualisation creatives in Europe, brought together by the desire to make a big impact with little pictures. Its mission is to rapidly create little pictures of climate for maximal human impact, and the vision is to reach every European by the end of decade with a little picture on Climate.

## Background on this CLIP
Europe has a diverse and complex history of wildfires, with different regions and countries experiencing unique patterns of fire activity. In the Mediterranean region, for example, wildfires are a recurrent threat, with high frequency during the hot and dry summer months. In Portugal, extensive areas of forest and rural land have been affected by wildfires, leading to ecological and economic impacts. In Northern Europe on the other hand, wildfires are less frequent but still occur, often associated with periods of prolonged drought and heatwaves. 

The unique patterns of wildfire activity in Europe create distinct fingerprints in satellite data that allow scientists to track and analyze burned areas over time. This was the underlying idea of the little picture shown below: Using data ranging from the early 2000s up to 2020 each horizontal line symbolizes  the share of burned area over the complete timespan. For Example 22% percent of the area burned in Norway between 2001 and 2020 did so in 2003.

## Data Sources

The CLIP uses the following datasets:

- [ESA Fire CCI: MODIS Fire_cci Burned Area Pixel product, version 5.1](https://catalogue.ceda.ac.uk/uuid/58f00d8814064b79a0c49662ad3af537), 
  Cate dataset identifier: `esacci.FIRE.mon.L4.BA.MODIS.Terra.MODIS_TERRA.v5-1.grid`.
- [cate.ds.data.countries/countries-110m.geojson](https://github.com/CCI-Tools/cate/blob/master/cate/ds/data/countries/countries-110m.geojson) 
  country polygons provided as public domain from [Natural Earth](https://www.naturalearthdata.com/).

## Data Preparation

### Description

Data preparation comprises the following steps:

* Opening the Fire CCI dataset `esacci.FIRE.mon.L4.BA.MODIS.Terra.MODIS_TERRA.v5-1.grid`.
* Opening the countries GeoJSON dataset `cate.ds.data.countries/countries-110m.geojson` 
* Select European countries Features from countries dataset.
* Use European countries to spatially subset the Fire dataset.
* Generate annual sums of burned areas of the Fire dataset.
* Group the annual Fire dataset by country codes.
* Generate the sums of burned areas for each country.
* Put burned area sums in a data frame and save a CSV files 
  `data/ba-europe-countries.csv` and the cumulative sums in 
  `data/ba-europe-countries-cumsums.csv`. The units are square meters.

### One-time script setup

If you do not have a Cate account yet, please visit [Cate App](https://cate.climate.esa.int/), select **Cate Cloud Service** and register. 
Using the Cate credentials, login to the [Cate JupyterLab](https://cate-lab.brockmann-consult.de/). 
From the JupyterLab's **Launcher**, open a **Terminal** window and type

```bash
cd ~/work
git clone https://github.com/trevalabs/pytrevalabs.git
git clone https://github.com/trevalabs/clip_05_burning_lands.git
```

Note you can also use the JupyterLab's **Git** extension (left side bar) to clone the repos.

### Running the script

In JupyterLab's **File Browser** navigate to `/clip_05_burning_lands/scripts/dataprep` and open
the Notebook [extract-burned-areas.ipynb](scripts/dataprep/extract-burned-areas.ipynb) and run it.

To stay in sync with the repos, open a **Terminal** window and

```bash
cd ~/work/pytrevalabs
git pull --rebase
cd ~/work/clip_05_burning_lands
git pull --rebase
```

Note you can also use the JupyterLab's **Git** extension (left side bar) to update the repos.

## Creating Visualizations

Creating the visualizations comprises the following steps:

* save the ba-europe-countries.csv file and the jupyter notebook named treva_labs_clip_fire_fingerprints.ipynb from the scripts folder into a location of your choice
* run the jupyter notebook named treva_labs_clip_fire_fingerprints.ipynb from the scripts folder
* the notebook iterates over the csv and saves two altair visualizations per country into an output folder
* the notebook can be run locally or on hosted services like Google Colab
* the resulting visualizations are saved as html files according to their country names

## CREDITS & LICENSE
- Idea by: [Ubilabs](https://www.ubilabs.com/)
- Processing Scripts by: [Brockmann Consult](https://climate.esa.int/)
- Visualization by: [Ubilabs](https://www.ubilabs.com/)

The code in this repository is published under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/)
