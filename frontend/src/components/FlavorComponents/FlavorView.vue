<template>
  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-database"
        no-action
        v-for="(flavor, index) in flavors.flavors"
        :key=index>
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-if="flavor.substrate && flavor.additive">
              {{ flavor.label }}
            </v-list-item-title>
            <v-list-item-title v-else-if="flavor.additive">
              {{ flavor.additive }}
            </v-list-item-title>
            <v-list-item-title v-else>
              {{ flavor.substrate }}
            </v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          :key=i
          v-for="(subItem, i) in flavor"
          v-if="i!=='id' && subItem && i!=='label' && i!=='spectrum'"
        >
          <v-list-item-content>
            {{ i }} : {{ subItem }}
          </v-list-item-content>
        </v-list-item>
        <v-divider inset></v-divider>
        <v-subheader inset>Spectrums</v-subheader>
        <v-list-item
          :key=i
          v-for="(spectrum, i) in flavor.spectrum"
          v-if="spectrum && metaLoaded"
        >
          <v-btn rounded color="grey" @click="$router.push({name: 'spectrum', params: {spectrumId: spectrum}})">
            <v-icon left>fa-chart-area</v-icon>
            {{ spectrumdata[spectrum].meta.RANGE}}
          </v-btn>

        </v-list-item>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>

import {mapState} from 'vuex';

export default {
  name: 'FlavorView',
  data() {
    return {
      loading: false,
      error: null,
      spectrumdata: {id: 1, meta: null},
      metaLoaded: false
    }
  },
  computed: {
    ...mapState(["flavors"]),
  },
  methods: {
    logdata(item) {
      console.log(item)
    },
    dummyFetch: async function (pk) {
      let fields = 'id,meta'
      return await this.$store.dispatch("flavors/getSpectrumDetailFields", {pk, fields})

    },
    fetchSpecturm: async function (pk) {
      var data = await this.dummyFetch(pk)
      this.spectrumdata[pk.toString()] = data
    }


  },
  async mounted() {
    await this.$store.dispatch("flavors/getFlavorsList")
    let m = Object.values(this.flavors.flavors).filter(e => {
      return e.spectrum.length > 0
    })

    Object.values(m).forEach(e => {
      e.spectrum.forEach(pk => {
        this.fetchSpecturm(pk)
      })
    })
    this.metaLoaded=true
    console.log(this.spectrumdata)
  }
  ,
}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>


