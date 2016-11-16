<template>
  <div id="stats">
    <div class="height-wrapper">
      <p class="height-text">
        <strong>Height: </strong>
        {{height}}
      </p>
    </div>
    <div class="weight-wrapper">
      <p class="weight-text">
        <strong>Weight: </strong>
        {{weight}}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'stats',
  props: [
    'height', 'weight'
  ]
}
</script>

<style scoped>
</style>
