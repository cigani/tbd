<template lang="html">
  <div>
    <router-view/>
    <h2><router-link to="/index">Index</router-link></h2>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
