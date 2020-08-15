<template>
  <v-form v-model="valid" v-if="!submitted">
    <v-container>
      <v-text-field
        v-for="(item, key) in model"
        :v-model=item
        :key=key
        :placeholder=item
        :label=item
      />
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="success"
          class="mr-4"
          @click="create"
          ripple
          rounded
          block
        >Create Account
        </v-btn>
      </v-card-actions>
    </v-container>
  </v-form>
  <div class="text-center" v-else>
    <v-btn
      color="success"
      class="mr-4"
      @click="newUser"
      left
      tile
    >Create Another User
      <v-icon right dark>mdi-cloud-upload</v-icon>
    </v-btn>
    <v-btn
      color="success"
      class="mr-4"
      @click="$router.push('Users')"
      ripple
      outlined
      tile
    >View Users
    </v-btn>
  </div>
</template>

<script>
import {mapGetters, mapActions, mapState} from 'vuex';
import store from "@/store/index.js";

export default {
  store,
  data: () => ({
    valid: false,
    submitted: false,
    model: {
      first_name: "First Name",
      last_name: 'Last Name',
      password: 'Password',
      email: 'email',
    }
  }),
  props: {},
  methods: {
    ...mapActions(["createUser"]),
    create() {
      let payload = this.model
      console.log(this.model.email)
      console.log(this.model.first_name)
      // this.$store.dispatch("createUser", payload)
      this.submitted = false;
    },
    newUser() {
      this.submitted = false;
    }
  }

};
</script>
