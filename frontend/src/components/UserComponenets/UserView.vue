<template>

  <v-card
    class="mx-auto">
    <v-list>
      <v-list-group
        prepend-icon="fa-user"
        no-action
        v-for="(user, index) in users.users"
        :key="index"
        v-if="user.is_active === true">
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="user.short_name">
            </v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item
          v-for="(subItem, i) in user"
          :key=subItem.id
          @click="logdata([user.id, i])"
          v-if="i!=='id'"
        >
          <v-list-item-content>
            <v-list-item-title>
              {{ i }} : {{ subItem }}
            </v-list-item-title>

          </v-list-item-content>
        </v-list-item>
        <v-btn outlined color="orange" @click="removeElement(user,user.id)">Delete User</v-btn>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script>

import {mapActions, mapState} from 'vuex';

export default {
  name: 'users',
  computed: {
    ...mapState(["users"]),
  },
  methods: {
    ...mapActions(["deleteUser"]),
    logdata(item) {
      console.log(item)
    },
    removeElement: function (user, pk) {
      console.log(user, pk)
      this.$store.dispatch("deleteUser", pk)
      this.users.users = this.users.users.filter(x => x.id !== user.id)
    },

  },
  submitted() {
    this.$store.dispatch("getUsersList")
  },
}

</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
</style>
