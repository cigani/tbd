<template>
  <div class="container">
    <v-toolbar
      dark
      color="teal">
      <v-toolbar-title>Compound</v-toolbar-title>
      <v-autocomplete
        v-model="additiveSelect"
        :items="additiveItems"
        :search-input.sync="additiveSearch"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="Search for Ions"
        solo-inverted
      ></v-autocomplete>
      <v-btn icon @click="$router.push({name:'flavors'})"><v-icon >fa-database</v-icon></v-btn>
    </v-toolbar>
    <v-btn
      outlined
      center
      block
      color="teal"
      @click="resetGraph"
      v-if="loaded"> {{ flavors.meta.SAMPLE }}
    </v-btn>
    <line-chart
      v-if="loaded"
      :datasets="displayedDatasets"
      :options="options"
      :labels="labels"
    ></line-chart>
  </div>
</template>

<script>
import {mapActions, mapState} from "vuex";
import LineChart from "../Chart/LineChart"
import Chart from 'chart.js'

var helpers = Chart.helpers;
const color = ['#9e0142', '#d53e4f', '#f46d43', '#fdae61', '#fee08b', '#ffffbf', '#e6f598', '#abdda4', '#66c2a5', '#3288bd', '#5e4fa2']
const Accent8 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666']


export default {
  name: "spectrums",
  components: {LineChart},
  data: () => ({
    loaded: false,
    additiveItems: [],
    additiveSearch: null,
    additiveSelect: null,
    additiveQmids: null,
    meta: null,
    temp: null,
    time: null,
    basic: ["Mass/%", "Temp./°C"],
    datasets: [],
    options: {
      responsive: true,
      legend: {
        display: true
      },
      tooltips: {
        mode: 'nearest'
      },
      scales: {
        xAxes: [{
          id: 'temp',
          display: 'auto',
          scaleLabel: {
            display: true,
            labelString: "Temperatrue (°C)"
          }
        },
          {
            id: 'time',
            display: 'auto',
            scaleLabel: {
              display: true,
              labelString: "Time (min)"
            }
          }],
        yAxes: [{
          id: "Temp./°C",
          display: 'auto',
          position: 'right',
          scaleLabel: {
            display: true,
            labelString: 'Temperature (°C)'
          },
          ticks: {
            beginAtZero: false,
            min: 0
          },
        }, {
          id: "qmid",
          display: 'auto',
          position: 'right',
          scaleLabel: {
            display: true,
            labelString: 'A'
          },
          ticks: {
            beginAtZero: false,
            min: 0
          }
        }, {
          id: "Mass/%",
          display: 'auto',
          position: 'left',
          scaleLabel: {
            display: true,
            labelString: 'Mass (%)'
          },
          ticks: {
            beginAtZero: false,
          }
        }]
      }
    }

  }),
  watch: {
    additiveSearch(val) {
      val && val !== this.additiveSelect && this.additiveQuery(val)
    },
  },


  computed: {
    ...mapState(["flavors"]),
    displayedDatasets() {
      if (this.additiveSearch in this.additiveQmids) {
        let i = 0
        this.labels = this.temp
        return this.datasets.filter(
          function (e) {
            if (this.indexOf(e.label) >= 0) {
              let color = Accent8[i % this.length];
              if (e.label.includes("QMID")) {
                e["backgroundColor"] = helpers.color(color).alpha(0.3).rgbString()
                e.yAxisID = 'qmid'
              } else {
                e["backgroundColor"] = helpers.color(color).alpha(0.05).rgbString()
                e.fillAlpha = 0.01
              }
              e.xAxisID = 'temp'
              i++
            }
            return this.indexOf(e.label) >= 0;
          },
          this.additiveQmids[this.additiveSearch] + ['Mass/%'] + ['QMID(m:164)/A']
        )
      }
      if (this.datasets) {
        let i = 0
        return this.datasets.filter(
          function (e) {
            if (this.indexOf(e.label) >= 0) {
              let color = Accent8[i % this.length];
              e["backgroundColor"] = helpers.color(color).alpha(0.3).rgbString()
              e.yAxisID = e.label
              e.xAxisID = 'time'
              i++

            }
            return this.indexOf(e.label) >= 0;
          },
          this.basic
        )
      }
    },
  },

  props: {},
  methods: {
    ...mapActions(["flavors/getSpectrum"]),
    ...mapActions(["flavors/getQmids"]),
    additiveQuery(v) {
      this.additiveItems = Object.keys(this.additiveQmids).filter(e => {
        return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
      })
    }
    ,
    loaddata: async function () {
      await this.$store.dispatch("flavors/getQmids")
      await this.$store.dispatch("flavors/getSpectrum", this.$route.params.spectrumId)
      this.additiveQmids = this.$store.state.flavors.qmids



    },

    makeDatasets: function () {
      let d = this.$store.state.flavors.spectrum

      this.time = d['Time/min'].map(e => e.replace(/^0+(\d)|(\d)0+$/gm, '$1$2')).map(e => e.substring(0, 5))
      this.temp = d['Temp./°C'].map(e => e.replace(/^0+(\d)|(\d)0+$/gm, '$1$2')).map(e => e.substring(0, 5))
      this.labels = this.time
      let colorId = 0
      for (const [key, value] of Object.entries(d)) {
        if (colorId === Accent8.length) {
          colorId = 0
        }
        let obj = {
          label: key,
          data: value.map(Number),
          backgroundColor: helpers.color(Accent8[colorId]).alpha(0.3).rgbString(),
          fillAlpha: 0.1,
          yAxisID: ''
        }
        this.datasets.push(obj)
        colorId += 1
      }
    },
    resetGraph() {
      this.additiveSearch = null
      this.additiveSelect = null
    },
  },


  async submitted() {
    await this.loaddata();
    this.makeDatasets();
    this.loaded = true
  },


}
</script>

<style scoped>

</style>
