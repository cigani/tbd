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
          :key=1
          v-for="(spectrum, i) in flavor.spectrum"
          v-if="spectruminfo && spectruminfo.map(e=> e.id===spectrum)"
        >
          <v-btn rounded color="grey" @click="$router.push({name: 'spectrum', params: {spectrumId: spectrum}})">
            <v-icon left >fa-chart-area</v-icon>
            {{ spectruminfo[i].meta.SAMPLE }}
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
      spectruminfo: null
    }
  },
  computed: {
    ...mapState(["flavors"]),
  },
  methods: {
    logdata(item) {
      console.log(item)
    },


  },
  async created() {
    await this.$store.dispatch("flavors/getFlavorsList")
    this.spectruminfo = await this.$store.dispatch("flavors/getSpectrumFields",
      "id,meta")
    console.log(this.spectruminfo)
  },
}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>


