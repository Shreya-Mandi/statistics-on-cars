import pandas as pd
import basic_profile
import cars
import dates
import json

# define the number of profiles to generate
NUM=1000

if __name__ == '__main__':
    ## generating the df
    df_basic_profiles=basic_profile.Profile(NUM).profiles
    df_cars=cars.Cars(NUM).cars
    df_dates=dates.Dates(NUM).dates

    # merging the files
    df_merged = pd.merge(df_basic_profiles,df_cars , left_index=True, right_index=True) # The first merge should not be outer merge.
    df_merged = pd.merge(df_merged,df_dates , left_index=True, right_index=True,how='outer')

    filename="final"
    df_merged.to_csv(f'{filename}.csv', index=False)

    # generating the metadata json

    # col data
    col_dicts = {}
    for col in df_merged.columns:
        col_dicts[col] = str(df_merged[col].dtype)

    # Data to be written
    data_name="car+profile+dates-data"
    dictionary = {
        "name": f"{data_name}",
        "#rows": df_merged.shape[0] ,
        "#columns": df_merged.shape[0],
        "columns": col_dicts
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open(f"{data_name}metadata.json", "w") as outfile:
        outfile.write(json_object)


