import json
from simplification.cutil import visvalingam_simplify

# GeoJSON dữ liệu đầu vào
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "California"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-124.409591, 41.998370], [-124.156605, 42.002207],
                        [-124.151412, 41.607800], [-124.329755, 41.535656],
                        [-124.541495, 41.501933], [-124.650244, 41.348394],
                        [-124.650244, 41.140835], [-124.387067, 41.141308],
                        [-124.341248, 41.043359], [-124.255933, 40.954383],
                        [-124.213628, 40.851591], [-124.126840, 40.800037],
                        [-124.115070, 40.968910], [-124.071765, 41.050299],
                        [-124.108051, 41.142204], [-124.010102, 41.359615],
                        [-124.158566, 41.520614], [-124.257062, 41.712453],
                        [-124.209280, 41.761907], [-124.305727, 41.883500],
                        [-124.341248, 42.000709], [-124.410064, 42.076801],
                        [-124.409591, 41.998370]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {"name": "Oregon"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-123.598961, 46.251454], [-123.121582, 46.292977],
                        [-122.822266, 46.088229], [-122.756348, 45.684477],
                        [-122.811279, 45.548207], [-122.904968, 45.659199],
                        [-122.966309, 45.659199], [-123.085938, 45.726906],
                        [-123.047180, 45.804423], [-123.211060, 45.913214],
                        [-123.370361, 45.926284], [-123.400574, 46.261240],
                        [-123.598961, 46.251454]
                    ]
                ]
            }
        }
    ]
}

# Hàm đơn giản hóa tọa độ bằng Visvalingam-Whyatt
def simplify_coordinates(coords, tolerance=0.01):
    return visvalingam_simplify(coords, tolerance)

# Đơn giản hóa dữ liệu GeoJSON
for feature in geojson_data["features"]:
    if feature["geometry"]["type"] == "Polygon":
        # Đơn giản hóa tất cả các vòng trong đa giác
        feature["geometry"]["coordinates"] = [
            simplify_coordinates(ring) for ring in feature["geometry"]["coordinates"]
        ]

# Lưu kết quả đơn giản hóa vào một tệp GeoJSON mới
output_file = "simplified_geojson_output.geojson"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(geojson_data, f)

print(f"Đã lưu tệp GeoJSON đã đơn giản hóa tại: {output_file}")
