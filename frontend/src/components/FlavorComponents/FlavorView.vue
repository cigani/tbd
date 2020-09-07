<template>
  <v-container
    fluid>
      <v-card
        class="mx-auto">
        <flavor-toolbar label="Flavor Database" additional="home"></flavor-toolbar>
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
            <v-subheader inset> Modify</v-subheader>
            <v-list-item>
              <v-col
                cols="12">
                <v-row
                  no-gutters
                  justify="space-around"
                  align="center">
                  <v-btn @click="$router.push({name: 'FlavorAddSpectrum', params:{flavorId: flavor.id}})"
                         color="blue lighten-4"
                  >Add Data
                  </v-btn>
                  <v-btn
                    @click="$router.push({name: 'flavor', params:{flavorId: flavor.id}})"
                    color="blue lighten-1"
                    right>Modify Entry
                  </v-btn>
                  <v-btn @click="deleteFlavor(flavor)"
                         color="red darken-4"
                         :disabled="!disabled"
                  >Delete Entry
                  </v-btn>
                  <v-checkbox v-model="disabled" label="Allow Delete"></v-checkbox>

                </v-row>
              </v-col>

            </v-list-item>
            <v-divider inset></v-divider>
            <v-subheader inset>Spectrums</v-subheader>
            <v-list-item
              :key=index
              v-for="(spectrum, index) in (flavor.spectrum)"
              v-if="spectrum[1]"
            >
              <v-btn rounded color="grey"
                     @click="$router.push({name: 'spectrum', params: {spectrumId: spectrum[0]}})">
                <v-icon left>fa-chart-area</v-icon>
                {{ ('SAMPLE' in spectrum[1]) ? spectrum[1].SAMPLE : 'N/A' }} - Mass: {{ ('SAMPLE MASS /mg' in spectrum[1]) ? spectrum[1]['SAMPLE MASS /mg'] : 'N/A' }}
              </v-btn>

            </v-list-item>
          </v-list-group>
        </v-list>
      </v-card>
  </v-container>
</template>

<script>

import {mapState} from 'vuex';
import FlavorToolbar from "@/components/FlavorComponents/FlavorToolbar/FlavorToolbar";

export default {
  name: 'FlavorView',
  components: {FlavorToolbar},
  data() {
    return {
      loading: true,
      error: null,
      disabled: false
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
    },
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


