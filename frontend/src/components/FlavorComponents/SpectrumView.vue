<template>
  <div class="container">
    <v-toolbar
      dark
      color="teal">
      <!--      <v-toolbar-title>Substrate</v-toolbar-title>-->
      <!--      <v-autocomplete-->
      <!--        v-model="substrateSelect"-->
      <!--        :loading="loadingSubstrate"-->
      <!--        :items="substrateItems"-->
      <!--        :search-input.sync="substrateSearch"-->
      <!--        cache-items-->
      <!--        class="mx-4"-->
      <!--        flat-->
      <!--        hide-no-data-->
      <!--        hide-details-->
      <!--        label="Substrate"-->
      <!--        solo-inverted-->
      <!--      ></v-autocomplete>-->
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
    <v-alert v-if="loaded"> {{ meta.SAMPLE }}</v-alert>
    <line-chart
      v-if="loaded"
      :datasets="displayedDatasets"
      :options="$options.options"
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

const options = {
  responsive: true,
  legend: {
    display: true
  },
  tooltips: {
    mode: 'nearest'
  },
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true
      }
    }]
  }
}


export default {
  name: "spectrums",
  components: {LineChart},
  options,
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
    additiveQmids: null,
    meta: null,
    basic: ["Mass/%", "Temp./°C"],
    datasets: []
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
      if (this.additiveSearch in this.additiveQmids) {
        let filt = this.datasets.filter(
          function (e) {
            return this.indexOf(e.label) >= 0;
          },
          this.additiveQmids[this.additiveSearch]
        );
        filt.forEach(function (item, index) {
          let color = Accent8[index % filt.length];
          item["backgroundColor"] = helpers.color(color).alpha(0.3).rgbString()
        });
        return filt
      }
      if (this.datasets) {
        let filt = this.datasets.filter(
          function (e) {
            return this.indexOf(e.label) >= 0;
          },
          this.basic
        )

        return filt
      }
    }
    ,

  },

  props: {},
  methods: {
    ...mapActions(["flavors/getSpectrum"]),
    ...mapActions(["flavors/getSubstrates"]),
    ...mapActions(["flavors/getAdditives"]),
    ...mapActions(["flavors/getQmids"]),
    additiveQuery(v) {
      this.loadingAdditive = true
      // Simulated ajax query
      setTimeout(() => {
        this.additiveItems = this.additives.filter(e => {
          return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
        })
        this.loadingAdditive = false
      }, 500)
    }
    ,
    loaddata: async function () {
      await this.$store.dispatch("flavors/getSubstrates")
      await this.$store.dispatch("flavors/getAdditives")
      await this.$store.dispatch("flavors/getQmids")
      await this.$store.dispatch("flavors/getSpectrum", this.$route.params.spectrumId)
      this.substrates = this.$store.state.flavors.substrates
      this.additives = this.$store.state.flavors.additives
      this.additiveQmids = this.$store.state.flavors.qmids
      this.meta = this.$store.state.flavors.meta

    }
    ,
  },


  async created() {
    await this.loaddata();
    let d = this.$store.state.flavors.spectrum
    let colorId = 0
    this.labels = d['Time/min']
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
    this.loaded = true
  },


}
</script>

<style scoped>

</style>
