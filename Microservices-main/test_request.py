import requests
import json

# Define the base URL of your Flask application
base_url = 'http://localhost:5000'

# Example of sending a GET request to the /info endpoint
info_response = requests.get(f'{base_url}/info')
print('Info Response:', info_response.json())

# Example of sending a GET request to the /health endpoint
health_response = requests.get(f'{base_url}/health')
print('Health Response:', health_response.text)


url = "http://127.0.01:5000/predict"
#url = "http://127.0.01:5000/health"
#url = "http://127.0.01:5000/info"

data = [
{"radius_mean":12.47,
    "texture_mean":18.6,
        "perimeter_mean":81.09,
            "area_mean":481.9,
                "smoothness_mean":0.09965,
                    "compactness_mean":0.1058,
                        "concavity_mean":0.08005,
                            "concave points_mean":0.03821,
                                "symmetry_mean":0.1925,
                                    "fractal_dimension_mean":0.06373,
                                        "radius_se":0.3961,"texture_se":1.044,
                                            "perimeter_se":2.497,"area_se":30.29,
                                                "smoothness_se":0.006953,
                                                    "compactness_se":0.01911,
                                                        "concavity_se":0.02701,
                                                            "concave points_se":0.01037,
                                                                "symmetry_se":0.01782,
                                                                    "fractal_dimension_se":0.003586,
                                                                        "radius_worst":14.97,
                                                                            "texture_worst":24.64,
                                                                                "perimeter_worst":96.05,
                                                                                    "area_worst":677.9,
                                                                                        "smoothness_worst":0.1426,
                                                                                            "compactness_worst":0.2378,
                                                                                                "concavity_worst":0.2671,
                                                                                                    "concave points_worst":0.1015,
                                                                                                        "symmetry_worst":0.3014,
                                                                                                            "fractal_dimension_worst":0.0875}
]
headers = {
    "Content-Type" : "application/json"
}
response = requests.post(url,data = json.dumps(data),headers = headers)
#response = requests.get(url)
print(response.text)