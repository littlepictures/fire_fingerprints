# little picture - fire fingerprints

## Background on this little picture
_inspired by #showyourstripes we represent annual burned area for Ireland_

Monitoring wildfires from space is crucial for understanding their impact on climate, including the release of greenhouse gases &amp; aerosols that influence the Earth system.

Satellites, such as Copernicus Sentinel-2 &amp; -3 capture optical, infrared &amp; thermal data globally, over decades to map &amp; assess fire-affected regions.
This data-driven approach enhances climate understanding, identifies long-term trends and improves the models used to predict future change and prepare for future fire events. The graphic represents the annual burned area across Ireland between 2001 to 2020.

https://climate.esa.int/en/little-pictures-gallery/Fire-fingerprints/

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
