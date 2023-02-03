# CLIP #05 - Burning Lands <img style="float: right;" src="https://raw.githubusercontent.com/trevalabs/.github/main/logos/trevelabs_logo.png" width="180">
<hr>

## TrevaLabs
 
[TrevaLabs](https://www.TrevaLabs.com) is a collective of climate data visualisation creatives in Europe, brought together by the desire to make a big impact with little pictures. Its mission is to rapidly create little pictures of climate for maximal human impact, and the vision is to reach every European by the end of decade with a little picture on Climate.

## Background on this CLIP
[SHORT DESCRIPTION ON WHAT THE CLIP SHOWS AND WHY IT MATTERS IN TERMS OF CLIMATE DATAVIZ (500-600 CHARACTERS)]

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
[STEP BY STEP DESCRIPTION ON WHAT THE DATA PROCESSING PROCESS. SHOULD BEGIN WITH A SHORT SUMMARY OF THE OVERALL PROCESS]

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at vestibulum nulla, ac tincidunt sem. Morbi in nisl at nisl feugiat faucibus sed eu neque. In fringilla, odio eu porttitor condimentum, tortor leo congue justo, id venenatis metus lectus sed libero. Mauris id arcu eros. Sed orci mauris, tincidunt nec ex non, eleifend pellentesque dolor. Mauris tellus ligula, tincidunt accumsan sapien accumsan, pellentesque rhoncus ex. Phasellus sollicitudin dolor eget porttitor gravida. Integer malesuada vehicula ante, ac interdum felis congue nec. Mauris in sagittis felis. 

To create a new visualization, follow these steps:
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at vestibulum nulla, ac tincidunt sem. Morbi in nisl at nisl feugiat faucibus sed eu neque. 
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at vestibulum nulla, ac tincidunt sem. Morbi in nisl at nisl feugiat faucibus sed eu neque. 
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at vestibulum nulla, ac tincidunt sem. Morbi in nisl at nisl feugiat faucibus sed eu neque. 

## CREDITS & LICENSE
- Idea by: [INSTITUTION](https://climate.esa.int/)
- Processing Scripts by: [INSTITUTION](https://climate.esa.int/)
- Visualization by: [INSTITUTION](https://climate.esa.int/)

The code in this repository is published under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/)
