<template>
  <div id="info">
    <div class="username-wrapper">
      <h3 class="username-text">
        {{username}}
      </h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'info',
  props: ['username']
}
</script>

<style scoped>
</style>
