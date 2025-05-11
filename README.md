Geo Routing Backend

Flask + Python API for a geolocation and routing web app.  
Handles address lookup and calculates driving routes between two locations.

Features

-   Converts place names (e.g. "Freiburg") into GPS coordinates
-   Calculates car routes between coordinates using OpenRouteService
-   Returns distance and estimated duration
-   CORS-enabled for frontend integration (e.g. React)
-   Lightweight and easy to extend

APIs Used

-   Nominatim (OpenStreetMap) for address-to-coordinate conversion
-   OpenRouteService for route calculation between two points

Tech Stack

-   Python 3.8+
-   Flask
-   requests (for external API calls)
-   flask-cors (for cross-origin support)
-   python-dotenv (for loading API keys from environment variables)
