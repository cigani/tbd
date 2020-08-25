<template>
  <div class="container">
    <v-toolbar
      dark
      color="teal">
      <v-toolbar-title>Substrate</v-toolbar-title>
      <v-autocomplete
        v-model="substrateSelect"
        :loading="loadingSubstrate"
        :items="substrateItems"
        :search-input.sync="substrateSearch"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="Substrate"
        solo-inverted
      ></v-autocomplete>
      <v-toolbar-title>Additive</v-toolbar-title>
      <v-autocomplete
        v-model="additiveSelect"
        :loading="loadingAdditive"
        :items="additiveItems"
        :search-input.sync="additiveSearch"
        cache-items
        class="mx-4"
        flat
        hide-no-data
        hide-details
        label="Additive"
        solo-inverted
      ></v-autocomplete>
    </v-toolbar>
    <v-alert> {{ substrateSearch }} -- {{ additiveSearch }} </v-alert>
    <line-chart
      v-if="loaded"
      :datasets="displayedDatasets"
      :options="$options.options"
      :labels="labels"/>
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
    loadingSubstrate: false,
    loadingAdditive: false,
    substrateItems: [],
    substrateSearch: null,
    substrateSelect: null,
    substrates: [],
    additiveItems: [],
    additiveSearch: null,
    additiveSelect: null,
    additives: [],
    flavorQmids: {'Menthol': ['76', '12', '44']},

  }),
  watch: {
    substrateSearch(val) {
      val && val !== this.substrateSelect && this.substrateQuery(val)
    },
    additiveSearch(val) {
      val && val !== this.additiveSelect && this.additiveQuery(val)
    },
  },


  computed: {
    ...mapState(["flavors"]),
    displayedDatasets() {
      if (this.additiveSearch in this.flavorQmids) {
        console.log("Additive", this.additiveSearch)
        let ff = []
        this.flavorQmids[this.additiveSearch].forEach(function (item, index) {
          ff.push("QMID(m:" + item + ")/A")
        });
        let filt = this.datasets.filter(
          function (e) {
            return this.indexOf(e.label) >= 0;
          },
          ff
        );
        filt.forEach(function (item, index){
          let colorIndex = index % filt.length;
          let color = Accent8[colorIndex];
          console.log(color, colorIndex, index)
          item["backgroundColor"] = helpers.color(color).alpha(0.3).rgbString()
        });
        return filt
      }
      if (this.datasets) {
        let basic = ["Mass/%", "Temp./°C"]
        return this.datasets.filter(
          function (e) {
            return this.indexOf(e.label) >= 0;
          },
          basic
        )
      }
    }
    ,

  },

  props: {},
  methods: {
    ...mapActions(["flavors/getSpectrum"]),
    ...mapActions(["flavors/getSubstrates"]),
    ...mapActions(["flavors/getAdditives"]),
    get_options() {
      return {
        fillAlpha: 0.1,
        responsive: true,
        tooltips: {
          mode: 'nearest'
        },
        color: function (context) {
          var index = context.dataIndex;
          var value = context.dataset.data[index];
          return value < 0 ? 'red' :  // draw negative values in red
            index % 2 ? 'blue' :    // else, alternate values in blue and green
              'green';
        },
        legend: {
          position: 'bottom',
        },
      }
    },
    substrateQuery(v) {
      this.loadingSubstrate = true
      // Simulated ajax query
      setTimeout(() => {
        this.substrateItems = this.substrates.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loadingSubstrate = false
      }, 200)
    },
    additiveQuery(v) {
      this.loadingAdditive = true
      // Simulated ajax query
      setTimeout(() => {
        this.additiveItems = this.additives.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loadingAdditive = false
      }, 500)
    },

  },

  async created() {
    this.loaded = false
    await this.$store.dispatch("flavors/getSubstrates")
    await this.$store.dispatch("flavors/getAdditives")
    this.substrates = this.$store.state.flavors.substrates
    this.additives = this.$store.state.flavors.additives
    let spectrum = this.$route.params.spectrumId
    await this.$store.dispatch("flavors/getSpectrum", spectrum)
    let d = this.$store.state.flavors.spectrum
    this.datasets = []
    let colorId = 0
    for (const [key, value] of Object.entries(d)) {
      if (colorId === Accent8.length) {
        colorId = 0
      }
      let obj = {
        label: key,
        data: value.map(Number),
        backgroundColor: helpers.color(Accent8[colorId]).alpha(0.3).rgbString(),
        fillAlpha: 0.1
      }
      this.datasets.push(obj)
      colorId += 1
    }
    this.labels = d['Time/min']
    this.options = this.get_options()
    this.loaded = true
  },

}
</script>

<style scoped>

</style>
