<template>
  <canvas ref="myChart" :width="width" :height="height"></canvas>
</template>
<script>
import {Line, mixins} from 'vue-chartjs'

export default {
  extends: Line,
  data() {
    return {
      chart: null
    }
  },
  props: {
    width: {
      type: Number,
      validator: value => value > 0
    },
    // The canvas's height.
    height: {
      type: Number,
      validator: value => value > 0
    },
    options: {
      type: Object,
      default: null
    },
    labels: Array,
    datasets: {
      type: Array
    },
  },
  watch: {
    datasets(newDatasets) {
      // Replace the datasets and call the update() method on Chart.js
      // instance to re-render the chart.
      this.chart.data.datasets = newDatasets;
      this.chart.update();
    },
    options(newOptions){
      this.chart.options = newOptions
      this.chart.update();
    }
  },
  mounted() {
    console.log(this.datasets)
    this.chart = new Chart(this.$refs.myChart, {
        type: 'line',
        data: {
          datasets: this.datasets,
          labels: this.labels,
        },
        options: this.options,

      },
    )
  },
  beforeDestroy() {
    // Don't forget to destroy the Chart.js instance.
    if (this.chart) {
      this.chart.destroy()
    }
  },
}
</script>
