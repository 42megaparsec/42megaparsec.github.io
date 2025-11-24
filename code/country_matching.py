

def map_keys(data, key_map):
    if isinstance(data, dict):
        return {
            key_map.get(k, k): map_keys(v, key_map)
            for k, v in data.items()
        }
    else:
        return data

country_mapping = {

    "United Kingdom": "UK",

    "South Korea": "South Korea",
    "Republic of Korea": "South Korea",
    "Rep. of Korea": "South Korea",
    "Korea, South": "South Korea",

    "Ivory Coast": "Ivory Coast",
    "Cote d'Ivoire": "Ivory Coast",
    "Côte D'Ivoire": "Ivory Coast",
    "Côte d'Ivoire": "Ivory Coast",

    "Democratic Republic of the Congo": "Democratic Republic of the Congo",
    "Dem. Rep. Congo": "Democratic Republic of the Congo",
    "D.R. Congo": "Democratic Republic of the Congo",
    "Dem. Rep. of the Congo": "Democratic Republic of the Congo",
    "Congo, Rep." : "Democratic Republic of the Congo",

    "Republic of the Congo": "Republic of the Congo",
    "Republic of Congo": "Republic of the Congo",
    "Congo": "Republic of the Congo",

    "Russia": "Russia",
    "Russian Federation": "Russia",

    "Myanmar": "Myanmar",
    "Burma/Myanmar": "Myanmar",

    "United States of America": "USA",
    "USA": "USA",
    'United States': "USA",

    "Czechia": "Czechia",
    "Czech Republic": "Czechia",

    "Türkiye": "Türkiye",
    "Turkiye": "Türkiye",
    "Turkey": "Türkiye",

    "Vietnam": "Vietnam",
    "Viet Nam": "Vietnam",

    "Gambia": "Gambia",
    "The Gambia": "Gambia",

    "Tanzania": "Tanzania",
    "United Republic of Tanzania": "Tanzania",
    "United Rep. of Tanzania": "Tanzania",

    "Cabo Verde": "Cape Verde",
    "Central African Rep.":"Central African Republic",
    "Lao People's Democratic Republic":"Laos",
    "Lao People's Dem. Rep.": "Laos",
    "Venezuela, Bolivarian Republic": "Venezuela",

    "Bolivia (Plurinational State of)": "Bolivia",

    "Bosnia Herzegovina": "Bosnia and Herzegovina",
    "Bosnia-Herzegovina": "Bosnia and Herzegovina",

    "Other Asia, nes" : "Taiwan",

    "China, Hong Kong SAR" : "Hong Kong",

    "Rep. of Moldova": "Moldova"
}