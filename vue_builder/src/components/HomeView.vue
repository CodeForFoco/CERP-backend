<template>
  <div class="home">
    <md-layout :md-gutter="8">

        <md-layout md-flex="50" md-column>
            <md-card>
                <md-card-header>
                    <div class="md-title">Options</div>
                </md-card-header>
                <md-card-content>
                  <md-input-container>
                    <label for="selected_option">Options</label>
                    <md-select name="selected_option" id="selected_option" v-model="selected_option">
                      <md-option value="county_map">County Map</md-option>
                      <md-option value="county_map_with_pres">County Map w/ Presidential Election Heatmap</md-option>
                      <md-option value="pres_pie">Pie of '16 Election</md-option>
                    </md-select>
                  </md-input-container>
                </md-card-content>
            </md-card>
        </md-layout>

        <!-- std_map -->
        <md-layout md-flex="50" md-column v-show="selected_option === 'county_map'">
            <md-card>
                <md-card-header>
                    <div class="md-title">Lamier County precincts</div>
                </md-card-header>
                <md-card-media>
                    <div id="std_map" class="map"></div>
                </md-card-media>
            </md-card>
        </md-layout>

        <!-- heat map -->
        <md-layout md-flex="50" md-column v-show="selected_option === 'county_map_with_pres'">
            <md-card>
                <md-card-header>
                    <div class="md-title">Lamier County Presidential Election Heatmap</div>
                </md-card-header>
                <md-card-media>
                    <div id="std_map_with_pres" class="map"></div>
                </md-card-media>
            </md-card>
        </md-layout>

        <!-- All precinct pie chart -->
        <md-layout md-flex="33" md-column v-show="selected_option === 'pres_pie'">
            <md-card>
                <md-card-header>
                    <div class="md-title">2016 Presidential Election</div>
                </md-card-header>
                <md-card-media>
                    <highcharts :options="genPieOptions('Votes', presidential_pie_data)"></highcharts>
                </md-card-media>
            </md-card>
        </md-layout>
    </md-layout>
  </div>
</template>

<script>
// By importing a config obj
// we can keep track of our api location globally
import config from '../config'

export default {
  name: 'HomeView',
  data () {
    return {
      ajaxRequest: false,
      presidential_pie_data: [],
      selected_option: 'county_map'
    }
  },
  methods: {
    presidential_pie: function (event) {
      // Only load once
      if (this.presidential_pie_data.length === 0) {
        this.ajaxRequest = true
        this.$http.get(
        config.API_LOCATION + '/api/presidential/all/pie'
        ).then(response => {
          this.ajaxRequest = false
          var res = response.body
          if (res.result) {
            this.presidential_pie_data = res.data
          } else {
            console.log('Stuff broke on the server')
          }
        }, response => {
          console.log('Stuff broke')
          this.ajaxRequest = false
        })
      }
    },
    std_map: function (event) {
      /* eslint-disable no-undef */
      var oldSelectedOption = this.selected_option
      this.selected_option = 'county_map'
      mapboxgl.accessToken = 'pk.eyJ1IjoiZGVpZHlvbWVnYSIsImEiOiJjajkwaWh1b2gxaTN2MnducmFmZ2Q0NHN4In0.xSg05BL0_xFAzPOqyES2-A'
      var map = new mapboxgl.Map({
        container: 'std_map',
        style: 'mapbox://styles/mapbox/light-v9',
        center: [-105.378461, 40.655812],
        zoom: 8.2
      })

      map.on('load', function () {
        this.selected_option = oldSelectedOption
        map.addLayer({
          'id': 'lamier-county',
          'type': 'fill',
          'source': {
            'type': 'geojson',
            'data': config.API_LOCATION + '/static/VoterPrecinct.geojson'
          },
          'paint': {
            'fill-color': '#888888',
            'fill-opacity': 0.4,
            'fill-outline-color': '#222'
          }
        })

        map.on('click', 'lamier-county', function (e) {
          console.log(e)
          var precinct = e.features[0].properties.PRECINCT
          new mapboxgl.Popup()
          .setLngLat(e.lngLat)
          .setHTML('Precinct: ' + precinct + '<br> <a href="/#/precinct/' + precinct + '">Learn More</a>')
          .addTo(map)
        })
      })
      console.log('Done')
    },
    std_map_with_pres: function (event) {
      this.selected_option = 'county_map_with_pres'
      this.$http.get(
        config.API_LOCATION + '/static/VoterPrecinct.geojson'
      ).then(response => {
        var geodata = JSON.parse(response.body)
        console.log(geodata)
        this.$http.get(
          config.API_LOCATION + '/api/presidential/all/heatmap'
        ).then(response => {
          var heatdata = response.body
          console.log(heatdata)
          // Ok boys, we can now iterate over and map stuff

          /* eslint-disable no-undef */
          var oldSelectedOption = this.selected_option
          mapboxgl.accessToken = 'pk.eyJ1IjoiZGVpZHlvbWVnYSIsImEiOiJjajkwaWh1b2gxaTN2MnducmFmZ2Q0NHN4In0.xSg05BL0_xFAzPOqyES2-A'
          var map = new mapboxgl.Map({
            container: 'std_map_with_pres',
            style: 'mapbox://styles/mapbox/light-v9',
            center: [-105.378461, 40.655812],
            zoom: 8.2
          })

          var features = geodata.features
          map.on('load', function () {
            this.selected_option = oldSelectedOption
            for (var index = 0; index < features.length; index++) {
              var feature = features[index]
              var precinct = feature.properties.PRECINCT
              var color = heatdata.data[precinct]
              if (typeof color === 'undefined') {
                color = '#888888'
              }
              map.addLayer({
                'id': 'precinct-' + precinct,
                'type': 'fill',
                'source': {
                  'type': 'geojson',
                  'data': feature
                },
                'paint': {
                  'fill-color': color,
                  'fill-opacity': 0.4,
                  'fill-outline-color': '#222'
                }
              })

              map.on('click', 'precinct-' + precinct, function (e) {
                new mapboxgl.Popup()
                .setLngLat(e.lngLat)
                .setHTML('Precinct: ' + e.features[0].properties.PRECINCT)
                .addTo(map)
              })
            }
          })
        }, response => {
          console.log('Stuff broke')
        })
      }, response => {
        console.log('Stuff broke')
      })
      console.log('Done')
    },
    genPieOptions: function (seriesName, data) {
      console.log(data)
      // We'll need to convert this into a more generic pie options
      // generator.
      return {
        'chart': {
          'type': 'pie'
        },
        'title': {
          'text': ' '
        },
        'credits': {
          'enabled': false
        },
        'plotOptions': {
          'pie': {
            'innerSize': 50,
            'depth': 45,
            'dataLabels': {
              'enabled': false
            },
            'colors': ['#dc3912', '#3366cc'],
            'showInLegend': true
          }
        },
        'series': [{
          'name': seriesName,
          'data': data
        }]
      }
    }
  },
  mounted: function () {
    // Mounted == onready
    this.presidential_pie() // Show election for all county by pie
    this.std_map() // Show election for all county by pie
    this.std_map_with_pres() // Show election for all county by pie
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  padding: 15px;
}

.md-column {
    padding-bottom: 15px;
}

.md-card-media {
    overflow: hidden;
}

/* Map stuff */
.map { height: 480px; }
</style>
