# grafana-kasa-power-strip

## SimpleJson plugin
This datasource needs `SimpleJson` plugin to be installed in Grafana.
You can use either:
1. `grafana-cli plugins install grafana-simple-json-datasource`
2. docker: `docker run -d --name=grafana -p 3000:3000 -e "GF_INSTALL_PLUGINS=grafana-simple-json-datasource" grafana/grafana`
