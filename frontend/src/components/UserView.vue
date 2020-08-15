<template>
  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-code"
        value="false"
        no-action
        v-for="user in users.users"
        :key="user.email">
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="user.short_name"></v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          v-for="(subItem, key) in user"
          :key="key"
          @click=""
        >
        <v-list-item-content>
          <v-list-item-title>
            {{key}} : {{subItem}}
          </v-list-item-title>
        </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>

import {mapGetters, mapActions, mapState} from 'vuex';
import store from "@/store/index.js";

export default {
  name: 'FirstComponent',
  store,
  computed: {
    ...mapState(["users"]),
  },
  mounted() {
    this.$store.dispatch("getUsersList")
    console.log(this.users)
  },

}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
