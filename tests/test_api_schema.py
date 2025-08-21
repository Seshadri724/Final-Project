from api.schemas import HouseFeatures

def test_schema_ok():
    payload = HouseFeatures(
        longitude=-122.05,
        latitude=37.37,
        housing_median_age=27.0,
        total_rooms=3885.0,
        total_bedrooms=661.0,
        population=1537.0,
        households=606.0,
        median_income=6.6085
    )
    assert payload.median_income > 0
