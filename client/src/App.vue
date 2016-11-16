<template>
  <div id="app">
    <h1>Vigor</h1>
    <router-link to="/">Home</router-link>
    <router-link to="/users/">Users</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>
