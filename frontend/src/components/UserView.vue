<template>
  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-user"
        no-action
        v-for="user in users.users"
        :key="user.id">
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="user.short_name">
            </v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          v-for="(subItem, i) in user"
          :key=subItem.id
          @click="logdata([user.id, id])"
          v-if="i!=='id'"
        >
        <v-list-item-content >
          <v-list-item-title >
            {{i}} : {{subItem}}
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
  methods:{
    logdata(item){
      console.log(item)
    }
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
