<template>
  <div class="home">
    <md-layout :md-gutter="8">
        <md-layout md-flex="33" md-column v-for="precinct in all_precincts" :key="precinct[0]">
            <md-card>
                <md-card-header>
                    <div class="md-title">Precinct: {{precinct[0]}}</div>
                </md-card-header>
                <md-card-media>
                    <highcharts :options="genPieOptions('Votes', precinct)"></highcharts>
                </md-card-media>
            </md-card>
        </md-layout>

        <md-layout md-flex="33" md-column v-if="ajaxRequest">
            <md-card>
                <md-card-header>
                    <div class="md-title">Loading...</div>
                </md-card-header>
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
      all_precincts: []
    }
  },
  methods: {
    loadPie: function (event) {
      this.ajaxRequest = true
      this.$http.get(
        config.API_LOCATION + '/pieme'
        ).then(response => {
          this.ajaxRequest = false
          this.all_precincts = response.body
        }, response => {
          console.log('Stuff broke')
          this.ajaxRequest = false
        })
    },
    genPieOptions: function (seriesName, data) {
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
          'data': [data[1], data[2]]
        }]
      }
    }
  },
  mounted: function () {
    // Mounted == onready
    this.loadPie()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.home {
  padding-bottom: 15px;
  padding-top: 15px;
}

.md-column {
    padding-bottom: 15px;
}

.md-card-media {
    overflow: hidden;
}
</style>
