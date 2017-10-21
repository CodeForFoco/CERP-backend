<template>
  <div id="app">
    <md-whiteframe class="master_frame" md-tag="md-toolbar" md-elevation="3">
      <div class="md-toolbar-container nav">
        <h2 class="md-title" style="flex: 1">CERP</h2>
        <router-link to="/" class="md-button" :class="`md-theme-${$material.currentTheme}`">Home<md-ink-ripple /></router-link>
        <router-link to="/about" class="md-button" :class="`md-theme-${$material.currentTheme}`">About<md-ink-ripple /></router-link>
        <router-link to="/contact" class="md-button" :class="`md-theme-${$material.currentTheme}`">Contact<md-ink-ripple /></router-link>
      </div>
    </md-whiteframe>

    <router-view/>

  </div>
</template>


<script>
export default {
  name: 'app'
}
</script>

<style>
#app {

}
.nav {
  color: #FFF;
}
body {
  background-color: #f7f7f7
}
body.md-theme-default {
  background-color: #f7f7f7
}
</style>
