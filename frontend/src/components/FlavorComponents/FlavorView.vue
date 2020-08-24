<template>
  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-user"
        no-action
        v-for="(flavor, index) in flavors.flavors"
        :key="index">
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="flavor.name">
            </v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          :key=subItem
          @click="logdata([subItem, i])"
          v-for="(subItem, i) in flavor"
          v-if="i!=='id' && subItem"
        >
          <v-list-item-content v-if="i !=='spectrum'">
            {{ i }} : {{ subItem }}
          </v-list-item-content>
          <v-list-item-content v-else>
            <v-btn rounded color="grey" @click="$router.push({name: 'spectrum', params: {spectrumId: subItem}})">
              <v-icon left>fa-chart-area</v-icon>
              {{ i }}
            </v-btn>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>

import {mapActions, mapState} from 'vuex';

export default {
  name: 'FlavorView',
  data() {
    return {
      loading: false,
      error: null
    }
  },
  computed: {
    ...mapState(["flavors"]),
  },
  methods: {
    ...mapActions(["flavors/getFlavorsList"]),
    logdata(item) {
      console.log(item)
    },
    fetchSpectrum(id) {

    }

  },
  created() {

    this.$store.dispatch("flavors/getFlavorsList")
  },
}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
