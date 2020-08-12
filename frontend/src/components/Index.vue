<template>
  <div class="pt-5">
    <div v-if="subscriptions && subscriptions.length">
      <div class="card mb-3" v-for="subscription of subscriptions" v-bind:key="subscription.id">
        <div class="row no-gutters">
          <div class="col-md-4">
            <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg"
                 preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail">
              <title>{{ subscription.full_name }}</title>
              <rect width="100%" height="100%" fill="#55595c"/>
              <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ subscription.email}}</text>
            </svg>
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ subscription.full_name }}</h5>
              <p class="card-text">{{ subscription.email }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <p v-if="subscriptions.length === 0">No subscriptions</p>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      subscriptions: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      let url = "http://localhost:8000/api/users/"
      axios.get(url)
        .then(response => {
          this.subscriptions = response.data
          console.log(response)
          console.log(response.data)
        });
    }
  },
}
</script>
