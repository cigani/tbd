<template>
  <div class="container">
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
  }),

  computed: {
    ...mapState(["flavors"]),
    displayedDatasets() {
      return this.datasets.slice(0, 5)
    }
    ,

  },

  props: {},
  methods: {
    ...mapActions(["flavors/getSpectrum"]),
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

  },


  async created() {
    this.loaded = false
    let spectrum = this.$route.params.spectrumId
    await this.$store.dispatch("flavors/getSpectrum", spectrum)
    let d = this.$store.state.flavors.spectrum
    this.datasets = []
    console.log(this.$props)
    let colorId = 0
    for (const [key, value] of Object.entries(d)) {
      if (colorId === Accent8.length) {
        colorId = 0
      }
      console.log(colorId)
      let obj = {
        label: key,
        data: value.map(Number),
        backgroundColor: helpers.color(Accent8[colorId]).alpha(0.3).rgbString(),
        fillAlpha: 0.1
      }
      this.datasets.push(obj)
      colorId+=1
    }
    this.labels = d['Time/min']
    this.options = this.get_options()
    console.log(this.options)
    this.loaded = true
  },

}
</script>

<style scoped>

</style>
