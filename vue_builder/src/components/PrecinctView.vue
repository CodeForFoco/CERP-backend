<template>
  <div class="precinct">
    <p>Precinct: {{ precinct }}</p>
  </div>
</template>

<script>
export default {
  name: 'PrecinctView',
  data () {
    return {
      precinct: this.$route.params.id
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
