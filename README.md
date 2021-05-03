# grafana-kasa-power-strip

## Setup
1. Install `SimpleJson` plugin
   This datasource needs `SimpleJson` plugin to be installed in Grafana.
   You can use either:
   1. `grafana-cli plugins install grafana-simple-json-datasource`
   2. docker: `docker run -d --name=grafana -p 3000:3000 -e "GF_INSTALL_PLUGINS=grafana-simple-json-datasource" grafana/grafana`
2. Configure Datasource in Grafana
   1. Configuration -> Data Sources -> Search for `SimpleJson`
   2. Enter URL: `localhost:5000` (or the address and port of the flask server)
3. Start the data server: `python3 server.py`

![Screenshot](https://github.com/anuragpeshne/grafana-kasa-power-strip/raw/main/powerstrip_screenshot.png "Screenshot")
