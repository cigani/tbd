<template>
  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-database"
        no-action
        v-for="(flavor, index) in flavors.flavors"
        :key=flavor.id>
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
        <v-subheader inset> Modify Flavors</v-subheader>
        <v-list-item>
          <v-btn @click="deleteFlavor(flavor)"
                 color="warning"
                 right
          >Delete Flavor
          </v-btn>
          <v-btn
          @click="$router.push({name: 'flavor', params:{flavorId: flavor.id}})"
          color="primary"
          right>Modify Flavor</v-btn>
        </v-list-item>
        <v-divider inset></v-divider>
        <v-subheader inset>Spectrums</v-subheader>
        <v-list-item
          :key=index
          v-for="(spectrum, index) in (flavor.spectrum)"
        >
          <v-btn rounded color="grey"
                 @click="$router.push({name: 'spectrum', params: {spectrumId: spectrum[0]}})">
            <v-icon left>fa-chart-area</v-icon>
            {{ spectrum[1].SAMPLE }} {{ index }}

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
      loading: true,
      error: null,
    }
  },
  computed: {
    ...mapState(["flavors"]),
  },
  methods: {
    logdata(item) {
      console.log(item)
    },
    deleteFlavor(flavor) {
      if (confirm("Are you certain you wish to delete this Flavor? All Spectrums attached will be deleted as well")) {
        this.$store.dispatch("flavors/deleteFlavor", flavor.id)
        this.flavors.flavors = this.flavors.flavors.filter(x => x.id !== flavor.id)
      }
    }
  },

  async mounted() {
    await this.$store.dispatch("flavors/getFlavorsList")
  }
  ,
}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>


