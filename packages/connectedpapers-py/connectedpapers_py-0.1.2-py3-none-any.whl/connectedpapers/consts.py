import os

# CONNECTED_PAPERS_REST_API = os.environ.get(
#     "CONNECTED_PAPERS_REST_API", "http://localhost:8002"
# )
CONNECTED_PAPERS_REST_API = os.environ.get(
    "CONNECTED_PAPERS_REST_API", "https://rest.connectedpapers.com"
)

TEST_TOKEN = "TEST_TOKEN"
ACCESS_TOKEN = os.environ.get("CONNECTED_PAPERS_API_KEY", TEST_TOKEN)
