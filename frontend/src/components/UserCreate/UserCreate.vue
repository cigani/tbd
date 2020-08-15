<template>
  <v-form v-model="valid" v-if="!submitted">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            prepend-icon="mdi-name"
            v-model="firstname"
            :rules="nameRules"
            :counter="10"
            label="First name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            prepend-icon="mdi-name"
            v-model="lastname"
            :rules="nameRules"
            :counter="10"
            label="Last name"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            prepend-icon="mdi-email"
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          />
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="password"
            prepend-icon="mdi-lock"
            label="Password"
            type="password"
            required
          />
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
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
        </v-col>
      </v-row>
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
    nameRules: [
      v => !!v || 'Name is required',
      v => v.length <= 10 || 'Name must be less than 10 characters',
    ],
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
    payload: {
      firstname: '',
      lastname: '',
      password: '',
      isadmin: '',
      email: '',
    }
  }),
  props: {
    submitted: false
  },
  methods: {
    ...mapActions(["createUser"]),
    create() {
      var payload = {
        first_name: this.firstname,
        last_name: this.lastname,
        is_admin: this.isadmin,
        email: this.email,
        password: this.password
      };
      console.log(payload)
      this.$store.dispatch("createUser", payload)
      this.submitted = true;
    },
    newUser() {
      this.submitted = false;
      this.payload = {};
    }
  }

};
</script>
