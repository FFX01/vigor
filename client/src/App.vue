<template>
  <div id="app">
    <h1>Vigor</h1>
    <nav>
      <ul role="navigation">
        <li><router-link :to="{name: 'home'}">Home</router-link></li>
        <li><router-link :to="{name: 'user-list'}">Users</router-link></li>
        <li><router-link :to="{name: 'program-list'}">Programs</router-link></li>
      </ul>
    </nav>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>
