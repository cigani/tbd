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
            v-model="payload.firstname"
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
            v-model="payload.lastname"
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
            v-model="payload.email"
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
            v-model="payload.password"
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
import {mapActions} from 'vuex';

export default {
  data: () => ({
    valid: false,
    submitted: false,
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
  methods: {
    ...mapActions(["postRegister"]),
    create() {
      const payload = {
        first_name: this.payload.firstname,
        last_name: this.payload.lastname,
        is_admin: this.payload.isadmin,
        email: this.payload.email,
        password: this.payload.password
      };
      this.$store.dispatch("postRegister", payload)
      console.log(this.$store.state)
      this.submitted = true;
    },
    newUser() {
      this.submitted = false;
    }
  }

};
</script>
